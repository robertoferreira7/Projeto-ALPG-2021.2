#Fazer um programa de livre escolha de cadastro, ou cálculos ou jogos que atendam aos critérios abaixo:

#[1]Estar bem comentado
#[2]Ter usado de forma correta as técnicas aprenddias em sala de aula.
#[3]Entrada, processamento e saída
#[4]Estruturas condicionais
#[5]Estruturas de repetição
#[6]Listas
#[7]Strings
#[8]Funções

#Pesquisa e utilização de novas técnicas e estruturas do Python.
#Pacotes necessários #Necessário instalar as dependências pelo pip: pip install -r requirements.txt
import qrcode
from PIL import ImageShow
import os.path 

alunos_cadastrados = [] #Lista vazia que irá receber os dados

def cadastro(dados_aluno): # Função para cadastro de usuário
    nome = input('Digite o nome do aluno(a): ')
    matricula = int(input('Nº da matrícula: '))
    curso = input('Nome do curso: ')
    periodo = int(input('Nº do perído: '))

    juntar = nome + " " + str(matricula) + " " +  curso + " " + str(periodo) #Variável que recebe os todos os dados
    alunos_cadastrados.append(juntar) #A lista recebe a variável "juntar"

    dados_aluno = qrcode.make(alunos_cadastrados) #Arquivo png(qrcode) é gerado com o numero da matrícula como nome e com a extensão .png
    dados_aluno.save("{}.png".format(matricula)) #Salvando o Qrcode

    with open('lista.txt', 'a+') as arquivo: #Criação de arquivo txt para guardar as informaçãoes dos(as) estudantes.
        for aluno in alunos_cadastrados: #Percorrendo a lista
            arquivo.write('\n' + aluno) #Escrevendo no arquivo .txt os elementos da lista. 

    print("QrCode criado e cadastro realizado com sucesso.") #Mostrando ao usuário que o QRcode foi criado.
    ImageShow.show(dados_aluno) #Abre o aplicativo de galeria de fotos e mostra o QRcode na tela.
    print(alunos_cadastrados)

def identificador(matricula): #Função que identificas, na pasta do codigo, se há ou matricula cadastrada. 
    while True: #Verifica se a matricula possui QRcode.
        if (os.path.isfile("{}.png".format(matricula))): #Percorre a pasta que está o programa, e verifica se há um qrcode com o nome da matrícula digitada
            print("Essa matrícula já possui QrCode.") #Mostra a mensagem caso na busca anterior o qrcode tenha sido encontradado
        else: #Caso não haja, perguta se quer criar um novo.
            resposta = input("Essa matrícula ainda não possui QrCode. Deseja realizar o cadastro? [S/N] ").upper() #Input com a resposta se quer ou não efetuar o cadastro de uma nova matrícula e geração de qrcode.
            while resposta != "S" and resposta != "N":
                resposta = input(
                    "Digite uma resposta válida: [S] para fazer um novo cadastro ou [N] para sair\nEssa matrícula ainda não possui QrCode. Deseja realizar o cadastro? [S/N] ").upper()
            if resposta == "S":
                cadastro(matricula) #Se quiser criar um cadastro, a função cadastro é chamada.
            elif resposta == "N":
                print("Ok")
        break


while True: #Após digitar a matricula, a função identificador é chamada, para veficiar a exitestência da matricula. 
    matricula = int(input("Digite o n° de matrícula: ")) #Primeiro input do programa
    identificador(matricula) #Chama a função identificador(matricula) para ver confirmar se há ou não uma matricula realizada.
    resposta = input("Deseja realizar nova busca por matrícula? [S/N] ").upper() 
    while resposta != "N" and resposta != "S":
        resposta = input(
            "Digite uma resposta válida: [S] para fazer uma nova busca ou [N] para finalizar o programa\nDeseja realizar nova busca por matrícula? [S/N] ").upper()
    if resposta == "N": #Se for "N" o programa é finalizado.
        break
    
