#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  : Jin Yanchao
@Email   : yanchao.jin@outlook.com
@Time    : 2019/5/7 17:00
"""
from tkinter import *
from tkinter import messagebox
from datetime import datetime
from models import smtp, sql
from view import drafts, inbox


def send(sender, password, receiver, subject, context):
    obj_smtp = smtp.Smtp()
    if obj_smtp.send_email(sender, password, receiver, context, subject):
        messagebox.showinfo('提示', '邮件发送成功')
    else:
        messagebox.showwarning('警告', '邮件发送失败')


def send_email(sender, receiver, subject, context):
    if sender.get() == '':
        messagebox.showerror('错误', '发件人不能为空')
        return
    else:
        if len(sender.get().split('@')) != 2:
            messagebox.showwarning('警告', '请输入正确的发件地址')
            return
    if receiver.get() == '':
        messagebox.showerror('错误', '收件人不能为空')
        return
    else:
        if len(receiver.get().split('@')) != 2:
            messagebox.showwarning('警告', '请输入正确的发件地址')
            return
    get_pwd = Toplevel()
    get_pwd.title('请输入密码(授权码)')
    scr_width = get_pwd.winfo_screenwidth()
    scr_height = get_pwd.winfo_screenheight()
    win_width = 300
    win_height = 150
    get_pwd.geometry(
        '%dx%d+%d+%d' % (win_width, win_height, (scr_width - win_width) / 2, (scr_height - win_height) / 2))
    get_pwd.resizable(0, 0)
    Label(get_pwd, text='自动配置仅对QQ、163、outlook、gmail邮箱可用').pack(pady=10)
    pwd = StringVar()
    entry = Entry(get_pwd, textvariable=pwd, width=20, font=('Verdana', 12))
    entry['show'] = '*'
    entry.pack(pady=10)
    Button(get_pwd, text='确定', width=10, height=1, font=('Arial', 11),
           command=lambda: send(sender.get(), pwd.get(), receiver.get(), subject.get(), context.get(0.0, END))) \
        .pack(pady=10)


def reset(sender, receiver, subject, context):
    if messagebox.askokcancel('注意', '确定要重置所以信息吗？'):
        sender.set('')
        receiver.set('')
        subject.set('')
        context.delete(0.0, END)


def save(sender, receiver, subject, context):
    dbsql = 'insert into h_email(sender, receiver, subject, context, p_date)values(%s, %s, %s, %s, %s)'
    values = (sender.get(), receiver.get(), subject.get(),
              context.get(0.0, END), datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    database = sql.Sql()
    database.ins_data(dbsql, values)


class Home(object):

    def __init__(self, item=None):
        self.win = Tk()
        self.win.title('主页 & 发送邮件')
        scr_width = self.win.winfo_screenwidth()
        scr_height = self.win.winfo_screenheight()
        win_width = 900
        win_height = 600
        self.win.geometry(
            '%dx%d+%d+%d' % (win_width, win_height, (scr_width - win_width) / 2, (scr_height - win_height) / 2))
        self.win.resizable(0, 0)
        sender = StringVar()
        receiver = StringVar()
        subject = StringVar()
        text = None
        if item is not None:
            sender.set(item[1])
            receiver.set(item[2])
            subject.set(item[3])
            text = item[4]
        header = Frame(self.win)
        Button(header, text='发送', width=12, height=1, font=('Arial', 11),
               command=lambda: send_email(sender, receiver, subject, context)).pack(side=LEFT, padx=10, pady=1)
        Button(header, text='重置', width=12, height=1, font=('Arial', 11),
               command=lambda: reset(sender, receiver, subject, context)).pack(side=LEFT, padx=10, pady=1)
        Button(header, text='保存', width=12, height=1, font=('Arial', 11),
               command=lambda: save(sender, receiver, subject, context)).pack(side=LEFT, padx=10, pady=1)
        Button(header, text='草稿箱', width=12, height=1, font=('Arial', 11),
               command=self.check_drafts).pack(side=LEFT, padx=10, pady=1)
        Button(header, text='收件箱', width=12, height=1, font=('Arial', 11),
               command=self.check_inbox).pack(side=LEFT, padx=10, pady=1)
        header.pack(pady=10)
        info = Frame(self.win)
        Label(info, text='发件人 : ', font=('Arial', 12)).grid(row=0, column=0, sticky=W, padx=5, pady=2)
        Label(info, text='收件人 : ', font=('Arial', 12)).grid(row=1, column=0, sticky=W, padx=5, pady=2)
        Label(info, text='主题 : ', font=('Arial', 12)).grid(row=2, column=0, sticky=E, padx=5, pady=2)
        Entry(info, textvariable=sender, width=60, font=('Verdana', 12)).grid(row=0, column=1, padx=5, pady=2)
        Entry(info, textvariable=receiver, width=60, font=('Verdana', 12)).grid(row=1, column=1, padx=5, pady=2)
        Entry(info, textvariable=subject, width=60, font=('Verdana', 12)).grid(row=2, column=1, padx=5, pady=2)
        info.pack(pady=10)
        Label(self.win, text='邮件内容', font=('Arial', 13)).pack(pady=10)
        context = Text(self.win, width=60, height=15, font=('Verdana', 14))
        if text is not None:
            context.insert(0.0, text)
        context.pack()
        self.win.mainloop()

    def check_drafts(self):
        self.win.destroy()
        global obj_drafts
        obj_drafts = drafts.Drafts()

    def check_inbox(self):
        self.win.destroy()
        global obj_inbox
        obj_inbox = inbox.Inbox()
