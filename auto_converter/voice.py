import requests, json, os, time

class Voicerss:
    def __init__(self, type='mp3', language='vi-vn'):
        self.type = type
        self.language = language
        self.token = json.loads(open('./config/func1.json', 'rb').read())['api-key']
    def generator (self, text, speed='0'):
        return 'http://api.voicerss.org/?key={0}&hl={1}&c={2}&f=16khz_16bit_stereo&src={3}&r={4}'.format(
            self.token,
            self.language,
            self.type.upper(),
            text,
            speed
        )
#  VIETNAMESE ONLY
class FPT_AI:
    def __init__ (self, token, voice) -> None:
        self.token = token
        self.voice = voice
    def generator (self, text, speed) -> bool:
        try:
           
            jsonResponse = ''
            if float(speed) < -3 or float(speed) > 3 and int(len(text)) > 3:
                speed = 3
            for x in range(3):
                headers = {}
                headers['api-key'] = self.token
                headers['voice'] = self.voice
                    #post to fpt.ai
                getResponse = requests.post(
                        url='https://api.fpt.ai/hmi/tts/v5',
                        headers=headers,
                        data=text.encode('utf-8')
                    )
                jsonResponse = getResponse.json()
                print(jsonResponse, end='\n\n')
            if jsonResponse['error'] == 0:
                return jsonResponse['async']
        except Exception as e:
            print(e)
            return False