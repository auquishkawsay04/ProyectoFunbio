import tkinter as tk
#from tkinter import ttk

FUENTE0 = ("SF Pro Display", 10)
FUENTE1 = ("SF Pro Display", 15)
FUENTE2 = ("SF Pro Display", 20)
FUENTE3 = ("SF Pro Display", 25)
FUENTE4 = ("SF Pro Display", 30)
FUENTE5 = ("SF Pro Display", 35)
FUENTE6 = ("SF Pro Display", 40)
FUENTE7 = ("SF Pro Display", 45)
FUENTE8 = ("SF Pro Display", 50)
FUENTE9 = ("SF Pro Display", 55)
FUENTE10 = ("SF Pro Display", 60)
FUENTE11 = ("SF Pro Display", 65)

class AuquishApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # tk.Tk.iconbitmap(self, default="logo.bmp")
        tk.Tk.wm_title(self, "Tendoux")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Login, Ramas, ActualizarRegistroNuevo, MostradorResultados, BuscadorDNI, HistoriaPacienteAntiguo, RegistrarNuevoPaciente):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Ramas)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

#INICIO CODIGO DAVID LINEA 45

class Login(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="#CCCCFF")

        def verificar_contrasena():
            if my_password.get() == "":
                controller.show_frame(Ramas)
                incorrect_password_label["text"] = " "
                my_password.set("")
            else:
                incorrect_password_label["text"] = "La contraseña que ingresó es incorrecta. Inténtelo de nuevo"

        label = tk.Label(self, text="TENDOUX", font=FUENTE7, bg="#CCCCFF")
        label.pack(pady=75, padx=40)

        password_label = tk.Label(self, text="Ingrese su contraseña", bg="#CCCCFF", fg="black", font=FUENTE1)
        password_label.pack(ipady=10)

        my_password = tk.StringVar()
        password_entry_box = tk.Entry(self, textvariable=my_password, width=22, font=FUENTE1, show="*", bg="white")
        password_entry_box.focus_set()
        password_entry_box.pack(ipady=7, pady=40)

        enter_button = tk.Button(self, text="INGRESAR", command=verificar_contrasena, relief="groove",
                                 borderwidth=0, width=15, height=1, font=FUENTE1, bg="#1168bf", fg="white")
        enter_button.pack(pady=40)

        incorrect_password_label = tk.Label(self, text=" ", bg="#CCCCFF", anchor="n", fg="white", font=FUENTE1)
        incorrect_password_label.pack(fill="both", expand=True)

class Ramas(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="#CCCCFF")

        Boton1 = tk.Button(self, text="Pacientes registrados", font=FUENTE2, bg="#1168bf",fg="white", width=30, height=2)
        Boton1.grid(row=2, column=2, pady=160, padx=180)

        Boton2 = tk.Button(self, text="Agregar nuevo paciente", font=FUENTE2, bg="#1168bf", fg="white", width=30, height=2)
        Boton2.grid(row=3, column=2, padx=10)

class ActualizarRegistroNuevo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="#CCCCFF")
#   titulo
        label12 = tk.Label(self, text="INGRESAR UN NUEVO REGISTRO", font=FUENTE2, bg="#c2deb5", fg="black", relief="groove", height=2)
        label12.grid(row=0, column=1, columnspan=3, pady=35, padx=90, ipadx=30, sticky="nsew")

        izquierda = tk.Label(self, bg="white")
        izquierda.grid(row=0, column=0, sticky="w", padx=130)

        derecha = tk.Label(self, bg="white")
        derecha.grid(row=0, column=4, sticky="e", padx=130)

# #   densidadosea
#         label1 = tk.Label(self, text="Densidad Ósea (gramos/cm^2):", font=FUENTE1, bg="#CCCCFF", fg="black", width=30, height=2)
#         label1.grid(row=1,column=1)
#
#         entrada_densidad = tk.Entry(self, font=FUENTE1, width=9, bg="white")
#         entrada_densidad.grid(row=1,column=2)
#
#  #   IMC
#         label2 = tk.Label(self, text="Índice de Masa Corporal:", font=FUENTE1, bg="#CCCCFF", fg="black", width=30,height=2)
#         label2.grid(row=2, column=1)
#
#         entrada_imc = tk.Entry(self, font=FUENTE1, width=9, bg="white")
#         entrada_imc.grid(row=2,column=2)
#
#
# #   tscore
#         label3 = tk.Label(self, text="T.Score:", font=FUENTE1, bg="#CCCCFF", fg="black", width=10, height=2)
#         label3.grid(row=3,column=1)
#
#         entrada_tscore = tk.Entry(self, font=FUENTE1, width=9, bg="white")
#         entrada_tscore.grid(row=3,column=2)
#
# #   boton resultados
#         button = tk.Button(self, text="Registrar y ver resultados", font=FUENTE1, relief="groove", borderwidth=2)
#         button.grid(row=4,column=1)


class MostradorResultados(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="#a281cc")
#   titulo
        labelM = tk.Label(self, text="Resultados del 04/12/19", font=FUENTE1, bg="#c2deb5", fg="black",relief="groove")
        labelM.grid(row=0,column=1)

#   estadooseoactual
        label1 = tk.Label(self, text="Estado óseo actual:", font=FUENTE1, bg="#a281cc")
        label1.grid(row=1,column=2)

        resultadoOseoDensitometria = tk.Label(self, text=" Osteoporosis Grave ", font=FUENTE0, bg="white")
        resultadoOseoDensitometria.grid(row=2, column=2)

#   recomendaciones
        label2 = tk.Label(self, text="Recomendaciones:", font=FUENTE1, bg="#a281cc")
        label2.grid(row=3,column=2)

        resultadoRecomendaciones = tk.Label(self, text=" Ir a la playa. ", font=FUENTE0, bg="white")
        resultadoRecomendaciones.grid(row=4, column=2)

#   boton imprimir resultados
        button = tk.Button(self, text="Imprimir resultados", font=FUENTE1, relief="groove", borderwidth=2)
        button.grid(row=5,column=3)











































































# -----------------------------------FIN CODIGO DAVID LINEA 230------------------------------------------------------
# -----------------------------------INICIO CODIGO NESTOR LINEA 231--------------------------------------------------

class BuscadorDNI(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white")

        def verficar_id():
            if paciente_id.get() == "74124434":

                #debemos ingresar la pagina del paciente regitrado aqui
                controller.show_frame(HistoriaPacienteAntiguo)
                paciente_id.set("")

#estoy teniendo problemas con el self dice que eno esta definido
        label = tk.Label(self, text="Ingrese el DNI ", font=FUENTE3, background="white")
        label.place(x=190, y=150)

        paciente_id = tk.StringVar()
        entry = tk.Entry(self , textvariable=paciente_id, font=FUENTE3, width=10, bg="white")
        entry.focus_set()
        entry.place(x=400, y=320)

        button = tk.Button(self, text="Aceptar", relief="groove", borderwidth=2, width=15, height=1,
                           font=FUENTE3, command=verficar_id)
        button.place(x=460, y=500)

class HistoriaPacienteAntiguo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white")

        label = tk.Label(self, text="JORGE PEREZ QUISPE", font=FUENTE3, background="white")
        label.place(x=190, y=150)

        label = tk.Label(self, text="Nombre", font=FUENTE3, background="white")
        label.place(x=200, y=220)

        entry = tk.Entry(self, font=FUENTE3, width=10, bg="white")
        entry.place(x=320, y=220)
        button1 = tk.Button(self, text="Actualizar Datos", font=FUENTE3, relief="groove", borderwidth=2, width=30, height=1)
        button1.place(x=140, y=400)

class RegistrarNuevoPaciente(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white")

        label = tk.Label(self, text="Ingrese los datos del nuevo paciente.", font=FUENTE3, background="white")
        label.place(x=190, y=150)

        label = tk.Label(self, text="Nombres y apellidos del nuevo paciente"    , font=FUENTE3, background="white")
        label.place(x=200, y=220)

        entry = tk.Entry(self, font=FUENTE3, width=10, bg="white")
        entry.place(x=320, y=220)

        label = tk.Label(self, text="DNI" , font=FUENTE3, background="white")
        label.place(x=200, y=320)

        entry = tk.Entry(self, font=FUENTE3, width=10, bg="white")
        entry.place(x=320, y=320)

        label = tk.Label(self, text="Edad" , font=FUENTE3, background="white")
        label.place(x=400, y=320)

        entry = tk.Entry(self, font=FUENTE3, width=10, bg="white")
        entry.place(x=520, y=220)

        label = tk.Label(self, text="Fecha de nacimiento", font=FUENTE3, background="white")
        label.place(x=600, y=320)

        entry = tk.Entry(self, font=FUENTE3, width=10, bg="white")
        entry.place(x=720, y=220)



app = AuquishApp()
app.geometry("1150x720")
app.resizable(False, False)
app.mainloop()