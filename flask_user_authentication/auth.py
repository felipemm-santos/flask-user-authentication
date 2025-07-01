from flask import Blueprint, redirect, render_template, request, flash, url_for

bp = Blueprint('auth', __name__, url_prefix="/auth",
                        template_folder='templates')

@bp.route("/login")
def login():
    return render_template("login.html")

@bp.route("/register", methods=["GET","POST"])
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