from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Email configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'vishnu241206@gmail.com'  # your email
app.config['MAIL_PASSWORD'] = 'nqwp reuq eqyk bdqa'     # Gmail app password or real password (not recommended)

mail = Mail(app)

# Routes for pages
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# Route for form submission
@app.route('/send_message', methods=['POST'])
def send_message():
    name = request.form['name']
    email = request.form['email']
    number = request.form['number']
    message = request.form['message']

    msg = Message(subject=f"Portfolio Message from {name}",
                  sender=app.config['MAIL_USERNAME'],
                  recipients=[app.config['MAIL_USERNAME']],
                  body=f"Name: {name}\nEmail: {email}\nPhone: {number}\n\nMessage:\n{message}")

    mail.send(msg)
    flash("Your message has been sent successfully!")
    return redirect('/contact')


if __name__ == '__main__':
    app.run(debug=True)
