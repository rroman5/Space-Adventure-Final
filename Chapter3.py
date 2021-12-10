import time
import Chapter4

def chapter3():
    time.sleep(2)
    print("################")
    print("#              #")
    print("#   Chapter 3  #")
    print("#              #")
    print("################")
    time.sleep(2)
    print("Marceline is relieved to see oxygen tanks at the storage room")
    time.sleep(1)
    print("Happy she has extra oxygen for herself")
    time.sleep(1)
    print("Although still has to find her way back home")
    time.sleep(1)
    print("*Puts it on*")
    choose_action3()

def choose_action3():
    time.sleep(2)
    print("You can choose one of the following actions\n")
    time.sleep(1)
    print("1. rest ")
    time.sleep(1)
    print("\n2.Takes the rest oxygen tanks to Marceline’s ship")
    time.sleep(1)
    print("\n3. Looks for more resources\n")
    action3()

def action3():
    time.sleep(2)
    print("###########################################")
    thirdoption = input("Please enter any of the 5 number to choose ----> ")
    while thirdoption != 'q':
        if thirdoption == '3':
            result = more_res()
        elif thirdoption == '1':
            result = chill_relax()
        elif thirdoption == '2':
            result = take_oxy()
        else:
            print("\ninvalid option. please do again. ")
        if result == True:
            time.sleep(1)
            choose_action3()
            thirdoption = input("\nPlease enter any number to start of exit for q ---->  ")
        else:
            break
    return result

def chill_relax():
    print("option 1: Rest\n")
    print("*" * 67)
    time.sleep(2)
    print("**  Marceline is taking advantage of her oxygen's and decides to ease off a bit ")
    time.sleep(3)
    print("Time passes by")
    time.sleep(3)
    stay = input("Do you want to rest more? y/n")
    stay = stay.upper()
    if stay == 'Y':
        print("Resting more ")
        time.sleep(2)
        done = True
    else:
        print("Marceline Gets up ")
        done = True
    return done

def take_oxy():
    print("option 2:Takes the rest oxygen tanks to Marceline’s ship ")
    print("*"* 67)
    time.sleep(2)
    print("Marceline decides to take all the oxygen tanks to her ship")
    time.sleep(1)
    print("One by One")
    time.sleep(1)
    print("Tank by Tank")
    time.sleep(1)
    print("carefully shipping it to her own")
    time.sleep(1)
    print("*Finished loading up")
    action3()

def more_res():
    print("option 3: Look for more resources")
    print("*"*67)
    time.sleep(2)
    print("Marceline is happy with her findings")
    time.sleep(1)
    print("but feels like there can be more stuff")
    Chapter4.chapter4()





def ch3():
    action3()





























