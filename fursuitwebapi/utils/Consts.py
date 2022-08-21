
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

#zmq
zmqip = "127.0.0.1"
zmqport = "4500"
context = None
socket = None


"""
zmq endpoints
"""