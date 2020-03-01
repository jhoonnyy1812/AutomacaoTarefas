import os
import sys
import speech_recognition as sr
import time


#####Funções básicas#####
def ouvir_microfone(k):
    #Habilita o microfone para ouvir o usuario
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        #Chama a funcao de reducao de ruido disponivel na speech_recognition
        microfone.adjust_for_ambient_noise(source)
        #Avisa ao usuario que esta pronto para ouvir
        if (k == 0):
            print("Diga o que você quer que eu faça: ")
        else:
            print("Está correto?")
        #Armazena a informacao de audio na variavel
        audio = microfone.listen(source)
    try:
        #Passa o audio para o reconhecedor de padroes do speech_recognition
        frase = microfone.recognize_google(audio,language='pt-BR')
#Caso nao tenha reconhecido o padrao de fala, exibe esta mensagem
    except sr.UnknownValueError:
        print("Não entendi.")
    return frase

#####Input do modo a ser utiizado na comunicação#####
modo = input("Você deseja a comunicação por voz ou por teclado? (0 = Voz e 1 = Teclado): ")

while(modo.rstrip() != '1' and modo.rstrip() != '0'):
    print("Não entendi, pode repetir?")
    modo = input()


#####Print da lista de tarefas previamente preparadas#####
lista = open("tarefas.txt","r")
print("Já tenho cadastradas essas tarefas: \n")
k = lista.readlines()
for i in range(len(k)):
    print("%.0f: "%(i+1) + k[i])
lista.close()

#####Carregamento da lista com os endereços dos programas a serem executados#####
lista2 = open("destinos.txt", "r")
y = lista2.readlines()

os.system("pause")

#####Comando por voz#####
if (modo == "0"):
    test1 = False
    while(test1 == False):
        tarefa = ouvir_microfone(0)
        print("Voce disse "+ tarefa)
        ans = ouvir_microfone(1)
        if(ans == "sim"):
            test1 = True
        else:
            print("Perdão, tente novamente.")

    for i in range(len(k)):
        if (tarefa == k[i].rstrip()):
            print("Executando tarefa.")
            os.system("pause")
    
    if(tarefa == k[0].rstrip()):
        os.startfile(y[1].rstrip())
        os.startfile(y[2].rstrip())
        os.startfile(y[3].rstrip())

    if(tarefa == k[1].rstrip()):
        os.startfile(y[3].rstrip())
        os.startfile(y[4].rstrip())

    if(tarefa == k[2].rstrip()):
        os.startfile(y[0])


afir = len(k)
#####Comando por teclado#####
if (modo == '1'):
    tarefa = input("Digite o número correspondente a sua tarefa: ")
    for i in range(len(k)):
        if (int(tarefa) == i):
            print("Executando tarefa.")
        elif(afir == (len(k)-1)):
            print("Tarefa não encontrada, poderia repetir? ")
            tarefa = input()
            i = 0
    if(tarefa == '1'):
        os.startfile(y[1].rstrip())
        time.sleep(5)
        os.startfile(y[2].rstrip())
        time.sleep(5)
        os.startfile(y[3].rstrip())
        time.sleep(5)
    elif(tarefa == '2'):
        os.startfile(y[3].rstrip())
        os.startfile(y[4].rstrip())
    elif(tarefa == '3'):
        os.startfile(y[0])