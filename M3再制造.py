print("""——--—M3再制造标签——--——""")
print(""" ┌————————————————————┐  """)
print(""" │▉▉            10% │      """)
print(""" └————————————————————┘  """)
print("""^^^^^^^^^^^^^^^^^^^\n""")
import datetime
daytime = datetime.datetime.now().strftime('%d/%m/20%y')
print(daytime)
YN = ("请输入时间月/日/年: ")
SN = input("请输入SN:")
PN = input("请输入PN:")
QN = "REMAN"
WN = "再制造"	
TN = input("请输入条形码:")
CUN = input("""请输入CHINA\\USA:""")
RAWD = input("""请输入E1P\E3\E12和RWD\AWD:""")
CAC = input("请输入CAC:")

f = open(r'C:\Users\xinglyang\Desktop\M3再制造\XIAJIA.txt','tw')
print("""^XA\n\
^CI28\n\
^CW1,E:ANMDS.TTF^FS\n\
^PW812\n\
^LL0406\n\
^FO680,50^A1N,120,105^FWR,0^FD{}^FS\n\
^FO500,50^A0N,120,105^FWR,0^FD^FS\n\
^FO350,50^A0N,120,105^FWR,0^FDPN:{}^FS\n\
^FO200,50^A0N,120,105^FWR,0^FDSN:{}^FS\n\
^FO50,50^A1N,120,105^FWR,0^FD状态信息:{}^FS\n\
^PQ2,0,1,Y^XZ""".format(QN,PN,SN,WN),file=f)
print("已保存至M3再制造\XIAJIA.txt中")
f.close()
f = open(r'C:\Users\xinglyang\Desktop\M3再制造\BAI.txt','tw')
print("""^XA^JUS^MNW^MTT^PON^PMN^LH0,0^JMA^PR2,2~SD35^JUS^LRN^CI0^XZ\n\
^XA^MMT^PW905^LL0406^JUS\n\
^FO32,16^GFA,01792,01792,00028,:Z64:eJzt0kEOwiAQBdAhLLp05bpHwUt07VHkaD1KjzBLFkblMwxapE00cSU/TQM8SIdJiXp6qph7jB/iK9CIoQlx1cYRZ7NNo2KcjGpLpxfYTcyIXbCAHTPsKiZzLIS0w2PI2RzmRMOiNY+YiuX8zE4xG7bRl2L8hZWerfsptWjPGufQI6LjNJ0b9ryiGOOpjXZs79xnJv+Z1d+DX01qPqT7oQ3vNjZNeubU5lUtqWdOv+fVev4wDx3NEl0=:2A19
^BY100,100^FT101,268^BXN,5,200,0,0,1,~\n\
^FH\^FDP{}:S{}^FS\n\
^FT31,118^A0N,22,22^FH\ ^FD(S) TESLA SERIAL NUMBER ^FS   ^FT31,298^A0N,22,22^FH\ ^FD(P) TESLA PART NUMBER ^FS ^FS\n\
^FT76,88^A0N,24,24^FH\ ^FDMADE IN {}^FS\n\
^FT26,153^A0N,32,32^FH\ ^FD{}^FS\n\
^FT26,333^A0N,32,32^FH\ ^FD{}^FS\n\
^FT26,364^A0N,26,26^FH\ ^FD ASY,HVBAT ^FS\n\
^FT171,364^A0N,26,26^FH\ ^FD{}^FS\n\
^FT670,364^A0N,26,26^FH\ ^FD{}^FS\n\
^FT26,390^A0N,26,26^FH\ ^FD 400VDC ^FS\n\
^FT171,390^A0N,26,26^FH\ ^FD3PH,M3Y,RMN  Remanufacturing^FS\n\
^FT550,390^A0N,26,40^FH\ ^FDCAC:^FS\n\
^FT630,390^A0N,28,40^FH\ ^FD{} ah^FS\n\
^FO258,46^GFA,23040,23040,00072,:Z64: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:A73F
^FS^PQ2,0,1,Y^XZ""".format(PN,SN,CUN,SN,PN,RAWD,daytime,CAC),file=f)
print("已保存至M3再制造\BAI.txt中")
f.close()
f = open(r'C:\Users\xinglyang\Desktop\M3再制造\XIAO.txt','tw')
print("""^FX ###Found in https://stash.teslamotors.com/projects/M3BPPE/repos/pack-labels/browse\n\
^FX ### To be printed on 38.1x50.8 mm labels\n\
^XA~TA000~JSN\n\
^JUS^MNW^MTT^PON^PMN^LH0,0^JMA^PR2,2~SD35^JUS^LRN^CI0^XZ^XA^MMT^PW905^LL0406^JUS\n\
^FX ###TESLALOGO\n\
^FO30,0^GFA,01792,01792,00028,:Z64:eJzt0kEOwiAQBdAhLLp05bpHwUt07VHkaD1KjzBLFkblMwxapE00cSU/TQM8SIdJiXp6qph7jB/iK9CIoQlx1cYRZ7NNo2KcjGpLpxfYTcyIXbCAHTPsKiZzLIS0w2PI2RzmRMOiNY+YiuX8zE4xG7bRl2L8hZWerfsptWjPGufQI6LjNJ0b9ryiGOOpjXZs79xnJv+Z1d+DX01qPqT7oQ3vNjZNeubU5lUtqWdOv+fVev4wDx3NEl0=:2A19^BY100,100\n\
^FX ###QR Code\n\
^FT100,250^BXN,5,200,0,0,1,~^FH\\^FDP{}:S{}^FS\n\
^FX ###Code128Bar Code\n\
^FT15,370^A0N,22,22^BY1^BCN,80,Y,N,N,A\n\
^FH\\^FD{}^FS\n\
^FX ###Setting up fixed titles\n\
^FT90,70^A0N,22,22^FH\\^FDMADE IN {}^FS\n\
^FT50,100^A0N,25,25^FH\\^FD(S)^FS\n\
^FT50,130^A0N,25,25^FH\\^FD(P)^FS\n\
^FT10,175^A0N,28,28^FH\\^FDSTYLE:^FS\n\
^FT210,195^A0N,29,29^FH\\^FDHVBAT^FS\n\
^FT30,280^A0N,22,22^FH\\^FDGB/T 34014 COMPLIANT:^FS\n\
^FX ###Setting up dynamic human readable\n\
^FT80,100^A0N,25,25^FH\\n\
^FD{}^FS\n\
^FT80,130^A0N,25,25^FH\\n\
^FD{}^FS\n\
^FT205,220^A0N,28,28^FH\\^FD400VDC^FS\n\
^FT230,245^A0N,28,28^FH\\^FD{}^FS\n\
^FX ###Two letter code\n\
^FO0,155^GFA,01152,01152,00012,:Z64:eJztkT1Ow0AQRmdi0FJEmAaJIlJaLoF9CdJzDIrINggkilDR5AyUNEg0LBUdXMEngE1nUOJl1jP7Q0UDHSut9DQ7mnn+DPB/fueMmshlG7k2kW2X8DogmiqOMUVgtSojt9OwINcp54GnTa4jqyBRggoSBW3wa+e02dfJpjuROvFGBiEZ143XjJy1bqxXo7pnDaPeK2jYPvb1IElz3BW5Q5nlWlwgGQtlfWTocf2MklyFixdgRouXrygp2rOLN2DGj6fFO3CimcHuFgrPKyvSqsXlA3CKSuPy3smCSxOv7mBXsz5e3wAnSp3NuYjKBMNpQhCtQmDfec6Gg5x8xal/HMuz452EJwkfcD/Um9ne0f5sGFFa29P1bGtrB4ec6sSDp+L64A+Prv8z/IIJwI88TngL/uh8ASBPgSs=:65A6^FS\n\
^FX ###Print Quantity\n\
^PQ2,0,1,Y^XZ""".format(PN,SN,TN,CUN,SN,PN,RAWD[0:2]),file=f)
print("已保存至M3再制造\XIAO.txt中")
f.close()
print(""" ╭╩╮ ╔════╗╔════╗╔════╗╔════╗╔════╗ """)
print("""(│▉▉▉▉▉▉▉▉  100% ***|||   │ """)
print("""╰⊙═⊙╯╚◎══◎╝╚◎══◎╝╚◎══◎╝╚◎══◎╝╚◎══◎╝""")
print("""———————————请关闭再来————————————""")
input()
