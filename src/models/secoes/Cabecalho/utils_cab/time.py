from pydantic import BaseModel, Field
import json

class Time(BaseModel):
    horas: int = Field(..., description="Horas", ge=0, lt=24)
    minutos: int = Field(..., description="Minutos", ge=0, lt=60)
    

if __name__ == "__main__":
    print(json.dumps(Time.model_json_schema(), indent=4))
    
    