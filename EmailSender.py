import smtplib
import ssl
from email.message import EmailMessage

EMAIL = "amityaduvanshi1858@gmail.com"
APP_PASSWORD = "vtqg bigh ahdm mplb"
RECEIVER = "amityadavnkt@gmail.com"
msg = EmailMessage()
msg["From"] = EMAIL
msg["To"]= RECEIVER
msg["Subject"]= "HANDS ON PYTHON"
msg.set_content("This email is shared by python code")
context= ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465,context=context) as server:
    server.login(EMAIL,APP_PASSWORD)
    server.send_message(msg)