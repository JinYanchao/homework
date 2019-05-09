#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  : Jin Yanchao
@Email   : yanchao.jin@outlook.com
@Time    : 2019/5/7 16:59
"""
from smtplib import *
from email.mime.text import MIMEText


class Smtp(object):

    def send_email(self, sender, password, receiver, context, subject):
        '''
        :param sender: 发件人邮箱
        :param password: 发件人的邮箱密码
        :param receiver: 收件人邮箱
        :param context: 发送的内容
        :param subject: 邮件主题
        :return: 返回布尔值，判断是否发送成功
        '''
        # 创建smtp信息内容
        msg = MIMEText(context, 'plain', 'utf-8')
        msg['From'] = '{}'.format(sender)
        msg['To'] = receiver
        msg['Subject'] = subject
        # 尝试连接到发件服务器，并发送邮件
        try:
            # 将用户输入的发件箱分析，为常用的邮件服务商设置服务器和端口
            host = sender.split('@')[1]
            smtp_dicts = {'qq.com': [465, 'SSL'],
                          '163.com': [465, 'SSL'],
                          'gmail.com': [587, 'STARTTLS'],
                          'outlook.com': [587, 'STARTTLS']}
            if host in smtp_dicts.keys():
                port = smtp_dicts[host][0]  # 端口
                security = smtp_dicts[host][1]  # 加密方式
                host = 'smtp.' + host  # 服务器
                if security == 'SSL':
                    server = SMTP_SSL(host, port)
                elif security == 'STARTTLS':
                    server = SMTP(host, port)
                    server.ehlo()
                    server.starttls()
                else:
                    server = SMTP(host, port)
                server.login(sender, password)  # 发件人登录
                server.sendmail(sender, receiver, msg.as_string())  # 发送邮件
                server.quit()  # 断开连接
        except SMTPException:
            return False
        else:
            return True
