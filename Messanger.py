message = dict({})

def clear():
    message.clear()

def addFile(filePath):
    source = []
    with open(filePath, 'rb') as file:
        byte = file.read(1)
        while byte != "":
            source.append(byte)
    set('audio-source', source)

# deletes Key and Value
def remove(key):
    if key in message:
        del message[key]

# set Key&Value pair
# value of the given key will be overwritten if exists
def set(key, value):
    message.__setitem__(key, value)

def getMessage():
    return message
#    @staticmethod
#    def send(self, endpoint):
