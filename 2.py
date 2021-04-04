from __future__ import print_function, unicode_literals

from PyInquirer import style_from_dict, Token, prompt, Separator
from pprint import pprint
from pyfiglet import Figlet
from datetime import datetime
import os,json,time
now = datetime.now()

current_time = now.strftime("%H:%M:%S") 
f = Figlet(font='slant')
print(f.renderText('Wifi-Debug')) 
print("Versin 1.0.1             Current Time ="+str(current_time))
# print(os.system('flutter --version'))

style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
    
})
def exicuteAdb(i):
    if i == 'Connected Devices':
        os.system('adb devices')
        
         
    elif i == 'Connect device':

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

                
                 
                

    elif i == 'Disconnect device':
        os.system('adb kill-server')
        print("device disconnected...")
        
    elif i=='Help':
        print()
        print("Connected Devices: Show connected devices\nConnect device: Use for connecting device using wifi-debug\nDisconnect device: It will kill adb tcpip server")
        print()
        
    else:
        print("Wrong input..")
        

questions = [
    {
        'type': 'list',
        'message': '',
        'name': 'Selected Wifi-Debug option:>',
        'choices': [
     
            {
                'name': 'Connected Devices'
            },
            {
                'name': 'Connect device'
            },
            {
                'name': 'Disconnect device'
            },
            {
                'name': 'Quit'
            },
            {
                'name': 'Help'
            },
            
            
        ],
        'validate': lambda answer: 'You must choose at least one topping.' \
            if len(answer) == 0 else True
    }
]


while True:
    print()
    answers = prompt(questions, style=style) 
    i=answers['Selected Wifi-Debug option:>']
    if i=='Quit':
        print("Exiting ...")
        time.sleep(1)
        break
    else:
        exicuteAdb(i)