import requests
import random
from BeautifulSoup import BeautifulSoup

queue = ['https://www.python.org/']
tot = 0.0
num = 0
inq = 1


while queue:
    count = 0
    url = queue.pop(0)
    inq-=1
    response = requests.get(url)
    html = response.content

    soup = BeautifulSoup(html)
    for link in soup.findAll('a'):
        hf = link.get("href")
	if hf:
	    hf = hf.encode('ascii')
            if hf[0 : 7] == "http://" or hf[0:7] == "https://":
                if "wikipedia" in hf:
                     count+=1
            else:
                hf = url + hf
                if "wikipedia" in hf:
                    count+=1
            if random.random()<=0.5 and inq <=10000000:
                queue.append(hf)
    tot += count
    num+=1
    print tot/num
