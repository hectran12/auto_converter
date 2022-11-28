url = "https://voicerss-text-to-speech.p.rapidapi.com/"

querystring = {"key":"99b1c6448bc542208aa670ce93d9b03e"}

payload = "src=xin%20ch%C3%A0o&hl=vi-vn&r=1&c=mp3&f=8khz_8bit_mono"
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "e4065064b1mshd019d41d00a5b5dp14efbbjsn431d859077ef",
	"X-RapidAPI-Host": "voicerss-text-to-speech.p.rapidapi.com"
}

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)