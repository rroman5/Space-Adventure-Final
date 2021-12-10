import time
import Chapter5

def chapter4():
    time.sleep(2)
    print("################")
    print("#              #")
    print("#   Chapter 4  #")
    print("#              #")
    print("################")
    time.sleep(2)
    print("“As Marceline Is finally able to have oxygen, she looks around the destroyed ship")
    time.sleep(1)
    print("Marceline finds herself with plenty of resources and hears something static")
    time.sleep(1)
    print("Marceline is ready to depart but a static noise stops her ")
    time.sleep(1)
    print("A roaring static noise that can be heard down the hallway")
    time.sleep(1)
    print("*Marceline looks straight down the hallway, where the noise is coming from*")
    choose_action4()

def choose_action4():
    time.sleep(2)
    print("You can choose one of the following actions\n")
    time.sleep(1)
    print("1. Head towards the noise ")
    time.sleep(1)
    print("\n2.Heads back to her ship")
    action4()


def action4():
    time.sleep(2)
    print("###########################################")
    fouroption = input("Please enter any of the 5 number to choose ----> ")
    while fouroption != 'q':
        if fouroption == '1':
            result = move_noise()
        elif fouroption != '2':
            result = head_back()
        else:
            print("\ninvalid option. please do again. ")
        if result == True:
            time.sleep(1)
            choose_action4()
            fouroption = input("\nPlease enter any number to start of exit for q ---->  ")
        else:
            break
    return result

def move_noise():
    print("option 1: Head towards the noise\n")
    print("*" * 67)
    time.sleep(2)
    print("*Wondering what could it be*")
    time.sleep(1)
    print("Can it be a creature?")
    time.sleep(1)
    print("What if its a person?")
    time.sleep(1)
    print("Theres only one way to find out")
    time.sleep(1)
    print("*Marceline slowly and carefully floats her way to the noise ")
    Chapter5.chapter5()
    #Right here fix when done with Chapter5.

def head_back():
    print("option 2: Head back to her ship")
    print("*"*67)
    time.sleep(2)
    print("Frighten of what it can be")
    time.sleep(1)
    print("Marceline takes the safe route and head back to her ship")




