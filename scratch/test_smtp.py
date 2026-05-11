import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

def test_email():
    SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
    SMTP_PORT = int(os.getenv('SMTP_PORT', 587))
    SMTP_EMAIL = os.getenv('SMTP_EMAIL', '')
    SMTP_PASSWORD = os.getenv('SMTP_PASSWORD', '')

    print(f"Testing SMTP with {SMTP_EMAIL} on {SMTP_SERVER}:{SMTP_PORT}...")
    
    if not SMTP_EMAIL or not SMTP_PASSWORD:
        print("Error: SMTP_EMAIL or SMTP_PASSWORD not set in .env")
        return

    msg = MIMEMultipart()
    msg['From'] = SMTP_EMAIL
    msg['To'] = SMTP_EMAIL # Send to self
    msg['Subject'] = "Test ParticipARD Email"
    msg.attach(MIMEText("This is a test email from ParticipARD scratch script.", 'plain'))

    try:
        print("Connecting to server...")
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        print("Starting TLS...")
        server.starttls()
        print("Logging in...")
        server.login(SMTP_EMAIL, SMTP_PASSWORD)
        print("Sending message...")
        server.send_message(msg)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"FAILED to send email: {e}")

if __name__ == "__main__":
    test_email()
