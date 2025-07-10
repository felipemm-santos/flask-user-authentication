from flask import Flask, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from . import models
    db.init_app(app)
    migrate.init_app(app, db)

    from . import auth
    app.register_blueprint(auth.bp)

    @app.route("/")
    @app.route("/index")
    def index():
        if "username" in session:
            return redirect(url_for("dashboard"))
        return render_template("index.html")
    
    @app.route("/dashboard")
    def dashboard():
        if "username" in session:
            return render_template("dashboard.html", username=session["username"])
        return redirect(url_for("index"))
    return app