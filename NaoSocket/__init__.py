# from NaoSocket import websocket
# 
# from websocket import create_connection
# ws = create_connection("ws://localhost:8080/NaoWebsocket/websocketendpoint")
# 
# # print("Sending 'Hello, World'...")
# # ws.send("Hello, World")
# # print("Sent")
# # print("Receiving...")
# # result =  ws.recv()
# # print("Received '%s'" % result)
# 
# #tts.say("FUCK BITCHES GET MONEY amk")
# #import time
# #counter = 0
# 
# # patient und aufgabe festlegen
# patiententoken="z-e-r-o"
# task="medikamenteinnahme"
# 
# #request json erzeugen
# requestjson="{\"task\": \""+ task + "\", \"patiententoken\": \""+patiententoken+"\"}"
# 
# #request abschicken
# ws.send(requestjson)
# result = ws.recv()
# 
# # ausgabe 
# ws.close()
# 
# from naoqi import ALProxy
# tts = ALProxy("ALTextToSpeech", "127.0.0.1", 53847)
# tts.say(result)
# 
# #counter += 1
# #time.sleep(4)



# import websocket
# import thread
# import time
# 
# def on_message(ws, message):
#     print(message)
# 
# def on_error(ws, error):
#     print(error)
# 
# def on_close(ws):
#     print("### closed ###")
# 
# def on_open(ws):
#     def run(*args):
#         for i in range(3):
#             time.sleep(1)
#             ws.send("Hello %d" % i)
#         time.sleep(1)
#         ws.close()
#         print("thread terminating...")
#     thread.start_new_thread(run, ())
# 
# 
# if __name__ == "__main__":
#     websocket.enableTrace(True)
#     ws = websocket.WebSocketApp("ws://localhost:8080/NaoWebsocket/websocketendpoint",
#                               on_message = on_message,
#                               on_error = on_error,
#                               on_close = on_close)
#     ws.on_open = on_open
#     ws.run_forever()


# ws.connect("ws://localhost:8080/NaoWebsocket/", http_proxy_host="proxy_host_name", http_proxy_port=8080)
