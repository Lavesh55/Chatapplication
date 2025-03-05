import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip="192.168.217.58"
port=1234
complete=(ip,port)
mess=input("enter your message")
encode_mess=mess.encode('ascii')# convert into binary
s.sendto(encode_mess,complete)
