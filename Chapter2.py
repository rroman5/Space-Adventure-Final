import time
import Chapter3

def chapter2():
    time.sleep(1)
    print("################")
    print("#              #")
    print("#   Chapter 2  #")
    print("#              #")
    print("################")
    time.sleep(2)
    print("Marceline finds herself inside the other destroyed ship, her oxygen is running out")
    time.sleep(1)
    print("Looking for any type of resource")
    time.sleep(1)
    choose_action2()

def choose_action2():
    time.sleep(2)
    print("You can choose one of the following actions\n")
    time.sleep(1)
    print("1. Take the last bit of oxygen and die ")
    time.sleep(1)
    print("\n2.Rest")
    time.sleep(1)
    print("\n3. Check the Cockpit\n")
    time.sleep(1)
    print("4. \nCheck the radio for some sort of help\n")
    time.sleep(1)
    print("5.\nruns towards the storage room\n")
    action2()


def action2():
    time.sleep(2)
    print("###########################################")
    secondoption = input("Please enter any of the 5 number to choose ----> ")
    while secondoption != 'q':
        if secondoption == '5':
            result = storage_room()
        elif secondoption == '1':
            result = quit_die()
        elif secondoption == '2':
            result = res_ting()
        elif secondoption == '3':
            result = cok_pit()
        elif secondoption == '4':
            result = check_radio()
        else:
            print("\ninvalid option. please do again. ")
        if result == True:
            time.sleep(1)
            choose_action2()
            secondoption = input("\nPlease enter any number to start of exit for q ---->  ")
        else:
            break
    return result




def quit_die():
    print("option 1: Take the last bit of oxygen and die\n")
    print("*" * 67)
    time.sleep(2)
    print("Marcelines head is spinning")
    time.sleep(1)
    print("Negative thoughts ")
    time.sleep(1)
    print("Doubt")
    time.sleep(1)
    print("*TAKES OF ASTRONAUT HELMET")
    time.sleep(1)
    print("*DIES*")


def res_ting():
    print("option 2: Rest\n")
    print("*" * 67)
    time.sleep(2)
    print("Marceline")
    time.sleep(1)
    print("**  Marceline rest at her ship....                    **")
    time.sleep(3)
    print("Time passes by")
    time.sleep(3)
    stay = input("Do you want to continue wasting oxygen? y/n")
    stay = stay.upper()
    if stay == 'Y':
        print("Resting more ")
        time.sleep(2)
        done = True
    else:
        print("Marceline Gets up ")
        done = True
    return done

def cok_pit():
    print("option 3: Check the cockpit")
    print("*"*67)
    time.sleep(2)
    print("Marceline walks towards the cockpit")
    time.sleep(1)
    print("**  Marceline sees that control unit is unstable ")
    time.sleep(3)
    print("and unable to function")
    time.sleep(3)
    stay = input("Want to go back to the main entrance  y/n")
    stay = stay.upper()
    if stay == 'Y':
        print("*Goes back* ")
        time.sleep(2)
        done = True
    else:
        print("Marceline stays ")
        done = True
    return done


def check_radio():
    print("option 4:Check the radio for some sort of help")
    print("*"*67)
    time.sleep(2)
    print("Marceline floats towards a buzzing phone")
    #NEEDS SOME EDITING AND FINISH TO CHAPTER 5

def storage_room():
    print("option 5:Runs towards the storage room ")
    print("*"*67)
    time.sleep(2)
    print("Marceline sees an open intact door")
    time.sleep(2)
    print("Floating towards the door")
    time.sleep(1)
    print("Marceline is stunned to what she is seeing")
    Chapter3.chapter3() #Right here ch3







def ch2():
    action2()








