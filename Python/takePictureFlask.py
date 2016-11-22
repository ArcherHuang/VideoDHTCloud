# pip install Flask

from flask import Flask
from flask import json
from flask import Response
import os

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
	return json.dumps({"status": 200, "comment": "call set Video Finish"})

if __name__ == "__main__":
    app.debug = True
    print "inet_addr: " + inet_addr
    app.run(
        host = inet_addr,
        port = 5000
    )