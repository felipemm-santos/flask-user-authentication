from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

if __name__ == "__main__":
  app.run()