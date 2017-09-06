#!/usr/bin/python3

import socket

NICK = "simplebot"
HOST = "irc.freenode.net"
PORT = 6667

server = socket.socket()
server.connect((HOST, PORT))

server.send(bytes("USER " + NICK + " " + NICK + " " + NICK + " :" + 
    NICK + "\r\n" + "NICK " + NICK + "\r\n" + "JOIN ##temp\r\n" +
    "PRIVMSG ##temp :Hi!\r\n", 'utf-8'))
    
# i'm not sure that this line is neccesery!so you may remove it!
server.send(bytes("PRIVMSG NickServ :identify whoo whoo", 'utf-8'))


server.recv(4096) # i don't want these bytes so i don't save them


while 1:
    lines = server.recv(1024).decode().split('\n')
    for l in lines:
        args = l.split()
        if len(args) >= 2 and args[0] == "PING":
            server.send(bytes("PONG " + args[1] + "\r\n", "utf-8"))
