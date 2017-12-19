import Messanger

with open("C:/Users/fdr/Desktop/test.wav", "rb") as wav:
    source = []
    byte = wav.read(1)
    while byte != "":
        source.append(byte)
        byte = wav.read(1)
        
Messanger.set("audio", source)

print Messanger.getMessage()
    
    