# Importa QRCode do pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode

import tkinter as tk
from tkinter import *

# Criando Funções
def inserir_url():
    pega_valor_url = entrada_url.get()

    # String que representa o QR Code
    s = pega_valor_url

    # Gera o QR Code
    url = pyqrcode.create(s)
    # Cria e salva o arquivo SVG nomeado "myqr.svg"
    url.svg("mysql.svg", scale=8)
    # Cria e salva o arquivo PNG nomeado "myqr.png"
    url.png("mysql.png", scale=6)


# Variavel que chama a janela
janela = tk.Tk()

# Titulo da Janela
janela.title('Gerador de QR Code')
# Tamanho da Janela
janela.geometry("330x400")

# Titulo
titulo = tk.Label(text="Gerador de QR Code")
titulo.grid(row=1, column=0, padx=20, pady=10)

# Entrada de Url
entrada_url = tk.Entry(width=50)
entrada_url.grid(row=2, column=0, padx=10, pady=10)


# Botão enviar url
botao_enviar_url = tk.Button(text="Enviar", command=inserir_url)
botao_enviar_url.grid(row=3, column=0, padx=15, pady=10)

# Display de QR Code
img_qr = PhotoImage(file="mysql.png")
label = Label(janela, image=img_qr)
label.grid(row=4, column=0, padx=15, pady=10)

# Criado por
titulo = tk.Label(text="Criado por Bruno Martins de Morais Silva")
titulo.grid(row=5, column=0, padx=15, pady=10)

janela.mainloop()


