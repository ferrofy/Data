import time as t

#____________________________________________________________
def Slow_Print(text):
    for char in text:
        print(char, end='', flush=True)
        t.sleep(0.04)
def Slow_Input(Inp):
    Slow_Print(Inp)
    return input()
#____________________________________________________________
def Exit_All_Commands():
    Slow_Print("OK Bye User Closing Bot Please Wait...\n")
    t.sleep(1)
    Slow_Print("Closing Bot In 3 Sec\n")
    t.sleep(1)
    Slow_Print("Closing Bot In 2 Sec\n")
    t.sleep(1)
    Slow_Print("Closing Bot In 1 Sec\n")
    t.sleep(1)
    Slow_Print("Bye User. Have A Good Day :)\n")
    Slow_Print("Exit...")

def Exit_F_Commands():
    print("Exiting --f Command Plz W8....")
    t.sleep(1)
    print("Exiting --f Command In 3 Sec")
    t.sleep(1)
    print("Exiting --f Command In 2 Sec")
    t.sleep(1)
    print("Exiting --f Command In 1 Sec")
    t.sleep(1)
    print("exit")
    
def Exit_I_Commands():
    print("Exiting --i Command Plz W8....")
    t.sleep(1)
    print("Exiting --i Command In 3 Sec")
    t.sleep(1)
    print("Exiting --i Command In 2 Sec")
    t.sleep(1)
    print("Exiting --i Command In 1 Sec")
    t.sleep(1)
    print("exit")
    
def Exit_T_Commands():
    print("Exiting --t Command Plz W8....")
    t.sleep(1)
    print("Exiting --t Command In 3 Sec")
    t.sleep(1)
    print("Exiting --t Command In 2 Sec")
    t.sleep(1)
    print("Exiting --t Command In 1 Sec")
    t.sleep(1)
    print("exit")

#____________________________________________________________
All_Commands = ["--i","--f","--t"]
F_Commands = ["--help","--exit"]
I_Commands = ["--help","--exit"]
T_Commands = ["--help","--exit"]
#____________________________________________________________
All_Commands_Help = ""
Help_F = ""
Help_I = "Help --i"
Help_T = ""

#____________________________________________________________
User_Name_Input = Slow_Input("Please Enter Your Name >>> ")
User_Name = User_Name_Input[:20] if len(User_Name_Input) > 10 else User_Name_Input  # Trim Name Upto 20 Char :)
Slow_Print(f"Nice To Meet You '{User_Name}'\n")

#____________________________________________________________
while True:
#Command Selection
    User_Selected_Command = Slow_Input("Which Type Of Command You Want >>> ").lower().strip()
    if User_Selected_Command in All_Commands:
# I Command
        while True:
            if User_Selected_Command == "--i":
                User_I_Command = Slow_Input(">>> --i ").lower().strip()
                if User_I_Command in I_Commands:
                    if User_I_Command == "":
                        print("")
                    elif User_I_Command == "--help":
                        print(Help_I)
                    elif User_I_Command == "--exit":
                        Exit_I_Commands()
                        break
                    else:
                        print("Plz Bro Type '--help'")
                else:
                    print("Plz Bro Type '--help'")
    # F Command
 
    elif User_Selected_Command == "--help":
        Slow_Print(All_Commands_Help)
    elif User_Selected_Command == "--exit":
        Exit_All_Commands()
        break
    else:
        Slow_Print("Please Select A Valid Command Or Type '--help'\n")
