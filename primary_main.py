import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.utils import formataddr

from file_picker import browse_file #module for file_picker


"""
# Email account credentials
sender_email = input("Email sending email account: ")
display_email = input("Enter email that will show it From: ")
mail_password = input("Enter email password : ")
receiver_email = input("Email receiving email account : ")
smtp_server = input("Email SMTP server (e.g., smtp.gmail.com) : ")
smtp_port = int(input("Enter SMTP port #: "))
"""

#attempt to insert browsefile
file_path = browse_file()

# Replace input function for the meantime since I'll be using the same email domain on testing phase
sender_email = "test@ghost-project.site"
display_email = "ghost@microsoft.com"
mail_password = "dP27aHzZ13E4"
receiver_email = "juliusdoyungan@gmail.com"
smtp_server = "smtp.zoho.com"
smtp_port = 587

# Create the email
msg = MIMEMultipart()
msg["From"] = formataddr((display_email, sender_email)) #A spoofing tactic but if the receipient was careful it's easy to detect
msg["To"] = receiver_email
msg["Subject"] = "Test Email from Python"

# Email body
body = input("Type your message here: ")
msg.attach(MIMEText(body, "plain"))

# Attach the document
if file_path:
    with open(file_path, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename={file_path.split('/')[-1]}")
    msg.attach(part)

try:
    # Connect to the server (example: Gmail SMTP)
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.ehlo()
    server.starttls()  # Secure the connection
    server.login(sender_email, mail_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")
finally:
    server.quit()