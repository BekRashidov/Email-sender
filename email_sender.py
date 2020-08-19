import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = #senders email
email['to'] = #recipients email
email['subject'] = #Emails subject

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(#'your sender email', 'your sender password')
    smtp.send_message(email)
    print('All good Bosss!')# Prints after the successful proccess