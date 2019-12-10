import socket
import sys
import struct



"""
 Received BCCT message from /192.168.30.26:
        Version: 0.1
        Message ID: 1
        Type: UNKNOWN TYPE
        Protocol: Unknown (0)
        Status: UNKNOWN TYPE
        Replies to: 25769803776
        Reply expected: true
        Next keep alive: 0
        Payload size: 0

"""


test = """<BroadsoftDocument protocol="NSOCI">
<sessionId> xs:normalizedString </sessionId>
<userId> xs:token </userId>
<phoneNumber> xs:token </phoneNumber>
<linePort> xs:token </linePort>
<command> OCICommand </command>
</BroadsoftDocument>
"""

bytematch = '>cccchhqb?bbhhqis'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('192.168.32.12', 2220)
print 'connecting to %s port %s' % server_address
sock.connect(server_address)

print sys.getsizeof(test)

x = struct.pack(bytematch, "B","C","C","T" , 1, 1, 14 , 0 , 1 ,0 , 0 , 16 , 0 , 0 , 0, test)

print x

sock.sendall(x)
data = sock.recv(1024)

y = struct.unpack('>cccchhqb?bbhhqi', data)
print y