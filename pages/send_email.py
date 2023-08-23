import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import streamlit as st


#remove watermark
hide_st_style = """<style>
footer {visibility: hidden;}
</style>"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# Streamlit file uploader
filename = st.file_uploader(":file_folder: Upload a file", type=(["csv","txt","xlsx","xls"]))
receiver_email = st.text_input("Enter receiver email-")
cc_mails = st.text_input("Enter cc email-")
bcc_mails = st.text_input("Enter bcc email-")
smtp_password = st.text_input("Enter your password",type='password')


if st.button("Send Email"):
# Assuming you have an SMTP server to send emails
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "swatikumari@mba.christuniversity.in"
    body = "Hii,\n PFA report for your references. \n\n Thank you for your time and consideration.\n\n Regards,\n Swati Kumari"
    

    if filename is not None:
    # Create a MIME message
       msg = MIMEMultipart()
       msg["From"] = sender_email
       msg["To"] = receiver_email
       msg['Cc'] = cc_mails if cc_mails else ''
       msg['Bcc'] = bcc_mails if bcc_mails else ''
       msg["Subject"] = "Test-Email"
       
       # Attach the body of the email
       msg.attach(MIMEText(body, 'plain'))

    # Open the uploaded file in binary mode
       with filename:
        # Attach the file as application/octet-stream
          part = MIMEBase("application", "octet-stream")
          part.set_payload(filename.read())
          encoders.encode_base64(part)
          part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename.name}",
        )
          msg.attach(part)
          
    recipients = [receiver_email]
    if cc_mails:
            recipients += cc_mails.split(",")
    if bcc_mails:
            recipients += bcc_mails.split(",")

    # Connect to the SMTP server and send the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, smtp_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        st.write("Email sent successfully!")
    except Exception as e:
        st.error(f"An error occurred: {e}")
