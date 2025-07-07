from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import qrcode, json
from django.contrib import messages
from .models import *
from .forms import *
import requests
import random
from django.http import JsonResponse


# Create your views here.
# ----------------------------------------Start User Registration and Login Views -------------------------------------------------
# Register view function to register a new user
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


# OTP sending function to mobile number apis integrations
def send_otp(mobile):
    message=''
    otp = str(random.randint(100000, 999999))
    # print('Your OTP is Here:', otp)
    url = "http://sms.messageindia.in/v2/sendSMS"
    # # API parameters
    params = {
        "username": "utkarshbharatresearch",  # Your API username
        "message": f"Your SAMUTKARSH BHARAT Login OTP: {otp}. Do not share it with anyone. SBRPLI",  # Message content
        "sendername": "SBRPLI",  # Sender name (approved by provider)
        "smstype": "TRANS",  # Transactional or promotional
        "numbers": f"{mobile}",  # Mobile numbers (comma-separated)
        "apikey": "9fcec71f-f3ee-4b7c-8099-ee8cbc06478b",  # Your API key
        "peid": "1701173858154413324",  # PE ID from provider
        "templateid": "1707173874194497085"  # Template ID from provider
    }
    # # Sending the GET request
    response = requests.get(url, params=params)
    # Print(response)
    RegisterSamautkarshOtp.objects.create(mobile=mobile, otp=otp)
   

# Step 1: Check if mobile exists
def scanner_mobile_verification(request):
    message=''
    mobile=''
        
    if request.method == "POST":
        form = MobileForm(request.POST)
        if form.is_valid():
            mobile = form.cleaned_data["mobile"]
            user_exists = RegisterSamautkarshRegistration.objects.filter(phone_number=mobile).exists()
            
            if user_exists:
                send_otp(mobile)
            else:
                messages.error(request, "Mobile number not registered.")
                return redirect("scanner_admin:scanner_verification_mobile")
            
            # Get admin record to extract role_level and role_sublevel
            admin = Admin.objects.filter(mobile=mobile).first()
            request.session["mobile"] = mobile  # Store mobile in session
            request.session['role']='scanner' # Store role in session
            request.session["role"] = admin.role

            if admin:
                request.session["mobile"] = mobile  # Store mobile in session
                request.session["role"] = admin.role
                request.session["role_level"] = str(admin.role_level)
                request.session["role_sublevel"] = str(admin.role_sublevel)
            else:
                messages.error(request, "Admin record not found for this mobile number.")
                return redirect("scanner_admin:scanner_verification_mobile")

            return redirect("scanner_admin:scanner_otp_verify")
    else:
        form = MobileForm()
    return render(request, "mobile_verification.html", {"form": form})

# Step2: OTP Verification functions
def scanner_otp_verification(request):

    message = ''
    mobile = request.session.get("mobile") # Get mobile from session
    role = request.session.get('role')
    role_level = request.session.get('role_level')
    role_sublevel = request.session.get('role_sublevel')
    
    # Redirect if mobile is not in session
    if not mobile:
        messages.warning(request, "Mobile number verification required")
        return redirect("scanner_admin:scanner_verification_mobile")
    
    if request.method == 'GET':
        form = OTPForm()
        return render(request, "otp_verification.html", {"form": form})

    if request.method == "POST":
        form = OTPForm(request.POST)
        if not form.is_valid():
            messages.error(request, "Invalid form submission. Please try again.")
            return redirect("scanner_admin:scanner_otp_verify")
            
        otp = form.cleaned_data["otp"]
        
        try:
            # Verify OTP
            otp_record = RegisterSamautkarshOtp.objects.filter(mobile=mobile, otp=otp).first()
            print(otp_record, "otp record")
            
            if not otp_record:
                messages.error(request, 'Invalid OTP. Please try again.')
                send_otp(mobile)  # Resend OTP
                return redirect("scanner_admin:scanner_otp_verify")
            
            # Check if the user exists
            try:
                user_name = scanner.objects.filter(
                    phone_number=mobile
                ).values_list("scanner_name", flat=True).first()
                
                if not user_name: 
                    messages.warning(request, 'User does not exist.')
                    return redirect("scanner_admin:scanner_verification_mobile")
                
                request.session['name'] = user_name
                
                # Check admin status
                admin = scanner.objects.filter(phone_number=mobile).first()
                if scanner.objects.filter(phone_number=mobile).exists():
                    # print('verifird',admin)
                    return redirect("scanner_admin:scan_qr")
                
                if not admin:
                    messages.warning(request, 'User does not exist.')
                    return redirect("scanner_admin:scanner_verification_mobile")
                
                if not admin:
                    messages.warning(request, 'You do not have admin privileges.')
                    return redirect("scanner_admin:scanner_verification_mobile")
                
                    
            except Exception as user_error:
                messages.error(request, f'Error verifying user: {str(user_error)}')
                return redirect("scanner_admin:scanner_verification_mobile")
                
        except Exception as otp_error:
            messages.error(request, f'Error during OTP verification: {str(otp_error)}')
            return redirect("scanner_admin:scanner_otp_verify")

    return render(request, "otp_verification.html", {"form": form, "message": message})


@csrf_exempt     
def scan_save_qr(request):
    """Saves the scanned QR code data."""
    if request.method == "POST": 
        try:
            data = json.loads(request.body)
            qr_data = data.get("qr_data", "")
            if not qr_data:
                return JsonResponse({
                    'status': 'error',
                    'message': 'No QR data received'
                }, status=400)
                
            user_exists = BarcodeScan.objects.filter(phone_number=qr_data).exists()
            count_number = ScannedPerson.objects.filter(phone_number=qr_data).count()+1
            if user_exists:
                barcodescan = ScannedPerson(
                    phone_number=qr_data, 
                    person_scanned=request.session.get('mobile')
                )
                barcodescan.save()
                return JsonResponse({
                    'status': 'success',
                    'message': f'आपका QR-Code स्कैन हो चुका है! अब तक {count_number} बार स्कैन किया जा चुका है।'
                })
            else:
                return JsonResponse({
                    'status': 'error',
                    'message': 'QR code not registered.'
                }, status=404)
                
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=500)
    
    return JsonResponse({
        'status': 'error',
        'message': 'Invalid request method'
    }, status=405)


@csrf_exempt     
def scan_qr(request):
    role = request.session.get('role')
    return render(request, "scan_qr.html", {"role": role})

def qr_history(request):
    """Displays the history of scanned QR codes."""
    qr_codes = QRCode.objects.order_by("-scanned_at")
    return render(request, "history.html", {"qr_codes": qr_codes})
