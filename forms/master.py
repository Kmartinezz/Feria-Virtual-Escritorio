import tkinter as tk
from tkinter import Menu, ttk
from tkinter.font import BOLD
import util.generic as utl
from tkinter import ttk, messagebox
from forms.mantenedor import Mantenedor
from .conexion import *

class Master:

    def __init__(self):

        def on_closing():
            if messagebox.askokcancel("Salir", "Quieres Salir"):
                pass
        
        def close_master():
            self.root.destroy()
            Mantenedor()
        
        self.root = tk.Tk()
        self.root.title("Main")
        self.root.geometry("600x400")
        self.root.config(bg = "#ffffff")
        self.root.resizable(width = 0, height = 0)

        logo = utl.leer_imagen("./img/logo2.png", (400, 400))

        label = tk.Label(self.root, image = logo, bg = "#ffffff")
        label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

        menubar = Menu(self.root)
        filemenu = Menu(menubar, tearoff = 0)
        filemenu.add_command(label = "Salir", command = self.root.quit)
        menubar.add_cascade(label = "Archivo", menu = filemenu)
        self.root.protocol(("WM_DELETE_WINDOW", on_closing))
        self.root.config(menu = menubar)

        #Mantenedor
        admin = Menu(menubar, tearoff = 0)
        admin.add_command(label = "Mantenedor", command = lambda: close_master())
        menubar.add_cascade(label = "Procesos", menu = admin)


        self.root.mainloop()