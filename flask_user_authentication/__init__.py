import os

from dotenv import load_dotenv
from flask import Flask, render_template

def create_app():
    app = Flask(__name__)
    app.secret_key = os.environ["SECRET_KEY"]
    
    from . import auth
    app.register_blueprint(auth.bp)

    @app.route("/")
    @app.route("/index")
    def home():
        return render_template("index.html")