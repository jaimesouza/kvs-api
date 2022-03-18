from fastapi import FastAPI, Response, HTTPException
from kvs.model import KVSPair, KVSPairUpdateRequest
from kvs.database import FakeDB


app = FastAPI()


# create a fake key-value database
db = FakeDB()


@app.get("/")
def root(response: Response):

    # add some information in the response header
    response.headers["app-name"] = "kvs-api"
    response.headers["app-author"] = "Jaime Freire"

    return {
        "Name": "Key-Value Store REST API",
        "Author": "Jaime Freire"
    }


@app.get("/api/pairs")
def fetch_pairs():
    return db.get_pairs()


@app.get("/api/pairs/{key}")
def fetch_value(key: str, response: Response):

    # check if the key exists in the database
    if db.key_exists(key):

        pair = db.get_pair_by_key(key)

        # add key-value info in the response header
        response.headers["key"] = key
        response.headers["value"] = pair.value

        return pair

    raise HTTPException(
        status_code=404,
        detail=f"key {key} does not exist"
    )


@app.post("/api/pairs", status_code=201)
def insert_pair(new_pair: KVSPair):

    # check if the key already exists
    if db.key_exists(new_pair.key):

        raise HTTPException(
            status_code=409,
            detail=f"key {new_pair.key} already exists"
        )

    # if it does not exists yet, insert it
    db.insert(new_pair)

    return new_pair


@app.put("/api/pairs/{key}", status_code=201)
def update_pair(pair_update: KVSPairUpdateRequest, key: str):

    # check if the key exists in the database
    if db.key_exists(key):
        # update the value
        pair = db.update(key=key, value=pair_update.value)

        return pair

    raise HTTPException(
        status_code=404,
        detail=f"key {key} does not exist"
    )


@app.delete("/api/pairs/{key}")
def delete_pair(key: str):

    # check if the key exists in the database
    if db.key_exists(key):
        # delete pair
        pair = db.delete(key)

        return pair

    raise HTTPException(
        status_code=404,
        detail=f"key {key} does not exist"
    )
