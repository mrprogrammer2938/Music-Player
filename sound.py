#!/usr/bin/python3
# This Code write by Mr.nope
# Version 1.2
import os,sys
from time import sleep as wait
try:
    from playsound import playsound
except ImportError:
    os.system("pip3 install playsound")
try:
    from colorama import Fore,init
    init()
except ImportError:
    os.system("pip3 install colorama")
End = '\033[0m'
banner = Fore.GREEN + """
----""" + Fore.RED + "[" + Fore.WHITE + "Music Player" + Fore.RED + " ]" + Fore.GREEN + "-----" + End + Fore.CYAN + """\n
Version: """ + Fore.LIGHTGREEN_EX + "1.2" + End
def cls():
    if sys.platform == 'linux':
        os.system("clear")
    elif sys.platform == 'win32':
        os.system("cls")
    else:
        print("\nPlease, run This Programm on Windows, Linux or MacOS\n")
        sys.exit()
def main():
    os.system("printf '\033]2;Music Player\a'")
    cls()
    print(banner)
    alarm_name = input("\nEnter Music File Name: ")
    wait(2)
    try:
        playsound(alarm_name)
        print("\n----------Play-----------\n")
        try1()
    except ValueError:
        print("\nMusic File Not Found!\n")
        wait(1)
        try1()
def try1():
    try_to_main = input("\nDo you want to try again? [y/n] ")
    if try_to_main == 'y':
        main()
    elif try_to_main == 'n':
        try2()
    else:
        try1()
def try2():
    try_to_exit = input("\npress Enter...")
    if try_to_exit == '':
        ext()
    else:
        ext()
def ext():
    cls()
    print("\nExiting...")
    sys.exit()
if __name__ == '__main__':
    try:
        try:
            main()
        except EOFError:
            print("NOooo....!\n")
            sys.exit()
    except KeyboardInterrupt:
        print("\nCtrl + C")
        print("\nStop !!!")
        sys.exit()