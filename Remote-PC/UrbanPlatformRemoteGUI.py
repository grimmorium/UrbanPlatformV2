import FreeSimpleGUI as sg
from pynput import keyboard
import socket
import time

mode = "R" #tryb default Ride
height = "M" #wysokosc default Middle
keyPressed = "_"

ipAddr = "127.0.0.1"
ipPort = 12000

enableUDP = False

def on_press(key):
    try:
        #print('alphanumeric key {0} pressed'.format(key.char))
        
        keyP = "#"
        fun = "000"
        
        if key.char == 'w':
            keyP = "1"
            fun = "000"
        
        if key.char == 'e':
            keyP = "2"
            fun = "000"
        
        if key.char == 'r':
            keyP = "3"
            fun = "000"
        
        if key.char == 's':
            keyP = "4"
            fun = "000"
        
        if key.char == 'd':
            keyP = "_"
            fun = "000"
        
        if key.char == 'f':
            keyP = "6"
            fun = "000"
        
        if key.char == 'x':
            keyP = "7"
            fun = "000"
        
        if key.char == 'c':
            keyP = "8"
            fun = "000"
        
        if key.char == 'v':
            keyP = "9"
            fun = "000"

        if key.char == '1':
            fun = "001"
        
        if key.char == '2':
            fun = "002"
        
        if key.char == '3':
            fun = "003"
        
        if key.char == '4':
            fun = "004"
        
        if key.char == '5':
            fun = "005"
        
        if key.char == '6':
            fun = "006"
        
        if key.char == '7':
            fun = "007"
        
        if key.char == '8':
            fun = "008"
        
        if key.char == '9':
            fun = "009"
        
        sendUDP(keyP, fun)
        
    except AttributeError:
        print('special key {0} pressed'.format(key))
        #sendUDP()
    

def on_release(key):
    True
    #print("Key released:"+keyPressed)
    #print('{0} released'.format(key))
    #sendUDP()

def sendUDP(_keyP, _fun):
    if enableUDP == True:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_socket.settimeout(1.0)
        message = str.encode(mode + height + _keyP + _fun)
        addr = (ipAddr, ipPort)
        start = time.time()
        client_socket.sendto(message, addr)
        try:
            data, server = client_socket.recvfrom(1024)
            end = time.time()
            elapsed = end - start
            print(f'{data} {elapsed}')
        except socket.timeout:
            print('REQUEST TIMED OUT')


listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

# All the stuff inside your window.
layout = [  [sg.Text("IP:")],[sg.InputText(key='IPit', default_text=ipAddr)], [sg.Text("Port:")], [sg.InputText(key='PORTit', default_text=ipPort)],
            [sg.Button('Connect')],
            [sg.Text("   ")],
            [sg.Text("Mode:  "), sg.Button('Walk'), sg.Button('Ride')],
            [sg.Text("Height:"), sg.Button('Low'), sg.Button('Middle'), sg.Button('High')],
            [sg.Text("   ")],
            [sg.Button("   \\   ", key='1'),sg.Button("   /\   ", key='2'),sg.Button("   /   ", key='3'), sg.Text("   "), sg.Button("001"), sg.Button("002"), sg.Button("003")],
            [sg.Button("  <   ", key='4'),sg.Button("   X   ", key='5'),sg.Button("  >   ", key='6'), sg.Text("  "), sg.Button("004"), sg.Button("005"), sg.Button("006")],
            [sg.Button("   /   ", key='7'),sg.Button("   \/   ", key='8'),sg.Button("   \   ", key='9'), sg.Text("   "), sg.Button("007"), sg.Button("008"), sg.Button("009")]
         ]

sg.set_options(scaling=3)

window = sg.Window('Urban Platform', layout)


# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    
    keyPr = "#"
    fun="000"
    
    if event == 'Connect':
        enableUDP = True
        ipAddr = values["IPit"]
        ipPort = int(values["PORTit"])
        window["IPit"].update(disabled="False")
        window["PORTit"].update(disabled="False")
    
    if event == 'Low':
        height = 'L'
    if event == 'Middle':
        height = 'M'
    if event == 'High':
        height = 'H'
    
    if event == 'Walk':
        mode = 'W'
    if event == 'Ride':
        mode = 'R'
    
    if event == '1':
        keyPr = '1'
    if event == '2':
        keyPr = '2'
    if event == '3':
        keyPr = '3'
    if event == '4':
        keyPr = '4'
    if event == '5':
        keyPr = '_'
    if event == '6':
        keyPr = '6'
    if event == '7':
        keyPr = '7'
    if event == '8':
        keyPr = '8'
    if event == '9':
        keyPr = '9'
    if event == '001':
        fun = '001'
    if event == '002':
        fun = '002'
    if event == '003':
        fun = '003'
    if event == '004':
        fun = '004'
    if event == '005':
        fun = '005'
    if event == '006':
        fun = '006'
    if event == '007':
        fun = '007'
    if event == '008':
        fun = '008'
    if event == '009':
        fun = '009'

    #print(event)
    #print(values)
    
    sendUDP(keyPr, fun)
    
    # if user closes window or clicks cancel
    if event == sg.WIN_CLOSED:
        break
    


window.close()