import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email account credentials
sender_email = "test@ghost-project.site"
display_email = "test@ghost-project.site"
mail_password = "dP27aHzZ13E4"
receiver_email = "juliusdoyungan@gmail.com"
smtp_server = "smtp.zoho.com"
smtp_port = 587

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