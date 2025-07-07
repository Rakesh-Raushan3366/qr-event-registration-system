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
from register_samautkarsh.smsapis import send_registration_sms, get_registration_mappings

# Create your views here.

def KaryakartaVikasVargPrathamSamanyaRegistration(request):
    if not request.session.get('mobile'):
         return redirect('otp_verification') 
    # Check if the mobile number is in the session
    mobile_number = request.session.get('mobile')
    # Fetch mappings from the function
    mappings = get_registration_mappings(request)

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
                return render(request, 'register_samautkarsh/KaryakartaVikasVargPrathamSamanyaRegistration.html', {'form': form, 'phone_number': mobile_number, 'mappings':mappings})
    # Render the registration form if the record does not exist or on first load
    return render(request, 'register_samautkarsh/KaryakartaVikasVargPrathamSamanyaRegistration.html', {'form': form, 'phone_number': mobile_number, 'mappings':mappings})



# view Registration informations!
def KaryakartaVikasVargPrathamSamanyaViewRegistration(request):
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
        
        return render(request, 'register_samautkarsh/KaryakartaVikasVargPrathamSamanyaViewRegistration.html', context)
        
    except (RegisterSamautkarshRegistration.DoesNotExist, BarcodeScan.DoesNotExist):
        # If no record exists, redirect to registration
        return redirect('karyakartavikasvargprathamsamanyaregistration')


# Update Registration Profile Details
def KaryakartaVikasVargPrathamSamanyaUpdateRegistration(request):
    if not request.session.get('mobile'):
        return redirect('otp_verification')
    
    mobile_number = request.session.get('mobile')
    # Fetch mappings from the function
    mappings = get_registration_mappings()

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
            return render(request, 'register_samautkarsh/KaryakartaVikasVargPrathamSamanyaUpdateRegistration.html', {'form': form,'phone_number': mobile_number, 'mappings': mappings})
    
    # Pre-populate form with existing data for GET request
    form = RegistrationForm(instance=record)
    return render(request, 'register_samautkarsh/KaryakartaVikasVargPrathamSamanyaUpdateRegistration', {'form': form,'phone_number': mobile_number, 'mappings': mappings})
#  End Update Registration Profile Details


# Logout Function
def user_logout(request):
    # Flush the session
    request.session.flush()
    logout(request)
    return redirect('/')