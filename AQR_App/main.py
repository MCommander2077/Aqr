import tkinter as tk
import tkinter.font as tkFont
import customtkinter as ctk
import requests


class App:
    def __init__(self, root):
        # setting title
        root.title("AQR Download")
        # setting window size
        width = 650
        height = 400
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_876 = ctk.CTkLabel(root, width=200, height=50, text='Adofai Quality Rating - 铺面下载')
        GLabel_876.place(x=0, y=0)

        GListBox_806 = tk.Listbox(root, cursor='arrow', selectmode='single')
        GListBox_806["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GListBox_806["font"] = ft
        GListBox_806["fg"] = "#333333"
        GListBox_806["justify"] = "center"
        GListBox_806.place(x=0, y=50, width=649, height=346)

        GButton_378 = ctk.CTkButton(root, width=100, height=30, text='刷新列表', command=self.GButton_378_command)
        GButton_378.place(x=280, y=10)

        GButton_681 = ctk.CTkButton(root, width=93, height=31, text='退出应用', command=self.GButton_681_command)
        GButton_681.place(x=520, y=10)

        GButton_544 = ctk.CTkButton(root, width=75, height=33, text='下载', command=self.GButton_544_command)
        GButton_544.place(x=570, y=360)

    def GButton_378_command(self):
        print("GButton_378_command")

    def GButton_681_command(self):
        print("GButton_681_command")
        print("Quiting...")
        exit(0)

    def GButton_544_command(self):
        print("GButton_544_command")

    def refresh_list(self):
        result = requests.get('')


if __name__ == "__main__":
    root = ctk.CTk()
    app = App(root)
    root.mainloop()
