import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Kuaidier:

    def __init__(self, fromaddr, password, smtp):
        self.fromaddr = fromaddr

        server = smtplib.SMTP(smtp)
        server.starttls()
        server.login(fromaddr, password)
        self.server = server

    def send(self, toaddr, subject, body):
        msg = MIMEMultipart()
        msg['From'] = self.fromaddr
        msg['To'] = toaddr
        # 邮件主题
        msg['Subject'] = subject
        # 邮件正文
        msg.attach(MIMEText(body, 'plain'))
        text = msg.as_string()
        self.server.sendmail(self.fromaddr, toaddr, text)

    def rest(self):
        self.server.quit()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.rest()


class KuaidierContext:
    
    def __init__(self, fromaddr, password, smtp):
        self.kuaidier = Kuaidier(fromaddr, password, smtp)

    def __enter__(self):
        return self.kuaidier

    def __exit__(self, *args):
        self.kuaidier.rest()