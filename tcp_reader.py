import socket
import threading

HOST = "127.0.0.1"  # IP for local host
PORT = 9971         # Listen port


# new thread
class StartThread(threading.Thread):
    '''New Thread'''

    def __init__(self, clientSocket, addr):
        threading.Thread.__init__(self)
        self.clientSocket = clientSocket
        self.addr = addr

    def run(self):
        print("accept tcp connection from: " + str(self.addr))
        while(True):
            message = self.clientSocket.recv(1024)  # receive message
            if len(message) == 0:
                print("close tcp connection from: " + str(self.addr))
                self.clientSocket.close();
                break;
            print(str(self.addr) + ": ", end = "")  # print
            print(message)      # revert to utf-8: message.decode('utf-8')


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
counter = 0                 # counter for receive
server.bind((HOST, PORT))   # bind port
server.listen(5)            # set max connections
while(True):
    clientSocket, addr = server.accept()
    thread = StartThread(clientSocket, addr)
    thread.start()