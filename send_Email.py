import smtplib
import ssl
from email.message import EmailMessage

subject = "Email from python code"
body = "This is a test email from python project"
sender_email = 'dahamkahawearachchi123@gmail.com'
reciever_email = 'dahamkahawearachchi123@gmail.com'
password = input('Enter a Password: ')

message = EmailMessage()
message["From"] = sender_email
message["To"] = reciever_email
message['Subject'] = subject

html = f"""
<html>
    <body>
        <h1>{subject}</h1>
        </p>{body}</p>
    </body>

</html>
"""

message.add_alternative(html, subtype='html')

context = ssl.create_default_context()

print('Sending Email')

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, reciever_email, message.as_string())

print("Success")