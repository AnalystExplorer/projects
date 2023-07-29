import streamlit as st
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
        server.set_debuglevel(1)

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

        st.success("Email sent successfully!")

    except Exception as e:
        st.error(f"Failed to send email. Error: {e}")

# Streamlit app
def main():
    st.title("Email Sender App")

    # Get input from the user
    email = st.text_input("Enter your email address:")
    password = st.text_input("Enter your email password:", type="password")
    send_to_email = st.text_input("Enter the receiver's email address:")
    cc_mails = st.text_input("Enter CC email addresses separated by commas (optional):")
    bcc_mails = st.text_input("Enter BCC email addresses separated by commas (optional):")
    subject = st.text_input("Enter the email subject:")
    body = st.text_area("Enter the email body:")
    attachment_file_path = st.text_input("Enter the file path of the attachment (optional):")

    if st.button("Send Email"):
        # Send the email
        send_email(email, 
                   password, 
                   send_to_email, 
                   cc_mails,
                   bcc_mails, 
                   subject,
                   body,
                   attachment_file_path)

if __name__ == "__main__":
    main()
