# VPX =   0
# Tanav = 1
# KMX =   2
# AKX =   3
# Angel = 4
# UCI =   5
# SSX =   6
# PPX =   7
# ________________________________________
import Investments as Inv

#____________________________________________________________________________________________________________________________________
# Total FerroFy Shares ( Approx 25 % Will Be Distributed To Public )
Total_FerroFy_Investments = Inv.Total_FerroFy_Investments

VPX_Shares_FerroFy   = ( Inv.VPX_Total_Investments / Total_FerroFy_Investments )   * 75
Tanav_Shares_FerroFy = ( Inv.Tanav_Total_Investments / Total_FerroFy_Investments ) * 75
KMX_Shares_FerroFy   = ( Inv.KMX_Total_Investments / Total_FerroFy_Investments )   * 75
AKX_Shares_FerroFy   = ( Inv.AKX_Total_Investments / Total_FerroFy_Investments )   * 75
Angel_Shares_FerroFy = ( Inv.Angel_Total_Investments / Total_FerroFy_Investments ) * 75
UCI_Shares_FerroFy   = ( Inv.UCI_Total_Investments / Total_FerroFy_Investments )   * 75
SSX_Shares_FerroFy   = ( Inv.SSX_Total_Investments / Total_FerroFy_Investments )   * 75
PPX_Shares_FerroFy   = ( Inv.PPX_Total_Investments / Total_FerroFy_Investments )   * 75
FerroFy_Sold_Shares = VPX_Shares_FerroFy + Tanav_Shares_FerroFy + KMX_Shares_FerroFy + AKX_Shares_FerroFy + Angel_Shares_FerroFy + UCI_Shares_FerroFy + SSX_Shares_FerroFy + PPX_Shares_FerroFy
FerroFy_Left_Shares = 100 - FerroFy_Sold_Shares

#____________________________________________________________________________________________________________________________________
#Pool ( Approx 25% Shares Under FerroFy Company )
Total_Pool_Investments = Inv.Total_Pool_Investments
VPX_Shares_Pool   = ( Inv.VPX_Total_Investments / Total_Pool_Investments )   * 75
Tanav_Shares_Pool = ( Inv.Tanav_Total_Investments / Total_Pool_Investments ) * 75
KMX_Shares_Pool   = ( Inv.KMX_Total_Investments / Total_Pool_Investments )   * 75
AKX_Shares_Pool   = ( Inv.AKX_Total_Investments / Total_Pool_Investments )   * 75
Angel_Shares_Pool = ( Inv.Angel_Total_Investments / Total_Pool_Investments ) * 75
UCI_Shares_Pool   = ( Inv.UCI_Total_Investments / Total_Pool_Investments )   * 75
SSX_Shares_Pool   = ( Inv.SSX_Total_Investments / Total_Pool_Investments )   * 75
PPX_Shares_Pool   = ( Inv.PPX_Total_Investments / Total_Pool_Investments )   * 75
Pool_Sold_Shares = VPX_Shares_Pool + Tanav_Shares_Pool + KMX_Shares_Pool + AKX_Shares_Pool + Angel_Shares_Pool + UCI_Shares_Pool + SSX_Shares_Pool + PPX_Shares_Pool
Pool_Left_Shares = 100 - Pool_Sold_Shares

#Farm ( Approx 25% Shares Under FerroFy Company )
Total_Farm_Investments = Inv.Total_Farm_Investments
VPX_Shares_Farm   = ( Inv.VPX_Total_Investments / Total_Farm_Investments )   * 75
Tanav_Shares_Farm = ( Inv.Tanav_Total_Investments / Total_Farm_Investments ) * 75
KMX_Shares_Farm   = ( Inv.KMX_Total_Investments / Total_Farm_Investments )   * 75
AKX_Shares_Farm   = ( Inv.AKX_Total_Investments / Total_Farm_Investments )   * 75
Angel_Shares_Farm = ( Inv.Angel_Total_Investments / Total_Farm_Investments ) * 75
UCI_Shares_Farm   = ( Inv.UCI_Total_Investments / Total_Farm_Investments )   * 75
SSX_Shares_Farm   = ( Inv.SSX_Total_Investments / Total_Farm_Investments )   * 75
PPX_Shares_Farm   = ( Inv.PPX_Total_Investments / Total_Farm_Investments )   * 75
Farm_Sold_Shares = VPX_Shares_Farm + Tanav_Shares_Farm + KMX_Shares_Farm + AKX_Shares_Farm + Angel_Shares_Farm + UCI_Shares_Farm + SSX_Shares_Farm + PPX_Shares_Farm
Farm_Left_Shares = 100 - Farm_Sold_Shares

#____________________________________________________________________________________________________________________________________
Plan_Pool_0xt_Shares   = [ (Inv.Investments_Pool_0xt[0] / Inv.Plan_Pool_Investments_0xt)*100 , (Inv.Investments_Pool_0xt[1] / Inv.Plan_Pool_Investments_0xt)*100 , (Inv.Investments_Pool_0xt[2] / Inv.Plan_Pool_Investments_0xt)*100 , (Inv.Investments_Pool_0xt[3] / Inv.Plan_Pool_Investments_0xt)*100 , (Inv.Investments_Pool_0xt[4] / Inv.Plan_Pool_Investments_0xt)*100 , (Inv.Investments_Pool_0xt[5] / Inv.Plan_Pool_Investments_0xt)*100 , (Inv.Investments_Pool_0xt[6] / Inv.Plan_Pool_Investments_0xt)*100 , (Inv.Investments_Pool_0xt[7] / Inv.Plan_Pool_Investments_0xt)*100 ] 
Plan_Pool_0x0_1_Shares = [ (Inv.Investments_Pool_0x0_1[0] / Inv.Plan_Pool_Investments_0x0_1)*100 , (Inv.Investments_Pool_0x0_1[1] / Inv.Plan_Pool_Investments_0x0_1)*100 , (Inv.Investments_Pool_0x0_1[2] / Inv.Plan_Pool_Investments_0x0_1)*100 , (Inv.Investments_Pool_0x0_1[3] / Inv.Plan_Pool_Investments_0x0_1)*100 , (Inv.Investments_Pool_0x0_1[4] / Inv.Plan_Pool_Investments_0x0_1)*100 , (Inv.Investments_Pool_0x0_1[5] / Inv.Plan_Pool_Investments_0x0_1)*100 , (Inv.Investments_Pool_0x0_1[6] / Inv.Plan_Pool_Investments_0x0_1)*100 , (Inv.Investments_Pool_0x0_1[7] / Inv.Plan_Pool_Investments_0x0_1)*100 ] 
Plan_Farm_0xt_Shares   = [ (Inv.Investments_Farm_0xt[0] / Inv.Plan_Farm_Investments_0xt)*100 , (Inv.Investments_Farm_0xt[1] / Inv.Plan_Farm_Investments_0xt)*100 , (Inv.Investments_Farm_0xt[2] / Inv.Plan_Farm_Investments_0xt)*100 , (Inv.Investments_Farm_0xt[3] / Inv.Plan_Farm_Investments_0xt)*100 , (Inv.Investments_Farm_0xt[4] / Inv.Plan_Farm_Investments_0xt)*100 , (Inv.Investments_Farm_0xt[5] / Inv.Plan_Farm_Investments_0xt)*100 , (Inv.Investments_Farm_0xt[6] / Inv.Plan_Farm_Investments_0xt)*100 , (Inv.Investments_Farm_0xt[7] / Inv.Plan_Farm_Investments_0xt)*100 ] 
Plan_Farm_0x0_1_Shares = [ (Inv.Investments_Farm_0x0_1[0] / Inv.Plan_Farm_Investments_0x0_1)*100 , (Inv.Investments_Farm_0x0_1[1] / Inv.Plan_Farm_Investments_0x0_1)*100 , (Inv.Investments_Farm_0x0_1[2] / Inv.Plan_Farm_Investments_0x0_1)*100 , (Inv.Investments_Farm_0x0_1[3] / Inv.Plan_Farm_Investments_0x0_1)*100 , (Inv.Investments_Farm_0x0_1[4] / Inv.Plan_Farm_Investments_0x0_1)*100 , (Inv.Investments_Farm_0x0_1[5] / Inv.Plan_Farm_Investments_0x0_1)*100 , (Inv.Investments_Farm_0x0_1[6] / Inv.Plan_Farm_Investments_0x0_1)*100 , (Inv.Investments_Farm_0x0_1[7] / Inv.Plan_Farm_Investments_0x0_1)*100 ]
