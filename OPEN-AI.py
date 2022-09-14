from crypt import methods
from warnings import catch_warnings
from flask import Flask,request
import flask
import openai
from flask_restful import Api,Resource

#Init
app =   Flask(__name__)
api =   Api(app)

#OPENAI CREDENTIALS
openai.api_key = "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"

 #Functions  
class correct_sentence(Resource):
    def post(self):
        try:
            request_body=request.json
            A=request_body["data"]


            gpt_prompt ="Correct this to standard English:\n\n"+ A
            response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=gpt_prompt,
            temperature=0.5,
            max_tokens=256,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
            )
            to_return=response

            return to_return,200
        except:
            return ({"ERROR":"Error Occured"}),500




class classification(Resource):
    def post(self):
        try:
            request_body=request.json
            A=request_body["data"]


            response = openai.Completion.create(
            model="text-davinci-002",
            prompt="Decide whether a Tweet's sentiment is positive, neutral, or negative.\n\nTweet: "+A+"\nSentiment:",
            temperature=0,
            max_tokens=60,
            top_p=1,
            frequency_penalty=0.5,
            presence_penalty=0
            )
            to_return=response

            return to_return,200
        except:
            return ({"ERROR":"Error Occured"}),500

class idea(Resource):
    def post(self):
        try:
            request_body=request.json
            A=request_body["data"]


            response = openai.Completion.create(
            model="text-davinci-002",
            prompt=A,
            temperature=0.6,
            max_tokens=150,
            top_p=1,
            frequency_penalty=1,
            presence_penalty=1
            )
            to_return=response

            return to_return,200
        except:
            return ({"ERROR":"Error Occured"}),500

class translate(Resource):
    def post(self):
        try:
            request_body=request.json
            A=request_body["data"]


            response = openai.Completion.create(
            model="text-davinci-002",
            prompt="Translate this into 1. French, 2. Spanish, 3. Japanese, 4. Russian, 5. Arabic, 6. Chinese and 7. Telegu:\n\n"+A+"\n\n.",
            temperature=0.3,
            max_tokens=100,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )
            to_return=response

            return to_return,200
        except:
            return ({"ERROR":"Error Occured"}),500

class emoji(Resource):
    def post(self):
        try:
            request_body=request.json
            A=request_body["data"]

            response = openai.Completion.create(
            model="text-davinci-002",
            prompt="Convert movie titles into emoji.\n\nBack to the Future: 👨👴🚗🕒 \nBatman: 🤵🦇 \nTransformers: 🚗🤖 \n"+A+":",
            temperature=0.8,
            max_tokens=60,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["\n"]
            )
            to_return=response

            return to_return,200
        except:
            return ({"ERROR":"Error Occured"}),500

class summary(Resource):
    def post(self):
        try:
            request_body=request.json
            A=request_body["data"]


            response = openai.Completion.create(
            model="text-davinci-002",
            prompt="Summarize this for a second-grade student:\n\n"+A,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )
            to_return=response

            return to_return,200
        except:
            return ({"ERROR":"Error Occured"}),500

class Complete(Resource):
    def post(self):
        try:
            request_body=request.json
            A=request_body["data"]


            response = openai.Completion.create(
            model="text-davinci-001",
            prompt=A,
            temperature=0.29,
            max_tokens=64,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )
            to_return=response

            return to_return,200
        except:
            return ({"ERROR":"Error Occured"}),500


class login(Resource):
    def post(self):
        try:
            request_body=request.json
            username=request_body["username"]
            password=request_body["password"]

            if username == "admin" and password == "admin":
                return ({"status":"login Successful"}),200
            else:
                return ({"status":"login UnSuccessful"}),401

        except:
            return ({"ERROR":"Internal error Occured"}),500


 #Mapping 
api.add_resource(correct_sentence,'/OPENAI/correct_sentence',methods=['POST'])
api.add_resource(classification,'/OPENAI/classification',methods=['POST'])
api.add_resource(idea,'/OPENAI/idea',methods=['POST'])
api.add_resource(translate,'/OPENAI/translate',methods=['POST'])
api.add_resource(emoji,'/OPENAI/emoji',methods=['POST'])
api.add_resource(summary,'/OPENAI/summary',methods=['POST'])
api.add_resource(Complete,'/OPENAI/Complete',methods=['POST'])
api.add_resource(login,'/OPENAI/login',methods=['POST'])
  
  
if __name__=='__main__':
    app.run(debug=True)