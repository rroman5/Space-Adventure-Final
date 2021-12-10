import time
#Author: Roberto Roman
#Date: 12/05/2021

import Chapter1
print("    #####################")
print("    #                   #")
print("    #  Space Adventure  #")
print("    #                   #")
print("    #####################")



print("Would you like to begin the game")
answer = input("Press y to continue (Y/N):  ")
if answer == 'n' or answer == 'N':
    time.sleep(1)
    print("Quitter")
elif answer == 'y' or answer == 'Y':
    time.sleep(2)
    print(" You are named Marceline")
    time.sleep(2)
    print(" Its a dark stare of darkness, In Marceline's ship's cockpit windown, her oxygen level is low")
    Chapter1.ch1()


