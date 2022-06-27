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

#Pacotes necessários
import qrcode
from PIL import ImageShow
import os.path 

alunos_cadastrados = []

def cadastro(dados_aluno): # Função para cadastro de usuário
    nome = input('Digite o nome do aluno(a): ')
    matricula = int(input('Nº da matrícula: '))
    curso = input('Nome do curso: ')
    periodo = int(input('Nº do perído: '))

    juntar = nome + " " + str(matricula) + " " +  curso + " " + str(periodo)
    alunos_cadastrados.append(juntar)

    dados_aluno = qrcode.make(alunos_cadastrados) #Arquivo png(qrcode) é gerado com o numero da matrícula.
    dados_aluno.save("{}.png".format(matricula))

    with open('lista.txt', 'a+') as arquivo: #Criação de arquivo TXT para guardar as informaçãoes dos(as) estudantes.
        for aluno in alunos_cadastrados:
            arquivo.write('\n' + aluno)

    print("QrCode criado e cadastro realizado com sucesso.")
    ImageShow.show(dados_aluno) #Abre o aplicativo de galeria de fotos e mostra o QRcode na tela.
    print(alunos_cadastrados)

def identificador(matricula): #Função que identificas, na pasta do codigo, se há ou matricula cadastrada. 
    while True: #Verifica se a matricula possui QRcode.
        if (os.path.isfile("{}.png".format(matricula))):
            print("Essa matrícula já possui QrCode.")
        else: #Senão exitir = qrcode gerado, perguta se quer criar um novo.
            resposta = input("Essa matrícula ainda não possui QrCode. Deseja realizar o cadastro? [S/N] ").upper()
            while resposta != "S" and resposta != "N":
                resposta = input(
                    "Digite uma resposta válida: [S] para fazer um novo cadastro ou [N] para sair\nEssa matrícula ainda não possui QrCode. Deseja realizar o cadastro? [S/N] ").upper()
            if resposta == "S":
                cadastro(matricula) #Se quiser criar um cadastro, a função cadastro é chamada.
            elif resposta == "N":
                print("Ok")
        break


while True: #Após digitar a matricula, a função identificador é chamada, para veficiar a exitestência da matricula. 
    matricula = int(input("Digite o n° de matrícula: "))
    identificador(matricula)
    resposta = input("Deseja realizar nova busca por matrícula? [S/N] ").upper()
    while resposta != "N" and resposta != "S":
        resposta = input(
            "Digite uma resposta válida: [S] para fazer uma nova busca ou [N] para finalizar o programa\nDeseja realizar nova busca por matrícula? [S/N] ").upper()
    if resposta == "N": #Se for "N" o programa é finalizado.
        break
    
