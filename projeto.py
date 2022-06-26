import qrcode
from PIL import ImageShow
import os.path 

alunos_cadastrados = []

def cadastro(dados_aluno):
    nome = input('Digite o nome do alune: ')
    matricula = int(input('Nº da matrícula: '))
    curso = input('Nome do curso: ')
    periodo = int(input('Nº do perído: '))

    juntar = nome + " " + str(matricula) + " " +  curso + " " + str(periodo)
    alunos_cadastrados.append(juntar)

    dados_aluno = qrcode.make(alunos_cadastrados)
    dados_aluno.save("{}.png".format(matricula))

    with open('lista.txt', 'a+') as arquivo:
        for aluno in alunos_cadastrados:
            arquivo.write('\n' + aluno)

    print("QrCode criado e cadastro realizado com sucesso.")
    ImageShow.show(dados_aluno)
    print(alunos_cadastrados)

def identificador(matricula):
    while True:
        if (os.path.isfile("{}.png".format(matricula))):
            print("Essa matrícula já possui QrCode.")
        else:
            resposta = input("Essa matrícula ainda não possui QrCode. Deseja realizar o cadastro? [S/N] ").upper()
            while resposta != "S" and resposta != "N":
                resposta = input(
                    "Digite uma resposta válida: [S] para fazer um novo cadastro ou [N] para sair\nEssa matrícula ainda não possui QrCode. Deseja realizar o cadastro? [S/N] ").upper()
            if resposta == "S":
                cadastro(matricula)
            elif resposta == "N":
                print("Ok")
        break


while True:
    matricula = int(input("Digite o n° de matrícula: "))
    identificador(matricula)
    resposta = input("Deseja realizar nova busca por matrícula? [S/N] ").upper()
    while resposta != "N" and resposta != "S":
        resposta = input(
            "Digite uma resposta válida: [S] para fazer uma nova busca ou [N] para finalizar o programa\nDeseja realizar nova busca por matrícula? [S/N] ").upper()
    if resposta == "N":
        break