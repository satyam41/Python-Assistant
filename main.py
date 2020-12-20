import smtplib
from email.message import EmailMessage


def sendEmail(reciverAddress, subject, message):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('thesatyam10@gmail.com', '1912025113')
    email = EmailMessage()
    email['From'] = 'thesatyam10@gmail.com'
    email['To'] = reciverAddress
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)
    print("Your message is sent.")


from_ = input("Enter reciver address: ")
subject = input("Enter subject of the email: ")
msg = input("Enter your message: ")
sendEmail(from_, subject, msg)
