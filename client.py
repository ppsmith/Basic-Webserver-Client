'''
Created on Feb 7, 2019
@author: ppsmith
'''

import sys
import socket
from urllib.request import localhost

for line in sys.stdin :
    address = line
    try:
        s = socket.socket()
        host_ip = socket.gethostbyname('localhost')
        s.connect((host_ip, 80))
        address = address.encode()
        s.send(address)
        
        while s.recv() > 0:
            response = s.recv()
            response = response.decode()
            sys.stdout.writelines(address)
            sys.stdout.writelines(response)
        s.close()
        
    except TimeoutError:
        print('Connection Error')
        continue
    except TypeError:
        print('Type Error')
        continue
    except socket.error as err:
        print(err)
        s.close()