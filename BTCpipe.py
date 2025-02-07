import requests
import json
import os
import argparse
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Content

def get_data(url):
    response = requests.get(url)
    if response.status_code == 200:
      message = response.json()
      return message
    else:
        return None

btc_data = get_data("https://api.coincap.io/v2/assets/bitcoin")

def send_mail():
  parser = argparse.ArgumentParser(description="Script for send mail")
  parser.add_argument("--YOU_SENDGRID_API_KEY", type=str, required=True, help="YOU_SENDGRID_API_KEY")
  parser.add_argument("--firstMail", type=str, required=True, help="mail1")
  parser.add_argument("--secondMail", type=str, required=True, help="mail2")
  args = parser.parse_args()
  SENDGRID_API_KEY = args.YOU_SENDGRID_API_KEY
  message = Mail(
    from_email=args.firstMail,
    to_emails=args.secondMail,
    subject='send bitcoin data',
    html_content= Content("text/html", json.dumps(btc_data))  
    )
  try:
    # Envoi de l'email via SendGrid API
    sg = SendGridAPIClient(SENDGRID_API_KEY)
    response = sg.send(message)
    print(f"Email envoyé avec statut : {response.status_code}")
  except Exception as e:
    print(f"Erreur lors de l'envoi de l'email : {e}")
send_mail()

