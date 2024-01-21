import smtplib
from password import password

email = "laresamdeola@yahoo.com"
password = password

with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
    connection.starttls()
    connection.login(
        user=email,
        password=password
    )
    connection.sendmail(
        from_addr=email,
        to_addrs="laresamdeola@gmail.com",
        msg="Subject:Hello World\n\nThis is the body of my email"
    )

