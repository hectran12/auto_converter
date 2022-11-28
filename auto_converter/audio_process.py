import requests, os, glob


class Audio_Hex:
    def __init__(self, path='./audio'):
        self.path = path

    def download_audio (self, link, name):
        doc = None
        try:
            doc = requests.get(link)
            with open('{0}/{1}.mp3'.format(
                self.path, name
            ), 'wb') as f:
              
                f.write(doc.content)
            return True
        except:
            print(doc.text)
            return False

    def save_audio(self, binary, filename):
        try:
            f = open('{0}/{1}.mp3'.format(
                self.path, filename
                ), 'w+', encoding='utf-8')
            f.write(binary)
            f.close()
            return True
        except Exception as e:
            print(e)
            return False

    def remove_all (self):
        os.chdir(self.path)
        files=glob.glob('*.bak')
        for filename in files:
            os.unlink(filename)
