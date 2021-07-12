print("""————————M3正常标签————————""")
print("""  ...╭ ╯╭ ╯╭ ╯""")
print(""". ╭╩═╮.╔════╗╔════╗╔════╗╔════╗   """)
print("""╭╯嘟嘟  ~~❏❏❏❏ ╠╣~~❏❏❏╠╣❏❏❏ ╠╣~❏❏❏❏~╟""")
print("""╰⊙═⊙╯╚⊙═⊙╝╚⊙═⊙╝╚⊙═⊙╝ ╚⊙═⊙╝\n""")

print(""" ╭╩══╮╔══════╗╔══════╗╔═══════╗ """)
print("""╭╯嘟嘟嘟╠╣不要跑╠╣对面的╠╣看我不撞死你们╣""")
print("""╰⊙══⊙╯╚◎════◎╝╚◎════◎╝╚◎═════◎╝\n""")

SN = input("请输入SN:")
PN = input("请输入PN:")
VIN = input("请输入VIN:")
QN = input("请输入发运地址:")
WN = input("请输入状态信息(已修复\再制造):")
TN = input("请输入条形码:")
CUN = input("""请输入CHINA\\USA:""")
RBN = input("""请输入RD\8B\8H:""")
RAWD = input("""请输入E1P\E3\E12和RWD\AWD:""")

f = open(r'C:\Users\xinglyang\Desktop\MUBAN\BAI.zpl','tw')
print("""^XA^JUS^MNW^MTT^PON^PMN^LH0,0^JMA^PR6,6~SD35^JUS^LRN^CI0^XZ\n\
^XA^MMT^PW905^LL0406^JUS\n\
^FO32,16^GFA,01792,01792,00028,:Z64:eJzt0kEOwiAQBdAhLLp05bpHwUt07VHkaD1KjzBLFkblMwxapE00cSU/TQM8SIdJiXp6qph7jB/iK9CIoQlx1cYRZ7NNo2KcjGpLpxfYTcyIXbCAHTPsKiZzLIS0w2PI2RzmRMOiNY+YiuX8zE4xG7bRl2L8hZWerfsptWjPGufQI6LjNJ0b9ryiGOOpjXZs79xnJv+Z1d+DX01qPqT7oQ3vNjZNeubU5lUtqWdOv+fVev4wDx3NEl0=:2A19^BY100,100^FT101,268^BXN,5,200,0,0,1,~\n\
^FH\^FDP{}:S{}^FS\n\
^FT96,88^A0N,24,24^FH\ ^FDMADE IN {}^FS\n\
^FT26,153^A0N,32,32^FH\ ^FD{}^FS\n\
^FT26,333^A0N,32,32^FH\ ^FD{}^FS\n\
^CF0,420^FO280,45 ^FD{}^FS\n\
^FT171,364^A0N,26,26^FH\ ^FD{}^FS\n\
^FT26,390^A0N,26,26^FH\ ^FD 400VDC ^FS\n\
^FT171,390^A0N,26,26^FH\ ^FD3PH, M3 ^FS\n\
^FT26,364^A0N,26,26^FH\ ^FD ASY,HVBAT^FS\n\
^FT31,118^A0N,22,22^FH\ ^FD(S) TESLA SERIAL NUMBER ^FS\n\
^FT31,298^A0N,22,22^FH\ ^FD(P) TESLA PART NUMBER ^FS ^FS\n\
^PQ2,0,1,Y\n\
^XZ""".format(PN,SN,CUN,SN,PN,RBN,RAWD),file=f)
print("已保存至BAI.zpl中")
f.close()

f = open(r'C:\Users\xinglyang\Desktop\MUBAN\XIAJIA.zpl','tw')
print("""^XA\n\
^CI28\n\
^CW1,E:ANMDS.TTF^FS\n\
^PW812\n\
^LL0406\n\
^FO680,50^A1N,120,105^FWR,0^FD{}^FS\n\
^FO500,50^A0N,120,105^FWR,0^FDVIN:{}^FS\n\
^FO350,50^A0N,120,105^FWR,0^FDPN:{}^FS\n\
^FO200,50^A0N,120,105^FWR,0^FDSN:{}^FS\n\
^FO50,50^A1N,120,105^FWR,0^FD状态信息:{}^FS\n\
^PQ2,0,1,Y^XZ""".format(QN,VIN,PN,SN,WN),file=f)
print("已保存至XIAJIA.zpl中")
f.close()

f = open(r'C:\Users\xinglyang\Desktop\MUBAN\XIAO.zpl','tw')
print("^FX ###Found in https://stash.teslamotors.com/projects/M3BPPE/repos/pack-labels/browse\n\
^FX ### To be printed on 38.1x50.8 mm labels\n\
^XA~\n\
TA000~JSN\n\
^JUS^MNW^MTT^PON^PMN^LH0,0^JMA^PR2,2~SD35^JUS^LRN^CI0^XZ^XA^MMT^PW905^LL0406^JUS\n\
^FX ###TESLA LOGO\n\
^FO30,0^GFA,01792,01792,00028,:Z64:eJzt0kEOwiAQBdAhLLp05bpHwUt07VHkaD1KjzBLFkblMwxapE00cSU/TQM8SIdJiXp6qph7jB/iK9CIoQlx1cYRZ7NNo2KcjGpLpxfYTcyIXbCAHTPsKiZzLIS0w2PI2RzmRMOiNY+YiuX8zE4xG7bRl2L8hZWerfsptWjPGufQI6LjNJ0b9ryiGOOpjXZs79xnJv+Z1d+DX01qPqT7oQ3vNjZNeubU5lUtqWdOv+fVev4wDx3NEl0=:2A19^BY100,100\n\
^FX ###QR Code\n\
^FT100,250^BXN,5,200,0,0,1,~\n\
^FH\^FDP{}:S{}^FS\n\
^FX ###Code 128 Bar Code\n\
^FT15,370^A0N,22,22^BY1^BCN,80,Y,N,N,A\n\
^FH\^FD{}^FS\n\
^FX ###Setting up fixed titles\n\
^FT90,70^A0N,22,22^FH\^FDMADE IN {}^FSreadable\n\
^FT80,100^A0N,25,25^FH\n\
^FD{}^FS\n\
^FT80,130^A0N,25,25^FH\n\
^FD{}^FS\n\
^FT230,245^A0N,28,28^FH\n\
^FD{}^FS\n\
^FX ###Two letter code\n\
^FO15,195^A0N,60,60\n\
^FD{}^FS\n\
^FT50,100^A0N,25,25^FH\\^FD(S)^FS\n\
^FT50,130^A0N,25,25^FH\\^FD(P)^FS\n\
^FT10,175^A0N,28,28^FH\\^FDSTYLE:^FS\n\
^FT210,195^A0N,29,29^FH\\^FDHVBAT^FS\n\
^FT30,280^A0N,22,22^FH\\^FDGB/T 34014 COMPLIANT:^FS\n\
^FX ###Setting up dynamic human\n\
^FT205,220^A0N,28,28^FH\\^FD400VDC^FS\n\
^FX ###Print Quantity\n\
^PQ2,0,1,Y^XZ".format(PN,SN,TN,CUN,SN,PN,RAWD[0:2],RBN,),file=f)
print("已保存至XIAO.zpl中")
f.close()
print(""" ╭╩╮ ╔════╗╔════╗╔════╗╔════╗╔════╗   """)
print("""╭╯GO╠╣      ╠╣比心  ╠╣爱你   ╠╣爱     ╠╣            """)
print("""╰⊙═⊙╯╚◎══◎╝╚◎══◎╝╚◎══◎╝╚◎══◎╝╚◎══◎╝""")
print("""—————————————————————————""")
input()