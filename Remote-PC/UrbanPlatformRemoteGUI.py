import FreeSimpleGUI as sg
from pynput import keyboard
import socket
import time
import os

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
layout_steering = [  [sg.Text("IP:")],[sg.InputText(key='IPit', default_text=ipAddr)], [sg.Text("Port:")], [sg.InputText(key='PORTit', default_text=ipPort)],
            [sg.Button('Connect')],
            [sg.Text("   ")],
            [sg.Text("Mode:  "), sg.Button('Walk'), sg.Button('Ride')],
            [sg.Text("Height:"), sg.Button('Low'), sg.Button('Middle'), sg.Button('High')],
            [sg.Text("   ")],
            [sg.Button("   \\   ", key='1'),sg.Button("   /\   ", key='2'),sg.Button("   /   ", key='3'), sg.Text("   "), sg.Button("001"), sg.Button("002"), sg.Button("003")],
            [sg.Button("  <   ", key='4'),sg.Button("   X   ", key='5'),sg.Button("  >   ", key='6'), sg.Text("  "), sg.Button("004"), sg.Button("005"), sg.Button("006")],
            [sg.Button("   /   ", key='7'),sg.Button("   \/   ", key='8'),sg.Button("   \   ", key='9'), sg.Text("   "), sg.Button("007"), sg.Button("008"), sg.Button("009")]
         ]

textImgPt0  = "   __        __";
textImgPt1  =    "  \ ____ /  ";
textImgPt2  =    "   |    |   ";
textImgPt2a = "      |    |   ";
textImgPt3  =    "___|    |___";
textImgPt4  =    "   |    |   ";
textImgPt4a = "      |    |   ";
textImgPt5  =    "   |____|   ";
textImgPt6  =    "__/      \__";

fnt = ("Courier New", 20)

layout_advanced = [ [sg.Input(s=15, key = 'freeSteps', default_text = '100')],
                    [sg.Text(textImgPt0, font = fnt)],
                    [sg.Button('/\\', key = 'FL1'),sg.Button('U', key = 'FL2'), sg.Text(textImgPt1, font = fnt), sg.Button('/\\', key = 'FR1'),sg.Button('U', key = 'FR2')],
                    [sg.Button('\\/', key = 'FL3'),sg.Button('D', key = 'FL4'), sg.Text(textImgPt2, font = fnt), sg.Button('\\/', key = 'FR3'),sg.Button('D', key = 'FR4')],
                    [sg.Text(textImgPt2a, font = fnt)],
                    [sg.Button('/\\', key = 'ML1'),sg.Button('U', key = 'ML2'), sg.Text(textImgPt3, font = fnt), sg.Button('/\\', key = 'MR1'),sg.Button('U', key = 'MR2')],
                    [sg.Button('\\/', key = 'ML3'),sg.Button('D', key = 'ML4'), sg.Text(textImgPt4, font = fnt), sg.Button('\\/', key = 'MR3'),sg.Button('D', key = 'MR4')],
                    [sg.Text(textImgPt4a, font = fnt)],
                    [sg.Button('/\\', key = 'BL1'),sg.Button('U', key = 'BL2'), sg.Text(textImgPt5, font = fnt), sg.Button('/\\', key = 'BR1'),sg.Button('U', key = 'BR2')],
                    [sg.Button('\\/', key = 'BL3'),sg.Button('D', key = 'BL4'), sg.Text(textImgPt6, font = fnt), sg.Button('\\/', key = 'BR3'),sg.Button('D', key = 'BR4')]
                ]

layout_main = [
                [
                    sg.TabGroup(
                                [[sg.Tab('Steering', layout_steering), sg.Tab('Advanced', layout_advanced)]]
                                )
                ]
            ]

sg.set_options(scaling=2.5)

window = sg.Window('Urban Platform', layout_main)


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
    #tab: advanced
    if event == 'FL1':
        fun = '911'
    if event == 'FL2':
        fun = '912'
    if event == 'FL3':
        fun = '913'
    if event == 'FL4':
        fun = '914'
    if event == 'FR1':
        fun = '921'
    if event == 'FR2':
        fun = '922'
    if event == 'FR3':
        fun = '923'
    if event == 'FR4':
        fun = '924'
        
    if event == 'ML1':
        fun = '931'
    if event == 'ML2':
        fun = '932'
    if event == 'ML3':
        fun = '933'
    if event == 'ML4':
        fun = '934'
    if event == 'MR1':
        fun = '941'
    if event == 'MR2':
        fun = '942'
    if event == 'MR3':
        fun = '943'
    if event == 'MR4':
        fun = '944'
        
    if event == 'BL1':
        fun = '951'
    if event == 'BL2':
        fun = '952'
    if event == 'BL3':
        fun = '953'
    if event == 'BL4':
        fun = '954'
    if event == 'BR1':
        fun = '961'
    if event == 'BR2':
        fun = '962'
    if event == 'BR3':
        fun = '963'
    if event == 'BR4':
        fun = '964'

    #print(event)
    #print(values)
    
    sendUDP(keyPr, fun)
    
    # if user closes window or clicks cancel
    if event == sg.WIN_CLOSED:
        break
    


window.close()