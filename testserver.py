import base64
import urllib2
import json
import sys

with open(sys.argv[1], "rb") as f:
    data = f.read()
    encoded = base64.b64encode(data)
    dict = {'photo': encoded}
    req = urllib2.Request('http://localhost/api/')
    #req.add_header('Content')
    response = urllib2.urlopen(req, json.dumps(dict))
    print response.read()