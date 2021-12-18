# Para crear las interfaces y traer los modulos
import tkinter as tk
from tkinter import ttk
from tkinter import *

# modulo para hacer la conección con SQLite
from sqlite3.dbapi2 import Row
import sqlite3

# Aditionals
from tkcalendar import DateEntry
from datetime import datetime

# Creación clase Producto
class Product:
    def __init__(self, window):
        self.__wind = window
        self.__wind.title('CRUD APPLICATION Products')
        # Creación de contenedor "Frame"
        # de esta forma se crea un label
        frame = LabelFrame(self.__wind, text = 'Register A New Product')
        # y de esta lo posicionamos en una fila y columna determinada
        frame.grid(row = 0, column = 0, columnspan = 3, pady=20)
        # NameInput
        Label(frame, text = 'Name: ').grid(row=1, column=0, pady=2)
        self._name = Entry(frame)
        self._name.focus()
        self._name.grid(row=1, column=1)
        # CodeInput
        Label(frame, text = 'Code: ').grid(row=2, column=0, pady=2)
        self._code = Entry(frame)
        self._code.grid(row=2, column=1)
        # PriceInput
        Label(frame, text = 'Price: ').grid(row=3, column=0, pady=2)
        self._price = Entry(frame)
        self._price.grid(row=3, column=1)
        # AmountInput
        Label(frame, text = 'Amount: ').grid(row=4, column=0, pady=2)
        self._amount = Entry(frame)
        self._amount.grid(row=4, column=1)
        # availableInput
        Label(frame, text = 'Available: ').grid(row=5, column=0, pady=2)
        self._available = ttk.Label(frame, text = "Is available")
        self._available.grid(row=5, column=1)
        # ComboBoxInput
        self._comboBox = ttk.Combobox(frame, values=["True", "False"], width=18, height=3)
        self._comboBox.current(0)
        self._comboBox.grid(row=5, column=1, pady=2)
        # DescriptionInput
        Label(frame, text = 'Description: ').grid(row=6, column=0)
        self._description = Text(frame, height=2, width=20)
        self._description.grid(row=6, column=1, pady=2)
        # Created_atInput
        Label(frame, text = 'Created at: ').grid(row=6, column=0)
        self._date: datetime = datetime.now()
        format_date = f"{self._date:%a, %b, %d, %y}"
        self._created_at = Entry(frame, width=18, font=("Calibri", 13, UNDERLINE))
        self._created_at.insert(END, format_date)
        self._created_at.config(state=DISABLED)
        self._created_at.grid(row=7, column=1, pady=2)
        # Boton para Crear productos
        ttk.Button(text='Save Product').grid(row=8, column=0, pady=10, padx=5, sticky=W+E+S+N)
        # Boton para Actualizar productos
        ttk.Button(text='Update Product').grid(row=8, column=1, pady=10, padx=5, sticky=W+E+S+N)
        # Boton para Borrar productos
        ttk.Button(text='Delete Product').grid(row=8, column=2, pady=10, padx=5, sticky=W+E+S+N)
        # Boton para Buscar productos
        ttk.Button(text='Search Product').grid(row=9, column=1, pady=10, padx=5, sticky=W+E+S+N)

        # TableView
        self._columns = ('Code', 'Name', 'Price', 'Description', 'Amount')#, 'Is Available', 'Create At')
        self._tree = ttk.Treeview(column=self._columns, show='headings')
        self._tree.grid(row=0, column=4, padx=5, columnspan=2)
        self._tree.heading('#1', text='Code', anchor=CENTER)
        self._tree.heading('#2', text='Name', anchor=CENTER)
        self._tree.heading('#3', text='Price', anchor=CENTER)
        self._tree.heading('#4', text='Description', anchor=CENTER)
        self._tree.heading('#5', text='Amount', anchor=CENTER)
        # self._tree.heading('#6', text='Is Available', anchor=CENTER)
        # self._tree.heading('#7', text='Create At', anchor=CENTER)

# comprobación si estamos en el archivo main
if __name__ == '__main__':
    window =  Tk()
    aplication = Product(window)
    window.mainloop()


