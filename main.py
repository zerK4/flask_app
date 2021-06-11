from flask import Flask, redirect, url_for, render_template, request, flash
from flask.helpers import flash
from flask_wtf import FlaskForm, form
from flask_wtf.recaptcha import validators
from wtforms import StringField, PasswordField
from wtforms.fields.simple import SubmitField, TextAreaField, TextField
from wtforms.widgets.core import TextArea
from flask_mail import Mail, Message
from wtforms.validators import InputRequired, required

app = Flask(__name__,template_folder='./templates',static_folder='./templates/static')
aapp = Flask(__name__)
app.config['SECRET_KEY'] = 'SecretKey'
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 25,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = 'sebastian.vacarita@gmail.com',
    MAIL_PASSWORD = 'Break.d0own!@'
)
mail = Mail(app)

class ContactForm(FlaskForm):
    name = StringField('Nume', validators=[InputRequired()], render_kw={"placeholder": "Nume"})
    email = StringField('Email', validators=[InputRequired()], render_kw={"placeholder": "E-mail"})
    phone = StringField('Telefon', validators=[InputRequired()], render_kw={"placeholder": "Numar de telefon"})
    subject = StringField('Subiect', validators=[InputRequired()], render_kw={"placeholder": "Subiect"})
    message = TextAreaField('Mesaj', validators=[InputRequired()], render_kw={"placeholder": "Mesaj"})
    submit = SubmitField('Trimite', validators=[InputRequired()])

@app.route('/sent')
def send_mail():
    name = request.form.get('name')
    email = request.form.get('email')
    subject = request.form.get('subject')
    message = request.form.get('message')
    msg = Message("Salut, ma numesc " + name ,
                  sender= 'sebastian.vacarita@gmail.com',
                  recipients=["sebastian.vacarita@gmail.com", request.form.get('email')])
    msg.body = "Tsting"
    msg.html = render_template('send_email.html')
    mail.send(msg)

@app.route('/contact', methods=['POST', 'GET'])
def form():
    form = ContactForm()   
    if form.validate_on_submit():
        send_mail()
        return redirect('/contact')    
 #   flash("Great, your email was sent to us, please wait to be contacted.")
    return render_template('form.html', form=form)



@app.route("/")
def home():
    return render_template("index.html")
@app.route("/planuri")
def planuri():
    return render_template("planuri.html")
@app.route("/pasi")
def pasi():
    return render_template("pasi.html")
@app.route("/intrebari")
def intrebari():
    return render_template("intrebari.html")
@app.route("/politica")
def politica():
    return render_template("politica.html")


if __name__ == "__main__":
    app.run(debug=True)
