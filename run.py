#!/usr/bin/python3
# This Programm write by Mr.nope
# Version 1.2.0
from os import system as command
import sys
try:
    from deep_translator import GoogleTranslator
except ImportError:
    os.system("pip3 install deep_translator")
from platform import uname
try:
    from colorama import Fore,init
    init()
except ImportError:
    os.system("pip3 install colorama")
End = '\033[0m'
opt = "\nEnter: "
system = uname()[0]
banner = Fore.BLUE + """
d888888P                                     dP            dP            
   88                                        88            88            
   88    88d888b. .d8888b. 88d888b. .d8888b. 88 .d8888b. d8888P .d8888b. 
   88    88'  `88 88'  `88 88'  `88 Y8ooooo. 88 88'  `88   88   88ooood8 
   88    88       88.  .88 88    88       88 88 88.  .88   88   88.  ... 
   dP    dP       `88888P8 dP    dP `88888P' dP `88888P8   dP   `88888P' 
                                                                         
              
""" + End
def cls():
    if system == 'Linux':
        command("clear")
    elif system == 'Windows':
        command("cls")
    else:
        print("\nPlease, Run This Programm on Linux, Windows and MacOS!\n")
        sys.exit()
def main():
    command("printf '\033]2;Translate\a'")
    cls()
    print(banner)
    print("\nUsage: " + Fore.GREEN + "Ctrl + D "  + End + "To Exit...!\n")
    word = input(opt)
    if word == '':
        try1()
    else:
        run(word)
def try1():
    try_to_menu = input("\nDo you want to try again? [y/n] ")
    if try_to_menu == 'y':
        main()
    elif try_to_menu == 'n':
        ext()
    else:
        try1()
def ext():
    cls()
    print("\nExiting...")
    sys.exit()
def run(var):
    len = input("\nEnter language1: ")
    len_2 = input("\nEnter language2: ")
    run_translate = GoogleTranslator(source=len,terget=len_2).translate(var)
    print("\n-----------------------------\n")
    print(run_translate)
    try1()
def try2():
    try_to_menu_2 = input("\npress Enter...")
    if try_to_menu_2 == '':
        main()
    else:
        main()
if __name__ == '__main__':
    try:
        try:
            main()
        except KeyboardInterrupt:
            print("\nCtrl + C")
            try2()
    except EOFError:
        print("\nCtrl + D")
        print("\nExiting...")
        sys.exit()