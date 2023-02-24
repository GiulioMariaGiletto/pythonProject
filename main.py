from bs4 import BeautifulSoup
import requests
import contextlib


req = requests.get("https://www.corrieredellosport.it/")
req1= requests.get("https://www.corrieredellosport.it/")
soup = BeautifulSoup(req1.text, "html.parser")
print(soup.title)
h2s = soup.findAll("h2")
for tit in h2s:
    print(tit.text)

for h2 in h2s:
    linkys = h2.findAll("a", href=True)
    for link in linkys:
        print(link)

for el in soup.findAll('img'):
    if el.get("alt") != "":
        imageName = f"{el.get('alt')}.png"
        src = el.get("src")
        if 'NoneType' not in type(src):
            print(type(src))
            if "jpg" in src:
                with contextlib.closing(requests.get(src)) as image:
                    with open(imageName, "wb") as destFile:
                        for block in image.iter_content(1024):
                            if block:
                                destFile.write(block)
                destFile.close()






















