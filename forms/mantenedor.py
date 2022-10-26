import tkinter as tk
from tkinter import Menu, ttk
from tkinter.font import BOLD
import util.generic as utl
from tkinter import ttk, messagebox
from .conexion import *

class Mantenedor:
                                        
    def __init__(self):

        #global ventana
        global modificar
        self.ventana = tk.Tk()                             
        self.ventana.title('Mantenedor')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()                                    
        #self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.geometry("1000x500")
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width = 0, height = 0)            
        
        logo =utl.leer_imagen("./img/logo2.png", (200, 200))
                        
        label = tk.Label( self.ventana, image=logo,bg='#ffffff' )
        label.place(x = 0,y = 0,relwidth = 1, relheight = 1)
        
        notebook = ttk.Notebook(self.ventana)
        notebook.grid()

        productor = ttk.Frame(notebook)
        cliExterno = ttk.Frame(notebook)
        comLocal = ttk.Frame(notebook)
        config = ttk.Frame(notebook)

        

        notebook.add(productor, text = "Productor")
        notebook.add(cliExterno, text = "Cliente Externo")
        notebook.add(comLocal, text = "Comerciante Local")
        notebook.add(config, text = "Configuracion")

        ##########----- CONFIGURACION -----##########
        ##########----- CONFIGURACION -----##########
        ##########----- CONFIGURACION -----##########
        ##########----- CONFIGURACION -----##########
        ##########----- CONFIGURACION -----##########

        def Salir():
            pass
            #Master()

        #Botones
        btnSalir = tk.Button(config, text = "Volver", command = lambda: Salir())
        btnSalir.grid(column = 0, row = 0)

        """ btnnew = tk.Button(productor, text = "Guardar", command = lambda:nuevo())
        btnnew.grid(column = 2, row = 6) 

        btnupdate = tk.Button(productor, text = "Seleccionar", command = lambda:actualizar())
        btnupdate.grid(column = 3, row = 6)   """


        ##########----- MANTENEDOR PRODUCTOR -----##########
        ##########----- MANTENEDOR PRODUCTOR -----##########
        ##########----- MANTENEDOR PRODUCTOR -----##########
        ##########----- MANTENEDOR PRODUCTOR -----##########
        ##########----- MANTENEDOR PRODUCTOR -----##########

        db = conexionBD()
        cur = db.cursor()
        modificar = False
        rut = tk.StringVar()
        nombre = tk.StringVar()
        apellido = tk.StringVar()
        empresa = tk.StringVar()

        def productorClick(event):
            id = tbProductores.selection()[0]
            if int(id) > 0:
                rut.set(tbProductores.item(id, "values")[1])
                nombre.set(tbProductores.item(id, "values")[2])
                apellido.set(tbProductores.item(id, "values")[3])
                empresa.set(tbProductores.item(id, "values")[4])

        #Labels y Entrys
        labelrut = tk.Label(productor, text = "RUT").grid(column = 0, row = 0, padx = 5, pady = 5)
        txtrut = tk.Entry(productor, textvariable = rut)
        txtrut.grid(column = 1, row = 0)

        labelnombre = tk.Label(productor, text = "Nombre").grid(column = 0, row = 1, padx = 5, pady = 5)
        txtnombre = tk.Entry(productor, textvariable = nombre)
        txtnombre.grid(column = 1, row = 1)

        labelapellido = tk.Label(productor, text = "Apellido").grid(column = 0, row = 2, padx = 5, pady = 5)
        txtapellido = tk.Entry(productor, textvariable = apellido)
        txtapellido.grid(column = 1, row = 2)

        labelempresa = tk.Label(productor, text = "Empresa").grid(column = 0, row = 3, padx = 5, pady = 5)
        txtempresa = tk.Entry(productor, textvariable = empresa)
        txtempresa.grid(column = 1, row = 3)

        labelMensaje = tk.Label(productor, text = " ", fg = "green")
        labelMensaje.grid(column = 0, row = 4, columnspan = 4)

        #Tabla de listar
        tbProductores = ttk.Treeview(productor, selectmode = tk.NONE)

        tbProductores["columns"] = ("ID", "RUT", "Nombre", "Apellido", "Empresa",)
        tbProductores.column("#0", width = 0, stretch = tk.NO)
        tbProductores.column("ID", width = 150, anchor = tk.CENTER)
        tbProductores.column("RUT", width = 200, anchor = tk.CENTER)
        tbProductores.column("Nombre", width = 200, anchor = tk.CENTER)
        tbProductores.column("Apellido", width = 200, anchor = tk.CENTER)
        tbProductores.column("Empresa", width = 250, anchor = tk.CENTER)
        tbProductores.heading("#0",text = "")
        tbProductores.heading("ID",text = "ID", anchor = tk.CENTER)
        tbProductores.heading("RUT",text = "RUT", anchor = tk.CENTER)
        tbProductores.heading("Nombre",text = "Nombre", anchor = tk.CENTER)
        tbProductores.heading("Apellido",text = "Apellido", anchor = tk.CENTER)
        tbProductores.heading("Empresa",text = "Empresa", anchor = tk.CENTER)

        tbProductores.grid(column = 0, row = 5, columnspan = 5)
        tbProductores.bind("<<TreeviewSelect>>", productorClick)

        #Botones
        btndelete = tk.Button(productor, text = "Eliminar", command = lambda:eliminar())
        btndelete.grid(column = 1, row = 6)

        btnnew = tk.Button(productor, text = "Guardar", command = lambda:nuevo())
        btnnew.grid(column = 2, row = 6) 

        btnupdate = tk.Button(productor, text = "Seleccionar", command = lambda:actualizar())
        btnupdate.grid(column = 3, row = 6)  


        #Funciones CRUD
        def modificarFalse():
            global modificar
            modificar = False
            tbProductores.config(selectmode = tk.NONE)
            btnnew.config(text = "Guardar")
            btnupdate.config(text = "Seleccionar")
            btndelete.config(state = tk.DISABLED)

        def modificarTrue():
            global modificar
            modificar = True
            tbProductores.config(selectmode = tk.BROWSE)
            btnnew.config(text = "Nuevo")
            btnupdate.config(text = "Modificar")
            btndelete.config(state = tk.NORMAL)
        

        def validar_datos():
            return len(rut.get()) and len(nombre.get()) and len(apellido.get()) and len(empresa.get())

        def limpiar_tablas():
            rut.set("")
            nombre.set("")
            apellido.set("")
            empresa.set("")

        def limpiar_datos():
            filas = tbProductores.get_children()
            for fila in filas:
                tbProductores.delete(fila)

        def listar_datos():
            limpiar_datos()
            query = "SELECT * FROM productor"
            cur.execute(query)
            filas = cur.fetchall()
            for fila in filas:
                id = fila[0]
                tbProductores.insert("", tk.END, id, text = id, values = fila)

        def eliminar():
            id = tbProductores.selection()[0]
            if int(id) > 0:
                query = "DELETE FROM productor WHERE id=" + id
                cur.execute(query)
                db.commit()
                tbProductores.delete(id)
                labelMensaje.config(text = "Se Eliminó Correctamente el Productor")
                limpiar_tablas()
            else:
                labelMensaje.config(text = "Seleccione un Productor para Eliminar")

        def nuevo():
            if modificar == False:
                if validar_datos():
                    val = (rut.get(), nombre.get(), apellido.get(), empresa.get())
                    query = "INSERT INTO productor (rut, nombre, apellido, empresa) VALUES(%s, %s, %s, %s)"
                    cur.execute(query, val)
                    db.commit()
                    labelMensaje.config(text = "Se Reistro Correctamente el Productor")
                    listar_datos()
                    limpiar_tablas()
                
                else:
                    labelMensaje.config(text = "Debe completar los campos", fg = "red")

            else:
                modificarFalse()
        
        def actualizar():
            print("Antes de if modificar")
            if modificar == True:
                print("Antes de if validar_datos")
                if validar_datos():
                    print("Despues if validar_datos")
                    id = tbProductores.selection()[0]
                    val = (rut.get(), nombre.get(), apellido.get(), empresa.get())
                    query = "UPDATE productor SET rut = %s, nombre = %s, apellido = %s, empresa = %s WHERE id = " +id
                    cur.execute(query, val)
                    db.commit()
                    labelMensaje.config(text = "Se Actualizó Correctamente El Productor")
                    listar_datos()
                    limpiar_tablas()
                
                else:
                    labelMensaje.config(text = "Debe completar los campos", fg = "red")

            else:
                modificarTrue()

        listar_datos()


    ##########----- MANTENEDOR CLIENTE EXTERNO -----##########
    ##########----- MANTENEDOR CLIENTE EXTERNO -----##########
    ##########----- MANTENEDOR CLIENTE EXTERNO -----##########
    ##########----- MANTENEDOR CLIENTE EXTERNO -----##########
    ##########----- MANTENEDOR CLIENTE EXTERNO -----##########

        db = conexionBD()
        cur = db.cursor()
        modificar = False
        rut = tk.StringVar()
        nombre = tk.StringVar()
        apellido = tk.StringVar()
        empresa = tk.StringVar()

        def cli_externo_Click(event):
            id = tbcli_externo.selection()[0]
            if int(id) > 0:
                rut.set(tbcli_externo.item(id, "values")[1])
                nombre.set(tbcli_externo.item(id, "values")[2])
                apellido.set(tbcli_externo.item(id, "values")[3])
                empresa.set(tbcli_externo.item(id, "values")[4])

        #Labels y Entrys
        labelrut = tk.Label(cliExterno, text = "RUT").grid(column = 0, row = 0, padx = 5, pady = 5)
        txtrut = tk.Entry(cliExterno, textvariable = rut)
        txtrut.grid(column = 1, row = 0)

        labelnombre = tk.Label(cliExterno, text = "Nombre").grid(column = 0, row = 1, padx = 5, pady = 5)
        txtnombre = tk.Entry(cliExterno, textvariable = nombre)
        txtnombre.grid(column = 1, row = 1)

        labelapellido = tk.Label(cliExterno, text = "Apellido").grid(column = 0, row = 2, padx = 5, pady = 5)
        txtapellido = tk.Entry(cliExterno, textvariable = apellido)
        txtapellido.grid(column = 1, row = 2)

        labelempresa = tk.Label(cliExterno, text = "Empresa").grid(column = 0, row = 3, padx = 5, pady = 5)
        txtempresa = tk.Entry(cliExterno, textvariable = empresa)
        txtempresa.grid(column = 1, row = 3)

        labelMensaje = tk.Label(cliExterno, text = " ", fg = "green")
        labelMensaje.grid(column = 0, row = 4, columnspan = 4)

        #Tabla de listar
        tbcli_externo = ttk.Treeview(cliExterno, selectmode = tk.NONE)

        tbcli_externo["columns"] = ("ID", "RUT", "Nombre", "Apellido", "Empresa",)
        tbcli_externo.column("#0", width = 0, stretch = tk.NO)
        tbcli_externo.column("ID", width = 150, anchor = tk.CENTER)
        tbcli_externo.column("RUT", width = 200, anchor = tk.CENTER)
        tbcli_externo.column("Nombre", width = 200, anchor = tk.CENTER)
        tbcli_externo.column("Apellido", width = 200, anchor = tk.CENTER)
        tbcli_externo.column("Empresa", width = 250, anchor = tk.CENTER)
        tbcli_externo.heading("#0",text = "")
        tbcli_externo.heading("ID",text = "ID", anchor = tk.CENTER)
        tbcli_externo.heading("RUT",text = "RUT", anchor = tk.CENTER)
        tbcli_externo.heading("Nombre",text = "Nombre", anchor = tk.CENTER)
        tbcli_externo.heading("Apellido",text = "Apellido", anchor = tk.CENTER)
        tbcli_externo.heading("Empresa",text = "Empresa", anchor = tk.CENTER)

        tbcli_externo.grid(column = 0, row = 5, columnspan = 5)
        tbcli_externo.bind("<<TreeviewSelect>>", cli_externo_Click)

        #Botones
        btndelete = tk.Button(cliExterno, text = "Eliminar", command = lambda:eliminar())
        btndelete.grid(column = 1, row = 6)

        btnnew = tk.Button(cliExterno, text = "Guardar", command = lambda:nuevo())
        btnnew.grid(column = 2, row = 6) 

        btnupdate = tk.Button(cliExterno, text = "Seleccionar", command = lambda:actualizar())
        btnupdate.grid(column = 3, row = 6)  


        #Funciones CRUD
        def modificarFalse():
            global modificar
            modificar = False
            tbcli_externo.config(selectmode = tk.NONE)
            btnnew.config(text = "Guardar")
            btnupdate.config(text = "Seleccionar")
            btndelete.config(state = tk.DISABLED)

        def modificarTrue():
            global modificar
            modificar = True
            tbcli_externo.config(selectmode = tk.BROWSE)
            btnnew.config(text = "Nuevo")
            btnupdate.config(text = "Modificar")
            btndelete.config(state = tk.NORMAL)
        

        def validar_datos():
            return len(rut.get()) and len(nombre.get()) and len(apellido.get()) and len(empresa.get())

        def limpiar_tablas():
            rut.set("")
            nombre.set("")
            apellido.set("")
            empresa.set("")

        def limpiar_datos():
            filas = tbcli_externo.get_children()
            for fila in filas:
                tbcli_externo.delete(fila)

        def listar_datos():
            limpiar_datos()
            query = "SELECT * FROM cliente_externo"
            cur.execute(query)
            filas = cur.fetchall()
            for fila in filas:
                id = fila[0]
                tbcli_externo.insert("", tk.END, id, text = id, values = fila)

        def eliminar():
            id = tbcli_externo.selection()[0]
            if int(id) > 0:
                query = "DELETE FROM cliente_externo WHERE id=" + id
                cur.execute(query)
                db.commit()
                tbcli_externo.delete(id)
                labelMensaje.config(text = "Se Eliminó Correctamente el Productor")
                limpiar_tablas()
            else:
                labelMensaje.config(text = "Seleccione un Productor para Eliminar")

        def nuevo():
            if modificar == False:
                if validar_datos():
                    val = (rut.get(), nombre.get(), apellido.get(), empresa.get())
                    query = "INSERT INTO cliente_externo (rut, nombre, apellido, empresa) VALUES(%s, %s, %s, %s)"
                    cur.execute(query, val)
                    db.commit()
                    labelMensaje.config(text = "Se Reistro Correctamente el Productor")
                    listar_datos()
                    limpiar_tablas()
                
                else:
                    labelMensaje.config(text = "Debe completar los campos", fg = "red")

            else:
                modificarFalse()
        
        def actualizar():
            print("Antes de if modificar")
            if modificar == True:
                print("Antes de if validar_datos")
                if validar_datos():
                    print("Despues if validar_datos")
                    id = tbcli_externo.selection()[0]
                    val = (rut.get(), nombre.get(), apellido.get(), empresa.get())
                    query = "UPDATE cliente_externo SET rut = %s, nombre = %s, apellido = %s, empresa = %s WHERE id = " +id
                    cur.execute(query, val)
                    db.commit()
                    labelMensaje.config(text = "Se Actualizó Correctamente El Productor")
                    listar_datos()
                    limpiar_tablas()
                
                else:
                    labelMensaje.config(text = "Debe completar los campos", fg = "red")

            else:
                modificarTrue()

        listar_datos()


        ##########----- MANTENEDOR COMERCIANTE LOCAL -----##########
        ##########----- MANTENEDOR COMERCIANTE LOCAL -----##########
        ##########----- MANTENEDOR COMERCIANTE LOCAL -----##########
        ##########----- MANTENEDOR COMERCIANTE LOCAL -----##########
        ##########----- MANTENEDOR COMERCIANTE LOCAL -----##########

        db = conexionBD()
        cur = db.cursor()
        modificar = False
        rut = tk.StringVar()
        nombre = tk.StringVar()
        apellido = tk.StringVar()
        empresa = tk.StringVar()

        def comerciante_local_Click(event):
            id = tbcomerciante_local.selection()[0]
            if int(id) > 0:
                rut.set(tbcomerciante_local.item(id, "values")[1])
                nombre.set(tbcomerciante_local.item(id, "values")[2])
                apellido.set(tbcomerciante_local.item(id, "values")[3])
                empresa.set(tbcomerciante_local.item(id, "values")[4])

        #Labels y Entrys
        labelrut = tk.Label(comLocal, text = "RUT").grid(column = 0, row = 0, padx = 5, pady = 5)
        txtrut = tk.Entry(comLocal, textvariable = rut)
        txtrut.grid(column = 1, row = 0)

        labelnombre = tk.Label(comLocal, text = "Nombre").grid(column = 0, row = 1, padx = 5, pady = 5)
        txtnombre = tk.Entry(comLocal, textvariable = nombre)
        txtnombre.grid(column = 1, row = 1)

        labelapellido = tk.Label(comLocal, text = "Apellido").grid(column = 0, row = 2, padx = 5, pady = 5)
        txtapellido = tk.Entry(comLocal, textvariable = apellido)
        txtapellido.grid(column = 1, row = 2)

        labelempresa = tk.Label(comLocal, text = "Empresa").grid(column = 0, row = 3, padx = 5, pady = 5)
        txtempresa = tk.Entry(comLocal, textvariable = empresa)
        txtempresa.grid(column = 1, row = 3)

        labelMensaje = tk.Label(comLocal, text = " ", fg = "green")
        labelMensaje.grid(column = 0, row = 4, columnspan = 4)

        #Tabla de listar
        tbcomerciante_local = ttk.Treeview(comLocal, selectmode = tk.NONE)

        tbcomerciante_local["columns"] = ("ID", "RUT", "Nombre", "Apellido", "Empresa",)
        tbcomerciante_local.column("#0", width = 0, stretch = tk.NO)
        tbcomerciante_local.column("ID", width = 150, anchor = tk.CENTER)
        tbcomerciante_local.column("RUT", width = 200, anchor = tk.CENTER)
        tbcomerciante_local.column("Nombre", width = 200, anchor = tk.CENTER)
        tbcomerciante_local.column("Apellido", width = 200, anchor = tk.CENTER)
        tbcomerciante_local.column("Empresa", width = 250, anchor = tk.CENTER)
        tbcomerciante_local.heading("#0",text = "")
        tbcomerciante_local.heading("ID",text = "ID", anchor = tk.CENTER)
        tbcomerciante_local.heading("RUT",text = "RUT", anchor = tk.CENTER)
        tbcomerciante_local.heading("Nombre",text = "Nombre", anchor = tk.CENTER)
        tbcomerciante_local.heading("Apellido",text = "Apellido", anchor = tk.CENTER)
        tbcomerciante_local.heading("Empresa",text = "Empresa", anchor = tk.CENTER)

        tbcomerciante_local.grid(column = 0, row = 5, columnspan = 5)
        tbcomerciante_local.bind("<<TreeviewSelect>>", comerciante_local_Click)

        #Botones
        btndelete = tk.Button(comLocal, text = "Eliminar", command = lambda:eliminar())
        btndelete.grid(column = 1, row = 6)

        btnnew = tk.Button(comLocal, text = "Guardar", command = lambda:nuevo())
        btnnew.grid(column = 2, row = 6) 

        btnupdate = tk.Button(comLocal, text = "Seleccionar", command = lambda:actualizar())
        btnupdate.grid(column = 3, row = 6)  


        #Funciones CRUD
        def modificarFalse():
            global modificar
            modificar = False
            tbcomerciante_local.config(selectmode = tk.NONE)
            btnnew.config(text = "Guardar")
            btnupdate.config(text = "Seleccionar")
            btndelete.config(state = tk.DISABLED)

        def modificarTrue():
            global modificar
            modificar = True
            tbcomerciante_local.config(selectmode = tk.BROWSE)
            btnnew.config(text = "Nuevo")
            btnupdate.config(text = "Modificar")
            btndelete.config(state = tk.NORMAL)
        

        def validar_datos():
            return len(rut.get()) and len(nombre.get()) and len(apellido.get()) and len(empresa.get())

        def limpiar_tablas():
            rut.set("")
            nombre.set("")
            apellido.set("")
            empresa.set("")

        def limpiar_datos():
            filas = tbcomerciante_local.get_children()
            for fila in filas:
                tbcomerciante_local.delete(fila)

        def listar_datos():
            limpiar_datos()
            query = "SELECT * FROM comerciante_local"
            cur.execute(query)
            filas = cur.fetchall()
            for fila in filas:
                id = fila[0]
                tbcomerciante_local.insert("", tk.END, id, text = id, values = fila)

        def eliminar():
            id = tbcomerciante_local.selection()[0]
            if int(id) > 0:
                query = "DELETE FROM comerciante_local WHERE id=" + id
                cur.execute(query)
                db.commit()
                tbcomerciante_local.delete(id)
                labelMensaje.config(text = "Se Eliminó Correctamente el Productor")
                limpiar_tablas()
            else:
                labelMensaje.config(text = "Seleccione un Productor para Eliminar")

        def nuevo():
            if modificar == False:
                if validar_datos():
                    val = (rut.get(), nombre.get(), apellido.get(), empresa.get())
                    query = "INSERT INTO comerciante_local (rut, nombre, apellido, empresa) VALUES(%s, %s, %s, %s)"
                    cur.execute(query, val)
                    db.commit()
                    labelMensaje.config(text = "Se Reistro Correctamente el Productor")
                    listar_datos()
                    limpiar_tablas()
                
                else:
                    labelMensaje.config(text = "Debe completar los campos", fg = "red")

            else:
                modificarFalse()
        
        def actualizar():
            print("Antes de if modificar")
            if modificar == True:
                print("Antes de if validar_datos")
                if validar_datos():
                    print("Despues if validar_datos")
                    id = tbcomerciante_local.selection()[0]
                    val = (rut.get(), nombre.get(), apellido.get(), empresa.get())
                    query = "UPDATE comerciante_local SET rut = %s, nombre = %s, apellido = %s, empresa = %s WHERE id = " +id
                    cur.execute(query, val)
                    db.commit()
                    labelMensaje.config(text = "Se Actualizó Correctamente El Productor")
                    listar_datos()
                    limpiar_tablas()
                
                else:
                    labelMensaje.config(text = "Debe completar los campos", fg = "red")

            else:
                modificarTrue()

        listar_datos()

        self.ventana.mainloop()