# SMTP Library
# SMTP (Simple Mail Transfer Protocol) is a protocol for sending emails.

import smtplib

hostname = 'smtp.gmail.com'
email = 'example@gmail.com' # Your Gmail address
password = 'bfrxjekchuzupwaq'  # App password for Gmail

with smtplib.SMTP(host=hostname) as connection:
    connection.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
    connection.login(user=email, password=password)
    connection.sendmail(
        from_addr=email,
        to_addrs=email,
        msg='Subject: Hello\n\nThis is the body of the email.'
    )
