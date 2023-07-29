import streamlit as st 
import smtplib as s 
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email import encoders
from email.mime.base import MIMEBase

def main():
    st.title("Email Sender Web Application")
    st.write("Build with streamlit and python")
    #activities=["send Email","about"]
    #choice=st.sidebar.selectbox("select activities", activities)
    #if choice== "send email":
        
    email_sender=st.text_input("Enter User Email - ")
    password= st.text_input("Enter User Password-",type="password")
    email_reciever=st.text_input("Enter Reciever Email- ")
    subject=st.text_input("your Email Subject- ")
    body=st.text_area("Your Email body- ")
    #upload your database
    fl=st.file_uploader(":file_folder: Upload a file to attach in the email", type=(["csv","txt","xlsx","xls"]))

    
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