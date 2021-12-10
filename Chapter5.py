import time


def chapter5():
    time.sleep(2)
    print("################")
    print("#              #")
    print("#   Chapter 5  #")
    print("#              #")
    print("################")
    time.sleep(2)
    print("Getting closer, and closer.......")
    time.sleep(1)
    print("As closer she gets,")
    time.sleep(1)
    print("Sounds are becoming clearer")
    time.sleep(1)
    print("IS ANYBODY THERE")
    time.sleep(1)
    print("Marceline comes a cross a radio ")
    choose_action5()

def choose_action5():
    time.sleep(2)
    print("Choose what to do")
    time.sleep(1)
    print("1. Answer")
    time.sleep(1)
    print("2.Run Off")
    action5()

def action5():
    time.sleep(2)
    print("###########################################")
    fiveoption = input("Please enter any of the 5 number to choose ----> ")
    while fiveoption != 'q':
        if fiveoption == '1':
            result = cont_estar()
        elif fiveoption != '2':
            result = run_off()
        else:
            print("\ninvalid option. please do again. ")
        if result == True:
            time.sleep(1)
            choose_action5()
            fiveoption = input("\nPlease enter any number to start of exit for q ---->  ")
        else:
            break
    return result

def cont_estar():
    print("option 1: Answer")
    print("*" * 67)
    time.sleep(2)
    print("Marceline is in schock")
    time.sleep(2)
    print("Slowly picking up")
    time.sleep(1)
    print("Marceline: Hello, Hello Anybody there")
    time.sleep(1)
    print("Responder: Hello can you read me")
    time.sleep(1)
    print("Marcelone: Yes!, Yes!, Help I'm lost, Please help me ")
    time.sleep(1)
    print("Responder: My coordinates are 12.0.12.3.41,are you familiar with this")
    time.sleep(1)
    print("Marceline: Yes, yes, OH my god.")
    time.sleep(1)
    print ("Marceline:So glad Im in contact with someone")
    time.sleep(1)
    print("Marceline:I was in a mission and we lost connenction due to a rock colliding with us")
    time.sleep(1)
    print("Responder: We know, we know. NO time wasting we'll talk later")
    time.sleep(1)
    print("Marceline: Copy that ")
    time.sleep(1)
    print("*Marceline rushes to her ship with*")
    time.sleep(1)
    print("*Zooming thru the hallway*")
    time.sleep(1)
    print("*Exits the destroyed ship*")
    time.sleep(1)
    print("*Enter her own ship*")
    time.sleep(1)
    print("*Buckels up*")
    time.sleep(1)
    print("Lifts off")
    time.sleep(2)
    print("####################")
    print("#                  #")
    print("#     The End      #")
    print("#                  #")
    print("####################")


def run_off():
    print("option 2: Run Off")
    print("*" * 67)
    time.sleep(1)
    print("Is set with all the resources Marceline has picked up")
    print("*Leaves*")






