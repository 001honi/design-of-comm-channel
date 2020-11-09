import socket, serial, time
from os import system
system("title "+"UDP-to-Serial")

UDP_IP = "127.0.0.1"
UDP_PORT = 5006
COM_PORT = 'COM9'

print(f"Transfer {UDP_IP} {UDP_PORT} > {COM_PORT}")

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

ser = serial.Serial(COM_PORT, baudrate=4800, timeout=0)

while True:
    data, addr = sock.recvfrom(128) # buffer size is 1024 bytes
    ser.write(data)
    # print(len(data)) 
    print(ser.readline())
