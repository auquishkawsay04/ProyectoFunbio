import tkinter as tk
from tkinter import ttk

LARGE_FONT = ("Arial", 80)
MEDIUM_FONT = ("Arial", 200)
SMALL_FONT = ("Verdana", 19)


class AuquishApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # tk.Tk.iconbitmap(self, default="logo.bmp")
        tk.Tk.wm_title(self, "Prototipe")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Login, PaginaInicio, PaginaBusquedaDni, PaginaRegistro):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Login   )

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class Login(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="white")

        def verificar_contrasena():
            if my_password.get() == "123":
                controller.show_frame(PaginaInicio)
                incorrect_password_label["text"] = " "
                my_password.set("")
            else:
                incorrect_password_label["text"] = "La contraseña que ingresó es incorrecta. Inténtelo de nuevo"

        label = tk.Label(self, text="título", font=LARGE_FONT, bg="blue")
        label.pack(pady=60, padx=40)

        password_label = tk.Label(self, text="Ingrese su contraseña", bg="white", fg="black", font=SMALL_FONT)
        password_label.pack(ipady=10)

        my_password = tk.StringVar()
        password_entry_box = tk.Entry(self, textvariable=my_password, width=22, font=SMALL_FONT, show="*", bg="white")
        password_entry_box.focus_set()
        password_entry_box.pack(ipady=7, pady=10)

        enter_button = tk.Button(self, text="INGRESAR", command=verificar_contrasena, relief="groove",
                                 borderwidth=2, width=15, height=1, font=SMALL_FONT)
        enter_button.pack(pady=10)

        incorrect_password_label = tk.Label(self, text=" ", bg="white", anchor="n", fg="white", font=SMALL_FONT)
        incorrect_password_label.pack(fill="both", expand=True)


class PaginaInicio(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="white")

        button1 = tk.Button(self, text="PACIENTES REGISTRADOS", font=MEDIUM_FONT, relief="groove",
                            borderwidth=2, width=30, height=1, command=lambda: controller.show_frame(PaginaBusquedaDni))
        button1.place(x=240, y=200)

        button2 = tk.Button(self, text="REGISTRAR UN NUEVO PACIENTE", font=MEDIUM_FONT, relief="groove",
                            borderwidth=2, width=30, height=1, command=lambda: controller.show_frame(PaginaRegistro))
        button2.place(x=240, y=400)


class PaginaBusquedaDni(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white")

        def verficar_id():
            if paciente_id.get() == "75692969":
                controller.show_frame(PaginaInicio)
                paciente_id.set("")

        label = ttk.Label(self, text="Ingrese el DNI del paciente", font=LARGE_FONT, background="white")
        label.place(x=190, y=150)

        paciente_id = tk.StringVar()
        entry = tk.Entry(self, textvariable=paciente_id, font=LARGE_FONT, width=10, bg="white")
        entry.focus_set()
        entry.place(x=400, y=320)

        button = tk.Button(self, text="Aceptar", relief="groove", borderwidth=2, width=15, height=1,
                           font=SMALL_FONT, command=verficar_id)
        button.place(x=460, y=500)


class PaginaRegistro(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white")

        label = tk.Label(self, text="Ingrese los datos del nuevo paciente.", font=MEDIUM_FONT, background="white")
        label.place(x=190, y=150)

        label = tk.Label(self, text="Nombre", font=SMALL_FONT, background="white")
        label.place(x=200, y=220)

        entry = tk.Entry(self, font=SMALL_FONT, width=10, bg="white")
        entry.place(x=320, y=220)


app = AuquishApp()
app.geometry("1250x820")
app.resizable(False, False)
app.mainloop()