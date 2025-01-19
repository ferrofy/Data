import time as t
from Python_Data import Entry_Help_Exit as Long_Text
from Python_Data import Commands as Commands
from Python_Data import Output as Output

#____________________________________________________________
def Slow_Print(text):
    for char in text:
        print(char, end='', flush=True)
        t.sleep(0.04)
def Slow_Input(Inp):
    Slow_Print(Inp)
    return input()

#____________________________________________________________
User_Name_Input = Slow_Input("Please Enter Your Name >>> ")
User_Name = User_Name_Input[:20] if len(User_Name_Input) > 10 else User_Name_Input  # Trim Name Upto 20 Char :)
Slow_Print(f"Nice To Meet You '{User_Name}'\n")
Slow_Print("_______________________________________\n")

#____________________________________________________________
while True:
#Command Selection
    User_Selected_Command = Slow_Input("Which Command You Want To Use >>> ").lower().strip()
    if User_Selected_Command in Commands.All_Commands:
        
#____________________________________________________________
        while True:
            if User_Selected_Command == "--f":
                User_F_Command = Slow_Input(">>> --f ").lower().strip()
                if User_F_Command in Commands.F_Commands:
                    if User_F_Command == "--rulebook" or "--infobook":
                        Slow_Print(Output.FerroFy_RuleBook)
                    elif User_F_Command == "--help":
                        Slow_Print(Long_Text.Help_F)
                    elif User_F_Command == "--exit":
                        Long_Text.Exit_F_Commands()
                        break
                    else:
                        Slow_Print("Plz Type '--help'")
                else:
                    Slow_Print("Plz Type '--help'")
                    
#____________________________________________________________
            elif User_Selected_Command == "--i":
                User_I_Command = Slow_Input(">>> --i ").lower().strip()
                if User_I_Command in Commands.I_Commands:
                    if User_I_Command == "":
                        Slow_Print("")
                    elif User_I_Command == "--help":
                        Slow_Print(Long_Text.Help_I)
                    elif User_I_Command == "--exit":
                        Long_Text.Exit_I_Commands()
                        break
                    else:
                        Slow_Print("Plz Type '--help'")
                else:
                    Slow_Print("Plz Type '--help'")

#____________________________________________________________
            elif User_Selected_Command == "--s":
                User_S_Command = Slow_Input(">>> --s ").lower().strip()
                if User_S_Command in Commands.S_Commands:
                    if User_S_Command == "":
                        Slow_Print("")
                    elif User_S_Command == "--help":
                        Slow_Print(Long_Text.Help_S)
                    elif User_S_Command == "--exit":
                        Long_Text.Exit_S_Commands()
                        break
                    else:
                        Slow_Print("Plz Type '--help'")
                else:
                    Slow_Print("Plz Type '--help'")

#____________________________________________________________
            elif User_Selected_Command == "--t":
                User_T_Command = Slow_Input(">>> --t ").lower().strip()
                if User_T_Command in Commands.T_Commands:
                    if User_T_Command == "":
                        Slow_Print("")
                    elif User_T_Command == "--help":
                        Slow_Print(Long_Text.Help_T)
                    elif User_T_Command == "--exit":
                        Long_Text.Exit_T_Commands()
                        break
                    else:
                        Slow_Print("Plz Type '--help'")
                else:
                    Slow_Print("Plz Type '--help'")
                    
#____________________________________________________________
    elif User_Selected_Command == "--help":
        Slow_Print(Long_Text.All_Commands_Help)
    elif User_Selected_Command == "--exit":
        Long_Text.Exit_All_Commands()
        break
    else:
        Slow_Print("Please Select A Valid Command Or Type '--help'\n")
