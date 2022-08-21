
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

context = None
socket = None


"""
zmq endpoints
"""