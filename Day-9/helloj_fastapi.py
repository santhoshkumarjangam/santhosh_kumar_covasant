from fastapi import FastAPI
from pydantic import BaseModel
from dicttoxml import dicttoxml


app = FastAPI()

class Model(BaseModel):
    name : str = "santhosh"

model = Model()

@app.get("/hello")
def hello():
    return {"Hello": model.name}

@app.get("/hello/{format}")
def hello(format):
    if format.upper() == "XML":
        data = {"Hello": model.name}
        xml_data = dicttoxml(data, custom_root='Greeting', attr_type=False)

        return xml_data
    else:
        return {"Hello": model.name}


@app.post("/hello")
def hello(body: Model):
    model.name = body.name
    return {"name":model.name, "updated":"True"}