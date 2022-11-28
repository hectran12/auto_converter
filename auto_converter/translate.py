import googletrans
from pprint import pprint
import logging
import threading
import time
class ExportTrans:
    def __init__(self, file, src='en', dest='vi') -> None:
        self.src = src
        self.dest = dest
        self.file = file
    def srt (self, time=True) -> dict or bool:
        try:
            f = open(self.file, 'r', encoding='utf-8')
            content = f.read().split("\n")
            c = 0
            subs = []
            subtitle = {}
            for x in content:
                if x != '':
                    if c == 0: 
                        subtitle['number'] = x
                        c += 1
                    elif c == 1:
                        subtitle['time'] = x 
                        c += 1
                    elif c == 2:
                        subtitle['content'] = x
                        #add to subs
                        subs.append(subtitle)
                        subtitle = {}
                        c = 0
            f.close()
            return subs
        except Exception as e:
            print(e)
            return False
        
    def translate (self, sub: dict) -> dict or bool:
      
        clone = []
        # func change, run with thread :)
        def trans (self, obj) -> dict or bool:
           
            try:
                # Initial 
                translator = googletrans.Translator()
                results = translator.translate(obj['content'], src=self.src, dest=self.dest)
           
                obj['content'] = results.text
                clone.append(obj)
            except:
                return False
        for obj in sub:
            x = threading.Thread(target=trans, args=(self, obj))
            x.start()
        checkStatus = False
        for sq in range(25):
            current = str(len(clone))
            max = str(len(sub))
            print('[+] Processing subtitles to another language: {0}/{1}'
                .format(current, max)
                , end='\r')
            if current == max:
                print('[+] Subtitles are successfully processed and translated into your language')
                checkStatus = True
                break
            time.sleep(1)

        if checkStatus == False:
            print('[+] An error has occurred internally.')
            return False
        
        for i in range(1,int(max)+1):
            for x in clone:
                if x['number'] == str(i):
                    sub[i-1] = x

        return sub