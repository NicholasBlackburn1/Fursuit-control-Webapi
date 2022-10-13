
"""
endpoints  non zmq
"""

base = "/fursuitcontrol/api"
apibase = base + "/v1.0/"

#endpoints
ledcontrol = apibase + "led/"
fancontrol = apibase + "fan/"
voicecontrol =  apibase + "voice/"
tempcontrol = apibase + "temp/"



"""
non web endpoints ie vars 
"""
# folder and api
folderbase = "FursuitControl/"
url = "0.0.0.0"

"""
led vars 
"""
ledstrip1 = 0
ledstrip2 = 1
ledstrip3 = 2
ledstrip4 = 3 

#zmq

context = None
socketrecv = None
socket = None

"""
zmq endpoints
"""