# pip install Flask

from flask import Flask
from flask import json
from flask import Response
import os
import httplib, json, urllib, base64

apiKey = ""
headers = {
	'Content-Type': "application/octet-stream",
	'Ocp-Apim-Subscription-Key': apiKey,
}

host = 'api.projectoxford.ai'
requestURL = '/emotion/v1.0/recognize'
localFilePath = './test.jpg'

#f = os.popen('ifconfig br-lan | grep "inet\ addr" | cut -d: -f2 | cut -d" " -f1') # AP model
f = os.popen('ifconfig apcli0 | grep "inet\ addr" | cut -d: -f2 | cut -d" " -f1') # Station model

inet_addr = f.read()
app = Flask(__name__)

# *****************************************************************************************
# GET http://mylinkit.local:5000/api/v1.0/takePicture
# *****************************************************************************************
@app.route("/api/v1.0/takePicture", methods=['GET'])
def setvideoon():
	os.system('fswebcam -i 0 -d v4l2:/dev/video0 --no-banner -p YUYV --jpeg 95 --save ./test.jpg')
	conn = httplib.HTTPSConnection(host)
	conn.request("POST", requestURL, open(localFilePath, 'rb'), headers)
	response = conn.getresponse()
	print(response.status, response.reason)
	data = response.read()
	conn.close()
	print(data)
	return json.dumps({"status": 200, "comment": data})

if __name__ == "__main__":
    app.debug = True
    print "inet_addr: " + inet_addr
    app.run(
        host = inet_addr,
        port = 5000
    )