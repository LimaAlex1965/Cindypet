import tkinter as tk
from tkinter import ttk
import sqlite3

janela = tk.Tk()

janela.title("CindyPet - Sistema Pet Shop")
janela.geometry("1200x900")
janela.configure(bg="#F2F6FA")

cabecalho = tk.Frame(janela, bg="#315D7A")
cabecalho.pack(fill="x")

titulo = tk.Label(
    cabecalho,
    text="🐾 CindyPet",
    font=("Arial", 22, "bold"),
    fg="white",
    bg="#315D7A"
)
titulo.pack(pady=15)

#_______________
#banco de dados:
#--------------

conexão = sqlite3.connect("cindy_pet.db")
cursor = conexão.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS agendamentos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_pet TEXT,
        nome_tutor TEXT,
        telefone TEXT,
        servico TEXT,
        data TEXT,
        horario TEXT,
        cep TEXT,
        logradouro TEXT,
        numero TEXT,
        cidade TEXT,
        uf TEXT,
        bairro TEXT
    )
""")

#------
#funções:
#------

def cadastrar():
    nome_pet = entrada_pet.get()
    nome_tutor = entrada_tutor.get()
    CEP = entrada_cep.get()
    logradouro = entrada_logradouro.get()
    numero = entrada_numero.get()
    cidade = entrada_cidade.get()
    UF = entrada_UF.get()
    bairro = entrada_bairro.get()
    telefone_tutor = entrada_tel.get()
    servico = combo_servico.get()
    data = entrada_data.get()
    horario = entrada_horario.get()

    cursor.execute("""
        INSERT INTO agendamentos (nome_pet, 
                                 nome_tutor,
                                telefone, 
                                servico, 
                                data, 
                                horario, 
                                cep, 
                                logradouro, 
                                numero, 
                                cidade, 
                                uf, 
                                bairro)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (nome_pet, nome_tutor, telefone_tutor, servico, data, horario, CEP, logradouro, numero, cidade, UF, bairro))


    conexão.commit()
    id_atendimento = cursor.lastrowid


    tabela.insert(
        "",
        "end",
        values=(id_atendimento, nome_pet, nome_tutor, telefone_tutor,servico, data, horario, CEP, logradouro, numero, cidade, UF, bairro )
    )

    entrada_pet.delete(0, tk.END)
    entrada_tutor.delete(0, tk.END)
    entrada_cep.delete(0, tk.END)
    entrada_logradouro.delete(0, tk.END)
    entrada_numero.delete(0, tk.END)
    entrada_cidade.delete(0, tk.END)
    entrada_UF.delete(0, tk.END)
    entrada_bairro.delete(0, tk.END)
    entrada_tel.delete(0, tk.END)
    combo_servico.set("")
    entrada_data.delete(0, tk.END)
    entrada_horario.delete(0, tk.END)

def limpar():
    entrada_pet.delete(0, tk.END)
    entrada_tutor.delete(0, tk.END)
    entrada_tel.delete(0, tk.END)
    entrada_cep.delete(0, tk.END)
    entrada_logradouro.delete(0, tk.END)
    entrada_numero.delete(0, tk.END)
    entrada_cidade.delete(0, tk.END)
    entrada_UF.delete(0, tk.END)
    entrada_bairro.delete(0, tk.END)
    combo_servico.set("")
    entrada_data.delete(0, tk.END)
    entrada_horario.delete(0, tk.END)
    print("Nome do pet após limpar:", entrada_pet.get())
    print("Nome do tutor após limpar:", entrada_tutor.get())


def seleciona():
    item = tabela.selection()
    valores = tabela.item(item, "values")
    if len(valores) < 13:
        limpar()
        print("Cadastro antigo: não possui informações de endereço.")
        return

    id_atendimento = valores[0]
    nome_pet = valores[1]
    nome_tutor = valores[2]
    telefone_tutor = valores[3]
    servico = valores[4]
    data = valores[5]
    horario = valores[6]
    cep = valores[7]
    logradouro = valores[8]
    numero = valores[9]
    cidade = valores[10]   
    UF = valores[11]
    bairro = valores[12]

    entrada_pet.delete(0, tk.END)
    entrada_pet.insert(0, nome_pet)
    entrada_tutor.delete(0, tk.END)
    entrada_tutor.insert(0, nome_tutor)
    entrada_tel.delete(0, tk.END)
    entrada_tel.insert(0, telefone_tutor)
    combo_servico.set("" )
    combo_servico.set(servico)
    entrada_data.delete(0, tk.END)
    entrada_data.insert(0, data)
    entrada_horario.delete(0, tk.END)
    entrada_horario.insert(0, horario)           
    entrada_cep.delete(0, tk.END)
    entrada_cep.insert(0, cep)
    entrada_logradouro.delete(0, tk.END)
    entrada_logradouro.insert(0, logradouro)
    entrada_numero.delete(0, tk.END)
    entrada_numero.insert(0, numero)
    entrada_cidade.delete(0, tk.END)
    entrada_cidade.insert(0, cidade)
    entrada_UF.delete(0, tk.END)
    entrada_UF.insert(0, UF)
    entrada_bairro.delete(0, tk.END)
    entrada_bairro.insert(0, bairro)

def carregar_agendamento():
    cursor.execute("SELECT * FROM agendamentos")
    registros = cursor.fetchall()
    for registro in registros:
        tabela.insert(
            "",
            "end",
            values=registro
        )


def atualizar():
    item = tabela.selection()
    if not item:
        print("Nenhum item selecionado para atualização.")
        return

    valores = tabela.item(item[0], "values")
    id_atendimento = valores[0]

    updated_pet = entrada_pet.get()
    updated_tutor = entrada_tutor.get()
    updated_telefone = entrada_tel.get()
    updated_servico = combo_servico.get()
    updated_data = entrada_data.get()
    updated_horario = entrada_horario.get()
    updated_cep = entrada_cep.get()
    updated_logradouro = entrada_logradouro.get() 
    updated_numero = entrada_numero.get()
    updated_cidade = entrada_cidade.get()
    updated_UF = entrada_UF.get()
    updated_bairro = entrada_bairro.get()

    cursor.execute("""
        update agendamentos
            set nome_pet = ?,
            nome_tutor = ?,
            telefone = ?,
            servico = ?,
            data = ?,
            horario = ?,
            cep = ?,
            logradouro = ?,
            numero = ?,
            cidade = ?,
            uf = ?,
            bairro = ?
        where id = ?
    """, (updated_pet, 
          updated_tutor, 
          updated_telefone, 
          updated_servico, 
          updated_data, 
          updated_horario, 
          updated_cep, 
          updated_logradouro, 
          updated_numero, 
          updated_cidade, 
          updated_UF, 
          updated_bairro, 
          id_atendimento))

    conexão.commit()

    tabela.item(item[0], values=(
                            id_atendimento, 
                                updated_pet, 
                              updated_tutor, 
                              updated_telefone, 
                              updated_servico, 
                              updated_data, 
                              updated_horario, 
                              updated_cep, 
                              updated_logradouro, 
                              updated_numero, 
                              updated_cidade, 
                              updated_UF,
                                updated_bairro))

    print("Agendamento atualizado com sucesso!")

def excluir():
    item = tabela.selection()
    if not item: 
        print("Nenhum item selecionado para exclusão.")
        return
    valores = tabela.item(item[0], "values")
    id_atendimento = valores[0]

    cursor.execute("DELETE FROM agendamentos WHERE id = ?", 
                   (id_atendimento,)
                   )
    conexão.commit()

    tabela.delete(item[0])
    limpar()

    print("Agendamento excluído com sucesso!")
#-------
#frames:
#------

formulario = tk.Frame(janela, bg="#EAF3F8")
formulario.pack(fill="x", padx=20, pady=20)

subtitulo = tk.Label(
    formulario,
    text="Cadastro de Agendamento",
    font=("Arial", 16, "bold"),
    fg="#315D7A",
    bg="#EAF3F8"
)
subtitulo.grid(row=0, column=0, columnspan=2, pady=15)

frame_endereco = tk.Frame(formulario, bg="#EAF3F8")
frame_endereco.grid(
    row=4, 
    column=0, 
    columnspan=2, 
    pady=5,
    sticky="w")

titulo_endereco = tk.Label(
    frame_endereco,
    text="Endereço do Tutor:",
    bg="#EAF3F8",
    font=("Arial", 13, "bold"),
    fg="#315D7A"
)
titulo_endereco.grid(row=0, column=0, pady=10)

frame_atendimento = tk.Frame(formulario, bg="#EAF3F8")
frame_atendimento.grid(
    row=5, 
    column=0, 
    columnspan=2, 
    pady=5,
    sticky="w")

titulo_atendimento = tk.Label(
    frame_atendimento,
    text="Dados do Atendimento:",
    bg="#EAF3F8",
    font=("Arial", 13, "bold"),
    fg="#315D7A"
)
titulo_atendimento.grid(row=0, column=0, pady=10)

frame_botoes = tk.Frame(formulario, bg="#EAF3F8")
frame_botoes.grid(
    row=6, 
    column=0, 
    columnspan=2, 
    pady=5,
    sticky="w")

titulo_botoes = tk.Label(
    frame_botoes,
    text="Ações:",
    bg="#EAF3F8",
    font=("Arial", 13, "bold"),
    fg="#315D7A"
)
titulo_botoes.grid(row=0, column=0, pady=10)

frame_tabela = tk.Frame(janela, bg="#EAF3F8")
frame_tabela.pack(fill="both", expand=True, padx=20, pady=10)

#----------------
# labels e entradas:
#----------------   

label_pet = tk.Label(
    formulario,
    text="Nome do Pet:",
    bg="#EAF3F8",
    font=("Arial", 12)
)
label_pet.grid(row=1, column=0, sticky="w", padx=10, pady=4)

entrada_pet = tk.Entry(formulario, width=40)
entrada_pet.grid(row=1, column=1, padx=10, pady=4)

label_tutor = tk.Label(
    formulario,
    text="Nome do Tutor:",
    bg="#EAF3F8",
    font=("Arial", 12)
)
label_tutor.grid(row=2, column=0, sticky="w", padx=10, pady=4)

entrada_tutor = tk.Entry(formulario, width=40)
entrada_tutor.grid(row=2, column=1, padx=10, pady=4)

label_tel = tk.Label(
    formulario,
    text="Telefone do Tutor:",
    bg="#EAF3F8",
    font=("Arial", 12)
)
label_tel.grid(row=3, column=0, sticky="w", padx=10, pady=4)

entrada_tel = tk.Entry(formulario, width=40)
entrada_tel.grid(row=3, column=1, padx=10, pady=4)

label_cep = tk.Label(
    frame_endereco,
    text="CEP:",
    bg="#EAF3F8",
    font=("Arial", 12)
)
label_cep.grid(row=1, column=0, sticky="w", padx=10, pady=4)

entrada_cep = tk.Entry(frame_endereco, width=40)
entrada_cep.grid(row=1, column=1, padx=10, pady=4)

    
label_logradouro = tk.Label(
    frame_endereco,
    text="Logradouro:",
    bg="#EAF3F8",
    font=("Arial", 12)
)
label_logradouro.grid(row=2, column=0, sticky="w", padx=10, pady=4)

entrada_logradouro = tk.Entry(frame_endereco, width=40)
entrada_logradouro.grid(row=2, column=1, padx=10, pady=4)

label_numero = tk.Label(
    frame_endereco,
    text="Número:",
    bg="#EAF3F8",
    font=("Arial", 12)
)
label_numero.grid(row=2, column=2, sticky="w", padx=10, pady=4)

entrada_numero = tk.Entry(frame_endereco, width=20)
entrada_numero.grid(row=2, column=3, padx=10, pady=4)

label_cidade = tk.Label(
    frame_endereco,
    text="Cidade:",
    bg="#EAF3F8",
    font=("Arial", 12)
)
label_cidade.grid(row=3, column=0, sticky="w", padx=10, pady=4)

entrada_cidade = tk.Entry(frame_endereco, width=40)
entrada_cidade.grid(row=3, column=1, padx=10, pady=4)

label_UF= tk.Label(
    frame_endereco,
    text="UF:",
    bg="#EAF3F8",
    font=("Arial", 12)
)
label_UF.grid(row=3, column=2, sticky="w", padx=10, pady=4)

entrada_UF = tk.Entry(frame_endereco, width=10)
entrada_UF.grid(row=3, column=3, padx=10, pady=4)

label_bairro = tk.Label(
    frame_endereco,
    text="Bairro:",
    bg="#EAF3F8",
    font=("Arial", 12)
)
label_bairro.grid(row=4, column=0, sticky="w", padx=10, pady=4)

entrada_bairro = tk.Entry(frame_endereco, width=40)
entrada_bairro.grid(row=4, column=1, padx=10, pady=4)

label_servico = tk.Label(
    frame_atendimento,
    text="Serviço:",
    bg="#EAF3F8",
    font=("Arial", 12)
)
label_servico.grid(row=1, column=0, sticky="w", padx=10, pady=4)

combo_servico = ttk.Combobox(
    frame_atendimento,
    values=["Banhoe e Tosa", "Vacinação", "Consulta"],
    width=30,
    state="readonly"
)
combo_servico.grid(row=1, column=1, padx=10, pady=4)

label_data = tk.Label(
    frame_atendimento,
    text="Data (dd/mm/yyyy):",
    bg="#EAF3F8",
    font=("Arial", 12)
)
label_data.grid(row=2, column=0, sticky="w", padx=10, pady=4)

entrada_data = tk.Entry(frame_atendimento, width=25)
entrada_data.grid(row=2, column=1, padx=10, pady=4)

label_horario = tk.Label(
    frame_atendimento,
    text="Horário (hh:mm):",
    bg="#EAF3F8",
    font=("Arial", 12)
)
label_horario.grid(row=2, column=2, sticky="w", padx=10, pady=4)

entrada_horario = tk.Entry(frame_atendimento, width=25)
entrada_horario.grid(row=2, column=3, padx=10, pady=4)

#-------------
#botoes:
#-----------

botao_buscar = tk.Button(
    frame_endereco,
    text="Buscar CEP",
    bg="#315D7A",
    fg="white",
    font=("Arial", 12),
    width=10
)
botao_buscar.grid(row=1, column=2, padx=10, pady=4)

botao_cadastrar = tk.Button(
    frame_botoes,
    text="Cadastrar",
    bg="#315D7A",
    fg="white",
    font=("Arial", 11),
    width=10,
    command=cadastrar
)
botao_cadastrar.grid(row=1, column=0, padx=10, pady=4)

botao_atualizar = tk.Button(
    frame_botoes,
    text="Atualizar",
    bg="#315D7A",
    fg="white",
    font=("Arial", 11),
    width=10,
    command=atualizar
)
botao_atualizar.grid(row=1, column=1, padx=10, pady=4)

botao_excluir = tk.Button(
    frame_botoes,
    text="Excluir",
    bg="#315D7A",
    fg="white",
    font=("Arial", 11),
    width=10,
    command=excluir
)
botao_excluir.grid(row=1, column=2, padx=10, pady=4)

botao_limpar = tk.Button(
    frame_botoes,
    text="Limpar",
    bg="#315D7A",
    fg="white",
    font=("Arial", 11),
    width=10,
    command=limpar
)
botao_limpar.grid(row=1, column=3, padx=10, pady=4)

#--------
#treeview:
#--------

tabela = ttk.Treeview(
    frame_tabela,
    columns=("id", "pet", "tutor", "telefone", "servico", "data", "horario"),
    show="headings",
    height=6
)
tabela.heading("id", text="ID",anchor="center")
tabela.heading("pet", text="Nome do Pet",anchor="center")
tabela.heading("tutor", text="Nome do Tutor",anchor="center")
tabela.heading("telefone", text="Telefone",anchor="center")
tabela.heading("servico", text="Serviço",anchor="center")
tabela.heading("data", text="Data",anchor="center")
tabela.heading("horario", text="Horário",anchor="center")

tabela.column("id",anchor="center")
tabela.column("pet",anchor="center")
tabela.column("tutor",anchor="center")  
tabela.column("telefone",anchor="center")
tabela.column("servico",anchor="center")
tabela.column("data",anchor="center")
tabela.column("horario",anchor="center")


tabela.pack(fill="both", expand=True)

tabela.bind("<<TreeviewSelect>>", lambda event: seleciona())

carregar_agendamento()

janela.mainloop()

