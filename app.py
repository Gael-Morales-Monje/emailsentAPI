from flask import Flask, request
from flask_cors import CORS

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart





app = Flask(__name__)


CORS(app)

list = [

]


@app.route("/sent")
def info():
    return list,200

@app.route("/sent",methods=['POST'])
def Post():
    smtp_server = "smtp.gmail.com"
    smtp_port = 587  # Puerto para TLS
    email = ""
    clave = ""
    recipient = ""
    body = ""
    req = request.json

    try:
        email = req["email"]
        recipient = req["recipient"]
        clave = req["clave"]
        body = req["body"]


        print(email, recipient, clave, body)
        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = recipient
        msg['Subject'] = "Asunto del correo"

        
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(email, clave)
        text = msg.as_string()
        server.sendmail(email, recipient, text)
        server.quit()
        print("Correo enviado exitosamente.")
        list.append(req)
        return "CORREO enviado",200
    except:

        return "Error",404





if __name__ == '__main__':
    app.run(debug=True)