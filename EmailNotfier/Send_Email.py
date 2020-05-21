import smtplib, ssl

smtp_server = 'smtp.gmail.com'
port = 465
#port = 587

sender = 'testingemail1777@gmail.com'
password = 'Testing.snow_1771'
stock = "XRP-USD"

receiver = '15JaSnow@gmail.com'
message = """\
From: {}
To: {}
Subject: {} Update 

Ripple just past listed support!

Click to see it on Yahoo Finance:
https://tinyurl.com/y5934rfq

""".format("JSnow Trading Inc.", receiver, stock)
context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port,context = context) as server:
    server.login(sender, password)
    #print('Successful Connection')
    server.sendmail(sender,receiver, message)
    print("Sent It!")