import os
import time
from pyfiglet import Figlet

import json
f = Figlet(font='slant')
print(f.renderText('Wifidebug')) 
print(os.system('flutter --version'))
print("Select options:\n1:List connected devices\n2:Connect device\n3:Disconnect device\n4:Quit\n5:Help")
def exicuteAdb(i):
    if i == 1:
        os.system('adb devices')
        
         
    elif i == 2:

        with open('data.json', 'r+') as f:
            data = json.load(f)
            print(os.system('adb devices'))
            if data['ip'] == '' and data['port'] == '':
                port = input("Enter Port number:")
                ip = input("Enter ip address:")
                d = {'ip': ip, 'port': port}

                try:

                    data['ip'] = ip
                    data['port'] = port
                    f.seek(0)
                    json.dump(d, f)
                except:
                    print("Something went wrong")
                os.system('adb kill-server')
                os.system('adb tcpip '+port)
                os.system('adb connect '+ip)
                
                 
            else:
                q1 = input("Do You want to use port number:" +
                        data['port']+" as defult,Press Y for yes:")
                print(q1.upper())
                if q1.upper() == 'Y':
                    port = data['port']
                else:
                    port = input("Enter Port number:")
                q2 = input("Do your phone ip is "+data["ip"]+",Press Y for yes:")
                if q2.upper() == 'Y':
                    ip = data['ip']
                else:
                    ip = input("Enter ip address:")

                d = {'ip': ip, 'port': port}

                try:

                    data['ip'] = ip
                    data['port'] = port
                    f.seek(0)
                    json.dump(d, f)
                except:
                    print("Something went wrong")
                os.system('adb kill-server')
                os.system('adb tcpip '+port)
                os.system('adb connect '+ip)

                
                 
                

    elif i == 3:
        os.system('adb kill-server')
        print("device disconnected...")
        
         
    elif i==4:
        print("Exiting ...")
        
        
        exit
    elif i==5:
        print("1:List connected devices\n2:Connect device\n3:Disconnect device\n4:Quit")
        
        
    else:
        print("Wrong input..")
        

while True:
    i=int(input(">>>"))
    if i==4:
        print("Exiting ...")
        time.sleep(1)
        break
        exit1
    else:
        exicuteAdb(i)
