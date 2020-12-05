import tkinter as tk

FUENTE21 = ("Bahnschrift SemiBold", 12)
FUENTE13 = ("Bahnschrift SemiBold", 13)
FUENTE16 = ("Bahnschrift SemiBold", 15)
FUENTE14 = ("Bahnschrift Light", 8)
FUENTE1 = ("Bahnschrift Light", 11)
FUENTE11 = ("Bahnschrift Light", 13)
FUENTE17 = ("Bahnschrift Light", 17)
FUENTE25 = ("Bahnschrift Light", 19)
FUENTE255 = ("Bahnschrift Light", 19)
FUENTE35 = ("Bahnschrift Light", 25)
FUENTE36 = ("Bahnschrift Light", 40)
FUENTEFLECHA = ("Calibri bold", 17)
FUENTEPIE = ("Bahnschrift Light", 10)


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
        columna0 = tk.Label(self, bg="WHITE").grid(row=0, column=0, ipadx=80)
        columna1 = tk.Label(self, bg="WHITE").grid(row=0, column=1, ipadx=80)
        columna2 = tk.Label(self, bg="WHITE").grid(row=0, column=2, ipadx=80)
        columna3 = tk.Label(self, bg="WHITE").grid(row=0, column=3, ipadx=80)
        columna4 = tk.Label(self, bg="WHITE").grid(row=0, column=4, ipadx=80)
        columna5 = tk.Label(self, bg="WHITE").grid(row=0, column=5, ipadx=80)
        columna6 = tk.Label(self, bg="WHITE").grid(row=0, column=6, ipadx=80)
        columna7 = tk.Label(self, bg="WHITE").grid(row=0, column=7, ipadx=80)

        row1 = tk.Label(self, bg="white").grid(row=1, column=7, sticky="nsew", ipadx=80, ipady=80)

        Boton1 = tk.Button(self, text="Pacientes registrados", font=FUENTE25, bg="#5b9fc9", fg="white", anchor="center",
                           relief="groove", borderwidth=2, command=lambda: controller.show_frame(BuscadorDNI))
        Boton1.grid(row=2, column=1, columnspan=4, sticky="NSEW", ipady=10)

        row3 = tk.Label(self, bg="white").grid(row=3, column=7, sticky="nsew", ipadx=80, ipady=50)

        Boton2 = tk.Button(self, text="Registrar nuevo paciente", font=FUENTE25,  bg="#5b9fc9", fg="white",
                           anchor="center", relief="groove", borderwidth=2,
                           command=lambda: controller.show_frame(RegistrarNuevoPaciente))
        Boton2.grid(row=4, column=1, columnspan=4, sticky="NSEW", ipady=11)

class ActualizarRegistroNuevo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="WHITE")

        #   columnas------------------------------------------------------------------------------------------------
        columna0 = tk.Label(self, bg="WHITE").grid(row=0, column=0, ipadx=80)
        columna1 = tk.Label(self, bg="WHITE").grid(row=0, column=1, ipadx=80)
        columna2 = tk.Label(self, bg="WHITE").grid(row=0, column=2, ipadx=80)
        columna3 = tk.Label(self, bg="WHITE").grid(row=0, column=3, ipadx=80)
        columna4 = tk.Label(self, bg="WHITE").grid(row=0, column=4, ipadx=80)
        columna5 = tk.Label(self, bg="WHITE").grid(row=0, column=5, ipadx=80)
        columna6 = tk.Label(self, bg="WHITE").grid(row=0, column=6, ipadx=80)
        columna7 = tk.Label(self, bg="WHITE").grid(row=0, column=7, ipadx=80)
        #   row1 ---------------------------------------------------------------------------------------------
        row1 = tk.Label(self, bg="white").grid(row=1, column=7, ipadx=80, ipady=10)

        #   NUEVA CONSULTA---------------------------------------------------------------------------------------------
        label = tk.Label(self, text="  NUEVA CONSULTA", font=FUENTE13, background="#5b9fc9", anchor="w", fg="white").grid(row=12, column=1, columnspan=6, sticky="NSEW", )

        row = tk.Label(self, bg="white").grid(row=13, column=7, ipadx=80, ipady=8)

        #   TALLA
        label = tk.Label(self, text=" Talla (cm):", font=FUENTE1, anchor="e", bg="white").grid(row=15, column=1,columnspan=2, sticky="nsew")
        tallaVariable = tk.Entry(self, font=FUENTE1, bg="white", width=1).grid(row=15, column=3, sticky="nsew")

        #   PESO
        label = tk.Label(self, text=" Peso (kg):", font=FUENTE1, anchor="e", bg="white").grid(row=15, column=4, columnspan=2, sticky="nsew")
        pesoVariable = tk.Entry(self, font=FUENTE1, bg="white", width=1).grid(row=15, column=6, sticky="nsew")

        #   CAIDAS ANTERIORES
        label = tk.Label(self, text="Número de fracturas luego de los 50 años* :", font=FUENTE1, anchor="e", bg="white").grid(row=17, column=1,columnspan=2, sticky="nsew")
        caidasVariable = tk.Entry(self, font=FUENTE1, bg="white", width=1).grid(row=17, column=3, sticky="nsew")

        #   FRACTURAS ANTERIORES
        label = tk.Label(self, text="Número de caídas en el último año:", font=FUENTE1, anchor="e", bg="white").grid(row=17, column=4, columnspan=2, sticky="nsew")
        fracturasVariables = tk.Entry(self, font=FUENTE1, bg="white", width=1).grid(row=17, column=6, sticky="nsew")

        row = tk.Label(self, bg="white").grid(row=20, column=7, ipadx=80, ipady=10)

        #   PADRES FRACTURAS
        label = tk.Label(self, text="¿Padres con fractura de cadera?", font=FUENTE1, anchor="center", bg="#e0e0e0", fg="black").grid(row=21, column=1, columnspan=2, sticky="nsew", ipady=5)
        padresVariable = tk.IntVar()
        boton1 = tk.Radiobutton(self, text="Sí", variable=padresVariable, value=1, font=FUENTE1, anchor="center", bg="white").grid(row=22, column=1, sticky="nsew")
        boton2 = tk.Radiobutton(self, text="No", variable=padresVariable, value=2, font=FUENTE1, anchor="center", bg="white").grid(row=22, column=2, sticky="nsew")

        #   FUMADOR ACTIVO
        label = tk.Label(self, text="¿Fumador activo?", font=FUENTE1, anchor="center", bg="#e0e0e0").grid(row=21, column=3, columnspan=2, sticky="nsew", ipady=5)
        fumadorVariable = tk.IntVar()
        boton1 = tk.Radiobutton(self, text="Sí", variable=fumadorVariable, value=1, font=FUENTE1,anchor="center", bg="white").grid(row=22, column=3, sticky="nsew")
        boton2 = tk.Radiobutton(self, text="No", variable=fumadorVariable, value=2, font=FUENTE1,anchor="center", bg="white").grid(row=22, column=4, sticky="nsew")

        #   ARTRITIS REUMATOIDE
        label = tk.Label(self, text=" ¿Sufre de artritis reumatoide? ", font=FUENTE1, anchor="center", bg="#e0e0e0").grid(row=21, column=5, columnspan=2, sticky="nsew", ipady=5)
        reumatoideVariable = tk.IntVar()
        boton1 = tk.Radiobutton(self, text="Sí", variable=reumatoideVariable, value=1, font=FUENTE1,anchor="center", bg="white").grid(row=22, column=5, sticky="nsew")
        boton2 = tk.Radiobutton(self, text="No", variable=reumatoideVariable, value=2, font=FUENTE1,anchor="center", bg="white").grid(row=22, column=6, sticky="nsew")

        row23 = tk.Label(self, bg="white").grid(row=23, column=7, ipadx=80)

        #   GLUCOCORTICOIDES
        label = tk.Label(self, text="¿Consume glucocorticoides?", font=FUENTE1, anchor="center", bg="#e0e0e0").grid(row=25, column=1, columnspan=2, sticky="nsew", ipady=5)
        glucoVariable = tk.IntVar()
        boton1 = tk.Radiobutton(self, text="Sí", variable=glucoVariable, value=1, font=FUENTE1, anchor="center", bg="white").grid(row=26, column=1, sticky="nsew")
        boton2 = tk.Radiobutton(self, text="No", variable=glucoVariable, value=2, font=FUENTE1, anchor="center", bg="white").grid(row=26, column=2, sticky="nsew")

        #   ALCOHOL
        label = tk.Label(self, text="¿Consume alcohol?", font=FUENTE1, anchor="center", bg="#e0e0e0").grid(row=25, column=3, columnspan=2, sticky="nsew", ipady=5)
        alcoholVariable = tk.IntVar()
        boton1 = tk.Radiobutton(self, text="Sí", variable=alcoholVariable, value=1, font=FUENTE1,anchor="center", bg="white").grid(row=26, column=3, sticky="nsew")
        boton2 = tk.Radiobutton(self, text="No", variable=alcoholVariable, value=2, font=FUENTE1,anchor="center", bg="white").grid(row=26, column=4, sticky="nsew")

        #   OSTEOPOROSIS SECUNDARIA
        label = tk.Label(self, text=" ¿Sufre de Osteoporosis Secundaria? ", font=FUENTE1, anchor="center", bg="#e0e0e0").grid(row=25, column=5, columnspan=2, sticky="nsew", ipady=5)
        secundariaVariable = tk.IntVar()
        boton1 = tk.Radiobutton(self, text="Sí", variable=secundariaVariable, value=1, font=FUENTE1,anchor="center", bg="white").grid(row=26, column=5, sticky="nsew")
        boton2 = tk.Radiobutton(self, text="No", variable=secundariaVariable, value=2, font=FUENTE1,anchor="center", bg="white").grid(row=26, column=6, sticky="nsew")

        row = tk.Label(self, bg="white").grid(row=27, column=7, ipadx=80, ipady=10)

        # TITULO-------------------------------------------------------------------------------------------------------

        label = tk.Label(self, text="Ingrese datos de densitometría\nósea →", font=FUENTE1, anchor="center", background="white", fg="black").grid(row=29, column=1,  columnspan=2, rowspan=4, sticky="nsew")

        #TABLA DATOS DEXA HORIZONTAL------------------------------------------------------------------------------------

        label = tk.Label(self, font=FUENTE1, anchor="center", background="white", fg="black").grid(row=29, column=3, sticky="nsew")
        label = tk.Label(self, text="DMO", font=FUENTE1, anchor="center", background="#e0e0e0", fg="black").grid(row=29, column=4, sticky="nsew")
        label = tk.Label(self, text="T-SCORE", font=FUENTE1, anchor="center", background="#e0e0e0", fg="black").grid(row=29, column=5, sticky="nsew")
        label = tk.Label(self, text="Z-SCORE", font=FUENTE1, anchor="center", background="#e0e0e0", fg="black").grid(row=29, column=6, sticky="nsew")

        # TABLA DATOS DEXA VERTICAL-------------------------------------------------------------------------------------

        label = tk.Label(self, text="L1-L4", font=FUENTE1, anchor="center", background="#e0e0e0", fg="BLACK").grid(row=30, column=3, sticky="nsew")
        label = tk.Label(self, text="Cuello Femoral", font=FUENTE1, anchor="center", background="#e0e0e0", fg="BLACK").grid(row=31, column=3, sticky="nsew")
        label = tk.Label(self, text="Trocánter", font=FUENTE1, anchor="center", background="#e0e0e0", fg="BLACK").grid(row=32, column=3, sticky="nsew")

        # INGRESO DE DATOS LUMBAR --------------------------------------------------------------------------------------

        lumbar_dmo = tk.Entry(self, font=FUENTE1, background="white", fg="black", width=1, justify="center").grid(row=30, column=4, sticky="nsew")
        lumbar_tscore = tk.Entry(self, font=FUENTE1, background="white", fg="black", width=1, justify="center").grid(row=30, column=5, sticky="nsew")
        lumbar_zcore = tk.Entry(self, font=FUENTE1, background="WHITE", fg="black", width=1, justify="center").grid(row=30, column=6, sticky="nsew")

        # INGRESO DE DATOS CUELLO --------------------------------------------------------------------------------------

        cuello_dmo = tk.Entry(self, font=FUENTE1, background="white", fg="black", width=1, justify="center").grid(row=31, column=4, sticky="nsew")
        cuello_tscore = tk.Entry(self, font=FUENTE1, background="white", fg="black", width=1, justify="center").grid(row=31, column=5, sticky="nsew")
        cuello_zcore = tk.Entry(self, font=FUENTE1, background="white", fg="black", width=1, justify="center").grid(row=31, column=6, sticky="nsew")

        # INGRESO DE TROCANTER --------------------------------------------------------------------------------------

        trocanter_dmo = tk.Entry(self, font=FUENTE1, background="white", fg="black", width=1, justify="center").grid(row=32, column=4, sticky="nsew")
        trocanter_tscore = tk.Entry(self, font=FUENTE1, background="white", fg="black", width=1, justify="center").grid(row=32, column=5, sticky="nsew")
        trocanter_zcore = tk.Entry(self, font=FUENTE1, background="white", fg="black", width=1, justify="center").grid(row=32, column=6, sticky="nsew")

        row = tk.Label(self, bg="white").grid(row=33, column=7, ipadx=80, ipady=18)

        #   BOTON FINALIZAR-----------------------------------------------------------------------------------------
        button = tk.Button(self, text="REGISTRAR", font=FUENTE16, relief="groove", borderwidth=2, height=1,
                            command=lambda: controller.show_frame(MostradorResultados))
        button.grid(row=34, column=5, columnspan=2, ipadx=27)

        row = tk.Label(self, bg="white").grid(row=35, column=7, ipadx=80, ipady=5)

        #   PIE-----------------------------------------------------------------------------------------

        pie = tk.Label(self,
                       text="* Excluyendo fracturas de alto impacto. Por ejemplo: accidentes de carros.",
                       font=FUENTEPIE, bg="white", anchor="w").grid(row=36, column=1, columnspan=3, sticky="nsew")

        botonRegresar = tk.Button(self, text="←", font=FUENTEFLECHA, relief="groove", borderwidth=2, width=5, height=1,
                                  command=lambda: controller.show_frame(HistoriaPacienteAntiguo), bg="white")
        botonRegresar.place(x=10, y=10)

class MostradorResultados(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="WHITE")

        #   columns----------------------------------------------------------------------------------------------------
        columna0 = tk.Label(self, bg="WHITE").grid(row=0, column=0, ipadx=80)
        columna1 = tk.Label(self, bg="WHITE").grid(row=0, column=1, ipadx=80)
        columna2 = tk.Label(self, bg="WHITE").grid(row=0, column=2, ipadx=80)
        columna3 = tk.Label(self, bg="WHITE").grid(row=0, column=3, ipadx=80)
        columna4 = tk.Label(self, bg="WHITE").grid(row=0, column=4, ipadx=80)
        columna5 = tk.Label(self, bg="WHITE").grid(row=0, column=5, ipadx=80)
        columna6 = tk.Label(self, bg="WHITE").grid(row=0, column=6, ipadx=80)
        columna7 = tk.Label(self, bg="WHITE").grid(row=0, column=7, ipadx=80)

        #   row1 ------------------------------------------------------------------------------------------------------
        row = tk.Label(self, bg="white").grid(row=1, column=7, ipadx=80, ipady=15)

        #   RESULTADOS DEL 20/05/2013----------------------------------------------------------------------------
        label = tk.Label(self, text="  RESULTADOS DEL 20/05/2013", font=FUENTE13, background="#5b9fc9", anchor="w",fg="white").grid(row=2, column=1, columnspan=6, sticky="NSEW")
        row = tk.Label(self, bg="white").grid(row=5, column=7, ipadx=80, ipady=0)

        resultado = tk.Label(self, text="    1. Usted tiene Osteoporosis Grave.¹", font=FUENTE11,
                                            bg="white", anchor="w").grid(row=14, column=1, columnspan=5, sticky="nsew")
        resultado = tk.Label(self, text="    2. Existe un 30% de riesgo de fractura en los próximos"
                                                       " 10 años, según su densidad mineral ósea de cuello femoral.²",
                                            font=FUENTE11, bg="white", anchor="w").grid(row=15, column=1, columnspan=6, sticky="nsew")

        row = tk.Label(self, bg="white").grid(row=16, column=7, ipadx=80, ipady=5)

        #   RECOMENDACIONES----------------------------------------------------------------------------
        label = tk.Label(self, text="  RECOMENDACIONES", font=FUENTE13, background="#5b9fc9", anchor="w",fg="white").grid(row=18, column=1, columnspan=6, sticky="NSEW")
        row = tk.Label(self, bg="white").grid(row=19, column=7, ipadx=80, ipady=0)

        recomendaciones = tk.Label(self, text="    1. Asistir con un médico especializado.", font=FUENTE11,
                                            bg="white", anchor="w").grid(row=21, column=1, columnspan=5, sticky="nsew")
        recomendaciones = tk.Label(self, text="    2. Ingerir alimentos ricos en vitamina D y calcio, como pescados, lacteos y huevos.",
                                            font=FUENTE11, bg="white", anchor="w").grid(row=22, column=1, columnspan=6, sticky="nsew")

        row = tk.Label(self, bg="white").grid(row=24, column=7, ipadx=80, ipady=5)

        #   DEXA----------------------------------------------------------------------------
        label = tk.Label(self, text="  DATOS DE DENSITOMETRÍA INGRESADOS", font=FUENTE13, background="#5b9fc9", anchor="w",fg="white").grid(row=25, column=1, columnspan=6, sticky="NSEW")
        row = tk.Label(self, bg="white").grid(row=26, column=7, ipadx=80, ipady=8)

        # TABLA DATOS DEXA HORIZONTAL------------------------------------------------------------------------------------

        label = tk.Label(self, font=FUENTE1, anchor="center", background="white", fg="black").grid(row=29, column=2,
                                                                                                   sticky="nsew")
        label = tk.Label(self, text="DMO (g/cm²)", font=FUENTE1, anchor="center", background="#e0e0e0", fg="black").grid(row=29,
                                                                                                                 column=3,
                                                                                                                 sticky="nsew")
        label = tk.Label(self, text="T-SCORE", font=FUENTE1, anchor="center", background="#e0e0e0", fg="black").grid(
            row=29, column=4, sticky="nsew")
        label = tk.Label(self, text="Z-SCORE", font=FUENTE1, anchor="center", background="#e0e0e0", fg="black").grid(
            row=29, column=5, sticky="nsew")

        # TABLA DATOS DEXA VERTICAL-------------------------------------------------------------------------------------

        label = tk.Label(self, text="L1-L4", font=FUENTE1, anchor="center", background="#e0e0e0", fg="BLACK").grid(
            row=30, column=2, sticky="nsew")
        label = tk.Label(self, text="Cuello Femoral", font=FUENTE1, anchor="center", background="#e0e0e0",
                         fg="BLACK").grid(row=31, column=2, sticky="nsew")
        label = tk.Label(self, text="Trocánter", font=FUENTE1, anchor="center", background="#e0e0e0", fg="BLACK").grid(
            row=32, column=2, sticky="nsew")

        # INGRESO DE DATOS LUMBAR --------------------------------------------------------------------------------------

        lumbar_dmo = tk.Label(self, text="1", font=FUENTE1, background="white", fg="black", width=1, justify="center").grid(
            row=30, column=3, sticky="nsew")
        lumbar_tscore = tk.Label(self, text="1", font=FUENTE1, background="white", fg="black", width=1, justify="center").grid(
            row=30, column=4, sticky="nsew")
        lumbar_zcore = tk.Label(self, text="1", font=FUENTE1, background="WHITE", fg="black", width=1, justify="center").grid(
            row=30, column=5, sticky="nsew")

        # INGRESO DE DATOS CUELLO --------------------------------------------------------------------------------------

        cuello_dmo = tk.Label(self, text="1", font=FUENTE1, background="white", fg="black", width=1, justify="center").grid(
            row=31, column=3, sticky="nsew")
        cuello_tscore = tk.Label(self, text="1", font=FUENTE1, background="white", fg="black", width=1, justify="center").grid(
            row=31, column=4, sticky="nsew")
        cuello_zcore = tk.Label(self, text="1", font=FUENTE1, background="white", fg="black", width=1, justify="center").grid(
            row=31, column=5, sticky="nsew")

        # INGRESO DE TROCANTER --------------------------------------------------------------------------------------

        trocanter_dmo = tk.Label(self, text="1", font=FUENTE1, background="white", fg="black", width=1, justify="center").grid(
            row=32, column=3, sticky="nsew")
        trocanter_tscore = tk.Label(self, text="1", font=FUENTE1, background="white", fg="black", width=1, justify="center").grid(
            row=32, column=4, sticky="nsew")
        trocanter_zcore = tk.Label(self, text="1", font=FUENTE1, background="white", fg="black", width=1, justify="center").grid(
            row=32, column=5, sticky="nsew")

        row = tk.Label(self, bg="white").grid(row=33, column=6, ipadx=80, ipady=8)

        # FRACTURAS FRAGILIDAD --------------------------------------------------------------------------------------

        fracturasFragilidad = tk.Label(self, text="Fracturas por fragilidad:", font=FUENTE1, anchor="e", background="#e0e0e0",fg="black").grid(row=35,column=2,columnspan=2, sticky="nsew")
        fracturasFragilidad = tk.Label(self, text="1", font=FUENTE1, anchor="center",background="#e0e0e0", fg="black").grid(row=35, column=4, columnspan=2, sticky="nsew")

        row = tk.Label(self, bg="white").grid(row=36, column=6, ipadx=80, ipady=30)

        pie = tk.Label(self, text="1. Según mayor valor de t-score de su densitometría. 2. Basado en calculadora de riesgo de fractura Garvan.",
                       font=FUENTEPIE, bg="white", anchor="w").grid(row=40, column=3, columnspan=5, sticky="nsew")

        botonRegresar = tk.Button(self, text="←", font=FUENTEFLECHA, relief="groove", borderwidth=2, width=5, height=1,
                                  command=lambda: controller.show_frame(HistoriaPacienteAntiguo), bg="white")
        botonRegresar.place(x=10, y=10)

class BuscadorDNI(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="white")
        columna0 = tk.Label(self, bg="WHITE").grid(row=0, column=0, ipadx=80)
        columna1 = tk.Label(self, bg="WHITE").grid(row=0, column=1, ipadx=80)
        columna2 = tk.Label(self, bg="WHITE").grid(row=0, column=2, ipadx=80)
        columna3 = tk.Label(self, bg="WHITE").grid(row=0, column=3, ipadx=80)
        columna4 = tk.Label(self, bg="WHITE").grid(row=0, column=4, ipadx=80)
        columna5 = tk.Label(self, bg="WHITE").grid(row=0, column=5, ipadx=80)
        columna6 = tk.Label(self, bg="WHITE").grid(row=0, column=6, ipadx=80)
        columna7 = tk.Label(self, bg="WHITE").grid(row=0, column=7, ipadx=80)

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

        botonRegresar = tk.Button(self, text="←", font=FUENTEFLECHA, relief="groove", borderwidth=2, width=5, height=1,
                                  bg="white", command=lambda: controller.show_frame(Ramas))
        botonRegresar.place(x=10, y=10)

class HistoriaPacienteAntiguo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="WHITE")

        #   columns---------------------------------------------------------------------------------------------------
        columna0 = tk.Label(self, bg="WHITE").grid(row=0, column=0, ipadx=80)
        columna1 = tk.Label(self, bg="WHITE").grid(row=0, column=1, ipadx=80)
        columna2 = tk.Label(self, bg="WHITE").grid(row=0, column=2, ipadx=80)
        columna3 = tk.Label(self, bg="WHITE").grid(row=0, column=3, ipadx=80)
        columna4 = tk.Label(self, bg="WHITE").grid(row=0, column=4, ipadx=80)
        columna5 = tk.Label(self, bg="WHITE").grid(row=0, column=5, ipadx=80)
        columna6 = tk.Label(self, bg="WHITE").grid(row=0, column=6, ipadx=80)
        columna7 = tk.Label(self, bg="WHITE").grid(row=0, column=7, ipadx=80)

        #   row1 ------------------------------------------------------------------------------------------------------
        row1 = tk.Label(self, bg="white").grid(row=1, column=7, ipadx=80, ipady=0)

        #   APELLIDOS Y NOMBRES DEL PACIENTE---------------------------------------------------------------------------
        label1 = tk.Label(self, text="  PACIENTE", font=FUENTE13, background="#5b9fc9",
                          anchor="w", fg="white").grid(row=2, column=1, columnspan=6, sticky="NSEW", )

        row3 = tk.Label(self, bg="white").grid(row=3, column=7, ipadx=80, ipady=0)

        nombreNuevoPaciente = tk.Label(self, text="Juan Carlos Solís", font=FUENTE255, bg="white", width=1).grid(row=4,
                                                                                                                column=1,
                                                                                                                columnspan=3,
                                                                                                                sticky="NSEW")

        row5 = tk.Label(self, bg="white").grid(row=5, column=7, ipadx=80, ipady=0)

        #   DATOS PERSONALES-------------------------------------------------------------------------------------------
        label2 = tk.Label(self, text="  DATOS PERSONALES", font=FUENTE13, background="#5b9fc9", anchor="w", fg="white")
        label2.grid(row=6, column=1, columnspan=6, sticky="NSEW", )

        row7 = tk.Label(self, bg="white").grid(row=7, column=7, ipadx=80)

        #   DNI
        label3 = tk.Label(self, text="DNI: ", font=FUENTE21, anchor="e", bg="white").grid(row=8, column=1,sticky="nsew")
        dniNuevoPaciente = tk.Label(self, text="75369685", font=FUENTE1, bg="white", width=1).grid(row=8, column=2,sticky="nsew")

        #   EDAD
        label4 = tk.Label(self, text="Edad: ", font=FUENTE21, anchor="e", bg="white").grid(row=8, column=3,sticky="nsew")
        nacimientoNuevoPaciente = tk.Label(self, text="60 años", font=FUENTE1, bg="white", width=1).grid(row=8,column=4,sticky="nsew")

        #  SEXO
        label7 = tk.Label(self, text="Sexo:", font=FUENTE21, anchor="e", background="white").grid(row=8, column=5, sticky="nsew")
        sexo = tk.Label(self, text="Masculino", font=FUENTE1, bg="white", width=1).grid(row=8, column=6, sticky="nsew")



        row11 = tk.Label(self, bg="white").grid(row=11, column=7, ipadx=80)

        #   ANTECEDENTES--------------------------------------------------------------------------------------------
        label9 = tk.Label(self, text="  HISTORIAL DE CONSULTAS", font=FUENTE13, background="#5b9fc9", anchor="w", fg="white")
        label9.grid(row=12, column=1, columnspan=6, sticky="NSEW", )

        row19 = tk.Label(self, bg="white").grid(row=19, column=7, ipadx=80)

        #   DNI
        tabla1 = tk.Label(self, text="FECHA", font=FUENTE1, anchor="center", background="#e0e0e0").grid(
            row=20, column=1, sticky="nsew")
        tabla2 = tk.Label(self, text="ESTADO ÓSEO", font=FUENTE1, anchor="center", background="#e0e0e0").grid(
            row=20, column=2, sticky="nsew")
        tabla3 = tk.Label(self, text="DMO (L1-L4)", font=FUENTE1, anchor="center", background="#e0e0e0").grid(
            row=20, column=3, sticky="nsew")
        tabla4 = tk.Label(self, text="DMO (CUELLO FEMORAL)", font=FUENTE1, anchor="center", background="#e0e0e0").grid(row=20, column=4, columnspan=2, sticky="nsew")
        tabla5 = tk.Label(self, text="RESULTADOS", font=FUENTE1, anchor="center", background="#e0e0e0").grid(row=20,
                                                                                                                 column=6,
                                                                                                                 sticky="nsew")

        #   Formato 1---
        fechaVariable1 = tk.Label(self, text="02/06/2013", font=FUENTE1, bg="white", width=1, relief="solid",
                                  borderwidth=1)
        fechaVariable1.grid(row=21, column=1, sticky="nsew")

        dmoVariable1 = tk.Label(self, text="Osteoporosis Grave", font=FUENTE1, bg="white", width=1, relief="solid", borderwidth=1)
        dmoVariable1.grid(row=21, column=2, sticky="nsew")

        scoreVariable1 = tk.Label(self, text="-2.112", font=FUENTE1, bg="white", width=1, relief="solid", borderwidth=1)
        scoreVariable1.grid(row=21, column=3, sticky="nsew")

        riesgoVariable1 = tk.Label(self, text="-2.987", font=FUENTE1, bg="white", width=1, relief="solid", borderwidth=1)
        riesgoVariable1.grid(row=21, column=4, columnspan=2, sticky="nsew")

        detalleVariable1 = tk.Button(self, text="Detalle...", font=FUENTE1, bg="white", width=1, relief="solid",
                                    borderwidth=1, command=lambda: controller.show_frame(MostradorResultados))
        detalleVariable1.grid(row=21, column=6, sticky="nsew")

        #   BOTON FINALIZAR----------------------------------------------------------------------------------------
        button1 = tk.Button(self, text="ACTUALIZAR DATOS", font=FUENTE16, relief="groove", borderwidth=2, height=1,
                            command=lambda: controller.show_frame(ActualizarRegistroNuevo))
        button1.grid(row=39, column=5, columnspan=2, ipadx=27, pady=35)

        botonRegresar = tk.Button(self, text="←", font=FUENTEFLECHA, relief="groove", borderwidth=2, width=5, height=1,
                                  command=lambda: controller.show_frame(Ramas), bg="white")
        botonRegresar.place(x=10, y=10)

class RegistrarNuevoPaciente(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="WHITE")

        #   columnas-------------------------------------------------------------------------
        columna0 = tk.Label(self, bg="WHITE").grid(row=0, column=0, ipadx=80)
        columna1 = tk.Label(self, bg="WHITE").grid(row=0, column=1, ipadx=80)
        columna2 = tk.Label(self, bg="WHITE").grid(row=0, column=2, ipadx=80)
        columna3 = tk.Label(self, bg="WHITE").grid(row=0, column=3, ipadx=80)
        columna4 = tk.Label(self, bg="WHITE").grid(row=0, column=4, ipadx=80)
        columna5 = tk.Label(self, bg="WHITE").grid(row=0, column=5, ipadx=80)
        columna6 = tk.Label(self, bg="WHITE").grid(row=0, column=6, ipadx=80)
        columna7 = tk.Label(self, bg="WHITE").grid(row=0, column=7, ipadx=80)

        #   separador ---------------------------------------------------------------------------------
        fila1 = tk.Label(self, bg="white").grid(row=1, column=7, ipadx=80, ipady=0)

        #   DATOS PERSONALES-------------------------------------------------------------------------------------------
        label = tk.Label(self, text="  DATOS PERSONALES", font=FUENTE13, background="#5b9fc9", anchor="w", fg="white").grid(row=2, column=1, columnspan=6, sticky="NSEW")

        row = tk.Label(self, bg="white").grid(row=3, column=7, ipadx=80)

        #   NOMBRE
        label = tk.Label(self, text="Nombres: ", font=FUENTE1, anchor="e", bg="white").grid(row=5, column=1, sticky="nsew")
        nombreVariable = tk.Entry(self, font=FUENTE1, bg="white", width=1).grid(row=5, column=2, sticky="nsew")

        #   APELLIDO
        label = tk.Label(self, text="Apellidos: ", font=FUENTE1, anchor="e", bg="white").grid(row=5, column=3,sticky="nsew")
        apellidoVariable = tk.Entry(self, font=FUENTE1, bg="white", width=1).grid(row=5, column=4, sticky="nsew")

        #   SEXO
        label = tk.Label(self, text="Sexo:", font=FUENTE1, anchor="e", background="white").grid(row=5, column=5, sticky="nsew")
        sexoVariable = tk.IntVar()
        boton1 = tk.Radiobutton(self, text="Masculino", variable=sexoVariable, value=1, font=FUENTE1, anchor="w",bg="white").grid(row=5, column=6, sticky="nsew", padx=5)
        boton2 = tk.Radiobutton(self, text="Femenino", variable=sexoVariable, value=2, font=FUENTE1, anchor="w",bg="white").grid(row=6, column=6, sticky="nsew", padx=5)

        #   DNI
        label = tk.Label(self, text="DNI: ", font=FUENTE1, anchor="e", bg="white").grid(row=8, column=1, sticky="nsew")
        dniVariable = tk.Entry(self, font=FUENTE1, bg="white", width=1).grid(row=8, column=2, sticky="nsew")

        #   NACIMIENTO
        label = tk.Label(self, text="F. Nacimiento: ", font=FUENTE1, anchor="e", bg="white").grid(row=8, column=3,sticky="nsew")
        nacimientoVariable = tk.Entry(self, font=FUENTE1, bg="white", width=1).grid(row=8, column=4, sticky="nsew")
        label = tk.Label(self, text="(DD/MM/AAAA) ", font=FUENTE14, anchor="ne", bg="white").grid(row=9, column=3,sticky="nsew")

        #   DEPARTAMENTO
        label = tk.Label(self, text="Departamento: ", font=FUENTE1, anchor="e", bg="white").grid(row=6, column=1, sticky="nsew")
        departamentoVariable = tk.Entry(self, font=FUENTE1, bg="white", width=1).grid(row=6, column=2, sticky="nsew")

        #   CIUDAD
        label = tk.Label(self, text="Ciudad: ", font=FUENTE1, anchor="e", bg="white").grid(row=6, column=3,sticky="nsew")
        ciudadVariable = tk.Entry(self, font=FUENTE1, bg="white", width=1).grid(row=6, column=4, sticky="nsew")


        row10 = tk.Label(self, bg="white").grid(row=10, column=7, ipadx=80)


        #   PRIMERA CONSULTA---------------------------------------------------------------------------------------------
        label = tk.Label(self, text="  PRIMERA CONSULTA", font=FUENTE13, background="#5b9fc9", anchor="w", fg="white").grid(row=12, column=1, columnspan=6, sticky="NSEW", )

        row = tk.Label(self, bg="white").grid(row=13, column=7, ipadx=80)

        #   TALLA
        label = tk.Label(self, text=" Talla (cm):", font=FUENTE1, anchor="e", bg="white").grid(row=15, column=1,columnspan=2, sticky="nsew")
        tallaVariable = tk.Entry(self, font=FUENTE1, bg="white", width=1).grid(row=15, column=3, sticky="nsew")

        #   PESO
        label = tk.Label(self, text=" Peso (kg):", font=FUENTE1, anchor="e", bg="white").grid(row=15, column=4, columnspan=2, sticky="nsew")
        pesoVariable = tk.Entry(self, font=FUENTE1, bg="white", width=1).grid(row=15, column=6, sticky="nsew")

        #   CAIDAS ANTERIORES
        label = tk.Label(self, text="Número de fracturas luego de los 50 años* :", font=FUENTE1, anchor="e", bg="white").grid(row=17, column=1,columnspan=2, sticky="nsew")
        caidasVariable = tk.Entry(self, font=FUENTE1, bg="white", width=1).grid(row=17, column=3, sticky="nsew")

        #   FRACTURAS ANTERIORES
        label = tk.Label(self, text="Número de caídas en el último año:", font=FUENTE1, anchor="e", bg="white").grid(row=17, column=4, columnspan=2, sticky="nsew")
        fracturasVariables = tk.Entry(self, font=FUENTE1, bg="white", width=1).grid(row=17, column=6, sticky="nsew")

        row = tk.Label(self, bg="white").grid(row=20, column=7, ipadx=80)

        #   PADRES FRACTURAS
        label = tk.Label(self, text="¿Padres con fractura de cadera?", font=FUENTE1, anchor="center", bg="#e0e0e0", fg="black").grid(row=21, column=1, columnspan=2, sticky="nsew", ipady=5)
        padresVariable = tk.IntVar()
        boton1 = tk.Radiobutton(self, text="Sí", variable=padresVariable, value=1, font=FUENTE1, anchor="center", bg="white").grid(row=22, column=1, sticky="nsew")
        boton2 = tk.Radiobutton(self, text="No", variable=padresVariable, value=2, font=FUENTE1, anchor="center", bg="white").grid(row=22, column=2, sticky="nsew")

        #   FUMADOR ACTIVO
        label = tk.Label(self, text="¿Fumador activo?", font=FUENTE1, anchor="center", bg="#e0e0e0").grid(row=21, column=3, columnspan=2, sticky="nsew", ipady=5)
        fumadorVariable = tk.IntVar()
        boton1 = tk.Radiobutton(self, text="Sí", variable=fumadorVariable, value=1, font=FUENTE1,anchor="center", bg="white").grid(row=22, column=3, sticky="nsew")
        boton2 = tk.Radiobutton(self, text="No", variable=fumadorVariable, value=2, font=FUENTE1,anchor="center", bg="white").grid(row=22, column=4, sticky="nsew")

        #   ARTRITIS REUMATOIDE
        label = tk.Label(self, text=" ¿Sufre de artritis reumatoide? ", font=FUENTE1, anchor="center", bg="#e0e0e0").grid(row=21, column=5, columnspan=2, sticky="nsew", ipady=5)
        reumatoideVariable = tk.IntVar()
        boton1 = tk.Radiobutton(self, text="Sí", variable=reumatoideVariable, value=1, font=FUENTE1,anchor="center", bg="white").grid(row=22, column=5, sticky="nsew")
        boton2 = tk.Radiobutton(self, text="No", variable=reumatoideVariable, value=2, font=FUENTE1,anchor="center", bg="white").grid(row=22, column=6, sticky="nsew")

        row23 = tk.Label(self, bg="white").grid(row=23, column=7, ipadx=80)

        #   GLUCOCORTICOIDES
        label = tk.Label(self, text="¿Consume glucocorticoides?", font=FUENTE1, anchor="center", bg="#e0e0e0").grid(row=25, column=1, columnspan=2, sticky="nsew", ipady=5)
        glucoVariable = tk.IntVar()
        boton1 = tk.Radiobutton(self, text="Sí", variable=glucoVariable, value=1, font=FUENTE1, anchor="center", bg="white").grid(row=26, column=1, sticky="nsew")
        boton2 = tk.Radiobutton(self, text="No", variable=glucoVariable, value=2, font=FUENTE1, anchor="center", bg="white").grid(row=26, column=2, sticky="nsew")

        #   ALCOHOL
        label = tk.Label(self, text="¿Consume alcohol?", font=FUENTE1, anchor="center", bg="#e0e0e0").grid(row=25, column=3, columnspan=2, sticky="nsew", ipady=5)
        alcoholVariable = tk.IntVar()
        boton1 = tk.Radiobutton(self, text="Sí", variable=alcoholVariable, value=1, font=FUENTE1,anchor="center", bg="white").grid(row=26, column=3, sticky="nsew")
        boton2 = tk.Radiobutton(self, text="No", variable=alcoholVariable, value=2, font=FUENTE1,anchor="center", bg="white").grid(row=26, column=4, sticky="nsew")

        #   OSTEOPOROSIS SECUNDARIA
        label = tk.Label(self, text=" ¿Sufre de Osteoporosis Secundaria? ", font=FUENTE1, anchor="center", bg="#e0e0e0").grid(row=25, column=5, columnspan=2, sticky="nsew", ipady=5)
        secundariaVariable = tk.IntVar()
        boton1 = tk.Radiobutton(self, text="Sí", variable=secundariaVariable, value=1, font=FUENTE1,anchor="center", bg="white").grid(row=26, column=5, sticky="nsew")
        boton2 = tk.Radiobutton(self, text="No", variable=secundariaVariable, value=2, font=FUENTE1,anchor="center", bg="white").grid(row=26, column=6, sticky="nsew")

        row = tk.Label(self, bg="white").grid(row=27, column=7, ipadx=80)

        # TITULO-------------------------------------------------------------------------------------------------------

        label = tk.Label(self, text="Ingrese datos de densitometría\nósea →", font=FUENTE1, anchor="center", background="white", fg="black").grid(row=29, column=1,  columnspan=2, rowspan=4, sticky="nsew")

        #TABLA DATOS DEXA HORIZONTAL------------------------------------------------------------------------------------

        label = tk.Label(self, font=FUENTE1, anchor="center", background="white", fg="black").grid(row=29, column=3, sticky="nsew")
        label = tk.Label(self, text="DMO", font=FUENTE1, anchor="center", background="#e0e0e0", fg="black").grid(row=29, column=4, sticky="nsew")
        label = tk.Label(self, text="T-SCORE", font=FUENTE1, anchor="center", background="#e0e0e0", fg="black").grid(row=29, column=5, sticky="nsew")
        label = tk.Label(self, text="Z-SCORE", font=FUENTE1, anchor="center", background="#e0e0e0", fg="black").grid(row=29, column=6, sticky="nsew")

        # TABLA DATOS DEXA VERTICAL-------------------------------------------------------------------------------------

        label = tk.Label(self, text="L1-L4", font=FUENTE1, anchor="center", background="#e0e0e0", fg="BLACK").grid(row=30, column=3, sticky="nsew")
        label = tk.Label(self, text="Cuello Femoral", font=FUENTE1, anchor="center", background="#e0e0e0", fg="BLACK").grid(row=31, column=3, sticky="nsew")
        label = tk.Label(self, text="Trocánter", font=FUENTE1, anchor="center", background="#e0e0e0", fg="BLACK").grid(row=32, column=3, sticky="nsew")

        # INGRESO DE DATOS LUMBAR --------------------------------------------------------------------------------------

        lumbar_dmo = tk.Entry(self, font=FUENTE1, background="white", fg="black", width=1, justify="center").grid(row=30, column=4, sticky="nsew")
        lumbar_tscore = tk.Entry(self, font=FUENTE1, background="white", fg="black", width=1, justify="center").grid(row=30, column=5, sticky="nsew")
        lumbar_zcore = tk.Entry(self, font=FUENTE1, background="WHITE", fg="black", width=1, justify="center").grid(row=30, column=6, sticky="nsew")

        # INGRESO DE DATOS CUELLO --------------------------------------------------------------------------------------

        cuello_dmo = tk.Entry(self, font=FUENTE1, background="white", fg="black", width=1, justify="center").grid(row=31, column=4, sticky="nsew")
        cuello_tscore = tk.Entry(self, font=FUENTE1, background="white", fg="black", width=1, justify="center").grid(row=31, column=5, sticky="nsew")
        cuello_zcore = tk.Entry(self, font=FUENTE1, background="white", fg="black", width=1, justify="center").grid(row=31, column=6, sticky="nsew")

        # INGRESO DE TROCANTER --------------------------------------------------------------------------------------

        trocanter_dmo = tk.Entry(self, font=FUENTE1, background="white", fg="black", width=1, justify="center").grid(row=32, column=4, sticky="nsew")
        trocanter_tscore = tk.Entry(self, font=FUENTE1, background="white", fg="black", width=1, justify="center").grid(row=32, column=5, sticky="nsew")
        trocanter_zcore = tk.Entry(self, font=FUENTE1, background="white", fg="black", width=1, justify="center").grid(row=32, column=6, sticky="nsew")

        row = tk.Label(self, bg="white").grid(row=33, column=7, ipadx=80, ipady=7)

        #   PIE-----------------------------------------------------------------------------------------

        pie = tk.Label(self,
                       text="* Excluyendo fracturas de alto impacto. Por ejemplo: No accidentes de carros.",
                       font=FUENTEPIE, bg="white", anchor="w").grid(row=35, column=1, columnspan=3, sticky="nsew")

        #   BOTON FINALIZAR-----------------------------------------------------------------------------------------
        button = tk.Button(self, text="REGISTRAR", font=FUENTE16, relief="groove", borderwidth=2, height=1,
                            command=lambda: controller.show_frame(MostradorResultados))
        button.grid(row=34, column=5, columnspan=2, ipadx=27)

        row = tk.Label(self, bg="white").grid(row=36, column=7, ipadx=80, ipady=4)

        #--------------------------------------------------------------

        botonRegresar = tk.Button(self, text="←", font=FUENTEFLECHA, relief="groove", borderwidth=2, width=5, height=1, bg="white", command=lambda: controller.show_frame(Ramas))
        botonRegresar.place(x=10, y=10)


app = AuquishApp()
app.resizable(False, False)
app.mainloop()
