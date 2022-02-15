from email import message
from flask import Flask, request
import requests
import json
import os
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

account_sid = os.environ.get('account_sid')
auth_token = os.environ.get('auth_token')
client = Client(account_sid, auth_token)



@app.route("/")
def index():
    req = requests.get('https://api.itbook.store/1.0/search/mongodb')
    # print(req.content)
    data = json.loads(req.content)

    for book in data['books']:
        # print(book['title'], book['price'], book['url'])
        mess = str(book['title'])
        url = str(book['url'])
        price = str(book['price'])
        message = client.messages.create(to=os.environ.get('receiver_no'),
                                        from_=os.environ.get('sender_no'),
                                        body= "Name: "+ mess + "\nPrice: " + price +"\nUrl: " + url)
    return data


