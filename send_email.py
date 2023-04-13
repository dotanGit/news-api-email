import smtplib
import ssl
import os


def send_email(message):
    host = "smtp.gmail.com"   # host: The hostname or IP address of the SMTP server that you want to connect to.
    port = 465   # port: The port number to use for the SMTP server. For SMTP_SSL, the default port is 465.

    user_name = "MyPythonProtfolio@gmail.com"   # email username - in order to connect to the email that will send the message
    password = os.getenv("PASSWORD")   # app password - in order to connect to the email that will send the message

    receiver = "MyPythonProtfolio@gmail.com"   # the email the receives the message
    context = ssl.create_default_context()   # create the default ssl (secure socket layer) a context is a set of parameters or options that define the security and communication settings for a particular operation or protocol.

    with smtplib.SMTP_SSL(host, port, context=context) as server:   # we use context as key because the order is important and if we want to associate context into context we need to use key
        server.login(user_name, password)
        server.sendmail(user_name, receiver, message)