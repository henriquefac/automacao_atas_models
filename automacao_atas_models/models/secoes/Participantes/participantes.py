from .utils_part import *
from pydantic import BaseModel, Field, field_validator
from typing import List, Tuple
import json

class Participantes(BaseModel):
    presentes : List[Presente] = Field(..., description="Lista dos Presentes")
    convidados : List[Convidado] = Field(..., description="Lista dos Convidados")
    ausentes : List[Ausente] = Field(..., description="Lista dos Ausentes")
    
    @classmethod
    def expand_schema(cls):
        """Expande os modelos aninhados para evitar referências '$defs' no JSON Schema."""
        schema = cls.model_json_schema()
        defs = schema.get("$defs", {})  

        dicts = [{key: item} for key, item in defs.items()]
        keys_properties = list(schema["properties"].keys())

        for key in keys_properties:
            ref_path = schema["properties"][key]["items"].get("$ref")
            if ref_path:
                name = ref_path.split("/")[-1]  
                
                schema["properties"][key]["items"] = next(
                    (dic[name]["properties"] for dic in dicts if name in dic),
                    schema["properties"][key]["items"]
                )

        schema.pop("$defs", None)
        return schema

    @classmethod
    def simple_schema(cls):
        """Expande os modelos aninhados para evitar referências '$defs' no JSON Schema."""
        schema = cls.model_json_schema()
        defs = schema.get("$defs", {})  

        dicts = [{key: item} for key, item in defs.items()]
        keys_properties = list(schema["properties"].keys())

        for key in keys_properties:
            ref_path = schema["properties"][key]["items"].get("$ref")
            if ref_path:
                name = ref_path.split("/")[-1]  
                
                schema["properties"][key] = next(
                    (dic[name]["properties"] for dic in dicts if name in dic),
                    schema["properties"][key]["items"]
                )

        schema.pop("$defs", None)
        return schema


if __name__ == "__main__":
    pass

    print(json.dumps(Participantes.model_json_schema(), indent=4))