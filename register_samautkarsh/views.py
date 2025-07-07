from django.http import HttpResponse # type: ignore # type: ignore
from django.contrib.auth import logout
from .models import QRCode
from io import BytesIO
from django.shortcuts import render, redirect
from django.conf import settings
from .models import *
from .forms import *
from ghosh_warg.models import GhoshVargRegister
from ghosh_warg.forms import GhoshVargRegisterForm
from django.contrib import messages
import json
from PIL import Image
import qrcode, json, os
import base64
from samautkarsh.smsapis import send_registration_sms, send_otp, get_registration_mappings
from .qrcode import *
from django.db.models import Min
from django.forms.models import model_to_dict


# Create your views here.
def homepage(request):
    request.session.flush()
    return render(request, 'register_samautkarsh/home.html')  


def role_glossary(request):
    # Get the mappings from the function
    mappings = get_registration_mappings(request)
    context =  {'mappings': mappings}
    return render(request, 'register_samautkarsh/role_glossary.html', context)

# Create your views here.
# ----------------------------------------Start User Registration and Login Views -------------------------------------------------

# Mobile Number Based Authentications
# Step 1: Check if mobile exists
def mobile_verification(request):
    message=''
    mobile=''
        
    if request.method == "POST":
        form = MobileForm(request.POST)
        if form.is_valid():
            mobile = form.cleaned_data["mobile"]
            user_exists = RegisterSamautkarshRegistration.objects.filter(phone_number=mobile).exists()
            scanner_exists = ScannerApprovals.objects.filter(phone_number=mobile,role='scanner').exists()
            try:
                user_exists1= BarcodeScan.objects.filter(phone_number=mobile)
                if user_exists1.status=='Approve' or user_exists1.status=='Reject':
                     request.session["status"] = user_exists1.status
            except:
                pass
            if user_exists:
                send_otp(mobile)
                request.session["mobile"] = mobile  # Store mobile in session
                return redirect("register_samautkarsh:otp_verification")
                # message='Mobile number already exists. Please login.'
                # user_exists1= BarcodeScan.objects.get(phone_number=mobile)
                # if user_exists1.status=='Approve' or user_exists1.status=='Reject':
                #     request.session["status"] = user_exists1.status
                #     send_otp(mobile)
                #     request.session["mobile"] = mobile  # Store mobile in session
                #     return redirect("otp_verification")
                # message='User has been successfully registerd!\nआपने अपना पंजीकरण सफलतापूर्वक पूर्ण कर लिया है।\nआपके "QR Code" की जानकारी दिए गए 👉 "SBRPLR SMS Code" 👈 द्वारा आपको शीघ्र भेजी जाएगी।'
                # messages.warning(request, message)
                # return redirect("mobile_verification")
            elif scanner_exists:
                send_otp(mobile)
                request.session["mobile"] = mobile 
                request.session['role']='scanner' # Store mobile in session
                return redirect("register_samautkarsh:otp_verification")
            else:
                send_otp(mobile)
                request.session["mobile"] = mobile  # Store mobile in session
                return redirect("register_samautkarsh:otp_verification")            
    else:
        form = MobileForm()
    return render(request, "register_samautkarsh/mobile_verification.html", {"form": form})

# Step 2: OTP Verification
def otp_verification(request):
    mobile = request.session.get("mobile")
    mappings = get_registration_mappings(request) # Get the mappings from the function
    message = ""
    
    if not mobile:
        return redirect("register_samautkarsh:mobile_verification")

    form = OTPForm()

    if request.method == "POST":
        form = OTPForm(request.POST)

        if form.is_valid():
            otp = form.cleaned_data["otp"]
            otp_record = RegisterSamautkarshOtp.objects.filter(mobile=mobile, otp=otp).first()

            if otp_record:
                # Save new user only after OTP verification
                RegisterSamautkarshUser.objects.create(mobile=mobile)

                # ✅ Set source_app to track app for future redirection
                request.session['source_app'] = 'register_samautkarsh'

                admin = Admin.objects.filter(mobile=mobile).first()
                if admin:
                    request.session['role_level'] = str(admin.role_level)
                    request.session['role'] = admin.role
                    request.session['role_sublevel'] = admin.role_sublevel

                    if admin.role == 'SUPERADMIN':
                        return redirect('core:superadmin_dashboard')
                    elif admin.role == 'ADMIN' and admin.role_level in ['Prant', 'Vibhag', 'Jilla', 'Nagar']:
                        return redirect('core:department_admin_dashboard')
                    elif admin.role == 'SUBADMIN':
                        return redirect('core:sub_admin_dashboard')

                elif request.session.get('role') == 'scanner':
                    return redirect('scan_qr')

                # Check if user is already registered
                
                elif RegisterSamautkarshRegistration.objects.filter(phone_number=mobile).exists():
                    return redirect("register_samautkarsh:view_registration")

                # If new user, redirect to registration page
                
                return redirect("register_samautkarsh:register")
            else:
                message = "Invalid OTP. Try again."
                messages.error(request, message)
                return redirect("register_samautkarsh:otp_verification")

    return render(request, "register_samautkarsh/otp_verification.html", {"form": form, "mappings":mappings})



def register(request):
    if not request.session.get('mobile'):
         return redirect('register_samautkarsh:otp_verification') 
    mobile_number = request.session.get('mobile')
    # Get the mappings from the function
    mappings = get_registration_mappings(request) 


    form1 = RegistrationForm()
    form = GhoshVargRegisterForm()
    try:
        # Check if the phone number already exists in the database
        record = RegisterSamautkarshRegistration.objects.get(phone_number=mobile_number)
    except RegisterSamautkarshRegistration.DoesNotExist:
        record = None

    if record:
        # If a record exists, redirect to the verification page
        return redirect('/')
    else:
        # If no record exists, proceed with registration
        if request.method == 'POST':
            form1 = RegistrationForm(request.POST)
            form = GhoshVargRegisterForm(request.POST)
            form.instance.phone_number = mobile_number
            
            if form.is_valid():
                # Set the mobile number from the session in the form
                form.instance.phone_number = mobile_number
                
                # Use `form.instance` instead of directly setting form fields
                registration = form.save(commit=True)
                registration1 = form1.save(commit=True)

                # Generate QR code with name and nagar
                name = registration.name
                phone=registration.phone_number
                nagar = registration.nagar
                dayitv=registration.dayitv
                ekai=registration.ekai

                state=''
                try:
                    picode = PincodeMaster.objects.filter(pincode=registration.pincode, nagar_hindi=nagar)

                    state = None
                    qr_data = f"Name: {name}, Phone Number: {phone},Nagar: {nagar},state: {state}, Dayitv: {dayitv}, ekai:{ekai}"    
                    qr_data = base64.b64encode(qr_data.encode()).decode()
                except PincodeMaster.DoesNotExist:
                        state=registration.state
                        if not state:
                            state=''
                        qr_data = f"Name: {name}, Phone Number: {phone},Nagar: {nagar}, State: {state}, Dayitv: {dayitv}, ekai:{ekai}"
                        qr_data = base64.b64encode(qr_data.encode()).decode()

                qr = qrcode.QRCode(version=1, box_size=10, border=5)
                qr.add_data(qr_data)
                qr.make(fit=True)
                qr_img = qr.make_image(fill='black', back_color='white').convert('RGBA')  # Ensure RGBA mode

                # Load the logo image
                logo_path = os.path.join(settings.BASE_DIR, 'register_samautkarsh/static/register_samautkarsh/assets/img', 'logo.jpg')

                if os.path.exists(logo_path):

                    logo = Image.open(logo_path).convert("RGBA")  # Convert logo to RGBA

                    # Resize logo to fit inside the QR code
                    qr_size = qr_img.size[0]  # QR code width
                    logo_size = qr_size // 8   # Logo should be 1/4th of the QR code size
                    logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

                    # Ensure QR code supports transparency before pasting
                    qr_img = qr_img.convert("RGBA")

                    # Paste logo at the center
                    logo_x = (qr_img.size[0] - logo.size[0]) // 2
                    logo_y = (qr_img.size[1] - logo.size[1]) // 2
                    qr_img.paste(logo, (logo_x, logo_y), logo)  # Ensure mask is used

                else:
                    pass
                    # print("❌ Logo not found! Skipping logo placement.")

                # Save the QR code
                qr_buffer = BytesIO()
                qr_img.save(qr_buffer, format="PNG")
                qr_buffer.seek(0)

                # Define the path for saving the QR code
                qr_directory = os.path.join(settings.BASE_DIR, 'register_samautkarsh','static', 'QRCodes')
                os.makedirs(qr_directory, exist_ok=True)  # Ensure the directory exists

                qr_filename = os.path.join(qr_directory, f"{phone}.jpg")
                barcodescan = BarcodeScan(name=name, phone_number=phone, nagar=nagar,dayitv=dayitv, qrcode=qr_filename)
                barcodescan.save()


                # Save the QR code image to the file
                with open(qr_filename, 'wb') as f:
                    f.write(qr_buffer.read())
                
                # Send an SMS to the user after registration
                send_registration_sms(phone) # Sms message call from smsapis.py

                request.session.flush()   
                # After successful registration and QR code generation, redirect to verification
                return redirect('register_samautkarsh:verify_registration')

            else:
                print(form.errors)
                # If form is invalid, re-render the form with error messages
                return render(request, 'register_samautkarsh/register.html', {'form': form, 'phone_number': mobile_number, 'mappings':mappings})

    # Render the registration form if the record does not exist or on first load
    return render(request, 'register_samautkarsh/register.html', {'form': form, 'phone_number': mobile_number, 'mappings':mappings})


def register_shatabdi(request):
    # if not request.session.get('mobile'):
    #      return redirect('otp_verification') 
        mappings = get_registration_mappings(request) # Get the mappings from the function
        form = EventRegisterForm()
                
        # If no record exists, proceed with registration
        if request.method == 'POST':
            form = EventRegisterForm(request.POST)
            if form.is_valid():
                # Set the mobile number from the session in the form
                  # Use `form.instance` instead of directly setting form fields
                registration = form.save(commit=True)

                # Generate and save QR code using helper functions
                #qr_filename = process_registration_qr(registration)
                '''
                # Save barcode scan record
                BarcodeScan.objects.create(
                    name=registration.name,
                    phone_number=registration.phone_number,
                    nagar=registration.nagar,
                    dayitv=registration.dayitv,
                    qrcode=qr_filename
                )
                '''
                # Send an SMS to the user after registration
                #send_registration_sms(phone) # Sms message call from smsapis.py

                request.session.flush()   
                # After successful registration and QR code generation, redirect to verification
                return redirect('register_samautkarsh:verify_registration')

            else:
                print(form.errors)
                # If form is invalid, re-render the form with error messages
                return render(request, 'register_samautkarsh/shatabdi_varsh.html', {'form': form, 'mappings':mappings})
        # Render the registration form if the record does not exist or on first load
        return render(request, 'register_samautkarsh/shatabdi_varsh.html', {'form': form,  'mappings':mappings})

# view Registration informations!
def view_registration(request):
    # Check if mobile number is in session (user is verified)
    if not request.session.get('mobile'):
        return redirect('register_samautkarsh:otp_verification')

    
    mobile_number = request.session.get('mobile')

    try:
        # Try to get the registration record
        record = GhoshVargRegister.objects.get(phone_number=mobile_number)
        barcode_record = BarcodeScan.objects.get(phone_number=mobile_number)
        barcodescan = BarcodeScan.objects.filter(phone_number=mobile_number).values_list('status', flat=True)[0]
        # Get the admin role and level from the session for server-side rendering
        # admin = Admin.objects.filter(mobile=mobile_number).first()
        # adminRoleLevel = request.session['role_level'] = str(admin.role_level)
        # adminRole = request.session['role'] = admin.role
        # adminSubLevel = request.session['role_sublevel'] = admin.role_sublevel
        # Prepare context data
        context = {
            # 'adminRoleLevel': adminRoleLevel,
            # 'adminRole': adminRole,
            # 'adminSubLevel': adminSubLevel,
            'data': record,
            'barcode': barcode_record,
            'phone_number': mobile_number,
            'barcodescan' : barcodescan,
            'is_registered': True
        }
        
        return render(request, 'register_samautkarsh/view_registration.html', context)
        
    #except (RegisterSamautkarshRegistration.DoesNotExist, BarcodeScan.DoesNotExist):
    except (GhoshVargRegister.DoesNotExist, BarcodeScan.DoesNotExist):   
        # If no record exists, redirect to registration
        return redirect('register')


# Update Registration Profile Details
def update_register(request):
    if not request.session.get('mobile'):
        return redirect('register_samautkarsh:otp_verification')
    
    mobile_number = request.session.get('mobile')
    mappings = get_registration_mappings(request) # Get the mappings from the function

    # Dynamice Data for DropDown
    categorycollege = (CategotyCollage.objects.values('category_name').annotate(category_college_id=Min('category_college_id')))
    collageAffilated = (CollageAffilated.objects.values('affilated_by').annotate(college_affilated_id=Min('college_affilated_id')))
    
    form1 = RegistrationForm()
    form = GhoshVargRegisterForm()
    try:
        # Get the existing record to update
        record1 = RegisterSamautkarshRegistration.objects.get(phone_number=mobile_number)
        record = GhoshVargRegister.objects.get(phone_number=mobile_number)
        record_dict = model_to_dict(record)
        print("Record data:", record_dict)

        
    except RegisterSamautkarshRegistration.DoesNotExist:
        # If no record exists, redirect to registration
        return redirect('register_samautkarsh:register')

    if request.method == 'POST':
        form1 = RegistrationForm(request.POST, instance=record)
        form = GhoshVargRegisterForm(request.POST, instance=record)
        if form.is_valid() and form1.is_valid():
            updated_record = form.save()
            updated_record1 = form1.save()
            print("update record")
            print(updated_record1)
            # Update QR code with new information
            name = updated_record.name
            phone = updated_record.phone_number
            nagar = updated_record.nagar_address
            dayitv = updated_record.dayitv
            state = ''
            
            try:
                pincode = PincodeMaster.objects.filter(pincode=updated_record.pincode, nagar_hindi=nagar)
                state = None
                qr_data = f"Name: {name}, Phone Number: {phone}, Nagar: {nagar}, state: {state}, Dayitv: {dayitv}"    
                qr_data = base64.b64encode(qr_data.encode()).decode()
            except PincodeMaster.DoesNotExist:
                state = updated_record.state
                if not state:
                    state = ''
                qr_data = f"Name: {name}, Phone Number: {phone}, Nagar: {nagar}, State: {state}, Dayitv: {dayitv}"
                qr_data = base64.b64encode(qr_data.encode()).decode()

            # Generate new QR code (same as register function)
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(qr_data)
            qr.make(fit=True)
            qr_img = qr.make_image(fill='black', back_color='white').convert('RGBA')

            # Add logo if exists (same as register function)
            logo_path = os.path.join(settings.BASE_DIR, 'register_samautkarsh/static/register_samautkarsh/assets/img', 'logo.jpg')
            if os.path.exists(logo_path):
                logo = Image.open(logo_path).convert("RGBA")
                qr_size = qr_img.size[0]
                logo_size = qr_size // 8
                logo = logo.resize((logo_size, logo_size), Image.LANCZOS)
                qr_img = qr_img.convert("RGBA")
                logo_x = (qr_img.size[0] - logo.size[0]) // 2
                logo_y = (qr_img.size[1] - logo.size[1]) // 2
                qr_img.paste(logo, (logo_x, logo_y), logo)

            # Save the QR code (same as register function)
            qr_directory = os.path.join(settings.BASE_DIR, 'register_samautkarsh', 'static', 'QRCodes')
            os.makedirs(qr_directory, exist_ok=True)
            qr_filename = os.path.join(qr_directory, f"{phone}.jpg")
            
            with open(qr_filename, 'wb') as f:
                qr_img.save(f, format="PNG")

            # Update BarcodeScan record
            try:
                barcode_record = BarcodeScan.objects.get(phone_number=phone)
                barcode_record.name = name
                barcode_record.nagar = nagar
                barcode_record.dayitv = dayitv
                barcode_record.save()
            except BarcodeScan.DoesNotExist:
                BarcodeScan.objects.create(
                    name=name,
                    phone_number=phone,
                    nagar=nagar,
                    dayitv=dayitv,
                    qrcode=qr_filename
                )

            # Send update confirmation SMS
            send_registration_sms(phone)  # Sms message call from smsapis.py
            
            request.session.flush()
            return redirect('register_samautkarsh:view_registration')
        else:
            print(form.errors)
            return render(request, 'register_samautkarsh/update_register.html', {'form': form,'phone_number': mobile_number, 'mappings': mappings, 'categorycollege': categorycollege, 'collageAffilated': collageAffilated})
    
    # Pre-populate form with existing data for GET request
    form = GhoshVargRegisterForm(instance=record)
    return render(request, 'register_samautkarsh/update_register.html', {'form': form,'phone_number': mobile_number, 'mappings': mappings, 'categorycollege': categorycollege, 'collageAffilated': collageAffilated})
#  End Update Registration Profile Details

# @csrf_exempt
# def save_qr(request):
#     """Saves the scanned QR code data."""
#     if request.method == "POST":
#             # Parse JSON data from the request body
#             data = json.loads(request.body)
#             qr_data = data.get("qr_data", "")  # Get the QR code data from the request body
#             # print(qr_data)  # Debugging output
#             if qr_data:
#                 # Save the QR code data to the database
#                 print(qr_data,type(qr_data))
#                 print(qr_data,"shelja jindaluhuhuh")
#                 user_exists = BarcodeScan.objects.filter(phone_number=qr_data).exists()
#                 if user_exists:
#                     barcodescan = ScannedPerson( phone_number=qr_data, person_scanned=request.session.get('mobile'))
#                     barcodescan.save()
#                     # Get the count_field data (assuming `count_field` is a model field)               
#                     #barcodescan = ScannedPerson( phone_number=user1.mobile, person_scanned=request.session.get('mobile'))
#                     barcodescan.save()
#                 return redirect('scan_qr')
#                 #return JsonResponse({"status": "success", "message": "QR code saved successfully!"})
#             else:
#                 return HttpResponse({"status": "error", "message": "No data received!"}, status=400)
# def scan_qr(request):
#     """Renders the QR scanning page."""
#     return render(request, "register_samautkarsh/scan_qr.html") take it



# def qr_history(request):
#     """Displays the history of scanned QR codes."""
#     qr_codes = QRCode.objects.order_by("-scanned_at")
#     return render(request, "register_samautkarsh/history.html", {"qr_codes": qr_codes})

    
def generate_qr(request, data):
    #qr = qrcode.make(data)
    QRCode.objects.create(data=data)
    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    buffer.seek(0)

    return HttpResponse(buffer.getvalue(), content_type="image/png")








'''
# QR-Code Generation Function here.
def verify_registration(request):
    verification_success = True  # Assume registration is successful

    # Fetch the latest registered user
    latest_user = RegisterSamautkarshRegistration.objects.last()

    if latest_user:
        name = latest_user.name
        nagar = latest_user.nagar_address

        # Combine name and nagar for QR code data
        qr_data = f"Name: {name}, Nagar: {nagar}"

        # Generate the QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_coscan_qrlor="white")

        # Convert QR code to base64 for rendering in template
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        qr_code_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
        buffer.close()

        # Pass QR code and user data to template
        context = {
            'verification_success': verification_success,
            'qr_code_base64': qr_code_base64,
            'name': name,
            'nagar': nagar,
        }
        return render(request, 'register_samautkarsh/verify_registration.html', context)
    else:
        context = {
            'verification_success': False,
        }

    return render(request, 'register_samautkarsh/verify_registration.html', context)
'''
# QR-Code Generation Function here.
def verify_registration(request):
    if request.session.get("status")=="Approve":
        verification_success = True  # Assume registration is successful
        print(request.session.get('mobile'))

        # Fetch the latest registered user
        latest_user = BarcodeScan.objects.get(phone_number=request.session.get('mobile'))
        print(latest_user.qrcode)
        context = {
                'verification_success': verification_success,
                'QR_CODE':f'/static/QRCodes/{os.path.basename(latest_user.qrcode)}'
            }
        return render(request, 'register_samautkarsh/pass.html', context)
    else:
        context = {
            'verification_success': False,
            'mobile': request.session.get('mobile')
        }

    return render(request, 'register_samautkarsh/pass.html', context)

# Logout Function
def user_logout(request):
    # Flush the session
    request.session.flush()
    logout(request)
    return redirect('/')