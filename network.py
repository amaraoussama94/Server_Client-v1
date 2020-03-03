# connect to th server via socket
import socket
import pickle  #conv buts to object  : serial obj


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = '192.168.43.73'  # same ip of the server in server.py
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()


    def get_p(self):
        return self.p

    def connect(self):#con byts to obj

        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048))
        except:
            pass

    def send(self, data):#conv obj to byts
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(str(e))


