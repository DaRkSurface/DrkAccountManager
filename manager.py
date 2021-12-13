#####################################################
## DrkAccountManager (DrkAM)                       ##
## Made to store accounts (passowords, acc etc.)   ##
## https://voidsecurity.ml                         ##
## Coded by: drk                                   ##
#####################################################

# Imports
import os
import time
from cryptography.fernet import Fernet
from termcolor import colored

# Global Variables
discord = "drk#1337"

# Defines
def art():
    print(colored("""
      _____             _              __  __ 
     |  __ \           | |       /\   |  \/  |
     | |  | | __ _ _ __| | __   /  \  | \  / |
     | |  | |/ _` | '__| |/ /  / /\ \ | |\/| |
     | |__| | (_| | |  |   <  / ____ \| |  | |
     |_____/ \__,_|_|  |_|\_\/_/    \_\_|  |_|

                {-- Made By Drk --}                            
                                          
    """, "yellow"))

def clearcmd():
    os.system('cls' if os.name == 'nt' else 'clear')

def credits():
    clearcmd()
    print(colored(""" 
      _____             _              __  __ 
     |  __ \           | |       /\   |  \/  |
     | |  | | __ _ _ __| | __   /  \  | \  / |
     | |  | |/ _` | '__| |/ /  / /\ \ | |\/| |
     | |__| | (_| | |  |   <  / ____ \| |  | |
     |_____/ \__,_|_|  |_|\_\/_/    \_\_|  |_|
        VoidSec       By drk        VoidSec
    
    
    """, "red"))
    print("""
          Made to store Void Accounts.
    
    """)
    time.sleep(2.5)
    usage()
def delete():
    sure = input("Are you sure you want to delete everything, this cant be undone? (Y/n): ")
    if sure == "n":
       print("Going back.")
       time.sleep(1)
       usage()
    elif sure == "y":
        print("Opening ./WFILE.txt")
        acfile = open("./WFILE.txt", "w")
        acfile.truncate(0)
        print("Successfully erased ./WFILE.txt")
        acfile.close()
        input("\nPress enter to go back...")
        usage()
    else:
        print("\nWRONG INPUT! Enter y or n")
        print("Going back.")
        time.sleep(2.5)
        usage() 

def encrypt():
    pass

def decrypt():
    pass

def darkamss():
    clearcmd()
    print("""
    [1] Set a new Master Password.
    [2] Go back 
    """)
    DAMSUSERIN = input("Enter Option: ") 
    if DAMSUSERIN == "1":
        print("Coming soon.")
        time.sleep(1.5)
        clearcmd()
        darkamss()
    elif DAMSUSERIN == "2":
        usage()

def usage():
    clearcmd()
    art()
    print("""
    [1] Store a new account.
    [2] Read every account.
    [3] Delete all accounts.
    [4] Coming Soon.
    
    [5] Credits.
    [6] Current state of DarkAM.
    [7] Settings.
    [8] Contact

    [9] Quit.
    
    """)
    USER_IN = input("Enter Option: ")
    if USER_IN == "1":
        write()

    elif USER_IN == "2":
        read()

    elif USER_IN == "3":
        delete()

    elif USER_IN == "4":
        cmsoon()

    elif USER_IN == "5":
        credits()

    elif USER_IN == "6":
        state()

    elif USER_IN == "7":
        darkamss()
    elif USER_IN == "8":
        print("""
        
        GitHub: https://github.com/DaRkSurface
        Discord: drk#1337
        """)
        input("\nPress enter to go back...")
        usage()




    elif USER_IN == "9":
        print("Quitting..")
        time.sleep(0.5)
        clearcmd()
        quit()
    else:
        print("Did not reckognize your input " + USER_IN + " try again.")
        time.sleep(2.5)
        usage()


def write():
    NAME = input("Name this account: ")
    MAIL = input("Email: ")
    PASSWD = input("Passwd: ")
    OTHER = input("Other Info: ")
    with open("./WFILE.txt", "a") as WFILE:
        WFILE.write("-----------------" + "\n")
        WFILE.write(NAME.upper() + "\n\n")
        print("\nSET: " + NAME + " As NAME.")
        WFILE.write("Email: " + MAIL + "\n")
        print("WROTE: " + MAIL)
        time.sleep(0.3)
        
        WFILE.write("Password: " + PASSWD + "\n")
        print("WROTE: " + PASSWD)
        time.sleep(0.3)

        WFILE.write("Other Info: " + OTHER + "\n")
        print("WROTE: " + OTHER)
        time.sleep(0.3)
        WFILE.write("-----------------" + "\n")
    
        WFILE.close()
        time.sleep(3)
        usage()

def read():
    with open("./WFILE.txt", "r+") as file:
        filecontent = file.read()
    print(filecontent)
    input("Press enter to go back...")
    usage()

def delall():
    print("Soon.")
    usage()

def cmsoon():
    print("Coming Soon.")
    time.sleep(1.5)
    usage()
    

def state():
    clearcmd()
    print(colored("DarkAM is not Secure. It is just a fun project by drk.\n", "green"))
    time.sleep(2)
    usage()

# Main Code
def main():
    clearcmd()
    art()
    if os.path.isfile('./MSKPS.txt'):
        with open("./MSKPS.txt", "r") as RMSKPS:
            MSFILE = RMSKPS.read()
        while True:
            MSKP = input("\nEnter Master Password: ")
            if MSKP == MSFILE:
                print("[+] Password", colored("CORRECT", "green"))
                time.sleep(1)
                break
            elif MSKP != MSFILE:
                print("[-] Password", colored("INCORRECT", "red"))
                time.sleep(1)
                continue
        

    else:
        MSKINPUT = input(colored("Enter Master Password That You Want To Use: ", "green"))
        MSFILE = open("./MSKPS.txt", "w")
        MSFILE.write(MSKINPUT)
        MSFILE.close()
    
    usage()

main()
