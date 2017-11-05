import re
import requests

def get(URL, i):
    req = requests.get(URL)

    if req.status_code !== 200:
        print("Status code different then 200!")
    else:
        text = req.text
        file = open("file"+str(i)+".html",'w')
        file.write(text)
        file.close()
        for m in re.finditer(r"https?://[^\"]*", text):
            print("%d=> %d-%d: %s" % (i, m.start(), m.end(), m.group(0)))
            i += 1
            get(m.group(0), i)
            
get("http://www.example.com", i=0)
