import requests
import audio_process, translate
class export:

    def TranslateSrt (self, file='001.srt', src='vi', dest='en'):
        audio = audio_process.Audio_Hex()
        expo = translate.ExportTrans(file, src=src, dest=dest)
        cv = expo.translate(expo.srt(expo))
        if type(cv) == bool:
            return False
        else: 
            return cv 
    