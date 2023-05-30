import tkinter as tk
from tkinter import messagebox

# Função de evento para o botão de cadastro
def cadastrar_usuario():
    nome = entry_nome.get()
    email = entry_email.get()
    senha = entry_senha.get()
    genero = ""
    if genero_var.get() == 1:
        genero = "Masculino"
    elif genero_var.get() == 2:
        genero = "Feminino"
    else:
        genero = "Prefiro não informar"

    interesses_selecionados = listbox_interesses.curselection()
    interesses = [listbox_interesses.get(i) for i in interesses_selecionados]

    # Aqui você pode adicionar a lógica de cadastro do usuário

    messagebox.showinfo("Cadastro realizado", "Usuário cadastrado com sucesso!")

# Criação da janela principal
window = tk.Tk()
window.title("Cadastro de Usuários")

# Frame
frame = tk.Frame(window, relief=tk.RAISED, borderwidth=1)
frame.pack(pady=10)

# Labels
label_nome = tk.Label(frame, text="Nome:")
label_nome.grid(row=0, column=0, sticky=tk.W)

label_email = tk.Label(frame, text="Email:")
label_email.grid(row=1, column=0, sticky=tk.W)

label_senha = tk.Label(frame, text="Senha:")
label_senha.grid(row=2, column=0, sticky=tk.W)

label_genero = tk.Label(frame, text="Gênero:")
label_genero.grid(row=3, column=0, sticky=tk.W)

label_interesses = tk.Label(frame, text="Interesses:")
label_interesses.grid(row=5, column=0, sticky=tk.W)

# Entries
entry_nome = tk.Entry(frame)
entry_nome.grid(row=0, column=1)

entry_email = tk.Entry(frame)
entry_email.grid(row=1, column=1)

entry_senha = tk.Entry(frame, show="*")
entry_senha.grid(row=2, column=1)

# Radio buttons para o gênero
genero_var = tk.IntVar()
genero_var.set(0)  # Valor padrão (nenhum selecionado)

radio_masculino = tk.Radiobutton(frame, text="Masculino", variable=genero_var, value=1)
radio_masculino.grid(row=3, column=1, sticky=tk.W)

radio_feminino = tk.Radiobutton(frame, text="Feminino", variable=genero_var, value=2)
radio_feminino.grid(row=4, column=1, sticky=tk.W)

radio_nao_informar = tk.Radiobutton(frame, text="Prefiro não informar", variable=genero_var, value=3)
radio_nao_informar.grid(row=5, column=1, sticky=tk.W)

# Listbox para interesses
interesses = ["Esportes", "Tecnologia", "Arte", "Música"]
listbox_interesses = tk.Listbox(frame, selectmode=tk.MULTIPLE)
listbox_interesses.grid(row=6, column=1, sticky=tk.W)
for interesse in interesses:
    listbox_interesses.insert(tk.END, interesse)

# Botão de cadastro
button_cadastrar = tk.Button(window, text="Cadastrar", command=cadastrar_usuario)
button_cadastrar.pack(pady=10)

# Executa o loop principal da janela
window.mainloop()
