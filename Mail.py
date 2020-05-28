# Python code to illustrate Sending mail from  
# your Gmail account  
import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import socket
socket.getaddrinfo('localhost', 8080)

  
class SendMail:
    def mail(str,email):
        # creates SMTP session 
        s = smtplib.SMTP('smtp.gmail.com', 587)   

        
        # start TLS for security 
        s.starttls() 
        
        # Authentication 
        s.login("Sender_Email_ID", "Password") 
        
        # message to be sent
        message=str
        #m="""Your password for the account in Agriculture Yield Enhancement System is: %s"""%(message) 
        #print (m)
        
        # sending the mail 
        s.sendmail("Receiver_email_id", email, message) 
        
        # terminating the session 
        s.quit() 
