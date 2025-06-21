from functools import partial
from time import sleep
from tkinter import *
from tkinter import messagebox as msgbox
from tkinter.ttk import *

root = Tk()
root.title("EasiVote")
root.geometry("500x700")
root_size = [500, 700]
root.resizable(False, False)
voting_table = {}
voting_widgets = {}


def on_add_opt():
    opt_name = add_opt_entry.get().strip()
    if not opt_name:
        msgbox.showwarning("未输入选项名称",
                           "你没有输入选项名称或输入的选项名称为空，请重新输入。")
        return
    elif opt_name in voting_table.keys():
        msgbox.showwarning("选项名称重复",
                           "你输入的选项名称已经存在，请重新输入。")
        return

    if len(voting_table) >= 14:
        root_size[1] += 35
        root.geometry(f"{root_size[0]}x{root_size[1]}")

    add_opt_entry.delete(0, END)
    voting_table[opt_name] = 0

    voting_widgets[opt_name] = {
        "widget": (tmp_widget := Frame(voting)),
        "label":  Label(tmp_widget,  text=opt_name, font=("Candara", 16)),
        "count":  Label(tmp_widget,  text="0",      font=("Candara", 20)),
        "add":    Button(tmp_widget, text="+", command=partial(on_voting_add, opt_name)),
        "sub":    Button(tmp_widget, text="-", command=partial(on_voting_sub, opt_name)),
        "clear":  Button(tmp_widget, text="×", command=partial(on_voting_clear, opt_name))
    }
    tmp_widget                       .pack(side="top",   padx=5, expand=False, fill="x", anchor="n")
    voting_widgets[opt_name]["label"].pack(side="left",  padx=5)
    voting_widgets[opt_name]["clear"].pack(side="right", padx=5)
    voting_widgets[opt_name]["sub"]  .pack(side="right", padx=5)
    voting_widgets[opt_name]["add"]  .pack(side="right", padx=5)
    voting_widgets[opt_name]["count"].pack(side="right", padx=5)


def on_voting_add(name):
    voting_table[name] += 1
    voting_widgets[name]["count"].config(text=str(voting_table[name]))


def on_voting_sub(name):
    if voting_table[name] == 0:
        return
    voting_table[name] -= 1
    voting_widgets[name]["count"].config(text=str(voting_table[name]))


def on_voting_clear(name):
    voting_table[name] = 0
    voting_widgets[name]["count"].config(text=str(voting_table[name]))


title =       Label(root, text="EasiVote", font=("Candara", 50, "bold"))
description = Label(root, text="适用于多种场景的投票小工具 by MacrosMeng", font=("Candara", 15))
title      .pack()
description.pack()
voting = Frame(root)
editor = Frame(root)
voting.pack(side="top", expand=True, fill="both")
editor.pack(side="bottom")
add_opt_tip =   Label(editor,  text="添加选项", font=("Candara", 12))
add_opt_entry = Entry(editor,  font=("Candara", 12))
add_button =    Button(editor, text="添加", command=on_add_opt)
add_opt_tip  .pack(side="left",  padx=(10, 0), pady=10)
add_opt_entry.pack(side="left",  padx=10     , pady=10, expand=True, fill="x")
add_button   .pack(side="right", padx=(0, 10), pady=10)

if __name__ == "__main__":
    t = int(input("Test Adding>"))
    for i in range(t):
        add_opt_entry.insert(0, "Opt" + str(i))
        on_add_opt()

root.mainloop()

