"""
main class
"""

import pathlib
from utils import consolelog, Consts
import app


# main function
def main():
    consolelog.info("starting apiserever...")

    app.create_app()
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "sqlite:///" + str(pathlib.Path().absolute()) + "/"+ Consts.folderbase + "avatar.db"
    )

    
    

    app.run(threaded=True, debug=True, host=Consts.url, port=2000)










if __name__ == '__main__':
    main()