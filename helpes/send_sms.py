import smtplib

def send_email(send_email, code):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(user='azizamindjanov14@gmail.com', password='vmrpzhealsmzwquw')
        server.sendmail(from_addr='azizamindjanov14@gmail.com', to_addrs=send_email, msg=code)
        print('Message sent!')

    except Exception as e:
        print(e)