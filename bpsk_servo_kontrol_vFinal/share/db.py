import socket
import sqlite3 as sql
import time
from os import system
system("title "+"UDP-to-Database")

# CREATE DATABASE & TABLE
#=======================================================================================
conn = sql.connect('./udp_sink.db')
curr = conn.cursor()

table = """CREATE TABLE IF NOT EXISTS UDP_SINK
(id, received)"""
curr.execute(table)
conn.commit()

# RESET
#=======================================================================================
curr.execute("""DELETE FROM UDP_SINK""")
conn.commit()
curr.execute("""INSERT INTO UDP_SINK VALUES 
(?,?)""", (1,0))
conn.commit()

# UDP CONNECTION
#=======================================================================================
UDP_IP = "127.0.0.1"
UDP_PORT = 5006

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

print("Transferring UDP Sink to Database...")
while True:
    data, addr = sock.recvfrom(128) 
    data = (data,)
    query = """Update UDP_SINK set received = ? where id = 1"""
    curr.execute(query, data)
    conn.commit()
    time.sleep(0.001) # 5ms delay
