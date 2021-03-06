import cv2, time
import numpy as np
import socket

# Socket Constants 
#=======================================================================================

UDP_IP = "127.0.0.1"
UDP_PORT = 5006

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

# OpenCV Constants 
#=======================================================================================

RED     = (0, 0, 255)
GREEN   = (0, 255, 0)
BLUE    = (255, 0, 0)
ORANGE  = (0, 69, 255)
MAGENTA = (240, 0, 159)

FONT = cv2.FONT_HERSHEY_SIMPLEX

# Functions
#=======================================================================================
def parse(data_string):
    start0 = data_string.find('<')+1
    len0   = data_string[start0:].find(',')
    end0   = start0+len0
    start1 = end0+1
    len1   = data_string[start1:].find('>')
    end1   = start1+len1

    param0 = data_string[start0:end0]
    param1 = data_string[start1:end1]

    return param0, param1


# Main Loop
#=======================================================================================
while True:
    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        break
    try:
        data, addr = sock.recvfrom(128) 
        data_string1 = "".join([chr(asc_d) for asc_d in data])
        # data, addr = sock.recvfrom(1024) 
        # data_string2 = "".join([chr(asc_d) for asc_d in data])
        # param0, param1 = parse(data_string1+data_string2)
        # print(data_string1)
        param0, param1 = parse(data_string1)
        rect_size0 = int(param0)/1023.0*325
        rect_size1 = int(param1)/1023.0*325
    except:
        param0, param1 = "None", "None"    
        rect_size0, rect_size1 = 0, 0

    INTERFACE = np.zeros((200,350,3))
    cv2.putText(INTERFACE, "Received Parameters", (10,55), FONT, 1, RED, 2, cv2.LINE_AA)

    cv2.putText(INTERFACE, "param0 |", (10,98), FONT, 0.6, GREEN, 1, cv2.LINE_AA)
    cv2.putText(INTERFACE, param0, (110,98), FONT, 0.6, GREEN, 1, cv2.LINE_AA)
    cv2.rectangle(INTERFACE, (10,108), (int(11+rect_size0), 120), GREEN, -1)

    cv2.putText(INTERFACE, "param1 |", (10,140), FONT, 0.6, ORANGE, 1, cv2.LINE_AA)
    cv2.putText(INTERFACE, param1, (110,140), FONT, 0.6, ORANGE, 1, cv2.LINE_AA)
    cv2.rectangle(INTERFACE, (10,150), (int(11+rect_size1), 162), ORANGE, -1)

    cv2.imshow("GUI - Receiver", INTERFACE)
