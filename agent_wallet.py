import json, os

class Wallet:
    def __init__(self, did=None):
        self.did = did
        self.credentials = []

    @classmethod
    def create(cls, name):
        return cls(did=f"did:aid:{name}")

    def store_credential(self, vc):
        self.credentials.append(vc)
        return True

    def create_presentation(self, fields, range=None):
        return {"@context": ["https://www.w3.org/2018/credentials/v1"], "verifiableCredential": []}
