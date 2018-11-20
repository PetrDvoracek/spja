from xmlrpc.client import ServerProxy


s = ServerProxy('http://localhost:10000')

a=5
b=6

print(s.add(1,2))

