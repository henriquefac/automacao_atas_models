from pydantic import BaseModel, Field, field_validator
from .utils_pautas import *
import json
class Pautas(BaseModel):
    pautas: list[UnidadeProponente] = Field(..., 
        description="Lista de unidades proponentes e suas respectivas pautas.",
        examples=[
            [
                {"unidade": "Departamento de TI", "pautas": ["Melhoria do sistema", "Atualizacao de servidores"]},
                {"unidade": "RH", "pautas": ["Plano de beneficios", "Contratacao de estagiarios"]}
            ]
        ]
    )
    
    @classmethod
    def expand_schema(cls):
        schema = cls.model_json_schema()
        
        schema["properties"]["pautas"]["items"] = UnidadeProponente.model_json_schema()["properties"]
        schema.pop("$defs", None)
        return schema
    
    @classmethod
    def simple_schema(cls):
        schema = cls.expand_schema()
        schema = schema["properties"]["pautas"]
        schema.pop("title")
        schema.pop("type")
        return schema
    
if __name__ == "__main__":
    print(json.dumps(Pautas.simple_schema(), indent=4))