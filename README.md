# 📲 QR-ERS – QR Code Event Registration System

**QR-ERS** is a smart, end-to-end event registration and access management system designed to **digitize attendee onboarding**, ensure **secure entry** with **QR code scanning**, and enable **real-time participant verification**. The system integrates **OTP-based login**, **SMS & WhatsApp alerts**, and a **role-based dashboard** for organizers and participants.

🌐 [www.samutkarsh.in](http://www.samutkarsh.in)

---

## ✅ Key Features

### 🎫 For Participants:
- Event registration with OTP-based mobile verification
- QR code auto-generated after successful registration
- SMS/WhatsApp confirmation with event and QR details
- Real-time updates on registration and check-in status

### 🧑‍💼 For Event Organizers:
- Admin dashboard to manage participants
- Check-in system with QR code scanner
- Export participant data to Excel
- Real-time attendance and validation logs
- Resend OTPs, bulk messages, and notifications

---

## 🧰 Tech Stack

| Layer       | Technology Used                      |
|-------------|---------------------------------------|
| Frontend    | HTML, CSS, Bootstrap, JavaScript      |
| Backend     | Python, Django, Django REST Framework |
| Database    | PostgreSQL / SQLite                   |
| QR Codes    | `qrcode` Python package               |
| Auth        | OTP-based mobile verification (Session-based) |
| Messaging   | Twilio API / Fast2SMS / WhatsApp API  |
| Others      | Scanner.js, Ajax, jQuery              |

---

## 🖼️ System Flow / Modules

```text
📲 User Mobile Registration
     ↓
🔐 OTP Verification
     ↓
📝 User Profile Registration
     ↓
🛡️ Admin Approval
     ↓
🎟️ QR Code Generation
     ↓
📧 SMS / WhatsApp Notification
     ↓
🛂 QR Code Check-In at Entry Gate
     ↓
📊 Real-time Admin Dashboard with Logs

qr-event-registration-system/
├── account/                       # User registration and login (OTP-based)
├── core/                          # Core event logic and check-in
├── register_samutkarsh/          # Event-specific registration handling
├── scanner_admin/                # QR code scanning admin interface
├── static/                       # CSS, JS, images, QR codes
├── templates/                    # HTML templates
├── media/                        # Generated QR codes and uploads
├── manage.py
├── requirements.txt
└── README.md


# Clone the project
git clone https://github.com/yourusername/qr-event-registration-system.git
cd qr-event-registration-system

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Start the development server
python manage.py runserver

