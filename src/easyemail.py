def sendemail(sender, reciever, password, subject, body, attachment=''):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders

    data = MIMEMultipart()
    data['From'] = sender
    data['To'] = reciever
    data['Subject'] = subject
    data.attach(MIMEText(body, 'plain'))
    
    if attachment == '':
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(sender, password)
        text = data.as_string()
        s.sendmail(sender, reciever, text)
        s.quit()

    else:
        attach = open(attachment, "rb")
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attach).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % attachment)
        data.attach(p)
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(sender, "password")
        text = data.as_string()
        s.sendmail(sender, reciever, text)
        s.quit()
