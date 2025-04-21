import json
from fastapi import FastAPI
from dicttoxml import dicttoxml

from data import weather_data, cities

app = FastAPI()

@app.get("/getwhether/{city}")
def index(city, format : str|None = "JSON"):
    if format.upper() == "XML":
        json_data = json.dumps(weather_data.get(city.capitalize(), {"details for city":"Not Found"}))
        data_dict = json.loads(json_data)
        xml_data = dicttoxml(data_dict, custom_root='weather', attr_type=False)

        return xml_data
    else:
        return weather_data.get(city.capitalize(), {"details for city":"Not Found"})
    
@app.get("/cities")
def all():
    json_cities = json.dumps(cities.get("cities"))

    return json_cities 
