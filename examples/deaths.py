import requests
import json

request = requests.get("reddit.com/r/dankmemes/hot.json")
meme = json.loads(request.content)

print(meme["data"]["children"][0])
