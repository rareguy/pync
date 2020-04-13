from socket import socket
from time import time,sleep

class Pync:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.sock = socket()
        self.sock.connect((self.ip, self.port))
        
    def receive(self, length=1024):
        """
        Receive data in 'length'-sized blocks
        Default:
        length = 1024 (bytes)
        """
        data = self.sock.recv(length)
        return data.decode()
        
    def receive_until(self, keyword, length=1024):
        """
        Receive data in 'length'sized iteration until it finds the keyword
        Default:
        length = 1024 (bytes)
        """
        buffer = ""
        while not keyword in buffer:
            data = self.sock.recv(length)
            buffer += data.decode()
        
        return buffer
    
    def receive_from(self, keyword, length=1024, junk=False):
        """
        Receive data in 'length'-sized iteration from the keyword until end, useful for waiting signals.
        If junk is set to True, you will also receive the previous data before it finds the keyword
        Default:
        length = 1024 (bytes)
        keyword = None
        junk = False
        Returns:
        buffer, junk
        """
        buffer = ""
        junky = ""
        while not keyword in buffer:
            junk += self.sock.recv(length)
        
        buffer = self.receive_all()
        if junk:
            return buffer, junky  
        return buffer
        
    def receive_all(self, timeout=2, length=1024):
        """
        Receive all data that can be accepted with 'timeout' idle time
        Default:
        timeout = 2 (seconds)
        length = 1024 (bytes)
        """
        buffer = ""
        self.sock.setblocking(0)
        datacount = 0
        begin=time()
        while True:
            if datacount and time() - begin > timeout:
                break
            elif time() - begin > timeout:
                return "no data"
            try:
                data=self.sock.recv(length)
                if data:
                    buffer += data
                    begin = time()
                    datacount += 1
                else:
                    sleep(0.1)
            except:
                pass
            
        return buffer
    
    def send(self, data="\n"):
        """
        Well, it sends... data
        Default:
        data = "\n"
        """
        self.sock.send(data.encode())
    
    def send_all(self, data):
        """
        It sends data until it breaks or it's done.
        Just using basic "sendall" from python3
        """
        self.sock.sendall(data.encode())
    
    def close(self):
        self.sock.close()