import socket, serial
from os import system
system("title "+"Serial-to-UDP")

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
COM_PORT = 'COM10'

print(f"Transfer {COM_PORT} > {UDP_IP} {UDP_PORT}")
  
sock = socket.socket(socket.AF_INET, # Internet
                       socket.SOCK_DGRAM) # UDP

ser = serial.Serial(COM_PORT, baudrate=2400, timeout=None)

while True:
    MESSAGE = ser.read(21)
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    print(MESSAGE)