from pydantic import BaseModel, Field, field_validator
from typing import Tuple
from datetime import date
import json

class Autor(BaseModel):
    value: str = Field(...,description= "Nome do autor responsavel pela ATA", min_length=3, max_length=100)

    @field_validator("value")
    @classmethod
    def validate_autor(cls, value):
        if not isinstance(value, str):
            raise ValueError("Valor de Autor tem que ser uma string")
        if value.strip() == "":  
            raise ValueError("Nome do autor não pode estar vazio")
        return value  
        
if __name__ == "__main__":
    print(json.dumps(Autor.model_json_schema(), indent=4, ensure_ascii=False))