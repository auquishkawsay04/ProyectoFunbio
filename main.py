import tkinter as tk

FUENTE21 = ("Bahnschrift SemiBold", 12)
FUENTE13 = ("Bahnschrift SemiBold", 15)
FUENTE16 = ("Bahnschrift SemiBold", 18)
FUENTE14 = ("Bahnschrift Light", 10)
FUENTE1 = ("Bahnschrift Light", 12)
FUENTE17 = ("Bahnschrift Light", 17)
FUENTE25 = ("Bahnschrift Light", 19)
FUENTE35 = ("Bahnschrift Light", 25)
FUENTE36 = ("Bahnschrift Light", 40)


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

        for F in (Login, Ramas, ActualizarRegistroNuevo, MostradorResultados, BuscadorDNI, HistoriaPacienteAntiguo,
                  RegistrarNuevoPaciente):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Login)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class Login(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="WHITE")

        def verificar_contrasena():
            if my_password.get() == "123":
                controller.show_frame(Ramas)
                incorrect_password_label["text"] = " "
                my_password.set("")
            else:
                incorrect_password_label["text"] = "La contraseña que ingresó es incorrecta. Inténtelo de nuevo"

        titulo = tk.Label(self, text="TENDOUX", font=FUENTE36, bg="#5b9fc9")
        titulo.pack(pady=75, padx=40, ipadx=350, ipady=10)

        password_label = tk.Label(self, text="Ingrese su contraseña", bg="white", fg="black", font=FUENTE17)
        password_label.pack(ipady=10)

        my_password = tk.StringVar()
        password_entry_box = tk.Entry(self, textvariable=my_password, width=22, font=FUENTE1, show="*", bg="white")
        password_entry_box.focus_set()
        password_entry_box.pack(ipady=7, pady=20)

        enter_button = tk.Button(self, text="ACEPTAR", command=verificar_contrasena, relief="groove", borderwidth=2,
                                 width=15, height=1, font=FUENTE17, fg="black")
        enter_button.pack(pady=40)

        incorrect_password_label = tk.Label(self, text=" ", bg="white", anchor="n", fg="red", font=FUENTE1)
        incorrect_password_label.pack(fill="both", expand=True)


class Ramas(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="white")

        #   columnas---------------------------------------------------------------------------------------------------
        columna0 = tk.Label(self, bg="white").grid(row=0, column=0, ipadx=80)
        columna1 = tk.Label(self, bg="white").grid(row=0, column=1, ipadx=80)
        columna2 = tk.Label(self, bg="white").grid(row=0, column=2, ipadx=80)
        columna3 = tk.Label(self, bg="white").grid(row=0, column=3, ipadx=80)
        columna4 = tk.Label(self, bg="white").grid(row=0, column=4, ipadx=80)
        columna5 = tk.Label(self, bg="white").grid(row=0, column=5, ipadx=80)
        columna6 = tk.Label(self, bg="white").grid(row=0, column=6, ipadx=80)
        columna7 = tk.Label(self, bg="white").grid(row=0, column=7, ipadx=80)

        row1 = tk.Label(self, bg="white").grid(row=1, column=7, sticky="nsew", ipadx=80, ipady=50)

        Boton1 = tk.Button(self, text="Pacientes registrados", font=FUENTE25, bg="#E7E6E6", fg="black", anchor="center",
                           relief="groove", borderwidth=2, command=lambda: controller.show_frame(BuscadorDNI))
        Boton1.grid(row=2, column=1, columnspan=4, sticky="NSEW", ipady=10)

        row3 = tk.Label(self, bg="white").grid(row=3, column=7, sticky="nsew", ipadx=80, ipady=50)

        Boton2 = tk.Button(self, text="Registrar nuevo paciente", font=FUENTE25, bg="#E7E6E6", fg="black",
                           anchor="center", relief="groove", borderwidth=2,
                           command=lambda: controller.show_frame(RegistrarNuevoPaciente))
        Boton2.grid(row=4, column=1, columnspan=4, sticky="NSEW", ipady=11)


class ActualizarRegistroNuevo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="WHITE")

        #   columnas------------------------------------------------------------------------------------------------
        columna0 = tk.Label(self, bg="white").grid(row=0, column=0, ipadx=80)
        columna1 = tk.Label(self, bg="white").grid(row=0, column=1, ipadx=80)
        columna2 = tk.Label(self, bg="white").grid(row=0, column=2, ipadx=80)
        columna3 = tk.Label(self, bg="white").grid(row=0, column=3, ipadx=80)
        columna4 = tk.Label(self, bg="white").grid(row=0, column=4, ipadx=80)
        columna5 = tk.Label(self, bg="white").grid(row=0, column=5, ipadx=80)
        columna6 = tk.Label(self, bg="white").grid(row=0, column=6, ipadx=80)
        columna7 = tk.Label(self, bg="white").grid(row=0, column=7, ipadx=80)

        #   row1 ---------------------------------------------------------------------------------------------
        row1 = tk.Label(self, bg="white").grid(row=1, column=7, ipadx=80, ipady=40)

        #   INGRESAR NUEVO REGISTRO AL DD/MM/AAAA-------------------------------------------------------------
        label1 = tk.Label(self, text="  INGRESAR NUEVO REGISTRO", font=FUENTE13, background="#5b9fc9", anchor="w",
                          fg="white").grid(row=2, column=1, columnspan=6, sticky="NSEW")

        row5 = tk.Label(self, bg="white").grid(row=5, column=7, ipadx=80, ipady=0)

        #   ALTURA
        label10 = tk.Label(self, text="Altura:  ", font=FUENTE1, anchor="e", bg="white").grid(row=6, column=1,
                                                                                              columnspan=2,
                                                                                              sticky="nsew")

        alturaNueva = tk.Entry(self, font=FUENTE1, bg="white", width=1).grid(row=6, column=3, sticky="nsew")

        #   TALLA
        label11 = tk.Label(self, text="Peso: ", font=FUENTE1, anchor="e", bg="white")
        label11.grid(row=6, column=4, columnspan=2, sticky="nsew")

        tallaNueva = tk.Entry(self, font=FUENTE1, bg="white", width=1).grid(row=6, column=6, sticky="nsew")

        #   DMO
        label10 = tk.Label(self, text="DMO:  ", font=FUENTE1, anchor="e", bg="white").grid(row=7, column=1,
                                                                                           columnspan=2, sticky="nsew")

        dmoNueva = tk.Entry(self, font=FUENTE1, bg="white", width=1).grid(row=7, column=3, sticky="nsew")

        #   T-Score
        label11 = tk.Label(self, text="T-Score: ", font=FUENTE1, anchor="e", bg="white")
        label11.grid(row=7, column=4, columnspan=2, sticky="nsew")

        scoreNueva = tk.Entry(self, font=FUENTE1, bg="white", width=1).grid(row=7, column=6, sticky="nsew")

        #   CANTIDAD DE CAIDAS ANTERIORES
        label10 = tk.Label(self, text="Cantidad de caídas anteriores:  ", font=FUENTE1, anchor="e", bg="white").grid(
            row=14, column=1, columnspan=2, sticky="nsew")

        caidasNueva = tk.Entry(self, font=FUENTE1, bg="white", width=1).grid(row=14, column=3, sticky="nsew")

        #   CANTIDAD DE FRACTURAS ANTERIORES
        label11 = tk.Label(self, text="Cantidad de fracturas anteriores: ", font=FUENTE1, anchor="e", bg="white")
        label11.grid(row=14, column=4, columnspan=2, sticky="nsew")

        fracturasNueva = tk.Entry(self, font=FUENTE1, bg="white", width=1).grid(row=14, column=6, sticky="nsew")

        #   CONSUME TABACO
        label12 = tk.Label(self, text=" ¿Consume tabaco con frecuencia? ", font=FUENTE1, anchor="e", bg="white").grid(
            row=15, column=1, columnspan=2, sticky="nsew", ipady=5)

        tabacoNuevoPaciente = tk.IntVar()
        botonTabaco1 = tk.Radiobutton(self, text="Sí", variable=tabacoNuevoPaciente, value=1, font=FUENTE1,
                                      anchor="center", bg="white")
        botonTabaco1.grid(row=15, column=3, sticky="nsew")
        botonTabaco2 = tk.Radiobutton(self, text="No", variable=tabacoNuevoPaciente, value=2, font=FUENTE1,
                                      anchor="center", bg="white")
        botonTabaco2.grid(row=16, column=3, sticky="nsew")

        #   BEBIDAS ALCOHOLICAS
        label13 = tk.Label(self, text=" ¿Bebe alcohol con frecuencia? ", font=FUENTE1, anchor="e", bg="white")
        label13.grid(row=15, column=4, columnspan=2, sticky="nsew", ipady=5)

        alcoholNuevoPaciente = tk.IntVar()
        botonAlcohol1 = tk.Radiobutton(self, text="Sí", variable=alcoholNuevoPaciente, value=1, font=FUENTE1,
                                       anchor="center", bg="white")
        botonAlcohol1.grid(row=15, column=6, sticky="nsew")
        botonAlcohol2 = tk.Radiobutton(self, text="No", variable=alcoholNuevoPaciente, value=2, font=FUENTE1,
                                       anchor="center", bg="white", )
        botonAlcohol2.grid(row=16, column=6, sticky="nsew")

        row17 = tk.Label(self, bg="white").grid(row=17, column=7, ipadx=80, ipady=50)

        #   BOTON ----------------------------------------------------------------------------------------------------
        button1 = tk.Button(self, text="Registrar y ver resultados", font=FUENTE16, relief="groove", borderwidth=2,
                            height=1, command=lambda: controller.show_frame(MostradorResultados))
        button1.grid(row=18, column=4, columnspan=3, ipadx=27, sticky="e")

        botonRegresar = tk.Button(self, text="←", font=FUENTE17, relief="groove", borderwidth=2, width=5, height=1,
                                  command=lambda: controller.show_frame(HistoriaPacienteAntiguo), bg="white")
        botonRegresar.place(x=10, y=10)


class MostradorResultados(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="WHITE")

        #   columns----------------------------------------------------------------------------------------------------
        column0 = tk.Label(self, bg="WHITE").grid(row=0, column=0, ipadx=80)
        column1 = tk.Label(self, bg="WHITE").grid(row=0, column=1, ipadx=80)
        column2 = tk.Label(self, bg="WHITE").grid(row=0, column=2, ipadx=80)
        column3 = tk.Label(self, bg="WHITE").grid(row=0, column=3, ipadx=80)
        column4 = tk.Label(self, bg="WHITE").grid(row=0, column=4, ipadx=80)
        column5 = tk.Label(self, bg="WHITE").grid(row=0, column=5, ipadx=80)
        column6 = tk.Label(self, bg="WHITE").grid(row=0, column=6, ipadx=80)
        column7 = tk.Label(self, bg="WHITE").grid(row=0, column=7, ipadx=80)

        #   row1 ------------------------------------------------------------------------------------------------------
        row1 = tk.Label(self, bg="white").grid(row=1, column=7, ipadx=80, ipady=30)

        #   RESULTADOS DEL 20/05/2013----------------------------------------------------------------------------
        label1 = tk.Label(self, text="  RESULTADOS DEL 20/05/2013", font=FUENTE13, background="#5b9fc9", anchor="w",
                          fg="white").grid(row=2, column=1, columnspan=6, sticky="NSEW")

        row5 = tk.Label(self, bg="white").grid(row=5, column=7, ipadx=80, ipady=0)

        #   Estado Óseo
        label3 = tk.Label(self, text="Estado Óseo: ", font=FUENTE21, anchor="e", bg="white").grid(row=8, column=1,
                                                                                                  sticky="nsew")

        estadoResultado = tk.Label(self, text="Osteoporosis Grave", font=FUENTE1, bg="white", anchor="w").grid(row=8,
                                                                                                               column=2,
                                                                                                               sticky="nsew")

        #   IMC
        label5 = tk.Label(self, text="IMC: ", font=FUENTE21, anchor="e", bg="white").grid(row=8, column=3,
                                                                                          sticky="nsew")

        imcResultado = tk.Label(self, text="17", font=FUENTE1, bg="white", anchor="w").grid(row=8, column=4,
                                                                                            sticky="nsew")
        #   DMO
        label5 = tk.Label(self, text="DMO: ", font=FUENTE21, anchor="e", bg="white").grid(row=8, column=5,
                                                                                          sticky="nsew")

        dmoResultado = tk.Label(self, text="1", font=FUENTE1, bg="white", anchor="w").grid(row=8, column=6,
                                                                                           sticky="nsew")

        ####
        row9 = tk.Label(self, bg="white").grid(row=9, column=7, ipadx=80, ipady=0)

        #   Riesgo de fractura
        label4 = tk.Label(self, text="Riesgo de fractura:", font=FUENTE21, anchor="e", bg="white").grid(row=10,
                                                                                                        column=1,
                                                                                                        sticky="nsew")

        nacimientoNuevoPaciente = tk.Label(self, text="90% *", font=FUENTE1, bg="white", anchor="w").grid(row=10,
                                                                                                          column=2,
                                                                                                          sticky="nsew")

        #   T-Score
        label6 = tk.Label(self, text="T-Score: ", font=FUENTE21, anchor="e", bg="white").grid(row=10, column=3,
                                                                                              sticky="nsew")

        tscoreResultado = tk.Label(self, text="2.3", font=FUENTE1, bg="white", anchor="w").grid(row=10, column=4,
                                                                                                sticky="nsew")

        #   Separacion
        row11 = tk.Label(self, bg="white").grid(row=11, column=7, ipadx=80, ipady=0)

        #   RECOMENDACIONES----------------------------------------------------------------------------
        label1 = tk.Label(self, text="  RECOMENDACIONES", font=FUENTE13, background="#5b9fc9", anchor="w",
                          fg="white").grid(row=12, column=1, columnspan=6, sticky="NSEW")

        row13 = tk.Label(self, bg="white").grid(row=13, column=7, ipadx=80, ipady=0)

        recomendacionesResultado = tk.Label(self, text="  Comer sano y hacer deporte.", font=FUENTE1, bg="white",
                                            anchor="w").grid(row=14, column=1, columnspan=5, sticky="nsew")

        row13 = tk.Label(self, bg="white").grid(row=15, column=7, ipadx=80, ipady=40)

        #   BOTON ----------------------------------------------------------------------------------------------------
        button1 = tk.Button(self, text="Imprimir", font=FUENTE16, relief="groove", borderwidth=2, height=1,
                            command=lambda: controller.show_frame(MostradorResultados))
        button1.grid(row=18, column=4, columnspan=3, ipadx=27, sticky="e")

        botonRegresar = tk.Button(self, text="←", font=FUENTE17, relief="groove", borderwidth=2, width=5, height=1,
                                  command=lambda: controller.show_frame(HistoriaPacienteAntiguo), bg="white")
        botonRegresar.place(x=10, y=10)


class BuscadorDNI(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="white")

        column0 = tk.Label(self, bg="white").grid(row=0, column=0, ipadx=80)
        column1 = tk.Label(self, bg="white").grid(row=0, column=1, ipadx=80)
        column2 = tk.Label(self, bg="white").grid(row=0, column=2, ipadx=80)
        column3 = tk.Label(self, bg="white").grid(row=0, column=3, ipadx=80)
        column4 = tk.Label(self, bg="white").grid(row=0, column=4, ipadx=80)
        column5 = tk.Label(self, bg="white").grid(row=0, column=5, ipadx=80)
        column6 = tk.Label(self, bg="white").grid(row=0, column=6, ipadx=80)
        column7 = tk.Label(self, bg="white").grid(row=0, column=7, ipadx=80)

        row1 = tk.Label(self, bg="white").grid(row=1, column=7, sticky="nsew", ipadx=80, ipady=50)

        label1 = tk.Label(self, text="Ingrese el DNI del paciente", font=FUENTE35, background="#5b9fc9",
                          anchor="center", fg="white").grid(row=2, column=1, columnspan=6, sticky="NSEW", ipady=10)

        row3 = tk.Label(self, bg="white").grid(row=3, column=7, sticky="nsew", ipadx=80, ipady=17)

        label2 = tk.Entry(self, font=FUENTE35, background="white", width=20, justify="right", fg="black").grid(row=4,
                                                                                                               column=1,
                                                                                                               columnspan=3,
                                                                                                               sticky="e")

        row4 = tk.Label(self, bg="white").grid(row=5, column=7, sticky="nsew", ipadx=80, ipady=17)

        button1 = tk.Button(self, text="BUSCAR", font=FUENTE35, relief="groove", borderwidth=2, height=1,
                            command=lambda: controller.show_frame(HistoriaPacienteAntiguo))
        button1.grid(row=6, column=5, columnspan=2, ipadx=30)

        botonRegresar = tk.Button(self, text="←", font=FUENTE17, relief="groove", borderwidth=2, width=5, height=1,
                                  bg="white", command=lambda: controller.show_frame(Ramas))
        botonRegresar.place(x=10, y=10)


class HistoriaPacienteAntiguo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="WHITE")

        #   columns---------------------------------------------------------------------------------------------------
        column0 = tk.Label(self, bg="white").grid(row=0, column=0, ipadx=80)
        column1 = tk.Label(self, bg="white").grid(row=0, column=1, ipadx=80)
        column2 = tk.Label(self, bg="white").grid(row=0, column=2, ipadx=80)
        column3 = tk.Label(self, bg="white").grid(row=0, column=3, ipadx=80)
        column4 = tk.Label(self, bg="white").grid(row=0, column=4, ipadx=80)
        column5 = tk.Label(self, bg="white").grid(row=0, column=5, ipadx=80)
        column6 = tk.Label(self, bg="white").grid(row=0, column=6, ipadx=80)
        column7 = tk.Label(self, bg="white").grid(row=0, column=7, ipadx=80)

        #   row1 ------------------------------------------------------------------------------------------------------
        row1 = tk.Label(self, bg="white").grid(row=1, column=7, ipadx=80, ipady=0)

        #   APELLIDOS Y NOMBRES DEL PACIENTE---------------------------------------------------------------------------
        label1 = tk.Label(self, text="  APELLIDOS Y NOMBRES DEL PACIENTE", font=FUENTE13, background="#5b9fc9",
                          anchor="w", fg="white").grid(row=2, column=1, columnspan=6, sticky="NSEW", )

        row3 = tk.Label(self, bg="white").grid(row=3, column=7, ipadx=80, ipady=0)

        nombreNuevoPaciente = tk.Label(self, text="Juan Carlos Solís", font=FUENTE25, bg="white", width=1).grid(row=4,
                                                                                                                column=1,
                                                                                                                columnspan=3,
                                                                                                                sticky="NSEW")

        row5 = tk.Label(self, bg="white").grid(row=5, column=7, ipadx=80, ipady=0)

        #   DATOS PERSONALES-------------------------------------------------------------------------------------------
        label2 = tk.Label(self, text="  DATOS PERSONALES", font=FUENTE13, background="#5b9fc9", anchor="w", fg="white")
        label2.grid(row=6, column=1, columnspan=6, sticky="NSEW", )

        row7 = tk.Label(self, bg="white").grid(row=7, column=7, ipadx=80)

        #   DNI
        label3 = tk.Label(self, text="DNI: ", font=FUENTE21, anchor="e", bg="white").grid(row=8, column=1,
                                                                                          sticky="nsew")

        dniNuevoPaciente = tk.Label(self, text="75369685", font=FUENTE1, bg="white", width=1).grid(row=8, column=2,
                                                                                                   sticky="nsew")

        #   EDAD
        label4 = tk.Label(self, text="Edad: ", font=FUENTE21, anchor="e", bg="white").grid(row=9, column=1,
                                                                                           sticky="nsew")

        nacimientoNuevoPaciente = tk.Label(self, text="59 años", font=FUENTE1, bg="white", width=1).grid(row=9,
                                                                                                         column=2,
                                                                                                         sticky="nsew")

        #   PESO
        label5 = tk.Label(self, text="Peso: ", font=FUENTE21, anchor="e", bg="white").grid(row=8, column=3,
                                                                                           sticky="nsew")

        pesoNuevoPaciente = tk.Label(self, text="60 kg", font=FUENTE1, bg="white", width=1).grid(row=8, column=4,
                                                                                                 sticky="nsew")

        #   ALTURA
        label6 = tk.Label(self, text="Altura: ", font=FUENTE21, anchor="e", bg="white").grid(row=9, column=3,
                                                                                             sticky="nsew")

        alturaNuevoPaciente = tk.Label(self, text="160 cm", font=FUENTE1, bg="white", width=1).grid(row=9, column=4,
                                                                                                    sticky="nsew")

        #  SEXO
        label7 = tk.Label(self, text="Sexo:", font=FUENTE21, anchor="e", background="white").grid(row=8, column=5,
                                                                                                  sticky="nsew")

        sexo = tk.Label(self, text="Femenino", font=FUENTE1, bg="white", width=1).grid(row=8, column=6, sticky="nsew")

        #  IMC
        label17 = tk.Label(self, text="IMC:", font=FUENTE21, anchor="e", background="white").grid(row=9, column=5,
                                                                                                  sticky="nsew")

        imc = tk.Label(self, text="18.3", font=FUENTE1, bg="white", width=1).grid(row=9, column=6, sticky="nsew")

        row11 = tk.Label(self, bg="white").grid(row=11, column=7, ipadx=80)

        #   ANTECEDENTES--------------------------------------------------------------------------------------------
        label9 = tk.Label(self, text="  ANTECEDENTES", font=FUENTE13, background="#5b9fc9", anchor="w", fg="white")
        label9.grid(row=12, column=1, columnspan=6, sticky="NSEW", )

        row13 = tk.Label(self, bg="white").grid(row=13, column=7, ipadx=80)

        #   CANTIDAD DE CAIDAS ANTERIORES
        label10 = tk.Label(self, text="Cantidad de caídas anteriores:  ", font=FUENTE21, anchor="e", bg="white").grid(
            row=14, column=1, columnspan=2, sticky="nsew")

        caidasNuevoPaciente = tk.Label(self, text="2", font=FUENTE1, bg="white", width=1).grid(row=14, column=3,
                                                                                               sticky="nsew")

        #   CANTIDAD DE FRACTURAS ANTERIORES
        label11 = tk.Label(self, text="Cantidad de fracturas anteriores: ", font=FUENTE21, anchor="e", bg="white")
        label11.grid(row=14, column=4, columnspan=2, sticky="nsew")

        fracturasNuevoPaciente = tk.Label(self, text="0", font=FUENTE1, bg="white", width=1)
        fracturasNuevoPaciente.grid(row=14, column=6, sticky="nsew")

        #   CONSUME TABACO
        label12 = tk.Label(self, text=" Consumidor de tabaco: ", font=FUENTE21, anchor="e", bg="white")
        label12.grid(row=15, column=1, columnspan=2, sticky="nsew", ipady=5)

        tabaco = tk.Label(self, text="Sí", font=FUENTE1, bg="white", width=1)
        tabaco.grid(row=15, column=3, sticky="nsew")

        #   BEBIDAS ALCOHOLICAS
        label12 = tk.Label(self, text=" Consumidor de alcohol: ", font=FUENTE21, anchor="e", bg="white")
        label12.grid(row=15, column=4, columnspan=2, sticky="nsew", ipady=5)

        alcohol = tk.Label(self, text="Sí", font=FUENTE1, bg="white", width=1)
        alcohol.grid(row=15, column=6, sticky="nsew")

        row17 = tk.Label(self, bg="white").grid(row=17, column=7, ipadx=80)

        #   HISTORIAL------------------------------------------------------------------------------------------------
        label14 = tk.Label(self, text="HISTORIAL", font=FUENTE13, anchor="center", background="#5b9fc9", fg="white")
        label14.grid(row=18, column=1, columnspan=6, sticky="NSEW", )

        row19 = tk.Label(self, bg="white").grid(row=19, column=7, ipadx=80)

        #   DNI
        tabla1 = tk.Label(self, text="FECHA", font=FUENTE21, anchor="center", background="#5b9fc9", fg="white").grid(
            row=20, column=1, sticky="nsew")
        tabla2 = tk.Label(self, text="DMO", font=FUENTE21, anchor="center", background="#5b9fc9", fg="white").grid(
            row=20, column=2, sticky="nsew")
        tabla3 = tk.Label(self, text="T-SCORE", font=FUENTE21, anchor="center", background="#5b9fc9", fg="white").grid(
            row=20, column=3, sticky="nsew")
        tabla4 = tk.Label(self, text="RIESGO DE FRACTURA", font=FUENTE21, anchor="center", background="#5b9fc9",
                          fg="white").grid(row=20, column=4, columnspan=2, sticky="nsew")
        tabla5 = tk.Label(self, text=" ", font=FUENTE21, anchor="center", background="#5b9fc9", fg="white").grid(row=20,
                                                                                                                 column=6,
                                                                                                                 sticky="nsew")

        #   Formato 1---
        fechaVariable1 = tk.Label(self, text="02/06/2013", font=FUENTE1, bg="white", width=1, relief="solid",
                                  borderwidth=1)
        fechaVariable1.grid(row=21, column=1, sticky="nsew")

        dmoVariable1 = tk.Label(self, text="1.0", font=FUENTE1, bg="white", width=1, relief="solid", borderwidth=1)
        dmoVariable1.grid(row=21, column=2, sticky="nsew")

        scoreVariable1 = tk.Label(self, text="2", font=FUENTE1, bg="white", width=1, relief="solid", borderwidth=1)
        scoreVariable1.grid(row=21, column=3, sticky="nsew")

        riesgoVariable1 = tk.Label(self, text="80%", font=FUENTE1, bg="white", width=1, relief="solid", borderwidth=1)
        riesgoVariable1.grid(row=21, column=4, columnspan=2, sticky="nsew")

        detalleVariable1 = tk.Label(self, text="Detalle...", font=FUENTE1, bg="white", width=1, relief="solid",
                                    borderwidth=1)
        detalleVariable1.grid(row=21, column=6, sticky="nsew")

        #   BOTON FINALIZAR----------------------------------------------------------------------------------------
        button1 = tk.Button(self, text="ACTUALIZAR DATOS", font=FUENTE16, relief="groove", borderwidth=2, height=1,
                            command=lambda: controller.show_frame(ActualizarRegistroNuevo))
        button1.grid(row=39, column=5, columnspan=2, ipadx=27, pady=35)

        botonRegresar = tk.Button(self, text="←", font=FUENTE17, relief="groove", borderwidth=2, width=5, height=1,
                                  command=lambda: controller.show_frame(Ramas), bg="white")
        botonRegresar.place(x=10, y=10)


class RegistrarNuevoPaciente(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="WHITE")

        #   columnas-------------------------------------------------------------------------
        columna0 = tk.Label(self, bg="white").grid(row=0, column=0, ipadx=80)
        columna1 = tk.Label(self, bg="white").grid(row=0, column=1, ipadx=80)
        columna2 = tk.Label(self, bg="white").grid(row=0, column=2, ipadx=80)
        columna3 = tk.Label(self, bg="white").grid(row=0, column=3, ipadx=80)
        columna4 = tk.Label(self, bg="white").grid(row=0, column=4, ipadx=80)
        columna5 = tk.Label(self, bg="white").grid(row=0, column=5, ipadx=80)
        columna6 = tk.Label(self, bg="white").grid(row=0, column=6, ipadx=80)
        columna7 = tk.Label(self, bg="white").grid(row=0, column=7, ipadx=80)

        #   separador ---------------------------------------------------------------------------------
        fila1 = tk.Label(self, bg="white").grid(row=1, column=7, ipadx=80, ipady=0)

        #   APELLIDOS Y NOMBRES DEL PACIENTE----------------------------------------------------------------
        label1 = tk.Label(self, text="  APELLIDOS Y NOMBRES DEL PACIENTE", font=FUENTE13, background="#5b9fc9",
                          anchor="w", fg="white").grid(row=2, column=1, columnspan=6, sticky="NSEW")

        #   separador
        fila3 = tk.Label(self, bg="white").grid(row=3, column=7, ipadx=80, ipady=0)

        nombreNuevoPaciente = tk.Entry(self, font=FUENTE25, bg="white", width=1).grid(row=4, column=1, columnspan=3,
                                                                                      sticky="NSEW")

        #   separador
        fila5 = tk.Label(self, bg="white").grid(row=5, column=7, ipadx=80, ipady=0)

        #   DATOS PERSONALES--------------------------------------------------------------------------------------------
        label2 = tk.Label(self, text="  DATOS PERSONALES", font=FUENTE13, background="#5b9fc9", anchor="w", fg="white")
        label2.grid(row=6, column=1, columnspan=6, sticky="NSEW", )

        row7 = tk.Label(self, bg="white").grid(row=7, column=7, ipadx=80)

        #   DNI
        label3 = tk.Label(self, text="DNI: ", font=FUENTE1, anchor="e", bg="white").grid(row=8, column=1, sticky="nsew")

        dniNuevoPaciente = tk.Entry(self, font=FUENTE1, bg="white", width=1).grid(row=8, column=2, sticky="nsew")

        #   NACIMIENTO
        label4 = tk.Label(self, text="F. Nacimiento: ", font=FUENTE1, anchor="e", bg="white").grid(row=9, column=1,
                                                                                                   sticky="nsew")

        nacimientoNuevoPaciente = tk.Entry(self, font=FUENTE1, bg="white", width=1).grid(row=9, column=2, sticky="nsew")

        label0 = tk.Label(self, text="(DD/MM/AAAA) ", font=FUENTE14, anchor="e", bg="white").grid(row=10, column=1,
                                                                                                  sticky="nsew")

        #   PESO
        label5 = tk.Label(self, text="Peso (kg): ", font=FUENTE1, anchor="e", bg="white").grid(row=8, column=3,
                                                                                               sticky="nsew")

        pesoNuevoPaciente = tk.Entry(self, font=FUENTE1, bg="white", width=1).grid(row=8, column=4, sticky="nsew")

        #   ALTURA
        label6 = tk.Label(self, text="Altura (cm): ", font=FUENTE1, anchor="e", bg="white").grid(row=9, column=3,
                                                                                                 sticky="nsew")

        alturaNuevoPaciente = tk.Entry(self, font=FUENTE1, bg="white", width=1).grid(row=9, column=4, sticky="nsew")

        #   SEXO
        label7 = tk.Label(self, text="Sexo:", font=FUENTE1, anchor="e", background="white").grid(row=8, column=5,
                                                                                                 sticky="nsew")

        sexoNuevoPaciente = tk.IntVar()
        botonM = tk.Radiobutton(self, text="Masculino", variable=sexoNuevoPaciente, value=1, font=FUENTE1, anchor="w",
                                bg="white").grid(row=8, column=6, sticky="nsew", padx=5)
        botonF = tk.Radiobutton(self, text="Femenino", variable=sexoNuevoPaciente, value=2, font=FUENTE1, anchor="w",
                                bg="white").grid(row=9, column=6, sticky="nsew", padx=5)

        row11 = tk.Label(self, bg="white").grid(row=11, column=7, ipadx=80)

        #   ANTECEDENTES----------------------------------------------------------------------------------------------
        label9 = tk.Label(self, text="  ANTECEDENTES", font=FUENTE13, background="#5b9fc9", anchor="w", fg="white")
        label9.grid(row=12, column=1, columnspan=6, sticky="NSEW", )

        row13 = tk.Label(self, bg="white").grid(row=13, column=7, ipadx=80)

        #   CANTIDAD DE CAIDAS ANTERIORES
        label10 = tk.Label(self, text="Cantidad de caídas anteriores:  ", font=FUENTE1, anchor="e", bg="white").grid(
            row=14, column=1, columnspan=2, sticky="nsew")

        caidasNuevoPaciente = tk.Entry(self, font=FUENTE1, bg="white", width=1).grid(row=14, column=3, sticky="nsew")

        #   CANTIDAD DE FRACTURAS ANTERIORES
        label11 = tk.Label(self, text="Cantidad de fracturas anteriores: ", font=FUENTE1, anchor="e", bg="white")
        label11.grid(row=14, column=4, columnspan=2, sticky="nsew")

        fracturasNuevoPaciente = tk.Entry(self, font=FUENTE1, bg="white", width=1)
        fracturasNuevoPaciente.grid(row=14, column=6, sticky="nsew")

        #   CONSUME TABACO
        label12 = tk.Label(self, text=" ¿Consume tabaco con frecuencia? ", font=FUENTE1, anchor="e", bg="white")
        label12.grid(row=15, column=1, columnspan=2, sticky="nsew", ipady=5)

        tabacoNuevoPaciente = tk.IntVar()
        botonTabaco1 = tk.Radiobutton(self, text="Sí", variable=tabacoNuevoPaciente, value=1, font=FUENTE1,
                                      anchor="center", bg="white")
        botonTabaco1.grid(row=15, column=3, sticky="nsew")
        botonTabaco2 = tk.Radiobutton(self, text="No", variable=tabacoNuevoPaciente, value=2, font=FUENTE1,
                                      anchor="center", bg="white")
        botonTabaco2.grid(row=16, column=3, sticky="nsew")

        #   BEBIDAS ALCOHOLICAS
        label13 = tk.Label(self, text=" ¿Bebe alcohol con frecuencia? ", font=FUENTE1, anchor="e", bg="white")
        label13.grid(row=15, column=4, columnspan=2, sticky="nsew", ipady=5)

        alcoholNuevoPaciente = tk.IntVar()
        botonAlcohol1 = tk.Radiobutton(self, text="Sí", variable=alcoholNuevoPaciente, value=1, font=FUENTE1,
                                       anchor="center", bg="white")
        botonAlcohol1.grid(row=15, column=6, sticky="nsew")
        botonAlcohol2 = tk.Radiobutton(self, text="No", variable=alcoholNuevoPaciente, value=2, font=FUENTE1,
                                       anchor="center", bg="white", )
        botonAlcohol2.grid(row=16, column=6, sticky="nsew")

        row17 = tk.Label(self, bg="white").grid(row=17, column=7, ipadx=80)

        #   EXAMENES MÉDICOS------------------------------------------------------------------------------------------
        label14 = tk.Label(self, text="  EXÁMENES MÉDICOS", font=FUENTE13, background="#5b9fc9", anchor="w", fg="white")
        label14.grid(row=18, column=1, columnspan=6, sticky="NSEW", )

        row19 = tk.Label(self, bg="white").grid(row=19, column=7, ipadx=80)

        #   FECHA
        label15 = tk.Label(self, text="Fecha de toma: ", font=FUENTE1, anchor="e", bg="white")
        label15.grid(row=20, column=1, sticky="nsew")

        fechaExamenNuevoPaciente = tk.Entry(self, font=FUENTE1, bg="white", width=1).grid(row=20, column=2,
                                                                                          sticky="nsew")

        #   DMO
        label16 = tk.Label(self, text="DMO: ", font=FUENTE1, anchor="e", bg="white").grid(row=20, column=3,
                                                                                          sticky="nsew")

        dmoNuevoPaciente = tk.Entry(self, font=FUENTE1, bg="white", width=1).grid(row=20, column=4, sticky="nsew")

        #   T-Score
        label17 = tk.Label(self, text="T-Score: ", font=FUENTE1, anchor="e", bg="white").grid(row=20, column=5,
                                                                                              sticky="nsew")

        scoreNuevoPaciente = tk.Entry(self, font=FUENTE1, bg="white", width=1).grid(row=20, column=6, sticky="nsew")

        #   (DD/MM/AAAA)
        label18 = tk.Label(self, text="(DD/MM/AAAA) ", font=FUENTE14, anchor="e", bg="white")
        label18.grid(row=21, column=1, sticky="nsew")

        #   (G/CM)
        label19 = tk.Label(self, text="(g/cm²) ", font=FUENTE14, anchor="e", bg="white")
        label19.grid(row=21, column=3, sticky="nsew")

        row22 = tk.Label(self, bg="white").grid(row=22, column=7, ipadx=80)

        #   BOTON FINALIZAR-----------------------------------------------------------------------------------------
        button1 = tk.Button(self, text="FINALIZAR", font=FUENTE16, relief="groove", borderwidth=2, height=1,
                            command=lambda: controller.show_frame(MostradorResultados))
        button1.grid(row=23, column=5, columnspan=2, ipadx=27)

        row24 = tk.Label(self, bg="white").grid(row=24, column=7, ipadx=80, ipady=10)

        botonRegresar = tk.Button(self, text="←", font=FUENTE17, relief="groove", borderwidth=2, width=5, height=1,
                                  bg="white", command=lambda: controller.show_frame(Ramas))
        botonRegresar.place(x=10, y=10)


app = AuquishApp()
app.resizable(False, False)
app.mainloop()
