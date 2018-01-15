from acrcloud.recognizer import ACRCloudRecognizer
from acrcloud.recognizer import ACRCloudRecognizeType

class MusicRecognizer:

    def __init__(self):
        self.config = {
            'host': 'identify-eu-west-1.acrcloud.com',
            'access_key': '9fc573829047880668ee383bd4ab4a19',
            'access_secret': 'Vmr1CS4OpBrLe0bl8UTFmzLqY46L25lyB7gJwOeK',
            'recognize_type': ACRCloudRecognizeType.ACR_OPT_REC_AUDIO,
        # you can replace it with [ACR_OPT_REC_AUDIO,ACR_OPT_REC_HUMMING,ACR_OPT_REC_BOTH], The SDK decide which type fingerprint to create accordings to "recognize_type".
            'debug': False,
            'timeout': 10  # seconds
        }

    def recognizeBuffer(self, buf):
        re = ACRCloudRecognizer(self.config)
        data = re.recognize_by_filebuffer(buf, 0, 10)
        return data

    #recognize by file path, and skip 0 seconds from from the beginning of sys.argv[1].
    # print(re.recognize_by_file(sys.argv[1], 0, 10))

    # print("duration_ms=" + str(ACRCloudRecognizer.get_duration_ms_by_file(sys.argv[1])))

    #buf = open(sys.argv[1], 'rb').read()
    #recognize by file_audio_buffer that read from file path, and skip 0 seconds from from the beginning of sys.argv[1].
    # print(re.recognize_by_filebuffer(buf, 0, 10))
