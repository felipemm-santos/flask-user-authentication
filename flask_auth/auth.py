from flask import Blueprint, redirect, render_template, request, flash, url_for

from flask_auth.models import User

from flask_auth import db

bp = Blueprint('auth', __name__, url_prefix="/auth",
                        template_folder='templates')

@bp.route("/login")
def login():
    return render_template("login.html")

@bp.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        error=False

        if not (first_name or last_name or email or password or confirm_password):
            flash("Por favor preencha todos os campos","error")
            error=True      

        if password != confirm_password:
            flash("As senhas não correspondem","error")
            error=True      

        if not error:
            user = User(first_name, last_name, email, password)
            db.session.add(user)
            db.session.commit()
            flash('Cadastro realizado com sucesso',"success")
            return redirect(url_for('auth.login'))
    
    return render_template("register.html")