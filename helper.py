from urllib.request import urlopen
import requests
import re as r

class Helper:
    def getIP(self):
        d = str(urlopen('http://checkip.dyndns.com/')
                .read())

        return r.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(d).group(1)
    def detect_language_code (self) -> str or None:
        try:
            myIp = self.getIP()
            getInfo = requests.get('http://ip-api.com/json/{0}?fields=status,countryCode'.format(
                myIp
            )).json()
            if getInfo['status'] == 'success':
                return getInfo['countryCode'].lower().replace(
                    'vn', 'vi'
                )
            else:
                return None
        except:
            return None


