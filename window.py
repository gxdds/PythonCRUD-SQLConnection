from tkinter import *
import tkinter.messagebox
import pyodbc

#conexao c banco
dados_conexao = ("Driver={SQLite3 ODBC Driver};"
           "Server=localhost;"
           "Database=Estoque.db")

conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()
print('Conexao bem sucedida')

def btn_clicked0(): #adicionar
    #PEGAR INFORMAÇAO DE TODOS OS CAMPOS
    nome_produto = entry2.get()
    preco_produto = entry1.get()
    qtd_produto = entry3.get()
    coment_produto = entry0.get("1.0", END)

    #ADICIONAR TUDO AO BANCO
    comando = f"""INSERT INTO Estoque(nome_produto, preco_produto, qtde_produto, coment_produto)
        VALUES
            ('{nome_produto}', '{preco_produto}', '{qtd_produto}', '{coment_produto}')"""
    cursor.execute(comando)
    cursor.commit()
    tkinter.messagebox.showinfo(title="Aviso ao adicionar", message="Produto adicionado com sucesso.")
    entry0.delete("1.0", END)
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)

def btn_clicked1(): #excluir
    #PEGAR A INFORMAÇAO DO CAMPO NOME (ENTRY 2)
    nome_produto = entry2.get()
    #BUSCAR E DELETAR NO BANCO DE DADOS
    comando = f"""DELETE from Estoque
                WHERE nome_produto = '{nome_produto}';
                """
    cursor.execute(comando)
    cursor.commit()

    #RETORNAR UMA MENSAGEM DIZENDO Q DELETOU
    tkinter.messagebox.showinfo(title="Aviso de Exclusão", message=f"{nome_produto} foi excluído do Banco de Dados")
    entry2.delete(0, END)
def btn_clicked2(): #atualizar
    #PEGAR INFORMACAO DO CAMPO NOME (ENTRY 2)
    nome_produto = entry2.get()
    #PEGAR INFORMACAO DO CAMPO QTDDE (ENTRY 3)
    qtd_produto = entry3.get()
    #BUSCAR PELO NOME NO BANCO DE DADOS E DIMINUIR OU AUMENTAR A QUANTIDADE
    comando = f"""UPDATE Estoque
            SET qtde_produto = {qtd_produto}
            WHERE nome_produto = '{nome_produto}';
            """
    cursor.execute(comando)
    cursor.commit()
    tkinter.messagebox.showinfo(title="Aviso ao Editar", message=f"Quantidade do produto ({nome_produto}) foi editada para {qtd_produto} com sucesso.")
    entry2.delete(0, END)
    entry3.delete(0, END)
def btn_clicked3(): #ver
    #PEGAR A INFORMAÇAO DO CAMPO NOME (ENTRY 2)
    nome_produto = entry2.get()
    #BUSCAR A INFORMAÇAO NO BANCO DE DADOS
    comando = f"""SELECT * from Estoque
                WHERE nome_produto = '{nome_produto}';
                """
    cursor.execute(comando)
    for linha in cursor.fetchall():
        texto = f"Item: {linha.nome_produto}\n Preco: {linha.preco_produto}\n Quantidade: {linha.qtde_produto}\n Comentário sobre: {linha.coment_produto}\n"
    #COLOCAR A INFORMAÇAO NUMA MESSAGE BOX
    tkinter.messagebox.showinfo(title="Aviso ao Editar", message=texto)
    entry2.delete(0, END)

#Entry0.get("1.0", END) #comentario
#print(entry1.get()) #preço
#print(entry2.get()) #nome
#print(entry3.get()) #quantidade


window = Tk()

window.geometry("909x448")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 448,
    width = 909,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    577.0, 216.0,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    114.5, 356.0,
    image = entry0_img)

entry0 = Text(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry0.place(
    x = 11, y = 332,
    width = 207,
    height = 46)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    114.5, 232.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry1.place(
    x = 11, y = 223,
    width = 207,
    height = 16)

entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvas.create_image(
    114.5, 177.0,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry2.place(
    x = 11, y = 168,
    width = 207,
    height = 16)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked0,
    relief = "flat")

b0.place(
    x = 267, y = 176,
    width = 86,
    height = 29)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked1,
    relief = "flat")

b1.place(
    x = 267, y = 234,
    width = 91,
    height = 30)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked2,
    relief = "flat")

b2.place(
    x = 266, y = 287,
    width = 86,
    height = 28)

img3 = PhotoImage(file = f"img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked3,
    relief = "flat")

b3.place(
    x = 266, y = 344,
    width = 101,
    height = 29)

entry3_img = PhotoImage(file = f"img_textBox3.png")
entry3_bg = canvas.create_image(
    114.5, 286.0,
    image = entry3_img)

entry3 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry3.place(
    x = 11, y = 277,
    width = 207,
    height = 16)


window.resizable(False, False)
window.mainloop()

cursor.close()
conexao.close()