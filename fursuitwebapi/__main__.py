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

    
    consolelog.Warning("starting ZMQ Server...")
    Consts.context = zmq.Context()
    Consts.socket = Consts.context.socket(zmq.PUB)

    Consts.socket.bind("tcp://"+Consts.url % Consts.zmqport)
    consolelog.PipeLine_Ok("started ZMQ Server...")

    appy.run(threaded=True, debug=True, host=Consts.url, port=2000)










if __name__ == '__main__':
    main()