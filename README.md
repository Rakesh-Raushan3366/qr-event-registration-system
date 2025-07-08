# 📲 QR-ERS – QR Code Event Registration System

A **secure, full-stack web platform** designed to **digitize event registrations**, improve **check-in verification**, and boost **communication** using modern technologies like **QR codes**, **OTP-based login**, **SMS/Email/WhatsApp notifications**, and **real-time QR scanning**.

🛠️ **Duration**: Jan 2025 – May 2025  
👨‍💻 **Role**: Full Stack Developer  
🌐 **Live Demo**: [www.samutkarsh.in](http://www.samutkarsh.in)

---

## 🚀 Project Overview

QR-ERS (QR Code Event Registration System) was built to **eliminate manual registration processes**, **enhance entry security**, and ensure **real-time participant management**. It serves as a comprehensive solution for both **event attendees and organizers**, streamlining everything from signup to on-site QR code scanning.

---

## ✅ Key Features

### 📝 Registration & Authentication
- 🧾 **Online Registration**: Secure multi-step form to capture participant & organization details.
- 🔐 **OTP-Based Login**: Mobile verification with Twilio/MSG91 for login & registration.
- 📩 **Email Notifications**: Auto-send confirmation emails with embedded QR codes.
- 📲 **WhatsApp Alerts**: Post-registration updates & QR codes sent via WhatsApp Cloud API.

### 🎯 QR Code Generation & Delivery
- 🖼️ **Unique QR Creation**: QR codes generated using Python's `qrcode` and linked to participant ID.
- 📧 **Multi-Channel Delivery**: QR sent via Email, SMS, and WhatsApp for easy access.
- 💾 **Auto-Save**: QR codes stored securely on the server and linked in admin view.

### 🎫 Real-Time QR Code Scanning
- 🖥️ **Browser-Based Scanner**: Integrated `Scanner.js` to allow staff to scan via webcam or mobile.
- ⚡ **Live Entry Validation**: Every scan is instantly checked via Django API endpoint.
- 🚦 **Success/Fail UI**: Bootstrap-powered modals provide visual feedback during scan.

### 🛠️ Admin & Analytics Dashboard
- 📌 **Live Metrics**: Track number of registrations, check-ins, and no-shows in real time.
- 📤 **Data Export**: Download participant data in Excel/CSV formats.
- 🧾 **Participant Status View**: Admins can view and edit participant statuses.
- 🧠 **Approval System**: Manually approve or block user registrations before QR generation.

---

## 🔐 Security & UX

- 🧩 **Duplicate Entry Prevention**: Users uniquely identified via mobile/email.
- 🔐 **Session-Based OTP Expiry**: Tokens expire securely after use.
- 🧪 **CSRF & Form Protection**: Django middleware safeguards all form submissions.
- 📱 **Fully Responsive UI**: Built with Bootstrap 5 for all screen sizes.

---

## 🧰 Tech Stack

| Layer        | Tools / Frameworks                                |
|--------------|----------------------------------------------------|
| Frontend     | HTML, CSS, Bootstrap 5, JavaScript, jQuery         |
| Backend      | Python, Django, Django REST Framework              |
| Database     | MySQL / SQLite                                |
| QR Code      | `qrcode` (Python library)                          |
| Messaging    | Twilio / MSG91 for SMS OTP, WhatsApp Cloud API     |
| Scanning     | `Scanner.js` (web-based QR code scanner)           |
| Auth         | Session-based OTP, Django User Auth, CSRF tokens   |

---

## 🧱 Folder Structure



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

