import json
import urllib.request

def load_json(url):
    # with open("mv_names.json", "r") as f:
    #     return json.loads(f.read())
    user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46'
    request = urllib.request.urlopen(urllib.request.Request(str(url), data=None, headers={'User-Agent': user_agent}))
    return json.loads(request.read())
