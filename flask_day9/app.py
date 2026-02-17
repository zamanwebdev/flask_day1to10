from flask import Flask, render_template, request, redirect, flash
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
app.secret_key = "supersecretkey"

# 🔴 এখানে তোমার Gmail বসাও
EMAIL_ADDRESS = "zamanwebdev@gmail.com"
EMAIL_PASSWORD = "sobs vucq rmia mjjk"

@app.route('/')
def contact():
    return render_template('contact.html')

@app.route('/send', methods=['POST'])
def send_email():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = EMAIL_ADDRESS
        msg['Subject'] = "New Contact Message"

        body = f"""
        Name: {name}
        Email: {email}
        Message: {message}
        """

        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()

        return render_template('success.html')


    except Exception as e:
        flash("Error sending email!", "danger")
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
