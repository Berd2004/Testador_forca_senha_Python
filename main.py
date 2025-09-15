import re
import tkinter as tk
from tkinter import messagebox


# Função para verificar força da senha
def verificar_forca_senha(senha: str):
    pontuacao = 0
    sugestoes = []

    # Tamanho
    if len(senha) >= 8:
        pontuacao += 2
    else:
        sugestoes.append("Use pelo menos 8 caracteres.")
        
    if len(senha) >= 12:
        pontuacao += 1
    else:
        sugestoes.append("Senhas com 12+ caracteres são mais seguras.")

    # Maiúsculas
    if re.search(r"[A-Z]", senha):
        pontuacao += 1
    else:
        sugestoes.append("Adicione letras maiúsculas.")
    # Minúsculas
    if re.search(r"[a-z]", senha):
        pontuacao += 1
    else:
        sugestoes.append("Adicione letras minúsculas.")
    # Números
    if re.search(r"\d", senha):
        pontuacao += 1
    else:
        sugestoes.append("Inclua números.")
    # Caracteres especiais
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha):
        pontuacao += 1
    else:
        sugestoes.append("Use caracteres especiais como !, @, #, $...")

    # Classificação
    if pontuacao <= 2:
        classificacao = "Senha FRACA"
    elif pontuacao <= 4:
        classificacao = "Senha MÉDIA"
    else:
        classificacao = "Senha FORTE"

    return classificacao, pontuacao, sugestoes


# Função chamada ao clicar no botão
def avaliar_senha():
    senha = entry_senha.get()
    classificacao, pontos, dicas = verificar_forca_senha(senha)

    resultado_texto = f"Pontuação: {pontos}/7 → {classificacao}\n"
    if dicas:
        resultado_texto += "\nSugestões para melhorar sua senha:\n"
        for d in dicas:
            resultado_texto += f"- {d}\n"
    else:
        resultado_texto += "\nSua senha já é muito forte! 🚀"

    # Mostra resultado na label
    label_resultado.config(text=resultado_texto)


# Criar janela principal
janela = tk.Tk()
janela.title("Verificador de Força de Senha")
janela.geometry("450x350")

# Label instrução
label_instrucao = tk.Label(janela, text="Digite sua senha:", font=("Arial", 12))
label_instrucao.pack(pady=10)

# Campo de entrada (senha)
entry_senha = tk.Entry(janela, show="*", width=30, font=("Arial", 12))
entry_senha.pack(pady=5)

# Botão para avaliar
botao_avaliar = tk.Button(janela, text="Avaliar Força", command=avaliar_senha, font=("Arial", 12))
botao_avaliar.pack(pady=10)

# Label para mostrar resultado
label_resultado = tk.Label(janela, text="", justify="left", font=("Arial", 11), fg="blue")
label_resultado.pack(pady=10)

# Iniciar loop da interface
janela.mainloop()
