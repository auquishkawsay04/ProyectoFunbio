import tkinter as tk


FUENTE0 = ("SF Pro Display", 10)
FUENTE1 = ("SF Pro Display", 15)
FUENTE2 = ("Calibri", 20)
FUENTE3 = ("SF Pro Display", 25)
FUENTE4 = ("SF Pro Display", 30)
FUENTE5 = ("SF Pro Display", 35)
FUENTE6 = ("SF Pro Display", 40)
FUENTE7 = ("Simplex_IV50", 45)
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

        self.show_frame(BuscadorDNI)

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

        label = tk.Label(self, text="TENDOUX", font=FUENTE7, bg="white")
        label.pack(pady=75, padx=40,ipadx=15)

        password_label = tk.Label(self, text="Ingrese su contraseña", bg="#CCCCFF", fg="black", font=FUENTE1)
        password_label.pack(ipady=10)

        my_password = tk.StringVar()
        password_entry_box = tk.Entry(self, textvariable=my_password, width=22, font=FUENTE1, show="*", bg="white")
        password_entry_box.focus_set()
        password_entry_box.pack(ipady=7, pady=40)

        enter_button = tk.Button(self, text="ACEPTAR", command=verificar_contrasena, relief="groove",
                                 borderwidth=0, width=15, height=1, font=FUENTE1, bg="#1168bf", fg="white")
        enter_button.pack(pady=40)

        incorrect_password_label = tk.Label(self, text=" ", bg="#CCCCFF", anchor="n", fg="red", font=FUENTE1)
        incorrect_password_label.pack(fill="both", expand=True)

class Ramas(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="#CCCCFF")

        # columnas
        columna0 = tk.Label(self, bg="#CCCCFF")
        columna0.grid(row=0, column=0, ipadx=80)

        columna1 = tk.Label(self, bg="#CCCCFF")
        columna1.grid(row=0, column=1, ipadx=80)

        columna2 = tk.Label(self, bg="#CCCCFF")
        columna2.grid(row=0, column=2, ipadx=80)

        columna3 = tk.Label(self, bg="#CCCCFF")
        columna3.grid(row=0, column=3, ipadx=80)

        columna4 = tk.Label(self, bg="#CCCCFF")
        columna4.grid(row=0, column=4, ipadx=80)

        columna5 = tk.Label(self, bg="#CCCCFF")
        columna5.grid(row=0, column=5, ipadx=80)

        columna6 = tk.Label(self, bg="#CCCCFF")
        columna6.grid(row=0, column=6, ipadx=80)

        columna7 = tk.Label(self, bg="#CCCCFF")
        columna7.grid(row=0, column=7, ipadx=80, ipady=10)

#separacion titulo
        fila1 = tk.Label(self, bg="#CCCCFF")
        fila1.grid(row=1, column=3, columnspan=2, sticky="nsew", ipady=65)

        Boton1 = tk.Button(self, text="Pacientes registrados", font=FUENTE2, bg="#E7E6E6",fg="black", width=30, height=1,
                           command=lambda: controller.show_frame(ActualizarRegistroNuevo))
        Boton1.grid(row=2, column=1, columnspan=5, sticky="w")

# separacion titulo y densidad
        fila2 = tk.Label(self, bg="#CCCCFF")
        fila2.grid(row=3, column=3, columnspan=2, sticky="nsew", ipady=50)

        Boton2 = tk.Button(self, text="Agregar nuevo paciente", font=FUENTE2, bg="#E7E6E6", fg="black", width=30, height=1)
        Boton2.grid(row=4, column=1, columnspan=5, sticky="w")

class ActualizarRegistroNuevo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="#CCCCFF")
#   titulo
        label2 = tk.Label(self, text="INGRESAR UN NUEVO REGISTRO", font=FUENTE2, bg="#c2deb5", fg="black", relief="groove", height=2)
        label2.grid(row=1, column=1, columnspan=6, ipadx=180)
# columnas
        columna0 = tk.Label(self, bg="#CCCCFF")
        columna0.grid(row=0, column=0,ipadx=80)

        columna1 = tk.Label(self, bg="#CCCCFF")
        columna1.grid(row=0, column=1,ipadx=80)

        columna2 = tk.Label(self, bg="#CCCCFF")
        columna2.grid(row=0, column=2, ipadx=80)

        columna3 = tk.Label(self, bg="#CCCCFF")
        columna3.grid(row=0, column=3, ipadx=80)

        columna4 = tk.Label(self, bg="#CCCCFF")
        columna4.grid(row=0, column=4,ipadx=80)

        columna5 = tk.Label(self, bg="#CCCCFF")
        columna5.grid(row=0, column=5,ipadx=80)

        columna6 = tk.Label(self, bg="#CCCCFF")
        columna6.grid(row=0, column=6,ipadx=80)

        columna7 = tk.Label(self, bg="#CCCCFF")
        columna7.grid(row=0, column=7,ipadx=80, ipady=10)

#separacion titulo y densidad
        fila2 = tk.Label(self, bg="#CCCCFF")
        fila2.grid(row=2, column=3, columnspan=2, sticky="nsew", ipady=8)
# densidadosea
        label1 = tk.Label(self, text="Densidad Ósea (gramos/cm^2):", font=FUENTE1, bg="#CCCCFF", fg="black", height=2)
        label1.grid(row=3,column=1, padx=50, columnspan=3,sticky="e")

        entrada_densidad = tk.Entry(self, font=FUENTE3, width=9, bg="#CCCCFF")
        entrada_densidad.grid(row=3,column=4, columnspan=2, sticky="w")
# separacion titulo y densidad
        fila4 = tk.Label(self, bg="#CCCCFF")
        fila4.grid(row=4, column=3, columnspan=2, sticky="nsew", ipady=8)
#  #   IMC
        label2 = tk.Label(self, text="Índice de Masa Corporal:", font=FUENTE1, bg="#CCCCFF", fg="black",height=2)
        label2.grid(row=5, column=1, padx=50, columnspan=3,sticky="e")

        entrada_imc = tk.Entry(self, font=FUENTE3, width=9, bg="#CCCCFF")
        entrada_imc.grid(row=5,column=4, columnspan=2, sticky="w")
# separacion
        fila7 = tk.Label(self, bg="#CCCCFF")
        fila7.grid(row=7, column=3, columnspan=2, sticky="nsew", ipady=8)
# #   tscore
        label2 = tk.Label(self, text="T-Score:", font=FUENTE1, bg="#CCCCFF", fg="black", height=2)
        label2.grid(row=8, column=1, padx=50, columnspan=3, sticky="e")

        entrada_tscore = tk.Entry(self, font=FUENTE3, width=9, bg="#CCCCFF")
        entrada_tscore.grid(row=8, column=4, columnspan=2, sticky="w")

# separacion
        fila9 = tk.Label(self, bg="#CCCCFF")
        fila9.grid(row=9, column=3, columnspan=2, sticky="nsew", ipady=8)

#comentario
        label3 = tk.Label(self, text="Comentario:", font=FUENTE1, bg="#CCCCFF", fg="black", height=2)
        label3.grid(row=10, column=1, padx=50, columnspan=3, sticky="e")

        textComentarios = tk.Text(self, font=FUENTE1, width=23, height=5, bg="#CCCCFF")
        textComentarios.grid(row=10, column=4,columnspan=3, sticky="w")

# separacion
        fila11 = tk.Label(self, bg="#CCCCFF")
        fila11.grid(row=11, column=3, columnspan=2, sticky="nsew", ipady=20)

#BOTONENTER
        button = tk.Button(self, text="Registrar y ver resultados", font=FUENTE1, relief="groove", borderwidth=3,
                           bg="#1168bf", fg="white", command=lambda: controller.show_frame(Ramas))
        button.grid(row=12, column=4, columnspan=3, ipadx=40)

# separacion
        fila11 = tk.Label(self, bg="#CCCCFF")
        fila11.grid(row=13, column=3, columnspan=2, sticky="nsew", ipady=20)

class MostradorResultados(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="#CCCCFF")
#   titulo
        label2 = tk.Label(self, text="RESULTADOS DEL 04/12/19", font=FUENTE2, bg="#c2deb5", fg="black",
                          relief="groove", height=2)
        label2.grid(row=1, column=1, columnspan=6, ipadx=180)

# columnas
        columna0 = tk.Label(self, bg="#CCCCFF")
        columna0.grid(row=0, column=0, ipadx=80)

        columna1 = tk.Label(self, bg="#CCCCFF")
        columna1.grid(row=0, column=1, ipadx=80)

        columna2 = tk.Label(self, bg="#CCCCFF")
        columna2.grid(row=0, column=2, ipadx=80)

        columna3 = tk.Label(self, bg="#CCCCFF")
        columna3.grid(row=0, column=3, ipadx=80)

        columna4 = tk.Label(self, bg="#CCCCFF")
        columna4.grid(row=0, column=4, ipadx=80)

        columna5 = tk.Label(self, bg="#CCCCFF")
        columna5.grid(row=0, column=5, ipadx=80)

        columna6 = tk.Label(self, bg="#CCCCFF")
        columna6.grid(row=0, column=6, ipadx=80)

        columna7 = tk.Label(self, bg="#CCCCFF")
        columna7.grid(row=0, column=7, ipadx=80, ipady=10)

# separacion titulo y densidad
        fila2 = tk.Label(self, bg="#CCCCFF")
        fila2.grid(row=2, column=3, columnspan=2, sticky="nsew", ipady=8)


#   estadooseoactual
        label1 = tk.Label(self, text="Estado óseo actual:", font=FUENTE1, bg="#CCCCFF")
        label1.grid(row=3, column=1, padx=50, columnspan=3, sticky="e")

        resultadoOseoDensitometria = tk.Label(self, text=" Osteoporosis Grave ", font=FUENTE1, bg="#CCCCFF")
        resultadoOseoDensitometria.grid(row=3, column=4, columnspan=2, sticky="w")

# separacion titulo y densidad
        fila4 = tk.Label(self, bg="#CCCCFF")
        fila4.grid(row=4, column=3, columnspan=2, sticky="nsew", ipady=8)

#   recomendaciones
        label2 = tk.Label(self, text="Recomendaciones generales:", font=FUENTE1, bg="#CCCCFF")
        label2.grid(row=5, column=1, padx=50, columnspan=3, sticky="e")
#
        resultadoRecomendaciones = tk.Label(self, text="It is a long established fact that a reader", font=FUENTE1, bg="#CCCCFF")
        resultadoRecomendaciones.grid(row=5, column=4, columnspan=6, sticky="w")

# separacion titulo y densidad
        fila6= tk.Label(self, bg="#CCCCFF")
        fila6.grid(row=6, column=3, columnspan=2, sticky="nsew", ipady=8)

#   recomendaciones
        label3 = tk.Label(self, text="Comentario:", font=FUENTE1, bg="#CCCCFF")
        label3.grid(row=7, column=1, padx=50, columnspan=3, sticky="e")
#
        resultadoComentario = tk.Label(self, text="It is a long established fact that a reader", font=FUENTE1, bg="#CCCCFF")
        resultadoComentario.grid(row=7, column=4, columnspan=6, sticky="w")

# separacion titulo y densidad
        fila7 = tk.Label(self, bg="#CCCCFF")
        fila7.grid(row=8, column=3, columnspan=2, sticky="nsew", ipady=70)

#   boton imprimir resultados
        button = tk.Button(self, text="Imprimir resultados", font=FUENTE1, relief="groove", borderwidth=2,
                           command=lambda: controller.show_frame(ActualizarRegistroNuevo))
        button.grid(row=9,column=5, columnspan=3, ipadx=10)



























# -----------------------------------FIN CODIGO DAVID LINEA 310------------------------------------------------------
# -----------------------------------INICIO CODIGO NESTOR LINEA 211--------------------------------------------------

class BuscadorDNI(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#CCCCFF")

     # columnas
        columna0 = tk.Label(self, bg="#CCCCFF")
        columna0.grid(row=0, column=0, ipadx=80)

        columna1 = tk.Label(self, bg="#CCCCFF")
        columna1.grid(row=0, column=1, ipadx=80)

        columna2 = tk.Label(self, bg="#CCCCFF")
        columna2.grid(row=0, column=2, ipadx=80)

        columna3 = tk.Label(self, bg="#CCCCFF")
        columna3.grid(row=0, column=3, ipadx=80)

        columna4 = tk.Label(self, bg="#CCCCFF")
        columna4.grid(row=0, column=4, ipadx=80)

        columna5 = tk.Label(self, bg="#CCCCFF")
        columna5.grid(row=0, column=5, ipadx=80)

        columna6 = tk.Label(self, bg="#CCCCFF")
        columna6.grid(row=0, column=6, ipadx=80)

        columna7 = tk.Label(self, bg="#CCCCFF")
        columna7.grid(row=0, column=7, ipadx=80)

        columna8 = tk.Label(self, bg="#CCCCFF")
        columna8.grid(row=0, column=0, ipadx=80)

        columna9 = tk.Label(self, bg="#CCCCFF")
        columna9.grid(row=0, column=1, ipadx=80)

        columna10 = tk.Label(self, bg="#CCCCFF")
        columna10.grid(row=0, column=2, ipadx=80)

        columna11 = tk.Label(self, bg="#CCCCFF")
        columna11.grid(row=0, column=3, ipadx=80, ipady=10)

    # FILAS

        fila0 = tk.Label(self, bg="#CCCCFF")
        fila0.grid(row=0, column=0, ipadx=80)

        fila1 = tk.Label(self, bg="#CCCCFF")
        fila1.grid(row=1, column=0, ipadx=80)

        fila2 = tk.Label(self, bg="#CCCCFF")
        fila2.grid(row=2, column=0, ipadx=80)

        fila3 = tk.Label(self, bg="#CCCCFF")
        fila3.grid(row=3, column=0, ipadx=80)

        fila4 = tk.Label(self, bg="#CCCCFF")
        fila4.grid(row=4, column=0, ipadx=80)

        fila5 = tk.Label(self, bg="#CCCCFF")
        fila5.grid(row=5, column=0, ipadx=80)

        fila6 = tk.Label(self, bg="#CCCCFF")
        fila6.grid(row=6, column=0, ipadx=80)

        fila7 = tk.Label(self, bg="#CCCCFF")
        fila7.grid(row=7, column=0, ipadx=80)

        fila8 = tk.Label(self, bg="#CCCCFF")
        fila8.grid(row=4, column=0, ipadx=80)

        fila9 = tk.Label(self, bg="#CCCCFF")
        fila9.grid(row=5, column=0, ipadx=80)

        fila10 = tk.Label(self, bg="#CCCCFF")
        fila10.grid(row=6, column=0, ipadx=80)

        fila11 = tk.Label(self, bg="#CCCCFF")
        fila11.grid(row=7, column=0, ipadx=80)


        def verficar_id():
            if paciente_id.get() == "74124434":

                #debemos ingresar la pagina del paciente regitrado aqui
                controller.show_frame(HistoriaPacienteAntiguo)
                paciente_id.set("")

#estoy teniendo problemas con el self dice que eno esta definido
        label = tk.Label(self, text="Ingrese el DNI ", font=FUENTE3, background="#CCCCFF")
        label.grid(row=3, column=0, columnspan=4, padx=20, sticky="n")

        paciente_id = tk.StringVar()
        entry = tk.Entry(self , textvariable=paciente_id, font=FUENTE3, width=10, bg="#CCCCFF")
        entry.focus_set()
        entry.grid(row=7, column=2, columnspan=4, padx=20, sticky="s")

        button = tk.Button(self, text="Aceptar", relief="groove", borderwidth=2, width=15, height=1,
                           font=FUENTE3, command=verficar_id)
        button.grid(row=7, column=4, columnspan=4, padx=20, sticky="s")

class HistoriaPacienteAntiguo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="")

        # columnas
        columna0 = tk.Label(self, bg="#CCCCFF")
        columna0.grid(row=0, column=0, ipadx=80)

        columna1 = tk.Label(self, bg="#CCCCFF")
        columna1.grid(row=0, column=1, ipadx=80)

        columna2 = tk.Label(self, bg="#CCCCFF")
        columna2.grid(row=0, column=2, ipadx=80)

        columna3 = tk.Label(self, bg="#CCCCFF")
        columna3.grid(row=0, column=3, ipadx=80)

        columna4 = tk.Label(self, bg="#CCCCFF")
        columna4.grid(row=0, column=4, ipadx=80)

        columna5 = tk.Label(self, bg="#CCCCFF")
        columna5.grid(row=0, column=5, ipadx=80)

        columna6 = tk.Label(self, bg="#CCCCFF")
        columna6.grid(row=0, column=6, ipadx=80)

        columna7 = tk.Label(self, bg="#CCCCFF")
        columna7.grid(row=0, column=7, ipadx=80)

        columna8 = tk.Label(self, bg="#CCCCFF")
        columna8.grid(row=0, column=0, ipadx=80)

        columna9 = tk.Label(self, bg="#CCCCFF")
        columna9.grid(row=0, column=1, ipadx=80)

        columna10 = tk.Label(self, bg="#CCCCFF")
        columna10.grid(row=0, column=2, ipadx=80)

        columna11 = tk.Label(self, bg="#CCCCFF")
        columna11.grid(row=0, column=3, ipadx=80, ipady=10)

        # FILAS

        fila0 = tk.Label(self, bg="#CCCCFF")
        fila0.grid(row=0, column=0, ipadx=80)

        fila1 = tk.Label(self, bg="#CCCCFF")
        fila1.grid(row=1, column=0, ipadx=80)

        fila2 = tk.Label(self, bg="#CCCCFF")
        fila2.grid(row=2, column=0, ipadx=80)

        fila3 = tk.Label(self, bg="#CCCCFF")
        fila3.grid(row=3, column=0, ipadx=80)

        fila4 = tk.Label(self, bg="#CCCCFF")
        fila4.grid(row=4, column=0, ipadx=80)

        fila5 = tk.Label(self, bg="#CCCCFF")
        fila5.grid(row=5, column=0, ipadx=80)

        fila6 = tk.Label(self, bg="#CCCCFF")
        fila6.grid(row=6, column=0, ipadx=80)

        fila7 = tk.Label(self, bg="#CCCCFF")
        fila7.grid(row=7, column=0, ipadx=80)

        fila8 = tk.Label(self, bg="#CCCCFF")
        fila8.grid(row=4, column=0, ipadx=80)

        fila9 = tk.Label(self, bg="#CCCCFF")
        fila9.grid(row=5, column=0, ipadx=80)

        fila10 = tk.Label(self, bg="#CCCCFF")
        fila10.grid(row=6, column=0, ipadx=80)

        fila11 = tk.Label(self, bg="#CCCCFF")
        fila11.grid(row=7, column=0, ipadx=80)

        # nombre
        label = tk.Label(self, text="JORGE PEREZ QUISPE", font=FUENTE3, background="#CCCCFF")
        label.place(x=190, y=150)

 #comenzamos con las zonas
    #primera tabla

        #Zona DNI
        label = tk.Label(self, text="DNI", font=FUENTE3, background="#CCCCFF")
        label.grid(row=3, column=0, columnspan=4, padx=20, sticky="s")

        label = tk.Label(self, text="DNI", font=FUENTE3, background="#CCCCFF")
        label.grid(row=3, column=2, columnspan=4, padx=20, sticky="s")

        # Zona edad
        label = tk.Label(self, text="Edad", font=FUENTE3, background="#CCCCFF")
        label.grid(row=4, column=0, columnspan=4, padx=20, sticky="s")

        label = tk.Label(self, text="60", font=FUENTE3, background="#CCCCFF")
        label.grid(row=4, column=2, columnspan=4, padx=20, sticky="s")

        # Zona nacimiento

        label = tk.Label(self, text="Fecha de nacimiento:", font=FUENTE3, background="#CCCCFF")
        label.grid(row=3, column=3, columnspan=4, padx=20, sticky="s")

        label = tk.Label(self, text="13-04-1960", font=FUENTE3, background="#CCCCFF")
        label.grid(row=3, column=4, columnspan=4, padx=20, sticky="s")

        #Zona sexo
        label = tk.Label(self, text="Sexo:", font=FUENTE3, background="#CCCCFF")
        label.grid(row=4, column=3, columnspan=4, padx=20, sticky="s")

        label = tk.Label(self, text="masculino", font=FUENTE3, background="#CCCCFF")
        label.grid(row=4, column=4, columnspan=4, padx=20, sticky="s")

        # Zona IMC
        label = tk.Label(self, text="IMC:", font=FUENTE3, background="#CCCCFF")
        label.grid(row=3, column=5, columnspan=4, padx=20, sticky="s")

        label = tk.Label(self, text="25% ", font=FUENTE3, background="#CCCCFF")
        label.grid(row=3, column=6, columnspan=4, padx=20, sticky="s")

    #tabla 2

        #Zona caidas
        #label = tk.Label(self, text="Cantidad de caídas anteriores:", font=FUENTE3, background="#CCCCFF")
        #label.grid(row=, column=, columnspan=4, padx=20, sticky="w")

        # label = tk.Label(self, text="3", font=FUENTE3, background="#CCCCFF")
       # label.grid(row=, column=, columnspan=4, padx=20, sticky="w")

        # Zona tabaco
          #label = tk.Label(self, text="Consumo de tabaco:", font=FUENTE3, background="#CCCCFF")
           #label.grid(row=, column=, columnspan=4, padx=20, sticky="w")

        #label = tk.Label(self, text="No", font=FUENTE3, background="#CCCCFF")
        #label.grid(row=, column=, columnspan=4, padx=20, sticky="w")

        # Zona Fracturas
        #label = tk.Label(self, text="Cantidad de fracturas anteriores:", font=FUENTE3, background="#CCCCFF")
        #label.grid(row=, column=, columnspan=4, padx=20, sticky="w")

        #label = tk.Label(self, text="1", font=FUENTE3, background="#CCCCFF")
       # label.grid(row=, column=, columnspan=4, padx=20, sticky="w")

        #Zona alcohol
        #label = tk.Label(self, text="Consumo de alcohol :", font=FUENTE3, background="#CCCCFF")
        #label.grid(row=, column=, columnspan=4, padx=20, sticky="w")

       # label = tk.Label(self, text="si", font=FUENTE3, background="#CCCCFF")
        #label.grid(row=, column=, columnspan=4, padx=20, sticky="w")


       #boton de actualizar
        button1 = tk.Button(self, text="Actualizar Datos", font=FUENTE3, relief="groove", borderwidth=2, width=30, height=1)
        button1.place(x=140, y=400)



class RegistrarNuevoPaciente(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#CCCCFF")
        # columnas
        columna0 = tk.Label(self, bg="#CCCCFF")
        columna0.grid(row=0, column=0, ipadx=80)

        columna1 = tk.Label(self, bg="#CCCCFF")
        columna1.grid(row=0, column=1, ipadx=80)

        columna2 = tk.Label(self, bg="#CCCCFF")
        columna2.grid(row=0, column=2, ipadx=80)

        columna3 = tk.Label(self, bg="#CCCCFF")
        columna3.grid(row=0, column=3, ipadx=80)

        columna4 = tk.Label(self, bg="#CCCCFF")
        columna4.grid(row=0, column=4, ipadx=80)

        columna5 = tk.Label(self, bg="#CCCCFF")
        columna5.grid(row=0, column=5, ipadx=80)

        columna6 = tk.Label(self, bg="#CCCCFF")
        columna6.grid(row=0, column=6, ipadx=80)

        columna7 = tk.Label(self, bg="#CCCCFF")
        columna7.grid(row=0, column=7, ipadx=80)

        columna8 = tk.Label(self, bg="#CCCCFF")
        columna8.grid(row=0, column=0, ipadx=80)

        columna9 = tk.Label(self, bg="#CCCCFF")
        columna9.grid(row=0, column=1, ipadx=80)

        columna10 = tk.Label(self, bg="#CCCCFF")
        columna10.grid(row=0, column=2, ipadx=80)

        columna11 = tk.Label(self, bg="#CCCCFF")
        columna11.grid(row=0, column=3, ipadx=80, ipady=10)

        #FILAS

        fila0 = tk.Label(self, bg="#CCCCFF")
        fila0.grid(row=0, column=0, ipadx=80)

        fila1 = tk.Label(self, bg="#CCCCFF")
        fila1.grid(row=1, column=0, ipadx=80)

        fila2 = tk.Label(self, bg="#CCCCFF")
        fila2.grid(row=2, column=0, ipadx=80)

        fila3 = tk.Label(self, bg="#CCCCFF")
        fila3.grid(row=3, column=0, ipadx=80)

        fila4 = tk.Label(self, bg="#CCCCFF")
        fila4.grid(row=4, column=0, ipadx=80)

        fila5 = tk.Label(self, bg="#CCCCFF")
        fila5.grid(row=5, column=0, ipadx=80)

        fila6 = tk.Label(self, bg="#CCCCFF")
        fila6.grid(row=6, column=0, ipadx=80)

        fila7 = tk.Label(self, bg="#CCCCFF")
        fila7.grid(row=7, column=0, ipadx=80)

        fila8 = tk.Label(self, bg="#CCCCFF")
        fila8.grid(row=4, column=0, ipadx=80)

        fila9 = tk.Label(self, bg="#CCCCFF")
        fila9.grid(row=5, column=0, ipadx=80)

        fila10 = tk.Label(self, bg="#CCCCFF")
        fila10.grid(row=6, column=0, ipadx=80)

        fila11 = tk.Label(self, bg="#CCCCFF")
        fila11.grid(row=7, column=0, ipadx=80)



        label = tk.Label(self, text="Nombres y apellidos del nuevo paciente", font=FUENTE3, background="#CCCCFF")
        label.grid(row=3, column=0, columnspan=4,padx=20, sticky="s")

        label= tk.Entry(self, font=FUENTE3, width=32, bg="white")
        label.grid(row=4, column=0, columnspan=4,padx=20, sticky="s")

        label = tk.Label(self, text="DNI" , font=FUENTE3, background="#CCCCFF")
        label.grid(row=7, column=0, padx=50, columnspan=1, sticky="W")

        label = tk.Label(self, text="edad", font=FUENTE3, background="#CCCCFF")
        label.grid(row=7, column=2, padx=50, columnspan=1, sticky="W")

        label = tk.Label(self, text="sexo", font=FUENTE3, background="#CCCCFF")
        label.grid(row=7, column=4, padx=50, columnspan=1, sticky="W")

        label = tk.Label(self, text="F.nacimiento", font=FUENTE3, background="#CCCCFF")
        label.grid(row=8, column=0, padx=50, columnspan=1, sticky="W")

        label = tk.Label(self, text="IMC(%)", font=FUENTE3, background="#CCCCFF")
        label.grid(row=8 , column=2, padx=50, columnspan=1, sticky="W")

        entry = tk.Entry(self, font=FUENTE3, width=10, bg="white")
        entry.grid(row=7, column=1, padx=50, columnspan=1, sticky="e")

        entry = tk.Entry(self, font=FUENTE3, width=10, bg="white")
        entry.grid(row=7, column=3, padx=50, columnspan=1, sticky="e")

        entry = tk.Entry(self, font=FUENTE3, width=10, bg="white")
        entry.grid(row=7, column=5, padx=50, columnspan=1, sticky="e")

        entry = tk.Entry(self, font=FUENTE3, width=10, bg="white")
        entry.grid(row=8, column=1, padx=50, columnspan=1, sticky="e")

        entry = tk.Entry(self, font=FUENTE3, width=10, bg="white")
        entry.grid(row=8, column=3, padx=50, columnspan=1, sticky="e")

        label = tk.Label(self, text="Datos Personales" ,width=75 ,font=FUENTE3, background="#7fffd4")
        label.grid(row=6, column=0, padx=50, columnspan=6, sticky="s")

        #entry = tk.Entry(self, font=FUENTE3, width=10, bg="white")
        #entry.place(x=520, y=220)

        #label = tk.Label(self, text="Fecha de nacimiento", font=FUENTE3, background="white")
        #label.place(x=600, y=320)

        #entry = tk.Entry(self, font=FUENTE3, width=10, bg="white")
        #entry.place(x=720, y=220)



app = AuquishApp()
#app.geometry("1150x720")
app.resizable(True, True)
app.mainloop()