"""
routs for the control uwu~
"""
from flask import Blueprint, abort
from flask import (
    jsonify,
    render_template,
    redirect,
    request,
    url_for,
    send_from_directory,
    send_file,
)
from utils import Consts, consolelog


apibp = Blueprint("apibp", __name__)

# main rounter
@apibp.route(Consts.apibase)
def index():
    return "hellow world~"




"""
Led control 
"""

# reports status of led lights actually get light status 
@apibp.route(Consts.ledcontrol+"status")
def ledstatus():
    consolelog.warning("grabbing status of led lights and groups")

    consolelog.PipeLine_Ok("got status of lights are ....")
    return jsonify({"status": "need to finish"})

#! color control red,green,blue,brightness
@apibp.route(Consts.ledcontrol+"setwholestripcolor")
def setledstripcolor(red, green, blue, brightness, strip):

    # loggs color 
    consolelog.PipeLine_Data("Color values for led strip"+" "+str(strip)+" ")
    consolelog.PipeLine_Data("red: "+str(red))
    consolelog.PipeLine_Data("green: "+str(green))
    consolelog.PipeLine_Data("blue: "+str(blue))
    consolelog.PipeLine_Data("brighightness: "+str(brightness))


    rgb = (red,green,blue)

    return jsonify({"status": "set colors t\o "+str(rgb)+" "+"to strip "+str(strip)})








"""
Fan Control 
"""

#reports fan status
@apibp.route(Consts.fancontrol+"status")
def fanstat():
    consolelog.PipeLine_Ok("got status of fan are ....")
    return jsonify({"status": "need to finish"})







"""
temp monitoring
"""

#reports tempature status status
@apibp.route(Consts.tempcontrol+"status")
def tempstatus():
    consolelog.warning("grabbing status of Temp")

    consolelog.PipeLine_Ok("got status of Temp are ....")
    return jsonify({"status": "need to finish"})







"""
voice modulation control 
"""
#need to finish
def voicestatus():
    consolelog.warning("grabbing status of voice")

    consolelog.PipeLine_Ok("got status of voice are ....")
    return jsonify({"status": "need to finish"})




