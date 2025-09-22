#importando a biblioteca e apelidando de "ctk" para facilitar a escrita das funções
import customtkinter as ctk
import re  


def avalia_forca_senha(senha:str):
    qtd_caracteres = len()
    pontuacao = 0
    sugestoes = []
     
     
    if qtd_caracteres > 8:
        pontuacao += 1
    else:
        sugestoes.append("Use pelo menos 8 caracteres!")
        
    if qtd_caracteres > 12:
        pontuacao  +=1
    else:
        sugestoes.append("Recomenda-se usar senhas com 12 caracteres para maior segurança")       
        
        #Letras Maiusculas
    if re.search(r"[A-Z]", senha):
        pontuacao  +=1  
        
    else:
        sugestoes.append("Adicione Letras Maiúsculas")        
         
    #Letras Minusculas
    if re.search(r"[a-z]", senha):
        pontuacao  +=1  
        
    else:
        sugestoes.append("Adicione Letras Minusculas")    
        
    #Numeros 
    if re.search(r"\d", senha):
        pontuacao  +=1  
        
    else:
        sugestoes.append("Adicione Números")     

    # Caracteres especiais
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha):
        pontuacao += 1
    else:
        sugestoes.append("Use caracteres especiais como @, #, _ , $...")
    
    
    # Classificação
    if pontuacao <= 2:
        classificacao = "Senha FRACA"
    elif pontuacao <= 4:
        classificacao = "Senha MÉDIA"
    else:
        classificacao = "Senha FORTE"

    return classificacao, pontuacao, sugestoes
    
    
 # Função chamada ao clicar no botão   
def verificar_senha():
    senha = campo_senha.get()
    classificacao, pontuacao, sugestoes = avalia_forca_senha(senha)
   
   
   

    
        
#configurando a aparência
ctk.set_appearance_mode('dark')

# criação da janela principal
app = ctk.CTk()
app.title('Teste de Força de Senha') #É o título da tela (aparece o no topo)
app.geometry('400x400') # Define o tamanho da tela do programa


##Campos
texto = ctk.CTkLabel(app, text='Teste de Força de Senha',font=("Arial", 25))
texto.pack(pady=10)

campo_senha = ctk.CTkEntry(app, placeholder_text='Teste sua senha aqui', show='')
campo_senha.pack(pady=6)


##botão

botao = ctk.CTkButton(app, text='Testar', command='verificar_senha', width=75)
botao.pack(pady=12)

resultado_forca_senha = ctk.CTkLabel(app, text="", justify="left", font=("Arial", 11), fg="blue" )
resultado_forca_senha.pack(pady=10)


#Iniciar a aplicação
app.mainloop()