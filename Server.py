# Server
# windows test
import socket
from _thread import *
import pickle
from player import Player
# via cmd -> ipconfig ->IPV4
server = '192.168.43.73'  # "IP" you wil gett an error: use 'IP'
port = 5555  # open port

players=[Player(0,0,50,50,(255,0,0)),Player(255,255,50,50,(0,255,0))]#store player object



def threaded_client(conn, player):
    # conn.send(str.encode("connected"))#validation token
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data  # update player position in the server

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]  # player 0 position
                else:
                    reply = players[1]  # player 1 position
                print("Received  ", data)
                print("Sending  ", reply)
            conn.sendall(pickle.dumps(reply))  # encode data and send it
        except:
            break
    print("Lost connection")
    conn.close


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # type of  connection

try:

    serversocket.bind((server, port))

except  socket.error as e:
    print(str(e))

# max_conn =2
serversocket.listen(2)  # open the port 2 pp  only can connect to the port
print("waiting for connection , Server Sttarted")
current_player = 0
while True:
    (conn, addr) = serversocket.accept()  # accept any connection and sotre the connection and IP adress
    print("connected to :  ", addr)
    start_new_thread(threaded_client, (conn, current_player))
    current_player += 1
    print("current_player :  ",current_player)




