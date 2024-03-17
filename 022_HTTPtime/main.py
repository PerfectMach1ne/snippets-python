# https://bhch.github.io/posts/2017/11/writing-an-http-server-from-scratch/
# I got an urge to HT the TP
import socket


class TCPServer:
    # host = '127.0.0.1'  # server addresss
    # port = 42069  # server port

    def __init__(self, host='127.0.0.1', port=42069) -> None:
        self.host = host
        self.port = port

    def start(self):
        # creates a socket object!
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)

        # bind the socket object to the address and port
        s.bind((self.host, self.port))
        # start listening for connections
        s.listen(5)

        print("Listening at", s.getsockname())

        while True:
            # accept any new connection
            conn, addr = s.accept()

            print("Connected by", addr)

            # read the data sent by the client!
            # this below reads only the first 1024 bytes
            data = conn.recv(4096)

            # send back the data to the client!
            conn.sendall(data)

            # close the connection
            conn.close()


if __name__ == "__main__":
    server = TCPServer()
    server.start()
