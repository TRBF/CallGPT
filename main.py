import os
import flask 
import dotenv
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse

app = flask.Flask(__name__) 
dotenv.load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_number = os.getenv("TWILIO_PHONE_NUMBER")
client = Client(account_sid, auth_token)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__=="__main__":
    app.run()

@app.route("/answer", methods=['GET', 'POST'])
def answer_call():
    resp = VoiceResponse()
    resp.say("Thank you for calling! Have a great day.", voice='Polly.Amy')


    return str(resp)
