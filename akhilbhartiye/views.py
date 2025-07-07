from samautkarsh.smsapis import send_registration_sms, send_otp, get_chetra_prant_mappings
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from django.conf import settings
from io import BytesIO
from PIL import Image
import qrcode, os
import requests
import base64
from register_samautkarsh.models import *
from register_samautkarsh.forms import *
from akhilbhartiye.models import *
from akhilbhartiye.forms import *


# Create your views here.

# Step 1: Check if mobile exists
def mobile_verification(request):
    message=''
    mobile=''
        
    if request.method == "POST":
        form = MobileForm(request.POST)
        if form.is_valid():
            mobile = form.cleaned_data["mobile"]
            # Check if the mobile number is already registered in AkhilBhartiyaRegistration
            user_exists = AkhilBhartiyaRegistration.objects.filter(mobile=mobile).exists()

            if user_exists:
                # If user exists, show error and do NOT send OTP
                messages.error(request, "Mobile number already registered.")
                return redirect("akhilbhartiye:mobile_verification")
            # scanner_exists = ScannerApprovals.objects.filter(phone_number=mobile,role='scanner').exists()
            # try:
            #     user_exists1= BarcodeScan.objects.filter(phone_number=mobile)
            #     if user_exists1.status=='Approve' or user_exists1.status=='Reject':
            #          request.session["status"] = user_exists1.status
            # except:
            #     pass
            # if user_exists:
            #     send_otp(mobile)
            #     request.session["mobile"] = mobile  # Store mobile in session
            #     return redirect("akhilbhartiye:otp_verification")

            # elif scanner_exists:
            #     send_otp(mobile)
            #     request.session["mobile"] = mobile 
            #     request.session['role']='scanner' # Store mobile in session
            #     return redirect("akhilbhartiye:otp_verification")
            # else:
            send_otp(mobile)
            request.session["mobile"] = mobile  # Store mobile in session
            return redirect("akhilbhartiye:otp_verification")            
    else:
        form = MobileForm()
    return render(request, "mobileverification.html", {"form": form})

# Step 2: OTP Verification
def otp_verification(request):
    mobile = request.session.get("mobile")
    message = ""

    if not mobile:
        return redirect("akhilbhartiye:mobile_verification")

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

                # Check if user is already registered
                if AkhilBhartiyaRegistration.objects.filter(mobile=mobile).exists():
                    return redirect("akhilbhartiye:mobile_verification")
                else:
                    # If user is not registered, redirect to registration page
                    return redirect("akhilbhartiye:akhilregisteration")


            else:
                message = "Invalid OTP. Try again."
                messages.error(request, message)
                return redirect("akhilbhartiye:otp_verification")

    return render(request, "otpverification.html", {"form": form})


# Akhil Bhartiya Registration here.
def AkhilBhartiyaRegisteration(request):
    # Check if mobile number is in session
    mobile_number = request.session.get('mobile')
    if not mobile_number:
        return redirect('akhilbhartiye:otp_verification')

    # Check if a record with the mobile number already exists
    try:
        record = AkhilBhartiyaRegistration.objects.get(mobile=mobile_number)
        return redirect('akhilbhartiye:mobile_verification')
    except AkhilBhartiyaRegistration.DoesNotExist:
        pass  # Proceed to registration

    # Fetch mappings for dropdowns or other data
    mappings = get_chetra_prant_mappings(request)

    if request.method == 'POST':
        form = AkhilBhartiyaRegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.mobile = mobile_number
            # From data save.
            registration.save()
            
            # ✅ Send SMS message
            try:
                url = "http://sms.messageindia.in/v2/sendSMS"
                sms_params = {
                    "username": "utkarshbharatresearch",
                    "message": f"Namaste ji, Your Reg. has been completed. Get the QR Code from https://samutkarsh.in/ Team Samurkarsh Bharat",  # Message content
                    "sendername": "SBRPLW",
                    "smstype": "TRANS",
                    "numbers": mobile_number,
                    "apikey": "9fcec71f-f3ee-4b7c-8099-ee8cbc06478b",
                    "peid": "1701173858154413324",
                    "templateid": "1707173883044603731"
                }

                response = requests.get(url, params=sms_params)
                if response.status_code == 200:
                    print("Registration message sent successfully.")
                else:
                    print(f"Failed to send Registration message. Status code: {response.status_code}")

            except requests.RequestException as e:
                print(f"SMS sending error: {str(e)}")

            # ✅ Send WhatsApp message
            try:
                url = "http://148.251.129.118/wapp/api/send"
                # API key and message details
                params = {
                "apikey": "747f01ec1e574d74bb6f557c6d304692",  # Your API key
                "mobile": mobile_number,  # Comma-separated mobile numbers
                "msg": "❍❍❍❖❖ केशवकुंज दर्शन ❖❖❍❍❍\n\n'⊰᯽⊱┈─╌❊ ⚜️ ❊╌─┈⊰᯽⊱'\n\nआपका नाम कार्यक्रम हेतु पंजीकृत हुआ है। केशवकुंज दर्शन हेतु आप सादर आमंत्रित हैं।\n\nसुरक्षा कारणों से आपकी सुविधा हेतु कार्यक्रम में प्रवेश अनुमति हेतु QR कोड संलग्न है।\n\nकृपया ध्यान दें ..!! \n\n👉 आपके जिले/विभाग के लिए जो दिन निश्चित हुआ है, उसी दिन आपका आना अपेक्षित है।\n\n👉 प्रवेश द्वार पर QR Code दिखाना आवश्यक है।\n\n👉कृपया अपना पहचान पत्र अपने साथ अवश्य लाएं\n\nविशेष :- कार्यक्रम स्थल पर सुविधा पूर्वक पहुंचने के लिए कृपया Metro का प्रयोग कर झंडेवालान मेट्रो स्टेशन पर उतरें।\n\nनिवेदक\n\nश्री केशव स्मारक समिति, दिल्ली"
                }
                # Sending the GET request
                response = requests.get(url, params=params)
                if response.status_code == 200:
                    print("WhatsApp message sent successfully.")
                else:
                    print(f"Failed to send WhatsApp message. Status code: {response.status_code}")
            except requests.RequestException as e:
                print(f"Error sending WhatsApp message: {str(e)}")
                

            # Clear session and redirect
            request.session.flush()
            return redirect('/')
        else:
            print(form.errors)  # Debug only; remove or log properly in production
    else:
        form = AkhilBhartiyaRegistrationForm()

    context = {'form': form, 'phone_number': mobile_number, 'mappings': mappings}
    # Render the registration form
    return render(request, 'akhil_bhartiya_registration.html', context)


# Logout Function
def user_logout(request):
    # Flush the session
    request.session.flush()
    logout(request)
    return redirect('/')