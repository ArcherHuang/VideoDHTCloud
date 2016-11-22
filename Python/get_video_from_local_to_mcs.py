# opkg update  
# opkg install ffmpeg  

# ******************************************************************************************
# Import Package                                                                           #
# ******************************************************************************************

import os

# ******************************************************************************************
# Set deviceId, deviceKey, dataChnId                                                       #
# ******************************************************************************************

deviceId = "DBKHFNIw"
deviceKey = "8fszdReA51m0vRjq"
dataChnId = "videoStream"
width = "176"
height = "144"

# ******************************************************************************************
# Send Video Stream To MCS                                                                 #
# ******************************************************************************************

cmd = "ffmpeg -s " + width + "x" + height + " -f video4linux2 -r 30 -i /dev/video0 -f mpeg1video -r 30 -b 800k http://stream-mcs.mediatek.com/" + deviceId + "/" + deviceKey + "/" + dataChnId + "/" + width + "/" + height
os.system(cmd)
