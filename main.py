import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = input("Subject: ")
msg['From'] = "test"
x = input("Body: ")
msg.set_content(x)
msg['To'] = input('To: ')

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("testingauto4@gmail.com", "testing@1")
server.send_message(msg)
server.quit()
print("Email sent!!")
