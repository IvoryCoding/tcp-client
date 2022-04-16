#   Date:        2022/04/16
#   Author:      Emma Gillespie
#   Description: A basic tcp client
#   Resources:

#!/usr/bin/python3

import socket
import argparse

def getMainPage(host, port, bytes):

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect((host, port))

    client.send(b"GET / HTTP/1.1\r\nHost: 192.168.1.85\r\n\r\n")

    response = client.recv(bytes) # length of response testing use 4096

    print(response)
    client.close()

if __name__ == "__main__":
    # Set the arguments
    parse = argparse.ArgumentParser(description="Python tcp client")
    parse.add_argument("host", help="Host name or IP address to tcp client")
    parse.add_argument("-p", "--port", help="The port to tcp client to")
    parse.add_argument("-b", "--bytes", help="Pass how many bytes of response to get")

    args = parse.parse_args()
    host = args.host
    port = args.port
    bytes = args.bytes

    getMainPage(host, int(port), int(bytes))
