import gevent
from gevent import monkey

monkey.patch_all()  # identify the waiting time and let the process switch
import socket
import re
import base64
import sys
import Matching
import Multitask_predict
import os
import account


class HTTPServer(object):

    def __init__(self, port):
        """Complete initialization of instance object"""
        # Create sockets, specify IP and datagram types
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Setting Port Multiplexing
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # Setting bindings, listening, receiving links
        server_socket.bind(("", port))
        server_socket.listen(128)

        # Reference to socket objects
        self.server_socket = server_socket

    def decode_base64(self, url):
        origStr = url
        if (len(origStr) % 3 == 1):
            origStr += "=="
        elif (len(origStr) % 3 == 2):
            origStr += "="
        origstr = bytes(origStr, encoding='ascii')
        usernumber = base64.b64decode(origstr).decode()
        return usernumber

    # Link Waiting for Sockets
    def start(self):
        # The server is multi-client oriented and receives client request links circularly
        print('server is waiting...')
        while True:
            client_socket, client_address = self.server_socket.accept()
            print('Server receives link request from %s' % str(client_address))
            # Processing link requests
            self.client_handler(client_socket)
            # Create a collaboration to achieve multitasking
            g1 = gevent.spawn(self.client_handler, client_socket)
            # Keep the main process alive (block the main process, wait for the co-process G1 to execute before exiting)
            g1.join()

    def client_handler(self, client_socket):
        '''Receive client link request and respond to corresponding data'''
        # Receive data

        request_data = client_socket.recv(4096)
        # Determine whether or not data is received
        if not request_data:
            print('Client has disconnected')
            client_socket.close()
            return

        # Decoding the received client request data
        request_str_data = request_data.decode()
        signal = request_str_data.split('/')[1].split(' ')[0]

        fo = open('datasets/final-rank/Tests/signal.txt', 'w')
        fo.write(self.decode_base64(signal) + signal)
        fo.close()

        print('User: ', self.decode_base64(signal))
        account.create_account()

        os.system('python Multitask_predict.py')
        Matching.start_matching(self.decode_base64(signal), 30)

        # Send response message
        response_line = "HTTP/1.1 200 OK\r\n\r\n"
        response_data = response_line.encode()
        client_socket.send(response_data)
        client_socket.close()


# Create main functions, define sockets, set command line custom port to run.
def main():
    port = 1300
    http_server = HTTPServer(port)
    http_server.start()


if __name__ == '__main__':
    print('server starts')
    print('=======================================================================================================')
    main()
