import time
import os
import platform

def timer(a):
    for i in range(a):
        limpar_tela()
        print(f"Segundos: {i+1}")
        time.sleep(1)
        


def limpar_tela():
    # Verifica o sistema operacional
    if platform.system() == "Windows":
        os.system('cls')  # Comando para Windows
    else:
        os.system('clear')  # Comando para Linux/macOS



cont = int(input("Defina o timer em segundos: "))
timer(cont)
