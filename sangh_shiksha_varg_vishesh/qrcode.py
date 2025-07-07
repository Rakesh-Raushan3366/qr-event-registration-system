import os
import base64
import qrcode
from io import BytesIO
from PIL import Image
from django.conf import settings
from .models import *

# This function generates a QR code for a given registration object. It encodes the registration details into the QR code and saves it as an image file.

def generate_qr_data(name, phone, nagar, dayitv, ekai, state=None):
    """Generate the data string to be encoded in the QR code."""
    data = f"Name: {name}, Phone Number: {phone}, Nagar: {nagar}"
    if state:
        data += f", State: {state}"
    data += f", Dayitv: {dayitv}, Ekai: {ekai}"
    return base64.b64encode(data.encode()).decode()

def create_qr_code(qr_data, logo_path=None):
    """Create a QR code image with optional logo."""
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(qr_data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill='black', back_color='white').convert('RGBA')
    
    if logo_path and os.path.exists(logo_path):
        logo = Image.open(logo_path).convert("RGBA")
        qr_size = qr_img.size[0]
        logo_size = qr_size // 8
        logo = logo.resize((logo_size, logo_size), Image.LANCZOS)
        
        logo_x = (qr_img.size[0] - logo.size[0]) // 2
        logo_y = (qr_img.size[1] - logo.size[1]) // 2
        qr_img.paste(logo, (logo_x, logo_y), logo)
    
    return qr_img

def save_qr_code(qr_img, phone_number):
    """Save QR code to the appropriate directory."""
    qr_directory = os.path.join(settings.BASE_DIR, 'register_samautkarsh', 'static', 'QRCodes')
    os.makedirs(qr_directory, exist_ok=True)
    
    qr_filename = os.path.join(qr_directory, f"{phone_number}.jpg")
    
    qr_buffer = BytesIO()
    qr_img.save(qr_buffer, format="PNG")
    qr_buffer.seek(0)
    
    with open(qr_filename, 'wb') as f:
        f.write(qr_buffer.read())
    
    return qr_filename

def get_logo_path():
    """Get the path to the logo image."""
    return os.path.join(settings.BASE_DIR, 'register_samautkarsh/static/register_samautkarsh/assets/img', 'logo.jpg')

def process_registration_qr(registration):
    """Main function to handle QR code generation for a registration."""
    try:
        # Try to get state from pincode
        pincode = PincodeMaster.objects.filter(pincode=registration.pincode, nagar_hindi=registration.nagar)
        state = None
    except PincodeMaster.DoesNotExist:
        state = registration.state or ''
    
    qr_data = generate_qr_data(
        name=registration.name,
        phone=registration.phone_number,
        nagar=registration.nagar,
        dayitv=registration.dayitv,
        ekai=registration.ekai,
        state=state
    )
    
    qr_img = create_qr_code(qr_data, get_logo_path())
    qr_filename = save_qr_code(qr_img, registration.phone_number)
    
    return qr_filename