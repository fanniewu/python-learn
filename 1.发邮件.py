import smtplib
from email.mime.text import MIMEText

#SMTP服务器
SMTPserver = "smtp.163.com"
#发送邮件的地址
sender = "qingwu0902@163.com"
#授权密码（不等同于登录密码）
password = "pwd1234"
#发送的内容
message = "Hello!"
#转为邮件文本
msg = MIMEText(message)
msg["Subject"] = "Hello"
msg["From"] = sender

#连接服务器
mailServer = smtplib.SMTP(SMTPserver, 25)
#登录
mailServer.login(sender, password)
#发送邮件
mailServer.sendmail(sender, ["wu_qinghua1018@hotmail.com"], msg.as_string())
mailServer.quit()
