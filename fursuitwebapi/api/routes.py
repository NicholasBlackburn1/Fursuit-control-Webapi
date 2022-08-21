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
from fursuitwebapi.utils import Consts

apibp = Blueprint("apibp", __name__)

# main rounter
@apibp.route(Consts.apibase)
def index():
    return "hellow world~"




"""
Led control 
"""

# reports status of led lights
@apibp.route(Consts.ledcontrol+"status")
def ledstatus():
    pass





"""
Fan Control 
"""

#reports fan status
@apibp.route(Consts.fancontrol+"status")
def fanstatus():
    pass






"""
temp monitoring
"""

#reports tempature status status
@apibp.route(Consts.tempcontrol+"status")
def tempstatus():
    pass






"""
voice modulation control 
"""

#reports tempature status status
@apibp.route(Consts.voicecontrol+"status")
def voicetatus():
    pass


