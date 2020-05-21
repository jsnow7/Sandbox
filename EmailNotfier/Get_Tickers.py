#Alpha Vantage only allows 500 requests per day
# Be careful of this limit especially when considering crypto
# With a portfolio of around 5 stocks refresh should happen every 14 min

#When looking for stocks to buy use closing prices
import smtplib, ssl
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

listOfTickers = ["XRP-USD"]
resistance = [0]
support = [0]
searchStart = ["2019-07-18 14:00:00"]
tickURL = ["https://urlzs.com/gohDA"]

for tick in range(len(listOfTickers)):
    ts = TimeSeries(key='EYDVHI1R1MMTH7TQ', output_format='pandas')
    data, meta_data = ts.get_intraday(symbol=listOfTickers[tick], interval='30min', outputsize='full')
    data = data[data.index >= searchStart[tick]]
    """
    data['4. close'].plot()
    data.info()
    plt.title('Intraday TimeSeries ' + listOfTickers[tick])
    ax = plt.gca()
    ax.invert_xaxis()
    plt.xticks(rotation=30)
    plt.show()
    """
    if data["4. close"].any() > resistance[tick]:
        smtp_server = 'smtp.gmail.com'
        port = 465
        # port = 587

        sender = 'testingemail1777@gmail.com'
        password = 'Testing.snow_1771'

        receiver = '15JaSnow@gmail.com'
        message = """\
                From: {}
                To: {}
                Subject: {} Update 


                Click to see it on Yahoo Finance:
                {}

                """.format("JSnow Trading Inc.", receiver, listOfTickers[tick], tickURL[tick])
        context = ssl.create_default_context()
     
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender, password)
            # print('Successful Connection')
            server.sendmail(sender, receiver, message)
            print("Sent It!")





#First Set up so that you have to manually set Support and Resistance