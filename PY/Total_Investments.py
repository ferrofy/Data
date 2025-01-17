#_______Mapping List Indexes to Names_______
# VPX    =  0
# Tanav  =  1
# KMX    =  2
# AKX    =  3
# Angel  =  4
# UCI    =  5
# SSX    =  6
# PPX    =  7
#__________________________________________________

import time

#___________________0xt_____________________
Investments_Pool_0xt = (510, 610, 20, 20, 0, 0, 0, 0)
Investments_Farm_0xt = [0, 0, 0, 20, 20, 0, 0, 0, 0, 125]
Investments_Browser_0xt = [0, 0, 0, 20, 20, 0, 0, 0, 0, 125]
Investments_NFT_0xt = [0, 0, 0, 20, 20, 0, 0, 0, 0, 125]

#_________________0x0_______________________
Investments_Pool_0x0 = [0, 0, 0, 20, 10, 0, 0, 0, 0, 125]
Investments_Farm_0x0 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Investments_Browser_0x0 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Investments_NFT_0x0 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

Total_Invested_Pool = sum(Investments_Pool_0xt) + sum(Investments_Pool_0x0)
#Total_Invested_Farm =
#Total_Invested_Browser =
#Total_Invested_NFT =

#_____________________________________________________
Total_Invested_Pool = sum(Investments_Pool_0xt) + sum(Investments_Pool_0x0)
Total_Invested_Farm = sum(Investments_Farm_0xt)
Total_Invested_Browser = sum(Investments_Browser_0xt)
Total_Invested_NFT = sum(Investments_NFT_0xt)
#_________________________________________________________
VPX_Total_Pool_Investments = Investments_Pool_0xt[0] + Investments_Pool_0x0[0]
VPX_Total_Farm_Investments = Investments_Farm_0xt[0]
VPX_Total_Browser_Investments = Investments_Browser_0xt[0]
VPX_Total_NFT_Investments = Investments_NFT_0xt[0]
#_________________________________________________________
Tanav_Total_Pool_Investments = Investments_Pool_0xt[1] + Investments_Pool_0x0[1]
Tanav_Total_Farm_Investments = Investments_Farm_0xt[1]
Tanav_Total_Browser_Investments = Investments_Browser_0xt[1]
Tanav_Total_NFT_Investments = Investments_NFT_0xt[1]
#_________________________________________________________
KMX_Total_Pool_Investments = Investments_Pool_0xt[2] + Investments_Pool_0x0[2]
KMX_Total_Farm_Investments = Investments_Farm_0xt[2]
KMX_Total_Browser_Investments = Investments_Browser_0xt[2]
KMX_Total_NFT_Investments = Investments_NFT_0xt[2]
#_________________________________________________________
AKX_Total_Pool_Investments = Investments_Pool_0xt[3] + Investments_Pool_0x0[3]
AKX_Total_Farm_Investments = Investments_Farm_0xt[3]
AKX_Total_Browser_Investments = Investments_Browser_0xt[3]
AKX_Total_NFT_Investments = Investments_NFT_0xt[3]
#_________________________________________________________
Angel_Total_Pool_Investments = Investments_Pool_0xt[4] + Investments_Pool_0x0[4]
Angel_Total_Farm_Investments = Investments_Farm_0xt[4]
Angel_Total_Browser_Investments = Investments_Browser_0xt[4]
Angel_Total_NFT_Investments = Investments_NFT_0xt[4]
#_________________________________________________________
UCI_Total_Pool_Investments = Investments_Pool_0xt[5] + Investments_Pool_0x0[5]
UCI_Total_Farm_Investments = Investments_Farm_0xt[5]
UCI_Total_Browser_Investments = Investments_Browser_0xt[5]
UCI_Total_NFT_Investments = Investments_NFT_0xt[5]
#_________________________________________________________
SSX_Total_Pool_Investments = Investments_Pool_0xt[6] + Investments_Pool_0x0[6]
SSX_Total_Farm_Investments = Investments_Farm_0xt[6]
SSX_Total_Browser_Investments = Investments_Browser_0xt[6]
SSX_Total_NFT_Investments = Investments_NFT_0xt[6]
#_________________________________________________________
PPX_Total_Pool_Investments = Investments_Pool_0xt[7] + Investments_Pool_0x0[7]
PPX_Total_Farm_Investments = Investments_Farm_0xt[7]
PPX_Total_Browser_Investments = Investments_Browser_0xt[7]
PPX_Total_NFT_Investments = Investments_NFT_0xt[7]
    
def Data():
    Total_Invested = (
        f"__________________________________________\n"
        f"               Total Invested             \n"
        f"__________________________________________\n"
        f"Pool: {Total_Invested_Pool}\n"
        f"Farm: {Total_Invested_Farm}\n"
        f"Browser: {Total_Invested_Browser}\n"
        f"NFT: {Total_Invested_NFT}\n"
        f"__________________________________________\n"
        f"      Per Person Total Investments        \n"
        f"__________________________________________\n"
        f"----- @VPX ------ \n"
        f"Pool: {VPX_Total_Pool_Investments}        |  0xt: {Investments_Pool_0xt[0]}     |  0x0-1: {Investments_Pool_0x0[0]}\n"
        f"Farm: {VPX_Total_Farm_Investments}        |  0xt: {Investments_Farm_0xt[0]}     |  0x0-1: {Investments_Farm_0x0[0]}\n"
        f"Browser: {VPX_Total_Browser_Investments}  |  0xt: {Investments_Browser_0xt[0]}  |  0x0-1: {Investments_Browser_0x0[0]}\n"
        f"NFT: {VPX_Total_NFT_Investments}          |  0xt: {Investments_NFT_0xt[0]}      |  0x0-1: {Investments_NFT_0x0[0]}\n"
        f"\n"
        f"----- @Tanav ------ \n"
        f"Pool: {Tanav_Total_Pool_Investments}       |    0xt: {Investments_Pool_0xt[1]}  |  0x0-1: {Investments_Pool_0x0[1]}\n"
        f"Farm: {Tanav_Total_Farm_Investments}       |  0xt: {Investments_Farm_0xt[1]}    |  0x0-1: {Investments_Farm_0x0[1]}\n"
        f"Browser: {Tanav_Total_Browser_Investments} |  0xt: {Investments_Browser_0xt[1]} |  0x0-1: {Investments_Browser_0x0[1]}\n"
        f"NFT: {Tanav_Total_NFT_Investments}         |  0xt: {Investments_NFT_0xt[1]}     |  0x0-1: {Investments_NFT_0x0[1]}\n"
        f"\n"
        f"----- @KMX ------ \n"
        f"Pool: {KMX_Total_Pool_Investments}        |  0xt: {Investments_Pool_0xt[2]}     |  0x0-1: {Investments_Pool_0x0[2]}\n"
        f"Farm: {KMX_Total_Farm_Investments}        |  0xt: {Investments_Farm_0xt[2]}     |  0x0-1: {Investments_Farm_0x0[2]}\n"
        f"Browser: {KMX_Total_Browser_Investments}  |  0xt: {Investments_Browser_0xt[2]}  |  0x0-1: {Investments_Browser_0x0[2]}\n"
        f"NFT: {KMX_Total_NFT_Investments}          |  0xt: {Investments_NFT_0xt[2]}      |  0x0-1: {Investments_NFT_0x0[2]}\n"
        f"\n"
        f"----- @AKX ------ \n"
        f"Pool: {AKX_Total_Pool_Investments}        |  0xt: {Investments_Pool_0xt[3]}     |  0x0-1: {Investments_Pool_0x0[3]}\n"
        f"Farm: {AKX_Total_Farm_Investments}        |  0xt: {Investments_Farm_0xt[3]}     |  0x0-1: {Investments_Farm_0x0[3]}\n"
        f"Browser: {AKX_Total_Browser_Investments}  |  0xt: {Investments_Browser_0xt[3]}  |  0x0-1: {Investments_Browser_0x0[3]}\n"
        f"NFT: {AKX_Total_NFT_Investments}          |  0xt: {Investments_NFT_0xt[3]}      |  0x0-1: {Investments_NFT_0x0[3]}\n"
        f"\n"
        f"----- @Angel ------ \n"
        f"Pool: {Angel_Total_Pool_Investments}        |  0xt: {Investments_Pool_0xt[4]}     |  0x0-1: {Investments_Pool_0x0[4]}\n"
        f"Farm: {Angel_Total_Farm_Investments}        |  0xt: {Investments_Farm_0xt[4]}     |  0x0-1: {Investments_Farm_0x0[4]}\n"
        f"Browser: {Angel_Total_Browser_Investments}  |  0xt: {Investments_Browser_0xt[4]}  |  0x0-1: {Investments_Browser_0x0[4]}\n"
        f"NFT: {Angel_Total_NFT_Investments}          |  0xt: {Investments_NFT_0xt[4]}      |  0x0-1: {Investments_NFT_0x0[4]}\n"
        f"\n"
        f"----- @UCI ------ \n"
        f"Pool: {UCI_Total_Pool_Investments}        |  0xt: {Investments_Pool_0xt[5]}     |  0x0-1: {Investments_Pool_0x0[5]}\n"
        f"Farm: {UCI_Total_Farm_Investments}        |  0xt: {Investments_Farm_0xt[5]}     |  0x0-1: {Investments_Farm_0x0[5]}\n"
        f"Browser: {UCI_Total_Browser_Investments}  |  0xt: {Investments_Browser_0xt[5]}  |  0x0-1: {Investments_Browser_0x0[5]}\n"
        f"NFT: {UCI_Total_NFT_Investments}          |  0xt: {Investments_NFT_0xt[5]}      |  0x0-1: {Investments_NFT_0x0[5]}\n"
        f"\n"
        f"----- @SSX ------ \n"
        f"Pool: {SSX_Total_Pool_Investments}        |  0xt: {Investments_Pool_0xt[6]}     |  0x0-1: {Investments_Pool_0x0[6]}\n"
        f"Farm: {SSX_Total_Farm_Investments}        |  0xt: {Investments_Farm_0xt[6]}     |  0x0-1: {Investments_Farm_0x0[6]}\n"
        f"Browser: {SSX_Total_Browser_Investments}  |  0xt: {Investments_Browser_0xt[6]}  |  0x0-1: {Investments_Browser_0x0[6]}\n"
        f"NFT: {SSX_Total_NFT_Investments}          |  0xt: {Investments_NFT_0xt[6]}      |  0x0-1: {Investments_NFT_0x0[6]}\n"
        f"\n"
        f"----- @PPX ------ \n"
        f"Pool: {PPX_Total_Pool_Investments}        |  0xt: {Investments_Pool_0xt[7]}     |  0x0-1: {Investments_Pool_0x0[7]}\n"
        f"Farm: {PPX_Total_Farm_Investments}        |  0xt: {Investments_Farm_0xt[7]}     |  0x0-1: {Investments_Farm_0x0[7]}\n"
        f"Browser: {PPX_Total_Browser_Investments}  |  0xt: {Investments_Browser_0xt[7]}  |  0x0-1: {Investments_Browser_0x0[7]}\n"
        f"NFT: {PPX_Total_NFT_Investments}          |  0xt: {Investments_NFT_0xt[7]}      |  0x0-1: {Investments_NFT_0x0[7]}\n"
        f"\n"
    )
    return Total_Invested

def slow_text(text, duration=0.04):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(duration)
    print()

# Execution
Data()
Total_Invested = Data()
slow_text(Total_Invested)
Exit = input()
