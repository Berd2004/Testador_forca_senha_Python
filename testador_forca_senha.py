#importando a biblioteca e apelidando de "ctk" para facilitar a escrita das funções
import customtkinter as ctk
import re  


def avalia_forca_senha(senha:str):
    qtd_caracteres = len(senha)
    pontuacao = 0
    sugestoes = []
     
     
    if qtd_caracteres > 8:
        pontuacao += 1
    else:
        sugestoes.append("Use pelo menos 8 caracteres!")
        
    if qtd_caracteres > 12:
        pontuacao +=1
    else:
        sugestoes.append("Recomenda-se usar senhas com 12 caracteres para maior segurança")       
        
        #Letras Maiusculas
    if re.search(r"[A-Z]", senha):
        pontuacao +=1  
        
    else:
        sugestoes.append("Adicione Letras Maiúsculas")        
         
    #Letras Minusculas
    if re.search(r"[a-z]", senha):
        pontuacao +=1  
        
    else:
        sugestoes.append("Adicione Letras Minusculas")    
        
    #Numeros 
    if re.search(r"\d", senha):
        pontuacao +=1  
        
    else:
        sugestoes.append("Adicione Números")     

    # Caracteres especiais
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha):
        pontuacao += 1
    else:
        sugestoes.append("Use caracteres especiais como @, #, _ , $...")
    
    # Classificação
    if pontuacao <= 3:
        classificacao = "Senha FRACA"
    elif pontuacao <= 4:
        classificacao = "Senha MÉDIA"
    elif pontuacao <= 6:
        classificacao = "Senha FORTE"
    else:
       classificacao = "Senha MUITO FORTE!"    

    return classificacao, pontuacao, sugestoes
    
    
    
 # Função chamada ao clicar no botão   
def verificar_senha():
    senha = campo_senha.get()
    classificacao, pontuacao, sugestoes = avalia_forca_senha(senha)
   
    if len(senha) > 16:
        resultado_forca_senha.configure(text="Por favor, digite uma senha de até 16 caracteres")
        return
        
   #verifica se o usuário deixou o campo senha vazio
    if not senha.strip():   
        resultado_forca_senha.configure(text="Por favor, digite uma senha para testar!")
        return
   
    resultado_texto = f"Pontuação: {pontuacao}/6 → {classificacao}\n"
    if sugestoes:
        resultado_texto += "\nSugestões para melhorar sua senha:\n"
        for dicas in sugestoes:
            resultado_texto += f"- {dicas}\n"
    else:
        resultado_texto += "\nSua senha já é muito forte, parabéns! 🚀"

    # Mostra resultado na label
    resultado_forca_senha.configure(text=resultado_texto)
   
       
#configurando a aparência
ctk.set_appearance_mode('dark')

# criação da janela principal
app = ctk.CTk()
app.title('Teste de Força de Senha') #É o título da tela (aparece o no topo)
app.geometry('400x300') # Define o tamanho da tela do programa


##Campos
texto = ctk.CTkLabel(app, text='Teste de Força de Senha',font=("Arial", 25))
texto.pack(pady=10)

campo_senha = ctk.CTkEntry(app, placeholder_text='Teste sua senha aqui', show='')
campo_senha.pack(pady=6)


##botão
botao = ctk.CTkButton(app, text='Testar', command=verificar_senha, width=75)
botao.pack(pady=12)

resultado_forca_senha = ctk.CTkLabel(app, text='', justify="left", font=("calibri", 13 , "bold"), text_color="white")
resultado_forca_senha.pack(pady=10)


#Iniciar a aplicação
app.mainloop()