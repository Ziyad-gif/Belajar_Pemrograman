import socket 

host = socket.gethostname()
ipad = socket.gethostbyname(host)

print("ip address anda adalah " +ipad)