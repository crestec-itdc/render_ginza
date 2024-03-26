from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

    #print(BaseModel)

@app.get("/")
async def root():
    return {"message": "Hello World2"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

@app.post("/items")
def update_item(item: Item):
    print(item.name)
    return {"item_name": item.name, "twice price": item.price * 2}




#from fastapi import FastAPI

#app = FastAPI()


#@app.get("/items/{item_id}")
#def read_item(item_id: int, q: str = None):
#    if q:
#        return {"item_id": item_id, "q": q}
#    return {"item_id": item_id}



#from pydantic import BaseModel

#class Item(BaseModel):
#    name: str
#    price: float

#@app.post("/items")
#def update_item(item: Item):
#    return {"item_name": item.name, "twice price": item.price * 2}

