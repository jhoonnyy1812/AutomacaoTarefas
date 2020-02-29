import os
import sys
import speech_recognition as sr


def ouvir_microfone(k):
    #Habilita o microfone para ouvir o usuario
    microfone = sr.Recognizer()
    frase = ""
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

test1 = False
rec_audio_resp = 0

lista = open("tarefas.txt","r")
print("Já tenho cadastradas essas tarefas: \n")
k = lista.readlines()
for i in range(len(k)):
    print("%.0f: "%(i+1) + k[i])
lista.close()

os.system("pause")

while(test1 == False):
    tarefa = ouvir_microfone(0)
    print("Voce disse "+ tarefa)
    ans = ouvir_microfone(1)
    if(ans == "sim"):
        test1 = True
    else:
        print("Perdão, tente novamente.")

lista2 = open("destinos.txt", "r")
y = lista2.readlines()

for i in range(len(k)):
    print(k[i])
    print(tarefa)
    if (tarefa == k[i].rstrip()):
        print("Executando tarefa.")

if (tarefa == k[2].rstrip()):
    os.startfile(y[0])