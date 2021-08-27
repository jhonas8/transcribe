from tkinter import *
from tkinter  import filedialog
import funcao as fun 


App = Tk()
App.title("Transcritor")
#Funções para serem executadas pelos botões

def main(): #Função principal que será a base de toda ação executada pela interface gráfica. Ela será disparada assim que clickado o botão de busca do vídeo
    video_address = filedialog.askopenfilename()
    Label(App, text=video_address).grid(column=0,row=1) #Exibe abaixo do botão inicial, o endereçõ do vídeo escolhido
    
    def pastaEscolher():
        pasta_destino = filedialog.askdirectory()
        
        def transcrever():
            print(pasta_destino)
            fun.Acao(video_address).fracionador(pasta_destino)
        
        Label(App,text=pasta_destino).grid(column=0,row=4)
        Button(App,text='Transcrever', command=transcrever).grid(column=0,row=3) #Exibe um botão para iniciar o ato de transcrever    
            
    
    Button(App,text='Escolha um destino pasta destino', command=pastaEscolher).grid(column=0,row=2)
    
Button(App, text='Selecione o vídeo', command=main).grid(column=0,row=0) #Botão criado para selecionar o caminho do vídeo

App.mainloop()