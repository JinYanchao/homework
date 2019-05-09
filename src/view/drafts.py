#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  : Jin Yanchao
@Email   : yanchao.jin@outlook.com
@Time    : 2019/5/7 17:01
"""
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from view import home
from models import sql


class Drafts(object):

    def __init__(self):
        self.database = sql.Sql()
        self.win = Tk()
        self.win.title('草稿箱')
        scr_width = self.win.winfo_screenwidth()
        scr_height = self.win.winfo_screenheight()
        win_width = 900
        win_height = 600
        self.win.geometry(
            '%dx%d+%d+%d' % (win_width, win_height, (scr_width - win_width) / 2, (scr_height - win_height) / 2))
        self.win.resizable(0, 0)
        var_search = StringVar()
        Label(self.win).grid(row=0, column=0)
        Label(self.win, text='主题 :', font=('Arial', 12)).grid(row=0, column=1, pady=10)
        var_entry = Entry(self.win, textvariable=var_search, width=30, font=('Verdana', 12))
        var_entry.grid(row=0, column=2, pady=10)
        Button(self.win, text='查询', font=('Arial', 12), width=10,
               command=lambda: self.search(var_entry)).grid(row=0, column=3, padx=5, pady=10)
        Button(self.win, text='删除', font=('Arial', 12), width=10,
               command=self.del_row).grid(row=0, column=4, padx=5, pady=10)
        Button(self.win, text='返回', font=('Arial', 12), width=10,
               command=self.return_home).grid(row=0, column=5, padx=5, pady=10)
        Label(self.win, width=5).grid(row=0, column=5)
        columns = ('ID', 'Sender', 'Receiver', 'Subject', 'Context', 'Date')
        self.tree_view = ttk.Treeview(self.win, height=25, show='headings', columns=columns)
        self.tree_view.bind('<Double-1>', self.tree_click)
        self.tree_view.column('ID', width=30, anchor='center')
        self.tree_view.column('Sender', width=145, anchor='center')
        self.tree_view.column('Receiver', width=145, anchor='center')
        self.tree_view.column('Subject', width=100, anchor='center')
        self.tree_view.column('Context', width=200, anchor='center')
        self.tree_view.column('Date', width=180, anchor='center')
        self.tree_view.heading('ID', text='ID')
        self.tree_view.heading('Sender', text='发件人')
        self.tree_view.heading('Receiver', text='收件人')
        self.tree_view.heading('Subject', text='主题')
        self.tree_view.heading('Context', text='内容')
        self.tree_view.heading('Date', text='时间')
        self.tree_view.grid(row=1, columnspan=7, padx=50, pady=5)
        dbsql = 'select id, sender, receiver, subject, context, p_date from h_email'
        results = self.database.sel_data(dbsql)
        self.insert_to_tree(results)
        self.win.mainloop()

    def insert_to_tree(self, results):
        k = 0
        for row in results:
            self.tree_view.insert('', k, values=(row[0], row[1], row[2], row[3], row[4], row[5]))
            k += 1

    def del_tree(self):
        items = self.tree_view.get_children()
        for item in items:
            self.tree_view.delete(item)

    def tree_click(self, event):
        for item in self.tree_view.selection():
            item_text = self.tree_view.item(item, 'values')
            self.win.destroy()
            global obj_home
            obj_home = home.Home(item_text)

    def search(self, var):
        dbsql = 'select id, sender, receiver, subject, context, p_date from h_email where subject like "%s"' % var.get()
        results = self.database.sel_data(dbsql)
        if len(results) == 0:
            messagebox.showwarning('警告', '没有主题为 ' + var.get() + ' 的邮件')
        else:
            self.del_tree()
            self.insert_to_tree(results)

    def del_row(self):
        item = self.tree_view.selection()
        if len(item) == 0:
            messagebox.showwarning('警告', '没有选定内容')
        elif messagebox.askokcancel('注意', '你确定要删除这条数据吗？'):
            item_text = self.tree_view.item(item, 'values')
            dbsql = 'delete from h_email where id=%s' % item_text[0]
            self.database.refresh(dbsql)
            self.del_tree()
            dbsql = 'select id, sender, receiver, subject, context, p_date from h_email'
            results = self.database.sel_data(dbsql)
            self.insert_to_tree(results)

    def return_home(self):
        self.win.destroy()
        global obj_home
        obj_home = home.Home()
