"""
main class
"""

import pathlib
from utils import consolelog, Consts
import app
import zmq


# main function
def main():
    consolelog.info("starting apiserever...")

    appy = app.create_app()
    appy.config["SQLALCHEMY_DATABASE_URI"] = (
        "sqlite:///" + str(pathlib.Path().absolute()) + "/"+ Consts.folderbase + "avatar.db"
    )

    # zmq stuff need to test in zmq
    consolelog.Warning("starting ZMQ Server (need to renable it)...")

    #Consts.context = zmq.Context()

    #!pub socket
    #Consts.socket = Consts.context.socket(zmq.PUB)
    #Consts.socket.bind("tcp://0.0.0.0:2556")

    #!recv socket
    #Consts.socketrecv = Consts.context.socket(zmq.SUB)
    #Consts.socketrecv.connect("tcp://0.0.0.0:2557")
    

    consolelog.PipeLine_Ok("started ZMQ Server (need to renable it)...")

    appy.run(threaded=True, debug=True, host=Consts.url, port=2000)










if __name__ == '__main__':
    main()