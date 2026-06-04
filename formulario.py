import tkinter as tk
from tkinter import messagebox

lista = []
def cadastro():
    from tkinter import messagebox
    codigo = int(campo.get())
    nome = campo1.get()
    phone = int(campo2.get())

    '''
    Cadastra um novo valor no arquivo clientes. Porem o codigo nao pode ser repetido.
    '''

    repeat = False

    with open('clientes.txt', "r", encoding="utf-8") as file:
        for linha in file:
            dados = linha.split(";")
            codigos = int(dados[0])
            if codigo == codigos:
                messagebox.showerror("Erro", "Ja existe esse codigo de cliente")
                repeat = True
    if not repeat:
        lista.append([codigo, nome, phone])
        with open("clientes.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(f'{codigo};{nome};{phone} \n')
        messagebox.showinfo('Sucesso', "informações cadastradas")

def consultar():
    '''
    permite consultar o arquivo clientes.
    '''
    texto = tk.Listbox(window)
    texto.grid(row=5, column=5)

    with open('clientes.txt', "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            texto.insert(tk.END, linha.strip())

def atualizar():
        '''
        atualiza o nome e o telefone do cliente.
        '''
        codigo = int(campo.get())
        nome = campo1.get()
        phone = int(campo2.get())

        consulta = False

        with open('clientes.txt', 'r', encoding="utf-8") as file:
            linhas = file.readlines()

        with open('clientes.txt', 'w', encoding="utf-8") as arquivo:
            for linha in linhas:
                dados = linha.strip().split(";")
                if int(dados[0]) == codigo:
                    arquivo.write(f"{codigo};{nome};{phone}\n")
                    consulta = True
                    messagebox.showinfo("SUCESSO", "Cliente atualizado com sucesso")
                else:
                    arquivo.write(linha)

        if not consulta:
            messagebox.showerror("ERRO", "Não existe esse codigo")

def excluir():
    '''
    excluir todo o cadastro do cliente.
    '''
    codigo = int(campo.get())
    nome = campo1.get()
    phone = int(campo2.get())

    consulta = False

    with open('clientes.txt', 'r', encoding="utf-8") as file:
        linhas = file.readlines()

    with open('clientes.txt', 'w', encoding="utf-8") as arquivo:
        for linha in linhas:
            dados = linha.strip().split(";")

            if int(dados[0]) == codigo:

                resposta = messagebox.askyesno(
                    title="AVISO",
                    message=f'voce tem certeza que quer excluir {dados[1]}?'
                )
                if resposta:
                    consulta = True
                    messagebox.showinfo("SUCESSO", "Cliente excluido com sucesso")
                else:
                    arquivo.write(linha)
            else:
                arquivo.write(linha)

    if not consulta:
        messagebox.showerror("ERRO", "Não existe esse codigo")

def fechar():
    resultado= messagebox.askyesno("AVISO", "DESEJA FECHAR ESTA JANELA?")
    if resultado:
        window.destroy()



window = tk.Tk()
window.title("cadastro de dados")
window.geometry("1080x720")

formulario = tk.Label(window, text='SISTEMA DE CADASTRO \n DE CLIENTE', font=('times new roman', 42))
formulario.place(x=202, y=150)

campo = tk.Entry(window)
campo.place(x=344, y=367, width=600, height=30)

texto = tk.Label(window, text='Código do cliente:', font=('times new roman', 33))
texto.place(x=13, y=350)

campo1 = tk.Entry(window)
campo1.place(x=344, y=469, width=600, height=30)

texto1 = tk.Label(window, text='Nome do cliente:', font=('times new roman', 36))
texto1.place(x=13, y=450)

campo2 = tk.Entry(window)
campo2.place(x=344, y=568, width=600, height=30)

texto2 = tk.Label(window, text='Digite o Telefone:', font=('times new roman', 33))
texto2.place(x=13, y=550)

cadastro = tk.Button(window, text='Cadastrar', font=('times new roman', 26), command=cadastro)
cadastro.place(x=175, y=625)

cadastro1 = tk.Button(window, text='Consultar', font=('times new roman', 26), command=consultar)
cadastro1.place(x=350, y=625)

cadastro2 = tk.Button(window, text='Atualizar', font=('times new roman', 26), command=atualizar)
cadastro2.place(x=525, y=625)

cadastro3 = tk.Button(window, text='Excluir', font=('times new roman', 26), command=excluir)
cadastro3.place(x=700, y=625)

cadastro = tk.Button(window, text='Fechar', font=('times new roman', 26), command=fechar)
cadastro.place(x=950, y=650)

window.mainloop()
