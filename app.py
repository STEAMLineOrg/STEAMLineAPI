from flask import Flask
api = Flask(__name__)

@api.route("/")
def home():
    return "Hello World! I'm using Flask!"

@api.route("/health")
def health():
    return ""