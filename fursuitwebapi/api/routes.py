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

apibp = Blueprint("apibp", __name__)


@apibp.route('/')
def index():
    return "hellow world~"

