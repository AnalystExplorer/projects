import streamlit as st
import smtplib as s
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email import encoders
from email.mime.base import MIMEBase

def email_send(sender_email,sender_pwd,reciever_email,smtp_server,subject,email_message,attachment_file=None):
    try:
        #setup the smtp server
        smtp_server = 'smtp.gmail.com'
        port=587
        #create connection to server
        server = s.SMTP(smtp_server, port)
        server.starttls()
        
        #login to the smtp server using sender email and pwd
        server.login(sender_email,sender_pwd)
        
        #create the email message
        message=MIMEMultipart()
        message['from']=sender_email
        message['to']=reciever_email
        message['subject']=subject
        message['message']=email_message
        
        #attach the body of the mail
        message.attach(MIMEText('email_message','plain'))
        
        # Attach the file
        if attachment_file:
            with open(attachment_file, "rb") as attachment:
                part = MIMEApplication(attachment.read())
                part.add_header(
                    "Content-Disposition",
                    f"attachment; filename= {attachment_file}"
                )
                message.attach(part)
                
                
        
        server.sendmail(sender_email, reciever_email, message.as_string())

        # Close the connection
        server.quit()

        st.success("Email sent successfully!")
        
    except Exception as e:
        st.success(f"Failed to send email. Error: {e}")
        

#create form to take inputs from user

def main():
    st.title("Email form")
    sender_email = st.text_input("Enter sender Email-")
    sender_pwd = st.text_input("Enter sender password-",type="password")
    reciever_email = st.text_input("Enter reciever email id- ")
    subject = st.text_input("enter subject-")
    email_message = st.text_area("Enter the email body- ")
    attachment_file = st.file_uploader("Enter the file to upload ")
    if st.button("Send Email"):
        if sender_email=="":
                    st.error("Please Fill User Email Field")
                    #speak("Please Fill User Email Field")
        elif sender_pwd=="":
                    st.error("please Fill Password Field")
                    #speak("Please Fill password Field")
        elif reciever_email=="":
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
    
    email_send(sender_email,sender_pwd,reciever_email,subject,email_message,attachment_file)
    
    
if __name__ == '__main__':
    main()
    



        

 
 
    
    
