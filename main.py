from tkinter import *
import pyshorteners

root = Tk()
root.title('Link Shortener')
root.geometry('500x500')

def shorten():
    if shorty.get():
        shorty.delete(0, END)
    if my_entry.get():
        url = pyshorteners.Shortener().tinyurl.short(my_entry.get())
        shorty.insert(END, url)


my_label = Label(root, text='Enter Link', font=('MS Gothic', 34))
my_label.pack(pady=20)

my_entry = Entry(root, font=('MS Gothic', 24))
my_entry.pack(pady=20)

my_button = Button(root, text='Shorten Link', command=shorten, font=('MS Gothic', 24))
my_button.pack(pady=20)

shorty_label = Label(root, text='Shortened Link', font=('MS Gothic', 14))
shorty_label.pack(pady=50)

shorty = Entry(root, font=('MS Gothic', 22), justify=CENTER, width=30, bd=0, bg='systembuttonface')
shorty.pack(pady=10)

root.mainloop()