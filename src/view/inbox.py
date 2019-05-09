#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  : Jin Yanchao
@Email   : yanchao.jin@outlook.com
@Time    : 2019/5/7 17:02
"""
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from view import home
from models import pop


class Inbox(object):

    def __init__(self):
        self.obj_pop = None
        self.win = Tk()
        self.win.title('收件箱')
        scr_width = self.win.winfo_screenwidth()
        scr_height = self.win.winfo_screenheight()
        win_width = 900
        win_height = 600
        self.win.geometry(
            '%dx%d+%d+%d' % (win_width, win_height, (scr_width - win_width) / 2, (scr_height - win_height) / 2))
        self.win.resizable(0, 0)
        Label(self.win, text='自动配置仅对QQ、163、outlook、gmail等邮箱可用', font=('Arial', 12)) \
            .grid(row=0, column=1, columnspan=4, pady=5)
        Label(self.win, width=13).grid(row=1, column=0, pady=2)
        Label(self.win, text='账号 : ', font=('Arial', 12)).grid(row=1, column=1, sticky=E, pady=2)
        Label(self.win, text='密码(授权码) : ', font=('Arial', 12)).grid(row=2, column=1, sticky=W, pady=2)
        user = StringVar()
        pwd = StringVar()
        Entry(self.win, textvariable=user, width=30, font=('Verdana', 12)).grid(row=1, column=2, pady=2)
        pwd_entry = Entry(self.win, textvariable=pwd, width=30, font=('Verdana', 12))
        pwd_entry['show'] = '*'
        pwd_entry.grid(row=2, column=2, pady=2)
        Button(self.win, text='登录', font=('Arial', 12), widt=10, height=2, command=lambda: self.login(user, pwd)). \
            grid(row=1, rowspan=2, column=3, padx=5, pady=3)
        Button(self.win, text='返回', font=('Arial', 12), widt=10, height=2, command=self.return_home). \
            grid(row=1, rowspan=2, column=4, padx=5, pady=3)
        # Label(self.win, text='主题 : ', font=('Arial', 12)).grid(row=3, column=1, sticky=E, pady=3)
        # var_search = StringVar()
        # var_entry = Entry(self.win, textvariable=var_search, width=30, font=('Verdana', 12))
        # var_entry.grid(row=3, column=2, pady=10)
        # Button(self.win, text='查询', font=('Arial', 12), width=10, command=lambda: self.search(var_entry)) \
        #     .grid(row=3, column=3, padx=5, pady=10)
        # Button(self.win, text='删除', font=('Arial', 12), width=10, command=self.del_row) \
        #     .grid(row=3, column=4, padx=5, pady=10)
        columns = ('Sender', 'Subject', 'Context', 'Date')
        self.tree_view = ttk.Treeview(self.win, height=23, show='headings', columns=columns)
        self.tree_view.bind('<Double-1>', self.tree_click)
        self.tree_view.column('Sender', width=150, anchor='center')
        self.tree_view.column('Subject', width=100, anchor='center')
        self.tree_view.column('Context', width=370, anchor='center')
        self.tree_view.column('Date', width=180, anchor='center')
        self.tree_view.heading('Sender', text='发件人')
        self.tree_view.heading('Subject', text='主题')
        self.tree_view.heading('Context', text='内容')
        self.tree_view.heading('Date', text='时间')
        self.tree_view.grid(row=4, columnspan=15, padx=50, pady=5)
        self.win.mainloop()

    def tree_click(self, event):
        for item in self.tree_view.selection():
            item_temp = self.tree_view.item(item, 'values')
            item_text = ['', '', item_temp[0], item_temp[1], item_temp[2]]
            self.win.destroy()
            global obj_home
            obj_home = home.Home(item_text)

    def search(self, var):
        pass

    def del_row(self):
        pass

    def login(self, user, pwd):
        if user.get() == '':
            messagebox.showerror('错误', '账号不能为空')
            return
        else:
            if len(user.get().split('@')) != 2:
                messagebox.showwarning('警告', '请输入正确的邮箱地址')
                return
        if pwd.get() == '':
            messagebox.showerror('错误', '密码不能为空')
            return
        self.obj_pop = pop.Pop(user.get(), pwd.get())
        mails = self.obj_pop.receiveEmail()
        self.insert_to_tree(mails)


    def insert_to_tree(self, results):
        k = 0
        for row in results:
            self.tree_view.insert('', k, values=(row['Sender'], row['subject'], row['context'], row['date']))
            k += 1

    def del_tree(self):
        items = self.tree_view.get_children()
        for item in items:
            self.tree_view.delete(item)

    def return_home(self):
        self.win.destroy()
        global obj_home
        obj_home = home.Home()
