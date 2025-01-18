# VPX =   0
# Tanav = 1
# KMX =   2
# AKX =   3
# Angel = 4
# UCI =   5
# SSX =   6
# PPX =   7
# ________________________________________

import time

print("Checking File For Code Errors...")

# _________________0xt_____________________
Investments_Pool_0xt = (510 , 610 , 20 , 20 , 0 , 0 , 0 , 0)
Investments_Farm_0xt = [95 , 0 , 0 , 30 , 20 , 0 , 0 , 180]
Investments_Brow_0xt = [95 , 0 , 0 , 30 , 20 , 0 , 0 , 160]
Investments_NFT__0xt = [95 , 0 , 0 , 20 , 10 , 0 , 0 , 160]

# ____________0x0 Plan - 1_________________
Investments_Pool_0x0_1 = [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0]
Investments_Farm_0x0_1 = [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0]
Investments_Brow_0x0_1 = [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0]
Investments_NFT__0x0_1 = [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0]

# ______________Overall Total________________
Total_Pool_Investments = sum(Investments_Pool_0xt) + sum(Investments_Pool_0x0_1)
Total_Farm_Investments = sum(Investments_Farm_0xt) + sum(Investments_Farm_0x0_1)
Total_Brow_Investments = sum(Investments_Brow_0xt) + sum(Investments_Brow_0x0_1)
Total_NFT__Investments = sum(Investments_NFT__0xt) + sum(Investments_NFT__0x0_1)

# ______________FerroFy Total________________
Total_FerroFy_Investments = Total_Pool_Investments + Total_Farm_Investments + Total_Brow_Investments + Total_NFT__Investments

# _____________Live Collecting_______________
Live_Pool_Investments = "Will Start Soon Stay Tuned :)"
Live_Farm_Investments = sum(Investments_Farm_0xt)
Live_Brow_Investments = sum(Investments_Brow_0xt)
Live_NFT__Investments = sum(Investments_NFT__0xt)

# ________________Total VPX__________________
VPX_Total_Investments = Investments_Pool_0xt[0] + Investments_Farm_0xt[0] + Investments_Brow_0xt[0] + Investments_NFT__0xt[0] + Investments_Pool_0x0_1[0] + Investments_Farm_0x0_1[0] + Investments_Brow_0x0_1[0] + Investments_NFT__0x0_1[0]
VPX_Total_Live_Investments = Investments_Farm_0xt[0] + Investments_Brow_0xt[0] + Investments_NFT__0xt[0] ####################################################################################################################################
VPX_Total_Pool_Investments = Investments_Pool_0xt[0] + Investments_Pool_0x0_1[0]
VPX_Total_Farm_Investments = Investments_Farm_0xt[0] + Investments_Farm_0x0_1[0]
VPX_Total_Brow_Investments = Investments_Brow_0xt[0] + Investments_Brow_0x0_1[0]
VPX_Total_NFT__Investments = Investments_NFT__0xt[0] + Investments_NFT__0x0_1[0]

# _______________Total Tanav_________________
Tanav_Total_Investments = Investments_Pool_0xt[1] + Investments_Farm_0xt[1] + Investments_Brow_0xt[1] + Investments_NFT__0xt[1] + Investments_Pool_0x0_1[1] + Investments_Farm_0x0_1[1] + Investments_Brow_0x0_1[1] + Investments_NFT__0x0_1[1]
Tanav_Total_Live_Investments = Investments_Farm_0xt[1] + Investments_Brow_0xt[1] + Investments_NFT__0xt[1] ####################################################################################################################################
Tanav_Total_Pool_Investments = Investments_Pool_0xt[1] + Investments_Pool_0x0_1[1]
Tanav_Total_Farm_Investments = Investments_Farm_0xt[1] + Investments_Farm_0x0_1[1]
Tanav_Total_Brow_Investments = Investments_Brow_0xt[1] + Investments_Brow_0x0_1[1]
Tanav_Total_NFT__Investments = Investments_NFT__0xt[1] + Investments_NFT__0x0_1[1]

# ________________Total KMX__________________
KMX_Total_Investments = Investments_Pool_0xt[2] + Investments_Farm_0xt[2] + Investments_Brow_0xt[2] + Investments_NFT__0xt[2] + Investments_Pool_0x0_1[2] + Investments_Farm_0x0_1[2] + Investments_Brow_0x0_1[2] + Investments_NFT__0x0_1[2]
KMX_Total_Live_Investments = Investments_Farm_0xt[2] + Investments_Brow_0xt[2] + Investments_NFT__0xt[2] ####################################################################################################################################
KMX_Total_Pool_Investments = Investments_Pool_0xt[2] + Investments_Pool_0x0_1[2]
KMX_Total_Farm_Investments = Investments_Farm_0xt[2] + Investments_Farm_0x0_1[2]
KMX_Total_Brow_Investments = Investments_Brow_0xt[2] + Investments_Brow_0x0_1[2]
KMX_Total_NFT__Investments = Investments_NFT__0xt[2] + Investments_NFT__0x0_1[2]

# ________________Total AKX__________________
AKX_Total_Investments = Investments_Pool_0xt[3] + Investments_Farm_0xt[3] + Investments_Brow_0xt[3] + Investments_NFT__0xt[3] + Investments_Pool_0x0_1[3] + Investments_Farm_0x0_1[3] + Investments_Brow_0x0_1[3] + Investments_NFT__0x0_1[3]
AKX_Total_Live_Investments = Investments_Farm_0xt[3] + Investments_Brow_0xt[3] + Investments_NFT__0xt[3] ####################################################################################################################################
AKX_Total_Pool_Investments = Investments_Pool_0xt[3] + Investments_Pool_0x0_1[3]
AKX_Total_Farm_Investments = Investments_Farm_0xt[3] + Investments_Farm_0x0_1[3]
AKX_Total_Brow_Investments = Investments_Brow_0xt[3] + Investments_Brow_0x0_1[3]
AKX_Total_NFT__Investments = Investments_NFT__0xt[3] + Investments_NFT__0x0_1[3]

# ________________Total Angel__________________
Angel_Total_Investments = Investments_Pool_0xt[4] + Investments_Farm_0xt[4] + Investments_Brow_0xt[4] + Investments_NFT__0xt[4] + Investments_Pool_0x0_1[4] + Investments_Farm_0x0_1[4] + Investments_Brow_0x0_1[4] + Investments_NFT__0x0_1[4]
Angel_Total_Live_Investments = Investments_Farm_0xt[4] + Investments_Brow_0xt[4] + Investments_NFT__0xt[4] ####################################################################################################################################
Angel_Total_Pool_Investments = Investments_Pool_0xt[4] + Investments_Pool_0x0_1[4]
Angel_Total_Farm_Investments = Investments_Farm_0xt[4] + Investments_Farm_0x0_1[4]
Angel_Total_Brow_Investments = Investments_Brow_0xt[4] + Investments_Brow_0x0_1[4]
Angel_Total_NFT__Investments = Investments_NFT__0xt[4] + Investments_NFT__0x0_1[4]

# ________________Total UCI__________________
UCI_Total_Investments = Investments_Pool_0xt[5] + Investments_Farm_0xt[5] + Investments_Brow_0xt[5] + Investments_NFT__0xt[5] + Investments_Pool_0x0_1[5] + Investments_Farm_0x0_1[5] + Investments_Brow_0x0_1[5] + Investments_NFT__0x0_1[5]
UCI_Total_Live_Investments = Investments_Farm_0xt[5] + Investments_Brow_0xt[5] + Investments_NFT__0xt[5] ####################################################################################################################################
UCI_Total_Pool_Investments = Investments_Pool_0xt[5] + Investments_Pool_0x0_1[5]
UCI_Total_Farm_Investments = Investments_Farm_0xt[5] + Investments_Farm_0x0_1[5]
UCI_Total_Brow_Investments = Investments_Brow_0xt[5] + Investments_Brow_0x0_1[5]
UCI_Total_NFT__Investments = Investments_NFT__0xt[5] + Investments_NFT__0x0_1[5]

# ________________Total SSX__________________
SSX_Total_Investments = Investments_Pool_0xt[6] + Investments_Farm_0xt[6] + Investments_Brow_0xt[6] + Investments_NFT__0xt[6] + Investments_Pool_0x0_1[6] + Investments_Farm_0x0_1[6] + Investments_Brow_0x0_1[6] + Investments_NFT__0x0_1[6]
SSX_Total_Live_Investments = Investments_Farm_0xt[6] + Investments_Brow_0xt[6] + Investments_NFT__0xt[6] ####################################################################################################################################
SSX_Total_Pool_Investments = Investments_Pool_0xt[6] + Investments_Pool_0x0_1[6]
SSX_Total_Farm_Investments = Investments_Farm_0xt[6] + Investments_Farm_0x0_1[6]
SSX_Total_Brow_Investments = Investments_Brow_0xt[6] + Investments_Brow_0x0_1[6]
SSX_Total_NFT__Investments = Investments_NFT__0xt[6] + Investments_NFT__0x0_1[6]

# ________________Total PPX__________________
PPX_Total_Investments = Investments_Pool_0xt[7] + Investments_Farm_0xt[7] + Investments_Brow_0xt[7] + Investments_NFT__0xt[7] + Investments_Pool_0x0_1[7] + Investments_Farm_0x0_1[7] + Investments_Brow_0x0_1[7] + Investments_NFT__0x0_1[7]
PPX_Total_Live_Investments = Investments_Farm_0xt[7] + Investments_Brow_0xt[7] + Investments_NFT__0xt[7] ####################################################################################################################################
PPX_Total_Pool_Investments = Investments_Pool_0xt[7] + Investments_Pool_0x0_1[7]
PPX_Total_Farm_Investments = Investments_Farm_0xt[7] + Investments_Farm_0x0_1[7]
PPX_Total_Brow_Investments = Investments_Brow_0xt[7] + Investments_Brow_0x0_1[7]
PPX_Total_NFT__Investments = Investments_NFT__0xt[7] + Investments_NFT__0x0_1[7]

time.sleep(2)
print("No Errors Found In Code")
