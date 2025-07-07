# Import necessary libraries
import requests
import random
from django.http import JsonResponse
from collections import defaultdict
import json
from .models import *


# Otp generation and sending function
def send_otp(mobile):
    message=''

    otp = str(random.randint(100000, 999999))
    url = "http://sms.messageindia.in/v2/sendSMS"
    # print(f'Your Mobile Number is: {mobile} and OTP is: {otp}')
    # API parameters
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

    # Sending the GET request
    response = requests.get(url, params=params)
    # Print response
    RegisterSamautkarshOtp.objects.create(mobile=mobile, otp=otp)

# Function to send an SMS to the user after registration
def send_registration_sms(phone_number):
    # Custom message for registration completion
    message = f"Namaste ji, Your Reg. has been completed. Get the QR Code from http://samutkarsh.in/ -- Team Samurkarsh Bharat"
    
    # API URL
    url = "http://sms.messageindia.in/v2/sendSMS"
    
    # API parameters
    params = {
        "username": "utkarshbharatresearch",  # Your API username
        "message": message,  # Message content
        "sendername": "SBRPLR",  # Sender name (approved by provider)
        "smstype": "TRANS",  # Transactional or promotional
        "numbers": phone_number,  # Mobile numbers (comma-separated)
        "apikey": "9fcec71f-f3ee-4b7c-8099-ee8cbc06478b",  # Your API key
        "peid": "1701173858154413324",  # PE ID from provider
        "templateid": "1707173875630312368"  # Template ID from provider
    }
    
    # Sending the GET request
    response = requests.get(url, params=params)
    
    # Handle the response (e.g., log it, check for errors, etc.)
    if response.status_code == 200:
        # print("SMS sent successfully!")
        pass
    else:
        print(f"Failed to send SMS. Status code: {response.status_code}")
    
    # Return the response for further processing if needed
    return response

# Example usage
phone_number = "9876543210"  # Replace with the actual phone number
send_registration_sms(phone_number)


# Function to get registration mappings
def get_registration_mappings(request):
    # if not request.session.get('mobile'):
    #     return JsonResponse({'error': 'Session expired or not verified'}, status=403)

    mappings = {}

    # Example: professions and prant
    mappings['professions'] = list(ProfessionMaster.objects.values_list("profession_name", flat=True))
    mappings['prant'] = list(PrantMaster.objects.values_list("prant_hindi", flat=True))

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

    # You can keep adding others like jilaToNagar, nagarToMandal etc. similarly
    return JsonResponse(mappings, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4})