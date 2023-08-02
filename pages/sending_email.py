import streamlit as st 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os

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
email = st.text_input("Enter your email address: ")
password = st.text_input("Enter your email password: ")
send_to_email = st.text_input("Enter reciever's email address: ")
cc_mails = st.text_input("Enter CC email addresses separated by commas, press Enter to skip: ")
bcc_mails = st.text_input("Enter BCC email addresses separated by commas, press Enter to skip): ")
subject = "Weekly-report"
body = "Hii,\n PFA report for your references. \n\n Thank you for your time and consideration.\n\n Regards,\n Swati Kumari"
attachment_file_path = st.file_uploader("Enter the file path of the attachment, press Enter to skip: ")
if st.button("Send Email"):
    try:
        st.success("Email Send Successfully.")
                #speak("Email Send Successfully.")
    except Exception as e:
        if email=="":
            st.error("Please Fill User Email Field")
                    #speak("Please Fill User Email Field")
        elif password=="":
            st.error("please Fill Password Field")
                    #speak("Please Fill password Field")
        elif send_to_email=="":
            st.error("Please Fill Reciever Email Field")
                    #speak("Please Fill Reciever Email Field")
        else:
            a= os.system("ping www.google.com")
            if a==1:
                st.error("Please Connect Your Internet connection")
                        #speak("Please Connect Your Internet connection")
            else:
                st.error("Wrong Email or Password-!")
                        #speak("Wrong Email or Password.!")
    else:
        st.markdown("this application is developed by####")

# Send the email
send_email(email, password, send_to_email, cc_mails, bcc_mails, subject, body, attachment_file_path)
