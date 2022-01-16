import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = ""  # Enter your address
receiver_email = ""  # Enter receiver address
password = ""
messageConfirm = """\
Subject: Confirmation mail

This message is to confirm you have registered successfully ,uname::: """

messageVerify = """\
Subject: verification mail

This message is to verify your password change your otp is :: """

def send_mail(reciever_mail,msg,flag):
    context = ssl.create_default_context()
    if flag == 0:
        message = messageConfirm+msg+"."
    if flag == 1:
        message = messageVerify+msg+"."
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, reciever_mail, message)
