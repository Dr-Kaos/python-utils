import re
import requests

URL = "https://github.com"

req = requests.get(URL)
text = req.text
i = 0

for m in re.finditer(r"https?[^\"]*", text):
    print("%d=> %d-%d: %s" % (i, m.start(), m.end(), m.group(0)))
    i += 1
