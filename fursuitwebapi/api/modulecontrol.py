"""
this class is for controling the submodules via zmq
"""
import time
from utils import consolelog as log

class modulecontrol(object):

    # controls led module
    def sendLedControl(self, sender, section, brightness, red, green, blue, soundact, currenttime):
        log.Debug("sending LED command to zmq")
        
        sender.send_string("LEDCONTROL")
        sender.send_json(
            {
                "section": int(section),
                "brightness": int(brightness),
                "red": int(red),
                "green": int(green),
                "blue": int(blue),
                "soundact": int(soundact),
                "time": str(currenttime),
            }
        )
        time.sleep(0.5)
        log.PipeLine_Ok("sent Face Count to zmq socket")