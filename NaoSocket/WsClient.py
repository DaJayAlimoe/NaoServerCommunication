'''
Created on 03.10.2017

@author: sam
'''
# from NaoSocket import websocket, NaoConnect
# from NaoSocket.websocket._socket import recv

from websocket import create_connection

class WsClient:
    def __init__(self, url):
        self.ws = create_connection(url)
        
    def send(self, send_data):
        self.ws.send(send_data)
        received_data = self.ws.recv()
        self.ws.close()
        return received_data

# '''ws = create_connection("ws://localhost:8080/NaoServer/websocketendpoint")
# #ws = create_connection("ws://se2-nao.ful.informatik.haw-hamburg.de:80/NaoWebsocket/websocketPatient")
# 
# import time
# counter = 0
# 
# # patient und aufgabe festlegen
# # patiententoken="1"
# # task="leseErinnerung"
# 
# # request json erzeugen
# # requestjson="{\"task\": \""+ task + "\", \"patiententoken\": \""+patiententoken+"\"}"
# 
# 
# import NaoConnect
# breakpoint=True
# timeout=False
# while (breakpoint and not timeout ):
#     # request abschicken
#     ws.send('hello!')
#     result = ws.recv()
#     result = "from webserver: ", result
# 
#     # ausgabe 
# #     NaoConnect.nao_say(result)
# #     time.sleep(4)
# #     counter += 1
# #     if counter == 5:
# #         timeout=True
# 
# ws.close()
# '''