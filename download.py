import requests

def download(url,locat):
    r = requests.get(url)
    with open(locat,'wb') as f:
        f.write(r.content)
