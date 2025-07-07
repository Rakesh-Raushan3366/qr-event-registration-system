import qrcode

# Data to encode
data = "SHELJA JINDAL"  # Replace with your desired text or URL

# Generate QR code
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR code (1 is the smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in the QR code grid
    border=4,  # Thickness of the border (minimum is 4)
)
qr.add_data(data)
qr.make(fit=True)

# Create an image of the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code as an image
img.save("qrcode.png")

print("QR code saved as 'qrcode.png'")

import qrcode
from PIL import Image, ImageDraw, ImageFont

# Data to encode and text to display
data = "SHELJA JINDAL"  # Replace with your desired URL or text
text_below = "Scan this code for more info"  # Replace with your desired text

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)
qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")  # Ensure RGB mode

# Create a blank canvas larger than the QR code to fit the text below
qr_width, qr_height = qr_img.size
font_size = 20
canvas_height = qr_height + font_size + 20
canvas = Image.new("RGB", (qr_width, canvas_height), "white")

# Paste QR code onto the canvas
canvas.paste(qr_img, (0, 0))

# Draw the text below the QR code
draw = ImageDraw.Draw(canvas)
try:
    # Load a TrueType font
    font = ImageFont.truetype("arial.ttf", font_size)
except IOError:
    # Fallback to default font
    font = ImageFont.load_default()

# Calculate text width and position it in the center
text_bbox = draw.textbbox((0, 0), text_below, font=font)  # Get bounding box of text
text_width = text_bbox[2] - text_bbox[0]  # Width of the text
text_x = (qr_width - text_width) // 2
text_y = qr_height + 10  # Position below the QR code

# Add the text to the canvas
draw.text((text_x, text_y), text_below, fill="black", font=font)

# Save the final image
canvas.save("qrcode_with_text.png")

print("QR code with text saved as 'qrcode_with_text.png'")


