from spam import spam_bot
from tkinter import *  
from PIL import Image, ImageTk
from tkinter import messagebox as MessageBox

class Program:

    def __init__(self):
        self.title = "WhatsApp Bot"
        self.icon = './images/icon3.ico'
        self.color = "#1a80b5"
        self.render = None

    def check_entry(self, contact, message, amout):
        try:
            if(len(contact) != 0 and len(message) != 0 and amout > 0):
                spam_bot(contact, message, amout)
            else:
                MessageBox.showerror("Alerta", "Ingresa los datos de forma correcta")                                                        
        except Exception as e: 
            MessageBox.showerror("Alerta", "Completa bien los campos\n" + f"{e}")

    def spam_window(self, ventana):

        contact = StringVar()
        message = StringVar()
        amount  = StringVar()

        #Frame principal
        bot_frame = Frame(ventana, width=900, height=700)
        bot_frame.config(
            bg= self.color,
        )
        bot_frame.place(x=0, y=0)

        image = Image.open('./images/spam_bot_bg.png')
        self.render = ImageTk.PhotoImage(image)
        label_image = Label(bot_frame, image= self.render)
        label_image.config(bg= self.color)

        label_image.place(x=0, y=0)

        #Frame del menú
        menu_frame = Frame(bot_frame, width=350, height=350)
        menu_frame.config(
        bg= self.color,
        )
        menu_frame.place(x=30, y=380)

        #Entry y labels CONTACTO
        label_contact = Label(menu_frame, text="Nombre del contacto")
        label_contact.config(
            bg=self.color,
            fg="white",
            justify= "left",
            padx=5, 
            pady=5, 
            font = ("Century Gothic", 12)
        )
        label_contact.grid(column=1, row=1, sticky=E)
        entry_contact = Entry(menu_frame, textvariable=contact)
        entry_contact.config(
            width=30,
            font= ("Century Gothic", 12)
        )
        entry_contact.grid(column=3, row=1,padx=5, pady=5, sticky=W)

        #Entry y labels MENSAJE
        label_message = Label(menu_frame, text="Mensaje")
        label_message.config(
            bg=self.color,
            fg="white",
            justify= "right",
            padx=5, 
            pady=5,
            font = ("Century Gothic", 12)
        )
        label_message.grid(column=1, row=5, sticky=E)
        entry_message = Entry(menu_frame, textvariable=message)
        entry_message.config(
            width=30,
            font= ("Century Gothic", 12)
        )
        entry_message.grid(column=3, row=5, padx=5, pady=5, sticky=W)

        #Entry y labels CANTIDAD
        label_amount = Label(menu_frame, text="Cantidad de mensajes")
        label_amount.config(
            bg=self.color,
            fg="white",
            justify= "left",
            padx=5, 
            pady=5,
            font = ("Century Gothic", 12)
        )
        label_amount.grid(column= 1, row=3, sticky=E)
        entry_amount = Entry(menu_frame, textvariable=amount)
        entry_amount.config(
            width=30,
            font= ("Century Gothic", 12)
        )
        entry_amount.grid(column=3, row=3, padx=5, pady=5, sticky=W)

        Label(menu_frame, text="", background=self.color).grid(column=0, row=6)

        #Botones de acciones
        button_run = Button(menu_frame, text= "Enviar", command= lambda:self.check_entry(contact.get(), message.get(), int(amount.get())))
        button_run.config(
            width=16,
            height=1,
            cursor= "hand1"
        )
        button_run.grid(column = 3, row= 7, sticky= E)
        button_clear = Button(menu_frame, text="Reset", cursor= "arrow" ,command= lambda: (contact.set(""), message.set(""), amount.set("") ))
        button_clear.config(
            width=16,
            height=1,
            cursor= "hand1"
        )
        button_clear.place(x=202, y=126)
        

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
        #Frame principal
        home_frame = Frame(ventana, width=900, height=700)
        home_frame.config(
            bg= self.color,
        )
        home_frame.place(x=0, y=0)
        image = Image.open('./images/home_bg.png')
        self.render = ImageTk.PhotoImage(image)
        label_image = Label(home_frame, image= self.render)
        label_image.config(bg=self.color)
        label_image.place(x=-2, y=-3)
        
        #Botones del menú principal
        button_spam = Button(label_image, text= "Bot de Spam", command= lambda: self.spam_window(ventana))
        button_spam.config(
            width=28,
            height=3,
            font= ("Arial", 12),
            cursor= "hand1"
        )
        button_spam.place(x=40,y=350)

        button_clear = Button(label_image, text="Respuesta automática", cursor= "arrow" )
        button_clear.config(
            width=28,
            height=3,
            font= ("Arial", 12),
            cursor= "hand1"
        )
        button_clear.place(x=380, y=350)

        

        #Menú superior
        menu_superior = Menu(ventana)
        menu_superior.add_command(label="Información", command= lambda: self.info_window(ventana))
        menu_superior.add_command(label="Salir", command=ventana.quit)
        ventana.config(menu=menu_superior)


        ventana.mainloop()
