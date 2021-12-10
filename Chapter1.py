import time
import Chapter2


def travel():
    time.sleep(1)
    print("option 1: Risk taking the last bit of oxygen she has. See whats in the other ship ")
    time.sleep(2)
    print("*" * 67)
    time.sleep(2)
    print("As marceline's ship makes way across the void of darkness,is getting closer to the destroyed ship""\n-----\n")
    time.sleep(1)
    print("Getting closer")
    time.sleep(4)
    print("And closer")
    time.sleep(4)
    print("And Closer")
    time.sleep(2)
    print("Marceline is now in the destroyed ship in front of airlock  ")
    travel1 = input("Open the airlock?(Y/N): ")
    if travel1.upper() == 'Y':
        time.sleep(4)
        print("A white mist awakens and starts to diminish \n\n ")
        Chapter2.chapter2()
        time.sleep(4)
        done = False
    else:
        done = True
    return done


def give_up():
    print("option 3: Give up \n")
    print("*" * 67)


    time.sleep(3)
    print('Marceline loses hope and is slowly giving up\n ')
    time.sleep(2)
    print("As Marceline stay in her ship time is passing and is wasting oxygen ")
    time.sleep(3)
    print("Oxygen level is slowly dimishing")
    time.sleep(3)
    print ("and slowing going into a deep blacked void of endless sleep")
    time.sleep(2)
    print("*Dies*")


def rest_inn():
    print("option 2: Rest ")
    print("*" * 67)
    print("**  Marceline rest at her ship....                    **")
    time.sleep(3)
    print("Time passes by")
    time.sleep(3)
    stay = input("Do you want to stay more? y/n")
    stay = stay.upper()
    if stay == 'Y':
        print("Resting more ")
        time.sleep(2)
        done = True
    else:
        print("Marceline Gets up ")
        done = True
    return done



def choose_action():
    time.sleep(2)
    print("You can choose one of the following actions\n")
    time.sleep(1)
    print("1. Risk taking the last bit of oxygen she has. See whats in the other ship")
    time.sleep(1)
    print("\n2.Rest")
    time.sleep(1)
    print("\n3. Give up\n")

    time.sleep(2)


def action():
   choose_action()
   print("###########################################")
   option = input("Please enter any of the 3 numbers to choose ---->  ")
   while option != 'q':
        if option == '1':
           result = travel()
        elif option == '2':
            result = rest_inn()
        elif option == '3':
            result = give_up()
        else:
            print("\ninvalid option. please do again. ")
        if result == True:
           time.sleep(1)
           choose_action()
           option = input("\nPlease enter any number to start of exit for q ---->  ")
        else:
            break
   return result


def chap1_intro():
    time.sleep(1)
    print("################")
    print("#              #")
    print("#   Chapter 1  #")
    print("#              #")
    print("################")
    time.sleep(2)
    print("Marceline is in a state of loneliness; sees a ship destroyed across")




def ch1():
    time.sleep(2)
    chap1_intro()
    action()

