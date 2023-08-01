#import all required libraries
import streamlit as st 
import smtplib as s 
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email import encoders
from email.mime.base import MIMEBase
import environ
from os.path import join,dirname, abspath

env = environ.Env()

env.read_env(env.str(
    'ENV_PATH',
    join(dirname(dirname(abspath(__file__))), '.env'
         )
))

SMTP_SERVER_ADDRESS = os.environ.get('SMTP_SERVER_ADDRESS')
PORT = os.environ.get('PORT')
SENDER_PASSWORD = os.environ.get('SENDER_PASSWORD')
SENDER_ADDRESS = os.environ.get('SENDER_ADDRESS')

SENDER_ADDRESS = "swatikumari@mba.christuniversity.in"
PORT = 587
SMTP_SERVER_ADDRESS = "smtp.gmail.com"
SENDER_PASSWORD = "Bangalore@123"




#define function to create message
def send_email(sender,receiver, smtp_server, smtp_port,email_message,subject,attachment=None):
    
    
    message = MIMEMultipart()
    message['TO'] = receiver
    message['Subject'] = subject
    message.attach(MIMEText(email_message,'plain','utf-8'))
    
    if attachment:
        att=MIMEApplication(attachment.read(),_subtype="text")
        att.add_header('content-Disposition', 'attachment', filename=attachment.name)
        message.attach(att)
        
    
    
#define function to create form
def main():
    with st.form("Email Form"):
        subject = st.text_input(label='Subject', placeholder="Please enter of your email subject")
        
        fullName = st.text_input(label = 'Full Name',placeholder="Please Enter your full name")
        rcv_email = st.text_input(label= ' Reciever Email Id', placeholder="Please Enter receiver email id")
        text = st.text_input(label='Email Text', placeholder="Please enter your text here")
        upload_file = st.file_uploader("attachment")
        submit_res = st.form_submit_button(label='send')
        

   if st.button("Send Email"):
            try:
                connection=s.SMTP('smtp.gmail.com',587)
                connection.starttls()
                connection.login(email_sender,password)
                message="Subject:{}\n\n{}".format(subject,body)
                connection.sendmail(email_sender,
                                    email_reciever,
                                    fl,
                                    message)
                connection.quit()
                st.success("Email Send Successfully.")
                #speak("Email Send Successfully.")
            except Exception as e:
                if email_sender=="":
                    st.error("Please Fill User Email Field")
                    #speak("Please Fill User Email Field")
                elif password=="":
                    st.error("please Fill Password Field")
                    #speak("Please Fill password Field")
                elif email_reciever=="":
                    st.error("Please Fill Reciever Email Field")
                    #speak("Please Fill Reciever Email Field")
                else:
                    a=os.system("ping www.google.com")
                    if a==1:
                        st.error("Please Connect Your Internet connection")
                        #speak("Please Connect Your Internet connection")
                    else:
                        st.error("Wrong Email or Password-!")
                        #speak("Wrong Email or Password.!")
            else:
                st.markdown("this application is developed by####")
    

if __name__ == "__main__":
    main()
