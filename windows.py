from spam import spam_bot
from tkinter import *
from PIL import Image, ImageTk

class Program:

    def __init__(self):
        self.title = "WhatsApp Bot"
        self.icon = './images/icon3.ico'
        self.color = "#44C694"
        self.render = None


    def spam_window(self, ventana):
        image = Image.open('./images/spam_image.png').resize((300, 300))
        self.render = ImageTk.PhotoImage(image)
        label_image = Label(ventana, image= self.render)
        label_image.config(bg="#44C694")

        contact = StringVar()
        message = StringVar()
        amount  = IntVar()
        amount.set("")

        label_image.place(x=550, y=50)

        home_frame = Frame(ventana, width=350, height=350)
        home_frame.config(
        bg="#44C694",
        bd=3
        )
        home_frame.place(x=30, y=380)

        #Entry y labels CONTACTO

        label_contact = Label(home_frame, text="Nombre del contacto")
        label_contact.config(
            bg="#44C694",
            justify= "left",
            padx=5, 
            pady=5, 
            font = ("Century Gothic", 12)
        )
        label_contact.grid(column=1, row=1, sticky=E)
        entry_contact = Entry(home_frame, textvariable=contact)
        entry_contact.config(
            width=30,
            font= ("Century Gothic", 12)
        )
        entry_contact.grid(column=3, row=1,padx=5, pady=5, sticky=W)

        #Entry y labels MENSAJE

        label_message = Label(home_frame, text="Mensaje")
        label_message.config(
            bg="#44C694",
            justify= "right",
            padx=5, 
            pady=5,
            font = ("Century Gothic", 12)
        )
        label_message.grid(column=1, row=5, sticky=E)
        entry_message = Entry(home_frame, textvariable=message)
        entry_message.config(
            width=30,
            font= ("Century Gothic", 12)
        )
        entry_message.grid(column=3, row=5, padx=5, pady=5, sticky=W)

        #Entry y labels CANTIDAD

        label_amount = Label(home_frame, text="Cantidad de mensajes")
        label_amount.config(
            bg="#44C694",
            justify= "left",
            padx=5, 
            pady=5,
            font = ("Century Gothic", 12)
        )
        label_amount.grid(column= 1, row=3, sticky=E)
        entry_amount = Entry(home_frame, textvariable=amount)
        entry_amount.config(
            width=30,
            font= ("Century Gothic", 12)
        )
        entry_amount.grid(column=3, row=3, padx=5, pady=5, sticky=W)
        
        button_run = Button(home_frame, text= "Enviar", command= lambda:spam_bot(contact.get(), message.get(), int(amount.get())))
        button_run.config(
            width=18,
            height=1
        )
        button_run.grid(column = 3, row= 7, sticky=E)

    def info_window(self, ventana):

        return None

    def start_home(self):
        
        ventana = Tk()
        ventana.geometry("900x700")
        ventana.title(self.title)
        ventana.resizable(0,0)
        ventana.config(
            bg= self.color
        )
        ventana.iconbitmap(self.icon)
        image = Image.open('./images/bot_image.png').resize((300, 300))
        self.render = ImageTk.PhotoImage(image)
        label_image = Label(ventana, image= self.render)
        label_image.config(bg="#44C694")
        label_image.place(x=550, y=50)

        #Menú superior
        menu_superior = Menu(ventana)
        menu_superior.add_command(label="Inicio")
        menu_superior.add_command(label="Spam bot", command= lambda: self.spam_window(ventana))
        menu_superior.add_command(label="Información", command= lambda: self.info_window(ventana))
        menu_superior.add_command(label="Salir", command=ventana.quit)
        ventana.config(menu=menu_superior)


        ventana.mainloop()
