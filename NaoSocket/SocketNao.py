'''
Created on 13.01.2018

@author: fdr
'''
import socket
import WsClient
import ast
import MusicRecognizer

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
    server_data = conn.recv(BUFFER_SIZE)
    if not server_data:
        break
    nao_data = None
    print "received data from Nao: ",
    server_data = ast.literal_eval(server_data)
    if server_data['mode'] and server_data['mode'] in EndPoints:
        wsClient = WsClient.WsClient("ws://localhost:8080/NaoServer/"++EndPoints[server_data['mode']])
        if server_data['message']:
            nao_data = wsClient.send(server_data['message'])
            print "received data from wsClient: ", nao_data
    else:
        if "audio-source" in server_data['message']:
            buf = server_data['message']['audio-source']
            mRec = MusicRecognizer()
            nao_data = mRec.recognizeBuffer(buf)
    if nao_data:
        if nao_data['to_speech']:
            conn.send(nao_data['to_speech'])
        conn.send(nao_data)
conn.close()