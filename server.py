Created on Feb 7, 2019

@author: ppsmith
'''

import sys
import os
import socket
from builtins import str
from urllib import request

def main():
    socketCreate()
    httpTest()
    quit()
    
def socketCreate():
    stuff = []
    while(True):       
        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET,  socket.SO_REUSEADDR, 1)
        host_ip = socket.gethostbyaddr('localhost')
        s.bind(('localhost', 6733))
        s.listen(1)
        stuff.append(s)
        
    for things in stuff:   
        connection, address = s.accept()
        stringData = connection.recv(1024).decode('utf-8')
        parsedData = httpTest(stringData)
        sendData = parsedData.encode()
        connection.sendall(sendData)
        s.close()
        
def httpTest(request):
#     for line in request:
    userInput = request #takes in host request
    sys.stdout.writelines(userInput)
    splitUserInput = userInput.split(" ", 2) #splits x on the first two spaces
    lastUserInput = splitUserInput[len(splitUserInput) - 1] #gets the last thing in userinpu  
    lowerCaseHTTP = lastUserInput.lower() #converts the lat entry nin x (hopefully the HTTP version request)n into lowercase   
    lowerSplit = lowerCaseHTTP.split("/") #splits the lowercase version of the httprequest on the "/"   
    numberSplit = lowerSplit[len(lowerSplit) - 1].split(".") #splits the http version number on the "."
          
    
    if(splitUserInput[0]) != "GET":
        return("ERROR")
#            continue
        
    if lowerSplit[len(lowerSplit) - len(lowerSplit)] != "http":
        return("ERROR -- Invalid HTTP-Version token2.")
#             continue

    if len(splitUserInput) == 2:
        return('Error -- Invalid Absolute-Path token3.')
#             continue
#     
    httpSpaceTest = splitUserInput[len(splitUserInput) - 1].split(" ")
    
    if len(httpSpaceTest) != 1 :
        return("ERROR -- Spurious token before CRLF4.")
#             continue
    
    for count, char in enumerate(numberSplit):
        numberSplit[count] = char.rstrip()
    httpWrong = False
        
    for char in numberSplit:
        try: 
            if not 48 <= ord(char) <= 57:
                return("ERROR -- Invalid HTTP-Version token5.")
                httpWrong = True
#                     continue
        except TypeError:
                return("ERROR -- Invalid HTTP-Version token6.")
                httpWrong = True
#                     continue
         
         
    if httpWrong:
       return('ERROR -- Invalid HTTP-Version Token')
               
    listAbsolutePath = list(splitUserInput[1])
    absWrong = False
    for count, char in enumerate(listAbsolutePath) :
        try:
            if not 0 <= ord(char) <= 127:
                return("ERROR -- Invalid Absolute-Path token7.")
                absWrong = True
#                 continue
        except TypeError:
            return("ERROR -- TypeError1.")
            absWrong = True
        
    if absWrong:
        print('ERROR')
        
    if(listAbsolutePath[0] != '/'):
        return("ERROR -- Invalid Absolute-Path token8.")
#         continue
        
    if (len(splitUserInput) > 3):
            return('ERROR -- Spurious token before CRLF9.')
#             continue
    address = splitUserInput[1]
    address= os.getcwd() + address
    addressSplitDot = address.split(".")
    addressSplitSlash = address.split('/')
    
    if(len(addressSplitDot) < 1):
        return("Error -- Invalid Absolute-Path token10.")
#         continue
    if(len(addressSplitSlash) < 1):
        return("Error -- Invalid Absolute-Path token11.")
#         continue
        
    if addressSplitDot[len(addressSplitDot) - 1].lower() == "txt" or addressSplitDot[len(addressSplitDot) - 1].lower() == 'htm' or addressSplitDot[len(addressSplitDot) - 1].lower() == 'html' or addressSplitSlash[len(addressSplitSlash) - 1] == "/":
        try:
            file = open(address)
            return (
                "Method = " + splitUserInput[0] + '\n' +
                "Request-URL = " + splitUserInput[1] + '\n' +
                "HTTP-Version = " + splitUserInput[2].rstrip() + '\n' +
                file.read().rstrip()) + '\n'
#             continue
        except FileNotFoundError:
            return(
                "Method = " + splitUserInput[0] + '\n' +
                "Request-URL = " + splitUserInput[1] + '\n' + 
                "HTTP-Version = " + splitUserInput[2].rstrip() + '\n' +
                '404 Not Found: ' + splitUserInput[1]) + '\n'
#             continue
        except Exception as e:
            return(
                "Method = " + splitUserInput[0] + '\n' +
                "Request-URL = " + splitUserInput[1] + '\n' +
                "HTTP-Version = " + splitUserInput[2].rstrip() + '\n' +
                'Error: ' + str(e)) + '\n'
#             continue
    else:
        return(
            "Method = " + splitUserInput[0] + '\n' +
            "Request-URL = " + splitUserInput[1] + '\n' +
            "HTTP-Version = " + splitUserInput[2].rstrip() + '\n' +
            '501 Not Implemented: ' + splitUserInput[1]) + '\n' 
#     continue
    
if __name__ == "__main__":
    main()
