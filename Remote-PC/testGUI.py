import tkinter as tk
import socket
import time

mode = "R" #tryb default Ride
height = "M" #wysokosc default Middle
keyPressed = "_"

ipAddr = "192.168.1.74"
ipPort = 12000

enableUDP = False


def on_press(key):
    print("in on_press(c)")
    #try:
        #print('alphanumeric key {0} pressed'.format(key.char)
    if True:
        keyP = "#"
        fun = "000"
        print('2' + keyP +' ' +  fun)
        
        if key.upper() == 'W':
            keyP = "1"
            fun = "000"
        
        if key.upper() == 'E':
            keyP = "2"
            fun = "000"
        
        if key.upper() == 'R':
            keyP = "3"
            fun = "000"
        
        if key.upper() == 'S':
            keyP = "4"
            fun = "000"
        
        if key.upper() == 'D':
            keyP = "_"
            fun = "000"
        
        if key.upper() == 'F':
            keyP = "6"
            fun = "000"
        
        if key.upper() == 'X':
            keyP = "7"
            fun = "000"
        
        if key.upper() == 'C':
            keyP = "8"
            fun = "000"
        
        if key.upper() == 'V':
            keyP = "9"
            fun = "000"

        if key.upper() == '1':
            keyP = "_"
            fun = "001"
        
        if key.upper() == '2':
            keyP = "_"
            fun = "002"
        
        if key.upper() == '3':
            keyP = "_"
            fun = "003"
        
        if key.upper() == '4':
            keyP = "_"
            fun = "004"
        
        if key.upper() == '5':
            keyP = "_"
            fun = "005"
        
        if key.upper() == '6':
            keyP = "_"
            fun = "006"
        
        if key.upper() == '7':
            keyP = "_"
            fun = "007"
        
        if key.upper() == '8':
            keyP = "_"
            fun = "008"
        
        if key.upper() == '9':
            keyP = "_"
            fun = "009"
        
        print('3' + keyP +' ' +  fun)
        
        sendUDP(keyP, fun, True)
        
    #except AttributeError:
    #    print('special key {0} pressed'.format(key))
    #    #sendUDP()

def sendUDP(_keyP, _fun, _enableUDP):
    print("in sendUDP enableUDP " + str(_enableUDP))
    if _enableUDP == True:
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

# Function to toggle the state of IP and PORT entry fields
def toggle_entries():
    state = 'readonly' if block_var.get() else 'normal'
    ip_entry.config(state=state)
    port_entry.config(state=state)
    if(state == 'readonly'):
        enableUDP = False
    else:
        enableUDP = True

# Function to handle button click events
def button_clicked(button_name):
    print(f"Button pressed: {button_name}")
    
    if(button_name=="Connect"):
        ip_entry.config(state='readonly')
        port_entry.config(state='readonly')
        enableUDP = True
    sendUDP('#', "000", True)
    
    on_press(button_name)

# Function to handle keyboard press events
def key_pressed(event):
    c = event.keysym
    #print(f"Key pressed: {event.keysym}")
    if event.keysym.isdigit():
        #print(f"Numerical key pressed: {event.keysym}")
        c = event.keysym
    
    on_press(c)
    
# Initialize the main window
root = tk.Tk()
root.tk.call('tk','scaling',3.0)

root.title("GUI Layout")

# Frame 1
frame1 = tk.Frame(root)
frame1.grid(row=0, column=0, sticky='ew', pady=(0, 10))  # Added padding for the blank row
tk.Label(frame1, text="IP:").grid(row=0, column=0)
ip_entry = tk.Entry(frame1)
ip_entry.insert(0, ipAddr)
ip_entry.grid(row=0, column=1)
tk.Label(frame1, text="Port:").grid(row=0, column=2)
port_entry = tk.Entry(frame1)
port_entry.insert(0, ipPort)
port_entry.grid(row=0, column=3)
tk.Label(frame1, text="    ").grid(row=1, column=0)
connect_button = tk.Button(frame1, text="Connect", command=lambda: button_clicked('Connect'))
connect_button.grid(row=1, column=1)
block_var = tk.BooleanVar()
block_check = tk.Checkbutton(frame1, text="Block", variable=block_var, command=toggle_entries)
block_check.grid(row=1, column=2)

# Frame 2
frame2 = tk.Frame(root)
frame2.grid(row=2, column=0, sticky='ew', pady=(0, 10))  # Added padding for the blank row
tk.Label(frame2, text="Mode:  ").grid(row=0, column=0)
walk_button = tk.Button(frame2, text="Walk", command=lambda: button_clicked('Walk'))
walk_button.grid(row=0, column=1)
ride_button = tk.Button(frame2, text="Ride", command=lambda: button_clicked('Ride'))
ride_button.grid(row=0, column=2)
tk.Label(frame2, text="Height:").grid(row=1, column=0)
low_button = tk.Button(frame2, text="Low", command=lambda: button_clicked('Low'))
low_button.grid(row=1, column=1)
middle_button = tk.Button(frame2, text="Middle", command=lambda: button_clicked('Middle'))
middle_button.grid(row=1, column=2)
high_button = tk.Button(frame2, text="High", command=lambda: button_clicked('High'))
high_button.grid(row=1, column=3)

# Frame 3
frame3 = tk.Frame(root)
frame3.grid(row=4, column=0, sticky='ew')
buttons = [
    ("   \\   ", 0, 0), ("   /\\   ", 0, 1), ("   /   ", 0, 2),
    ("  <   ", 1, 0), ("   X   ", 1, 1), ("  >   ", 1, 2),
    ("   /   ", 2, 0), ("   \\/   ", 2, 1), ("   \\   ", 2, 2)
]
for text, row, col in buttons:
    button = tk.Button(frame3, text=text, command=lambda b=text: button_clicked(b.strip()))
    button.grid(row=row, column=col)

numbers = ["001", "002", "003", "004", "005", "006", "007", "008", "009"]
for index, number in enumerate(numbers):
    button = tk.Button(frame3, text=number, command=lambda n=number: button_clicked(n))
    button.grid(row=index//3, column=4+index%3)

# Bind the key press event
root.bind('<KeyPress>', key_pressed)

# Start the main loop
root.mainloop()
