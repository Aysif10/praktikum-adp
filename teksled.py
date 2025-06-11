import os
import time
from termcolor import colored

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def teks_LED(teks,lebar,langkah,durasi,text_color):
    delay=durasi/langkah
    teks_terisi = ' ' * lebar + teks + ' ' * lebar
    scroll = len(teks_terisi) - lebar + 1 

    index = 0

    for langkah in range(langkah):
        clear()
        posisi = index % scroll
        window = teks_terisi[posisi:posisi + lebar]
        print('+' + '-' * lebar + '+')
        print('|', end='')
        for karakter in window:
            print(colored(karakter, text_color), end='')
        print('|')
        print('+' + '-' * lebar + '+')
        index += 1
        time.sleep(delay)
teks_LED(teks="Happy Eid",lebar=9, langkah=20, durasi=20 ,text_color= 'red')