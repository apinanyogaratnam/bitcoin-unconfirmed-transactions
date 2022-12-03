from flask_restful import Resource
import os


class Home(Resource):
    def __init__(self: "Home") -> None:
        pass

    def get(self: "Home") -> dict:
        return {"status": "OK", "pid": os.getpid()}
