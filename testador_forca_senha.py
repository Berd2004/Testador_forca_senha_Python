#importando a biblioteca e apelidando de "ctk" para facilitar a escrita das funções
import customtkinter as ctk  



def verificar_senha():
    senha = campo_senha.get()
    pontuacao = 0
    sugestoes = []
    qtd_caracteres = len()

    if qtd_caracteres > 8:
        pontuacao += 1
    else:
        sugestoes.append("Use pelo menos 8 caracteres")
        
        
#configurando a aparência
ctk.set_appearance_mode('dark')

# criação da janela principal
app = ctk.CTk()
app.title('Teste de Força de Senha') #É o título da tela (aparece o no topo)
app.geometry('400x400') # Define o tamanho da tela do programa


##Campos
texto = ctk.CTkLabel(app, text='Teste de Força de Senha',font=("Arial", 22))
texto.pack(pady='10')

campo_senha = ctk.CTkEntry(app, placeholder_text='Teste sua senha aqui', show='')
campo_senha.pack(pady='5')


##botão

botao = ctk.CTkButton(app, text='Testar', command='verificar_senha', width=70)
botao.pack(pady='12')

#Iniciar a aplicação
app.mainloop()