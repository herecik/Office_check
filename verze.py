import os
import socket 

def call_cmd(string):
    print("\nHOST NAME: " + socket.gethostname() + "\n")
    os.system("cmd /k " + string)
    



print("1 - Office 2010 (32-bit) na 32-bitové verzi Windows\n2 - Office 2010 (32-bit) na 64-bitové verzi Windows\n3 - Office 2010 (64-bit) na 64-bitové verzi Windows\n4 - Office 2013 (32-bit) na 32-bitové verzi Windows\n5 - Office 2013 (32-bit) na 64-bitové verzi Windows\n6 - Office 2013 (64-bit) na 64-bitové verzi Windows\n7 - Office 2016/2019 (32-bit) na 32-bitové verzi Windows\n8 - Office 2016/2019 (32-bit) na 64-bitové verzi Windows\n9 - Office 2016/2019 (64-bit) na 64-bitové verzi Windows \n")
x = input("Cislo? ")

if(x == "1"):
    call_cmd('cscript "C:\Program Files\Microsoft Office\Office14\OSPP.VBS" /dstatus')
elif(x == "2"):
    call_cmd('cscript "C:\Program Files (x86)\Microsoft Office\Office14\OSPP.VBS" /dstatus')
elif(x == "3"):
    call_cmd('cscript "C:\Program Files\Microsoft Office\Office14\OSPP.VBS" /dstatus')
elif(x == "4"):
    call_cmd('cscript "C:\Program Files\Microsoft Office\Office15\OSPP.VBS" /dstatus')
elif(x == "5"):
    call_cmd('cscript "C:\Program Files (x86)\Microsoft Office\Office15\OSPP.VBS" /dstatus')
elif(x == "6"):
    call_cmd('cscript "C:\Program Files\Microsoft Office\Office15\OSPP.VBS" /dstatus')
elif(x == "7"):
    call_cmd('cscript "C:\Program Files\Microsoft Office\Office16\OSPP.VBS" /dstatus')
elif(x == "8"):
    call_cmd('cscript "C:\Program Files (x86)\Microsoft Office\Office16\OSPP.VBS" /dstatus')
elif(x == "9"):
    call_cmd('cscript "C:\Program Files\Microsoft Office\Office16\OSPP.VBS" /dstatus')
else:
    print("Vyber pouze cislo 1-9")

