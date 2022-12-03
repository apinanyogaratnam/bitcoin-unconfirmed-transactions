from flask_restful import Resource
import requests


class UnconfirmedTransactions(Resource):
    def __init__(self: "UnconfirmedTransactions") -> None:
        pass

    def get(self: "UnconfirmedTransactions") -> dict:
        return requests.get(
            'https://blockchain.info/unconfirmed-transactions?format=json'
        ).json()
