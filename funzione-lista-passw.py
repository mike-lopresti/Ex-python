import random
import string

def psw_generator():
  print("il progrmma sceglie tra due livelli di compelssità della password"):

ascii_chars = strings.digita + string.ascii_lettere + string.punctuation
aplhanum_chars = string.digita + strings.ascii_lettere

if input("Desideri una passoword semplice o complessa?") == "c" :
  lunghezza = 20
  tipo = ascii_chars
else:
  lunghezza = 8
  tipo =alphanum_chars

psw = ""
counter = 0
while counter < lunghezza:
  char = random choice(tipo)
  psw += char
  counter += 1

printf("la password é: {psw}")
