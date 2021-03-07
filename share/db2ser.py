import serial, time
import sqlite3 as sql
from os import system
system("title "+"Database-to-Serial")

COM_PORT = 'COM9'
print(f"Transfer Database > {COM_PORT}")

try:
    conn = sql.connect('./udp_sink.db')
    ser = serial.Serial(COM_PORT, baudrate=3200, timeout=1)
except:
    print("Error!")

while True:
    curr = conn.execute("SELECT id, received from UDP_SINK")
    for row in curr:
        data = row[1]
    ser.write(data)
    print(ser.readline())
