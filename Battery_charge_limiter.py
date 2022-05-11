#!/usr/bin/env python3

import tkinter
import os
import sys
import subprocess

# Creating a new window and configurations
window = tkinter.Tk()
window.title("ASUS Battery Utility")
window.minsize(width=550, height=300)
window.config(padx=20, pady=50)

# Ensuring sudo privileges
if os.geteuid() != 0:
    subprocess.call(['sudo', '-S', 'python3', *sys.argv])
    sys.exit()


def set_charge_limit():

    try:
        percentage = int(entry1.get())
    except ValueError:
        entry1.delete(0, "end")
        entry1.config(background="white")
    else:
        if percentage > 100:
            percentage = 100
        if percentage < 5:
            percentage = 5
        entry1.delete(0, "end")
        entry1.insert(0, str(percentage))
        with open("/sys/class/power_supply/BAT0/charge_control_end_threshold", mode="w") as bat_file:
            bat_file.write(str(percentage))
        refresh()


def return_key_pressed(event):
    set_charge_limit()


def refresh():
    entry1.delete(0, "end")
    entry1.focus_set()
    with open("/sys/class/power_supply/BAT0/charge_control_end_threshold", mode="r") as bat_file_read:
        current_value = bat_file_read.read()
        label2.config(text=f"Battery Charge Percent Limit: {current_value}")


# UI setup
label2 = tkinter.Label(text="Battery Charge Percent Limit:")
label2.grid(column=1, row=1)

button1 = tkinter.Button(text="Set", command=set_charge_limit)
button1.grid(column=1, row=3)
button1.config(padx=10, pady=10)

entry1 = tkinter.Entry(width=4)
entry1.focus_set()
entry1.grid(column=1, row=2)

refresh()
window.bind('<Return>', return_key_pressed)


window.mainloop()
