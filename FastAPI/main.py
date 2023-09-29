from enum import Enum
from typing import Annotated

import pydantic
from fastapi import FastAPI
from fastapi import Query


class Item(pydantic.BaseModel):
    name: str = "vân anh"
    description: str | None = None
    price: float
    tax: float | None = None


class ModelName(str, Enum):
    resnet = "resnet"
    lenet = "lenet"
    alexnet = "alexnet"


app = FastAPI()


@app.post("/items")
async def create_item(item: Item):
    return item


@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dump()}
    if q:
        result.update({"q": q})
    return result


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    print(model_name.alexnet)
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {
        "model_name": model_name,
        "message": "have some residual"
    }


@app.get("/")
async def root():
    return {
        "message": "hello world"
    }


@app.get("/items/{id}")
async def return_items(id: int):
    return {"item_id": id}


@app.get("users/me")
async def read_user():
    return {
        "user_id": "lmao its me"
    }


@app.get("users/{id}")
async def read_user(id: str):
    return {
        "user_id": id
    }


@app.get("/file/{file_path : path}")
async def read_file(file_path: str):
    return {
        "file_path": file_path
    }


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


# @app.get("/items/")
# async def read_items(q: Annotated[list[str] | None, Query(max_length=50)] = "anh yeu em") -> dict:
#     # results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     # if q:
#     #     results.update(
#     #         {
#     #             "q": q
#     #         }
#     #     )
#     # return results
#     query_items: dict[str, list[str] | None] = {"q": q}
#     return query_items
# @app.get("/items/")
# async def read_items(q: Annotated[list[str] | None, Query()] = None):
#     query_items = {"q": q}
#     return query_items
@app.get("/items/")
async def read_items(q: Annotated[list[str], Query()] = []):
    query_items = {"q": q}
    return query_items


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        print(f"{q} is not null ")
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
