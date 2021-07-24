from spam import spam_bot
from tkinter import *

ventana = Tk()
ventana.geometry("900x700")
ventana.title("WhatsApp Bot")
ventana.resizable(0,0)
ventana.config(
    bg= "lightgray"
)

# Pantallas

home_frame = Frame(ventana)
spam_frame = Frame(ventana)
info_frame = Frame(ventana)


def home():
    return None

def spam_window():

    contact = StringVar()
    message = StringVar()
    amount  = IntVar()
    
    label_contact = Label(ventana, text="Nombre del contacto")
    label_contact.config(
        bg="lightgray",
        justify= "left",
        padx=5, 
        pady=5
    )
    label_contact.grid(column=1, row=1, sticky=E)
    entry_contact = Entry(ventana, textvariable=contact).grid(column=3, row=1,padx=5, pady=5, sticky=W)

    label_message = Label(ventana, text="Mensaje")
    label_message.config(
        bg="lightgray",
        justify= "left",
        padx=5, 
        pady=5
    )
    label_message.grid(column=1, row=3, sticky=E)
    entry_message = Entry(ventana, textvariable=message).grid(column=3, row=3, padx=5, pady=5, sticky=W)

    label_amount = Label(ventana, text="Cantidad de mensajes")
    label_amount.config(
        bg="lightgray",
        justify= "left",
        padx=5, 
        pady=5
    )
    label_amount.grid(column= 1, row=5, sticky=E)
    entry_amount = Entry(ventana, textvariable=amount).grid(column=3, row=5, padx=5, pady=5, sticky=W)
    
    button_run = Button(ventana, text= "Enviar", command= lambda:spam_bot(contact.get(), message.get(), int(amount.get())))
    button_run.config(
        width=25,
        height=2
    )
    button_run.grid(column = 3, row= 6, sticky=E)



def information():
    return None


#Menú superior
menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio")
menu_superior.add_command(label="Spam bot", command= spam_window)
menu_superior.add_command(label="Salir", command=ventana.quit)
ventana.config(menu=menu_superior)


ventana.mainloop()