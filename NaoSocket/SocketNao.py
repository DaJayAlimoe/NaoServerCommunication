'''
Created on 13.01.2018

@author: fdr
'''
import socket
import WsClient
import ast

EndPoints = {'reminder' : 'websocketErinnerung', 'music' : 'websocketMusikErkennung', 'patient' : 'websocketPatient'}
TCP_IP = '127.0.0.1'
TCP_PORT = 5550
BUFFER_SIZE = 25  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), TCP_PORT))
s.listen(1)
conn, addr = s.accept()

print 'Connection address:', addr
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print "received data from Nao: ",
    nao_data = ast.literal_eval(data)
    wsClient = WsClient.WsClient("ws://localhost:8080/NaoServer/"++EndPoints[nao_data['mode']])
#     TODO ws client aufruf
    data_from_ws = wsClient.send(nao_data['message'])
    print "received data from wsClient: ", data_from_ws
#     send to Nao
    conn.send(data_from_ws)  # echo
    
conn.close()