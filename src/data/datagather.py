import requests
import json
import time
import io

encryptedid = "vjZU8CeGfMlz7P7M_9bOYPu8-4NTcbvGzPmEMNjkKXB2RvA"
key = "RGAPI-ab439e76-ee6c-4454-9ee4-d8b7b35ba846"
url = "https://euw1.api.riotgames.com/lol/match/v4/matchlists/by-account/" + encryptedid

print("URL: " + url)
r = requests.get(url, params = {"api_key":key})
print(r.status_code)
if r.status_code != 200:
	exit()

data = json.loads(r.text)
baseIdGame = int(data["matches"][0]["gameId"])

urlgame = "https://euw1.api.riotgames.com/lol/match/v4/matches/"
s = unicode("\n", "utf-8")
numberOKS = 0


with io.open('datas3.json', 'a', encoding='utf-8') as f:
	for i in xrange(0,1100):
		gameid = baseIdGame + i
		rgame = requests.get(urlgame + str(gameid), params = {"api_key":key})
		if rgame.status_code == 200:
			dataGame = json.loads(rgame.text)
			f.write(json.dumps(dataGame, ensure_ascii=False))
			f.write(s)
			numberOKS += 1
		else:
			print "POZO: LA I ES : " + str(i)
			print rgame.status_code
			print rgame.text
			if(rgame.status_code == 429):
				print "GAMEOVER"
				exit()
		print "OKS: " + str(numberOKS)
		time.sleep(0.85)


f.close()
