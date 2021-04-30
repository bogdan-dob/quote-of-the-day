import requests, schedule, time
from credentials import cellphone, twilio_number, account_sid, auth_token
from twilio.rest import Client

response = requests.get("https://zenquotes.io/api/today")
json_response = response.json()[0]
quote = json_response['q']
author = json_response['a']

#formatting of final message
sms_msg = "\"" + quote + "\"\n" + "-" + author

def send_quote(msg):
    client = Client(account_sid, auth_token)
    
    client.messages.create(
        body=msg,
        from_=twilio_number,
        to=cellphone
        )

# send a message every morning
schedule.every().day.at("10:30").do(send_quote, sms_msg)

while True:
    schedule.run_pending()
    time.sleep(10)