from flask_restful import Resource


class HealthCheck(Resource):
    def __init__(self: "HealthCheck") -> None:
        pass

    def get(self: "HealthCheck") -> dict:
        return {"status": "OK"}
