from fastapi import FastAPI
from pydantic import BaseModel
import spacy

app = FastAPI()

class Item(BaseModel):
    value: str
    #price: float

    #print(BaseModel)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

@app.post("/items")
def update_item(item: Item):
    print(item.value)

    nlp = spacy.load('ja_ginza_electra') # or ja_ginza (in case with low memory)
    #f = open('out.txt','r',encoding='UTF-8')
    #src=f.read()
    src=item.value

    doc = nlp(src)
    output = ""
    for sent in doc.sents:
        print(sent)
        output = output + sent.text + "\n"
    #f.close()
    #return {"item_name": doc.sents}
    #return {"output": item.name, "twice price": item.price * 2}
    return {"output": output}




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

