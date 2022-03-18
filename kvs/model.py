from pydantic import BaseModel


class KVSPair(BaseModel):
    key: str
    value: str


class KVSPairUpdateRequest(BaseModel):
    value: str
