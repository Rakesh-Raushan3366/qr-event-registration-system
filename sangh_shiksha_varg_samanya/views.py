from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout
from .models import QRCode
from io import BytesIO
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import login, authenticate
from .models import *
from .forms import *
from django.core.cache import cache
from django.utils.timezone import now
from django.contrib import messages
import json, random
from qrcode.image.pil import PilImage
from PIL import Image
from collections import defaultdict
import pandas as pd
import qrcode, json, os
import requests
import base64
from .smsapis import send_registration_sms, send_otp, get_registration_mappings
from .qrcode import *


# Create your views here.
def homepage(request):
    request.session.flush()
    return render(request, 'register_samautkarsh/home.html')  

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
                return redirect("otp_verification")
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
                return redirect("otp_verification")
            else:
                send_otp(mobile)
                request.session["mobile"] = mobile  # Store mobile in session
                return redirect("otp_verification")            
    else:
        form = MobileForm()
    return render(request, "register_samautkarsh/mobile_verification.html", {"form": form})

# Step 2: OTP Verification
def otp_verification(request):
    message=''
    mobile = request.session.get("mobile")
    if not mobile:
        return redirect("mobile_verification")

    if request.method=='GET':
        mobile=''
        message=''

    if request.method == "POST":
        form = OTPForm(request.POST)
        mobile_number = request.session.get("mobile")
    
        if form.is_valid():
            otp = form.cleaned_data["otp"]
            otp_record = RegisterSamautkarshOtp.objects.filter(mobile=mobile, otp=otp).first()

            if otp_record:
                # Check if the user is already registered
                if RegisterSamautkarshUser.objects.filter(mobile=mobile).exists():
                    return redirect("view_registration") 
                    
                RegisterSamautkarshUser.objects.create(mobile=mobile)  # Save new user
                if request.session.get('role')=='scanner':
                    return redirect('scan_qr')
                if request.session.get("status") =='Approve' or request.session.get("status")=='Reject':
                    return redirect("verify_registration")
                # return redirect('updateregister')
                return redirect("register")
            else:
                message="Invalid OTP. Try again."
                messages.error(request, message )
                return redirect("otp_verification")
    else:
        form = OTPForm()
    return render(request, "register_samautkarsh/otp_verification.html", {"form": form})


def register(request):
    if not request.session.get('mobile'):
         return redirect('otp_verification') 
    mappings={}
    mobile_number = request.session.get('mobile')
    # Fetch professions and prant as lists
    professions = list(ProfessionMaster.objects.values_list("profession_name", flat=True))
    prant = list(PrantMaster.objects.values_list("prant_hindi", flat=True))
    
    # Add to mappings as lists
    mappings['professions'] = professions
    mappings['prant'] = prant
    #print(profession_result)
    request.session.pop('otp_verified', None)
    
    #Pincode Data Extraction
    raw_data = PincodeMaster.objects.values_list("pincode", "nagar_hindi")
    raw_data = PincodeMaster.objects.filter(state="Delhi").values_list("pincode", "nagar_hindi")
    pincode_areas = defaultdict(list)
    delhiPincode=[]
    for pincode, nagar in raw_data:
        pincode_areas[pincode].append(nagar)
        delhiPincode.append(pincode)
    pincode_areas = dict(pincode_areas)
    mappings['pincodeToNagar']=pincode_areas
    mappings['delhiPincodes']=delhiPincode

    raw_data = PincodeMaster.objects.values_list("pincode", "nagar_hindi")
    raw_data = PincodeMaster.objects.exclude(state ="Delhi").values_list("pincode", "state")
    statePincodes=[]
    pincode_areas = defaultdict(list)
    for pincode, nagar in raw_data:
        pincode_areas[pincode].append(nagar)
        statePincodes.append(pincode)
    pincode_areas = dict(pincode_areas)
    mappings['pincodeToState']=pincode_areas
    mappings['statePincodes']=statePincodes


    #dayitv data extraction
    raw_data = DayitvMaster.objects.select_related("ekai_id").values_list("dayitv_name", "ekai_id__ekai_name")
    result = {}
    # Iterate over the data to group by categories
    for item, category in raw_data:
        category = category.lower()  # Convert category to lowercase
        if category not in result:
            result[category] = []  # Initialize a list for the category if it doesn't exist
        result[category].append(item)  # Append the item to the appropriate category list
    # print(result)
    result['ekai_nagar'] = result.pop('nagar')
    mappings['dayitvaMapping'] = result

    #bastiToUpbasti extraction
    raw_data = UpbastiMaster.objects.select_related("basti_id").values_list("upbasti_hindi", "basti_id__basti_hindi")
    result = {}
    # print(raw_data)
    # Iterate over the data to group by categories
    for item, category in raw_data:
        #category = category.lower()  # Convert category to lowercase
        if category not in result:
            result[category] = []  # Initialize a list for the category if it doesn't exist
        result[category].append(item)  # Append the item to the appropriate category list
    mappings['bastiToUpbasti'] = result


    #mandalTOBasti extraction
    raw_data = BastiMaster.objects.select_related("mandal_id").values_list("basti_hindi", "mandal_id__mandal_hindi")
    result = {}
    # Iterate over the data to group by categories
    for item, category in raw_data:
        #category = category.lower()  # Convert category to lowercase
        if category not in result:
            result[category] = []  # Initialize a list for the category if it doesn't exist
        result[category].append(item)  # Append the item to the appropriate category list
    mappings['mandalToBasti'] = result

    #nagarToMandal extraction
    raw_data = MandalMaster.objects.select_related("nagar_id").values_list("mandal_hindi", "nagar_id__nagar_hindi")
    result = {}
    # Iterate over the data to group by categories
    for item, category in raw_data:
        #category = category.lower()  # Convert category to lowercase
        if category not in result:
            result[category] = []  # Initialize a list for the category if it doesn't exist
        result[category].append(item)  # Append the item to the appropriate category list
    mappings['nagarToMandal'] = result

    #jilaToNagar extraction
    raw_data = NagarMaster.objects.select_related("jila_id").values_list("nagar_hindi", "jila_id__jila_hindi")
    result = {}
    # Iterate over the data to group by categories
    for item, category in raw_data:
        #category = category.lower()  # Convert category to lowercase
        if category not in result:
            result[category] = []  # Initialize a list for the category if it doesn't exist
        result[category].append(item)  # Append the item to the appropriate category list
    mappings['jilaToNagar'] = result

    #VibhagToJila extraction
    raw_data = ZilaMaster.objects.select_related("vibhag_id").values_list("jila_hindi", "vibhag_id__vibhag_hindi")
    result = {}
    # Iterate over the data to group by categories
    for item, category in raw_data:
        #category = category.lower()  # Convert category to lowercase
        if category not in result:
            result[category] = []  # Initialize a list for the category if it doesn't exist
        result[category].append(item)  # Append the item to the appropriate category list
    mappings['VibhagToJila'] = result

    #prantToVibhag extraction
    raw_data = VibhagMaster.objects.select_related("prant_id").values_list("vibhag_hindi", "prant_id__prant_hindi")
    result = {}
    # Iterate over the data to group by categories
    for item, category in raw_data:
        #category = category.lower()  # Convert category to lowercase
        if category not in result:
            result[category] = []  # Initialize a list for the category if it doesn't exist
        result[category].append(item)  # Append the item to the appropriate category list
    mappings['prantToVibhag'] = result

    with open("data_mapping.json", "w", encoding="utf-8") as f:
        json.dump(mappings, f, ensure_ascii=False, indent=4)
    
    with open("data_mapping_pincode.json", "w", encoding="utf-8") as f:
        json.dump(pincode_areas, f, ensure_ascii=False, indent=4)
    
    form = RegistrationForm()
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
            form = RegistrationForm(request.POST)
            form.instance.phone_number = mobile_number
            
            if form.is_valid():
                # Set the mobile number from the session in the form
                form.instance.phone_number = mobile_number
                  # Use `form.instance` instead of directly setting form fields
                registration = form.save(commit=True)

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
                return redirect('/')

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
        print(form)
        print('Shelja')
                
        # If no record exists, proceed with registration
        if request.method == 'POST':
            print(request.method)
            print("akash")
            form = EventRegisterForm(request.POST)
            if form.is_valid():
                # Set the mobile number from the session in the form
                  # Use `form.instance` instead of directly setting form fields
                registration = form.save(commit=True)
                
                print(form)
                print(registration)

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
                return redirect('/')

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
        return redirect('otp_verification')
    
    mobile_number = request.session.get('mobile')
    try:
        # Try to get the registration record
        record = RegisterSamautkarshRegistration.objects.get(phone_number=mobile_number)
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
        
        return render(request, 'register_samautkarsh/view_registration.html', context)
        
    except (RegisterSamautkarshRegistration.DoesNotExist, BarcodeScan.DoesNotExist):
        # If no record exists, redirect to registration
        return redirect('register')


# Update Registration Profile Details
def update_register(request):
    if not request.session.get('mobile'):
        return redirect('otp_verification')
    
    mobile_number = request.session.get('mobile')
    mappings = {}
    
    # Fetch professions and prant as lists
    professions = list(ProfessionMaster.objects.values_list("profession_name", flat=True))
    prant = list(PrantMaster.objects.values_list("prant_hindi", flat=True)) 
    # Add to mappings as lists
    mappings['professions'] = professions
    mappings['prant'] = prant

    request.session.pop('otp_verified', None)
    
    #Pincode Data Extraction
    raw_data = PincodeMaster.objects.values_list("pincode", "nagar_hindi")
    raw_data = PincodeMaster.objects.filter(state="Delhi").values_list("pincode", "nagar_hindi")
    pincode_areas = defaultdict(list)
    delhiPincode=[]
    for pincode, nagar in raw_data:
        pincode_areas[pincode].append(nagar)
        delhiPincode.append(pincode)
    pincode_areas = dict(pincode_areas)
    mappings['pincodeToNagar']=pincode_areas
    mappings['delhiPincodes']=delhiPincode

    raw_data = PincodeMaster.objects.values_list("pincode", "nagar_hindi")
    raw_data = PincodeMaster.objects.exclude(state ="Delhi").values_list("pincode", "state")
    statePincodes=[]
    pincode_areas = defaultdict(list)
    for pincode, nagar in raw_data:
        pincode_areas[pincode].append(nagar)
        statePincodes.append(pincode)
    pincode_areas = dict(pincode_areas)
    mappings['pincodeToState']=pincode_areas
    mappings['statePincodes']=statePincodes


    #dayitv data extraction
    raw_data = DayitvMaster.objects.select_related("ekai_id").values_list("dayitv_name", "ekai_id__ekai_name")
    result = {}
    # Iterate over the data to group by categories
    for item, category in raw_data:
        category = category.lower()  # Convert category to lowercase
        if category not in result:
            result[category] = []  # Initialize a list for the category if it doesn't exist
        result[category].append(item)  # Append the item to the appropriate category list
    # print(result)
    result['ekai_nagar'] = result.pop('nagar')
    mappings['dayitvaMapping'] = result

    #bastiToUpbasti extraction
    raw_data = UpbastiMaster.objects.select_related("basti_id").values_list("upbasti_hindi", "basti_id__basti_hindi")
    result = {}
    # print(raw_data)
    # Iterate over the data to group by categories
    for item, category in raw_data:
        #category = category.lower()  # Convert category to lowercase
        if category not in result:
            result[category] = []  # Initialize a list for the category if it doesn't exist
        result[category].append(item)  # Append the item to the appropriate category list
    mappings['bastiToUpbasti'] = result


    #mandalTOBasti extraction
    raw_data = BastiMaster.objects.select_related("mandal_id").values_list("basti_hindi", "mandal_id__mandal_hindi")
    result = {}
    # Iterate over the data to group by categories
    for item, category in raw_data:
        #category = category.lower()  # Convert category to lowercase
        if category not in result:
            result[category] = []  # Initialize a list for the category if it doesn't exist
        result[category].append(item)  # Append the item to the appropriate category list
    mappings['mandalToBasti'] = result

    #nagarToMandal extraction
    raw_data = MandalMaster.objects.select_related("nagar_id").values_list("mandal_hindi", "nagar_id__nagar_hindi")
    result = {}
    # Iterate over the data to group by categories
    for item, category in raw_data:
        #category = category.lower()  # Convert category to lowercase
        if category not in result:
            result[category] = []  # Initialize a list for the category if it doesn't exist
        result[category].append(item)  # Append the item to the appropriate category list
    mappings['nagarToMandal'] = result

    #jilaToNagar extraction
    raw_data = NagarMaster.objects.select_related("jila_id").values_list("nagar_hindi", "jila_id__jila_hindi")
    result = {}
    # Iterate over the data to group by categories
    for item, category in raw_data:
        #category = category.lower()  # Convert category to lowercase
        if category not in result:
            result[category] = []  # Initialize a list for the category if it doesn't exist
        result[category].append(item)  # Append the item to the appropriate category list
    mappings['jilaToNagar'] = result

    #VibhagToJila extraction
    raw_data = ZilaMaster.objects.select_related("vibhag_id").values_list("jila_hindi", "vibhag_id__vibhag_hindi")
    result = {}
    # Iterate over the data to group by categories
    for item, category in raw_data:
        #category = category.lower()  # Convert category to lowercase
        if category not in result:
            result[category] = []  # Initialize a list for the category if it doesn't exist
        result[category].append(item)  # Append the item to the appropriate category list
    mappings['VibhagToJila'] = result

    #prantToVibhag extraction
    raw_data = VibhagMaster.objects.select_related("prant_id").values_list("vibhag_hindi", "prant_id__prant_hindi")
    result = {}
    # Iterate over the data to group by categories
    for item, category in raw_data:
        #category = category.lower()  # Convert category to lowercase
        if category not in result:
            result[category] = []  # Initialize a list for the category if it doesn't exist
        result[category].append(item)  # Append the item to the appropriate category list
    mappings['prantToVibhag'] = result

    try:
        # Get the existing record to update
        record = RegisterSamautkarshRegistration.objects.get(phone_number=mobile_number)
    except RegisterSamautkarshRegistration.DoesNotExist:
        # If no record exists, redirect to registration
        return redirect('register')

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
            return render(request, 'register_samautkarsh/update_register.html', {'form': form,'phone_number': mobile_number, 'mappings': mappings})
    
    # Pre-populate form with existing data for GET request
    form = RegistrationForm(instance=record)
    return render(request, 'register_samautkarsh/update_register.html', {'form': form,'phone_number': mobile_number, 'mappings': mappings})
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
#     return render(request, "register_samautkarsh/scan_qr.html")


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