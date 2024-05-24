from pydantic import BaseModel

class Data(BaseModel):
    temperature : float
    humidity : float
    light : float