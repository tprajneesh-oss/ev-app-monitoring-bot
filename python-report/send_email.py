import smtplib, os
from email.message import EmailMessage

EMAIL = os.environ['EMAIL_USER']
PASSWORD = os.environ['EMAIL_PASS']

msg = EmailMessage()
msg['Subject'] = 'Daily EV Charging Report'
msg['From'] = EMAIL
msg['To'] = EMAIL
msg.set_content('Attached is today EV charging status report.')

with open('EV_Daily_Report.xlsx', 'rb') as f:
    msg.add_attachment(
        f.read(),
        maintype='application',
        subtype='vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        filename='EV_Daily_Report.xlsx'
    )

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL, PASSWORD)
    smtp.send_message(msg)

print("Email sent successfully")
