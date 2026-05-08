import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email account credentials
sender_email = input("Email sending email account: ")
display_email = input("Enter email that will show it From: ")
mail_password = input("Enter email password : ")
receiver_email = input("Email receiving email account : ")
smtp_server = input("Email SMTP server (e.g., smtp.gmail.com) : ")
smtp_port = int(input("Enter SMTP port #: "))

# Create the email
msg = MIMEMultipart()
msg["From"] = display_email
msg["To"] = receiver_email
msg["Subject"] = "Test Email from Python"

# Email body
body = "Hello, this is a test email sent from Python!"
msg.attach(MIMEText(body, "plain"))

try:
    # Connect to the server (example: Gmail SMTP)
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Secure the connection
    server.login(sender_email, mail_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")
finally:
    server.quit()