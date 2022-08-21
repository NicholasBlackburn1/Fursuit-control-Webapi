"""
this class is for controling the submodules via zmq
"""
import time
from utils import consolelog as log

class modulecontrol(object):

    """
    controls led module
    @sender: zmq sender
    @section: led strip zone (1-4)

    @brightness: sets brightness of led strip (0-255)
    @red: sets red color value of strip (0-255)
    @green: sets green color value of strip (0-255)
    @blue: sets blue color value of strip (0-255)

    @soundact: allows sections to respond to surroundign sound
    
    """
    def sendLedControl(self, socket, section, brightness, red, green, blue, soundact, currenttime):
        log.Debug("sending LED command to zmq")

        socket.send_string("LEDCONTROL")
        socket.send_json(
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


    
    """
    controls fan module
    @sender: zmq sender
    @fan:  fan select

    @speed: sets speed of fan (0-255)
    @timecontroled: sets fan controled by thermal probe (0-1)
    
    """
    
    def sendFanControl(self, socket, fan, speed, temcontroled, currenttime):
        log.Debug("sending FAN command to zmq")

        socket.send_string("FANCONTROL")
        socket.send_json(
            {
                "fan": int(fan),
                "speed": int(speed),
                "temcontroled": int(temcontroled),
                "time": str(currenttime),
            }
        )
        time.sleep(0.5)
        log.PipeLine_Ok("sent Face Count to zmq socket")


 
    """
    controls Voice module
    @sender: zmq sender
    @mic:  mic select
    @speaker:  speaker select

    @octive: sets the pitch of the audio (0-255)
    @semitone: sets the pitch of the audio (0-255)
    @speed: sets speed of output audio 

    @inputvol: sets gain of mic (0-255)
    @outputvol: sets volume of output (0-255)
    """
    
    def sendVoiceControl(self, socket, octive, semitone, speed, inputvol, outputvol, mic, speaker, currenttime):
        log.Debug("sending VOCIE command to zmq")

        socket.send_string("VOICECONTROL")
        socket.send_json(
            {   
                "mic":  str(mic),
                "speaker": str(speaker),
                "octive": int(octive),
                "semitone": int(semitone),
                "speed": int(speed),
                "inputvol": int(inputvol),
                "outputvol": int(outputvol),
                "time": str(currenttime),
            }
        )
        time.sleep(0.5)
        log.PipeLine_Ok("sent Face Count to zmq socket")




    """
    recves temp data

    @probe: selects the probe
    @temp: grabs current temp 

    """
    def recvTempData(self, socket, probe, temp, currenttime):
        log.Debug("Recving temp data...")

        socket.recv_string("TEMPCONTROL")
        socket.send_json(
            {   
                "probe":  str(probe),
                "temp": str(temp),
                "time": str(currenttime),
            }
        )
        time.sleep(0.5)
        log.PipeLine_Ok("RECVED TEMP to zmq socket")




    