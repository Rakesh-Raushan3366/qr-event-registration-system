import imgkit

# Define input HTML content
html_content = """
<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>प्रवेश पास</title>
</head>
<body style="text-align:center; font-family:Arial, sans-serif;">
    <h2>श्री केशव स्मारक समिति</h2>
    <h1 style="color: red;">केशव कुंज प्रवेशोत्सव</h1>
    <h3>प्रवेश पास</h3>
    <img src="image.png" alt="प्रवेश पास" style="max-width:90%; height:auto;">
    <p style="color: red; font-weight: bold;">विशेष: कृपया किसी के साथ साझा न करें।</p>
</body>
</html>
"""

# Save the HTML file
html_file = "pass.html"
with open(html_file, "w", encoding="utf-8") as file:
    file.write(html_content)

# Convert HTML to Image
imgkit.from_file(html_file, "pass.png")

print("Image saved as pass.png")


url = "http://148.251.129.118/wapp/api/send"

            # API key and message details
params = {
    "apikey": "747f01ec1e574d74bb6f557c6d304692",  # Your API key
    "mobile": '8287769377',
    "media": "pass.png"   # Comma-separated mobile numbers
                }

# Sending the GET request
response = requests.get(url, params=params)

# Print response
print("Status Code:", response.status_code)
print("Response:", response.text)
