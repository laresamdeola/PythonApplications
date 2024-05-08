# import smtplib
# from password import password
#
# email = "laresamdeola@yahoo.com"
# password = password
#
# with smtplib.SMTP_SSL("smtp.mail.yahoo.com", 587) as connection:
#     # connection.starttls()
#     connection.login(
#         user=email,
#         password=password
#     )
#     connection.sendmail(
#         from_addr=email,
#         to_addrs="laresamdeola@gmail.com",
#         msg="Subject:Hello World\n\nThis is the body of my email"
#     )
#

# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
#
# # Email configuration
# yahoo_smtp_server = 'smtp.mail.yahoo.com'
# yahoo_smtp_port = 465
# yahoo_email = 'laresamdeola@yahoo.com'
# yahoo_password = 'cwir coeg bdwp pscr'
#
# recipient_email = 'laresamdeola@gmail.com'
# subject = 'Hello Lare'
# body = 'This is a test email sent using Python.'
#
# # Create a multipart message
# message = MIMEMultipart()
# message['From'] = yahoo_email
# message['To'] = recipient_email
# message['Subject'] = subject
#
# # Attach body to the email
# message.attach(MIMEText(body, 'plain'))
#
# # Create SMTP session
# server = smtplib.SMTP(yahoo_smtp_server, yahoo_smtp_port)
# server.starttls()  # Enable TLS encryption
# server.login(yahoo_email, yahoo_password)  # Login to Yahoo Mail
#
# # Send email
# server.sendmail(yahoo_email, recipient_email, message.as_string())
#
# # Quit SMTP session
# server.quit()
#
# print("Email sent successfully!")

import yagmail

yag = yagmail.SMTP('daaresamuel@gmail.com', 'Gloriaoyedele27#')
contents = ['Hello, this is a test email']
yag.send('laresamdeola@yahoo.com', 'Emailed using Python', contents)
