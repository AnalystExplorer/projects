import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject = "An email with attachment from Python"
body = "This is an email with attachment sent from Python"
sender_email = "swatikumari@mba.christuniversity.in"
receiver_email = "ksswati97@gmail.com"
password = "Bangalore@123"

# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email  # Recommended for mass emails

# Add body to email
message.attach(MIMEText(body, "plain"))

filename = "dataset.csv"  # In same directory as script

# Open PDF file in binary mode
with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email    
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Add attachment to message and convert message to string
message.attach(part)
text = message.as_string()

# Log in to server using secure context and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def send_email(email, password, send_to_email, cc_mails, bcc_mails, subject, body, attachment_file_path):
    try:
        # Set up the SMTP server
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587  # SMTP port (587 is for TLS)

        # Create a connection to the server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()

        # Log in to the SMTP server using your credentials
        server.login(email, password)

        # Create the email message
        message = MIMEMultipart()
        message['From'] = email
        message['To'] = send_to_email
        message['Cc'] = cc_mails if cc_mails else ''
        message['Bcc'] = bcc_mails if bcc_mails else ''
        message['Subject'] = subject

        # Attach the body of the email
        message.attach(MIMEText(body, 'plain'))

        # Attach the file
        if attachment_file_path:
            with open(attachment_file_path, "rb") as attachment:
                part = MIMEApplication(attachment.read())
                part.add_header(
                    "Content-Disposition",
                    f"attachment; filename= {attachment_file_path}"
                )
                message.attach(part)

        # Send the email
        recipients = [send_to_email]
        if cc_mails:
            recipients += cc_mails.split(",")
        if bcc_mails:
            recipients += bcc_mails.split(",")

        server.sendmail(email, recipients, message.as_string())

        # Close the connection
        server.quit()

        print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email. Error: {e}")

# Get input from the user
email = input("Enter your email address: ")
password = input("Enter your email password: ")
send_to_email = input("Enter reciever's email address: ")
cc_mails = input("Enter CC email addresses separated by commas, press Enter to skip: ")
bcc_mails = input("Enter BCC email addresses separated by commas, press Enter to skip): ")
subject = "Weekly-report"
body = "Hii,\n PFA report for your references. \n\n Thank you for your time and consideration.\n\n Regards,\n Swati Kumari"
attachment_file_path = input("Enter the file path of the attachment, press Enter to skip: ")

# Send the email
send_email(email, password, send_to_email, cc_mails, bcc_mails, subject, body, attachment_file_path)
