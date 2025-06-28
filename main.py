import os

from dotenv import load_dotenv
from flask import Flask, flash, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = os.environ["SECRET_KEY"]

@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        full_name = request.form['full_name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        error=False

        if not (full_name or email or password or confirm_password):
            flash("Por favor preencha todos os campos","error")
            error=True      

        if password != confirm_password:
            flash("As senhas não correspondem","error")
            error=True      

        if not error:
            flash('Cadastro realizado com sucesso',"success")
            return redirect(url_for('login'))
    
    return render_template("register.html")

if __name__ == "__main__":
  app.run()