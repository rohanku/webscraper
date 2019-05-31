import csv
import requests
import random
from BeautifulSoup import BeautifulSoup

queue = ['https://www.togamath.com', 'https://www.pythonforbeginners.com']
tot = 0.0
num = 0
inq = 1


outfile = open("./websites.csv", "w")
writer = csv.writer(outfile)

while queue:
	count = 0
	url = queue.pop(0)
	inq-=1
	visited = [url]
	queue2 = [url]
	pages = 0
	while queue2:
		counta = 0
		urll = queue2.pop(0)
		pages += 1
		response = ""
		try:
			response = requests.get(urll)
		except requests.exceptions.ConnectionError:
	    		print "Connection Error"
			continue
		except requests.exceptions.InvalidURL:
    			print "Invalid URL"
			continue
		html = response.content
	
		soup = BeautifulSoup(html)
		for link in soup.findAll('a'):
			hf = link.get("href")
			if hf != None:
				if hf:
					hf = hf.encode('ascii')
				if "//" not in hf:
					hf = url + hf
					if hf not in visited:
						visited.append(hf)
						queue2.append(hf)
				if "wikipedia" in hf:
					counta+=1
		print urll + ": " + str(counta)
		count+=counta
	print "SOLVED: There are " + str(count) + " wikipedia links on " + url
	writer.writerow([url, str(count), str(pages)])
