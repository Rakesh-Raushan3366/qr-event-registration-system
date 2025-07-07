from samautkarsh.smsapis import send_registration_sms, send_otp, get_registration_mappings
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from django.conf import settings
from io import BytesIO
from PIL import Image
import qrcode, os
import base64
from register_samautkarsh.models import *
from register_samautkarsh.forms import *
from .models import *
from .forms import *


# Create your views here.

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
                return redirect("ghosh_warg:otp_verification")

            elif scanner_exists:
                send_otp(mobile)
                request.session["mobile"] = mobile 
                request.session['role']='scanner' # Store mobile in session
                return redirect("ghosh_warg:otp_verification")
            else:
                send_otp(mobile)
                request.session["mobile"] = mobile  # Store mobile in session
                return redirect("ghosh_warg:otp_verification")            
    else:
        form = MobileForm()
    return render(request, "mobile_verification.html", {"form": form})

# Step 2: OTP Verification
def otp_verification(request):
    mobile = request.session.get("mobile")
    message = ""
    
    if not mobile:
        return redirect("ghosh_warg:mobile_verification")

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
                    elif admin.role == 'SUBADMIN':
                        return redirect('core:sub_admin_dashboard')

                elif request.session.get('role') == 'scanner':
                    return redirect('scan_qr')

                # Check if user is already registered
                
                elif RegisterSamautkarshRegistration.objects.filter(phone_number=mobile).exists():
                    return redirect("ghosh_warg:ghoshwargviewregistration")

                # If new user, redirect to registration page
                
                return redirect("ghosh_warg:ghoshwargregisteration")
            else:
                message = "Invalid OTP. Try again."
                messages.error(request, message)
                return redirect("ghosh_warg:otp_verification")

    return render(request, "otp_verification.html", {"form": form})

# Ghosh Varg Registration here.
def GhoshWargRegisteration(request):
    if not request.session.get('mobile'):
         return redirect('ghosh_warg:otp_verification') 
    mobile_number = request.session.get('mobile')

    # Fetch mappings from the function
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
        return redirect('ghosh_warg:mobile_verification')
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
                return redirect('ghosh_warg')

            else:
                print(form.errors)
                # If form is invalid, re-render the form with error messages
                return render(request, 'ghoshwargregisteration.html', {'form': form, 'phone_number': mobile_number, 'mappings':mappings})
    # Render the registration form if the record does not exist or on first load
    return render(request, 'ghoshwargregisteration.html', {'form': form, 'phone_number': mobile_number, 'mappings':mappings})



# view Registration informations!
def GhoshWargViewRegistration(request):
    # Check if mobile number is in session (user is verified)
    if not request.session.get('mobile'):
        return redirect('ghosh_warg:otp_verification')
    
    mobile_number = request.session.get('mobile')
    try:
        # Try to get the registration record
        record = GhoshVargRegister.objects.get(phone_number=mobile_number)
        barcode_record = BarcodeScan.objects.get(phone_number=mobile_number)
        barcodescan = BarcodeScan.objects.filter(phone_number=mobile_number).values_list('status', flat=True)[0]
        # Prepare context data
        context = {
            'data': record,
            'barcode': barcode_record,
            'phone_number': mobile_number,
            'barcodescan' : barcodescan,
            'is_registered': True
        }
        
        return render(request, 'ghoshwargviewregistration.html', context)
        
    except (RegisterSamautkarshRegistration.DoesNotExist, BarcodeScan.DoesNotExist):
        # If no record exists, redirect to registration
        return redirect('ghosh_warg:ghoshwargregisteration')


# Update Registration Profile Details
def GhoshWargUpdateRegistration(request):
    if not request.session.get('mobile'):
        return redirect('ghosh_warg:otp_verification')
    
    mobile_number = request.session.get('mobile')
    mappings = get_registration_mappings()  # Fetch mappings from the function

    try:
        # Get the existing record to update
        record = RegisterSamautkarshRegistration.objects.get(phone_number=mobile_number)
    except RegisterSamautkarshRegistration.DoesNotExist:
        # If no record exists, redirect to registration
        return redirect('ghosh_warg:ghoshwargregisteration')

    if request.method == 'POST':
        form = RegistrationForm(request.POST, instance=record)
        if form.is_valid():
            updated_record = form.save()
            
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
            return redirect('/')
        else:
            print(form.errors)
            return render(request, 'ghoshwargupdateregistration.html', {'form': form,'phone_number': mobile_number, 'mappings': mappings})
    
    # Pre-populate form with existing data for GET request
    form = RegistrationForm(instance=record)
    return render(request, 'ghoshwargupdateregistration.html', {'form': form,'phone_number': mobile_number, 'mappings': mappings})
#  End Update Registration Profile Details


# Logout Function
def user_logout(request):
    # Flush the session
    request.session.flush()
    logout(request)
    return redirect('/')