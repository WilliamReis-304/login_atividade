from tkinter import *
from tkinter.ttk import *

banco = {
    "exemplo@email.com" : ["nome","senha"]
}
#Criando a tela ------------------------------------

janela = Tk()
janela.geometry("750x550")
abas = Notebook(janela)
guia1 = Frame(abas)
guia2 = Frame(abas)
abas.add(guia1,text="login")
abas.add(guia2,text="cadastro")
abas.pack()

#Adicionando widgets para guia de login ------------

tituloLogin = Label(guia1,text="LOGIN",font="Arial 25")
textoEmail = Label(guia1,text="Digite seu e-mail",font="Arial 12")
textoSenha = Label(guia1,text="Digite sua senha",font="Arial 12")
email = Entry(guia1,width = 30,font="Arial 12")
senha = Entry(guia1,width = 30,font="Arial 12")
status= Label(guia1,text=" ",font="Arial 12")


#Adicionando widgets para guia de cadastro ---------

tituloCadastro = Label(guia2,text="Cadastro",font="Arial 25")
cadastroNome = Label(guia2,text="Cadastre seu nome",font="Arial 12")
cadastroEmail = Label(guia2,text="Cadastre um e-mail",font="Arial 12")
cadastroSenha = Label(guia2,text="Cadastre uma senha",font="Arial 12")
cad_nome = Entry(guia2,width = 30,font="Arial 12")
cad_email = Entry(guia2,width = 30,font="Arial 12")
cad_senha = Entry(guia2,width = 30,font="Arial 12")
cad_status= Label(guia2,text=" ",font="Arial 12")

#Posicionando widgets na tela de login ------------

tituloLogin.pack()
textoEmail.pack()
email.pack()
textoSenha.pack()
senha.pack()
status.pack()

#Posicionando widgets na tela de cadastro ------------

tituloCadastro.pack()
cadastroNome.pack()
cad_nome.pack()
cadastroEmail.pack()
cad_email.pack()
cadastroSenha.pack()
cad_senha.pack()
cad_status.pack()

#Criando as funções ----------------------------------

def checarLogin():
    if email.get() in banco.keys():
        if senha.get() == banco[email.get()][1]:
            status.configure(text=f"Login realizado! Bem vindo, {banco[email.get()][0]}!")
    else:
        status.configure(text="Email ou senha incorreto!")

def checarCadastro():
    soma=0
    for i in cad_email.get():
        if i == "@":
            soma+=1
    if soma ==1:
        checarSenha()
    else:
        cad_status.configure(text="Formato de Email não reconhecido")

def checarSenha():
    if len(cad_senha.get()) >= 6:
        cadastrar()
    else:
        cad_status.configure(text="A senha deve conter 6 caracteres")

def cadastrar():
    banco.update({cad_email.get():[cad_nome.get(),cad_senha.get()]})
    cad_status.configure(text="Cadastro realizado com sucesso!")



#criando e organizando botões ------------------------

login = Button(guia1,text="login",command = checarLogin)
cadastro = Button(guia2,text="cadastrar",command = checarCadastro)
login.pack()
cadastro.pack()

janela.mainloop()