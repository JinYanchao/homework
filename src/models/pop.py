#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  : Jin Yanchao
@Email   : yanchao.jin@outlook.com
@Time    : 2019/5/7 16:59
"""
import poplib
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr


class Pop(object):

    def __init__(self, user, password):
        host = 'pop.' + user.split('@')[1]
        self.host = host
        self.user = user
        self.password = password

    def connectMail(self):
        server = poplib.POP3_SSL(self.host, 995)
        server.user(self.user)
        server.pass_(self.password)
        return server

    def receiveEmail(self):
        server = self.connectMail()
        resp, mails, objects = server.list()
        index = len(mails)
        if index > 20:
            index = 20
        emails = []
        for i in range(index, 1, -1):
            resp, lines, octets = server.retr(i)
            lists = []
            print(i)
            for line in lines:
                lists.append(line.decode('utf-8'))
            msg_content = '\r\n'.join(lists)
            msg = Parser().parsestr(msg_content)
            mail = self.print_info(msg)
            emails.append(mail)
            if index - i >= 20:
                break
        server.quit()
        return emails

    def decode_str(self, s):
        value, charset = decode_header(s)[0]
        if charset:
            value = value.decode(charset)
        return value

    def guess_charset(self, msg):
        charset = msg.get_charset()
        if charset is None:
            content_type = msg.get('Content-Type', '').lower()
            pos = content_type.find('charset=')
            if pos >= 0:
                charset = content_type[pos + 8:].strip()
        return charset

    def print_info(self, msg):
        text = {'sender': '', 'receiver': '', 'subject': '', 'context': '', 'date': ''}
        for header in ['From', 'To', 'Subject', 'Date']:
            value = msg.get(header, '')
            if value:
                if header == 'Subject':
                    value = self.decode_str(value)
                    text['subject'] = value
                elif header == 'From':
                    text['sender'] = value.split('\t')[1]
                elif header == 'Date':
                    text['date'] = value
                elif header == 'To':
                    text['receiver'] = self.decode_str(value)
            else:
                hdr, addr = parseaddr(value)
                name = self.decode_str(addr)
                value = name + '<' + addr + '>'
                text['receiver'] = value
        for part in msg.walk():
            filename = part.get_filename()
            content_type = part.get_content_type()
            charset = self.guess_charset(part)
            if filename:
                filename = self.decode_str(filename)
                data = part.get_payload(decode=True)
                if filename != None or filename != '':
                    print('Accessory:' + filename)
            else:
                email_content_type = ''
                content = ''
                if content_type == 'text/plain':
                    email_content_type = 'text'
                elif content_type == 'text/html':
                    email_content_type = 'html'
                if charset:
                    content = part.get_payload(decode=True).decode(charset)
                text['context'] = content
        return text
