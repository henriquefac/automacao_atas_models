from .utils_cab import *
from pydantic import BaseModel, Field, field_validator
from typing import Tuple, Union
import json

class Cabecalho(BaseModel):
    data : Date = Field(...,
        description="Data da Reunião")
    time : Time = Field(..., 
        description="Hórario da Reunião")
    modalidade : Modalidade = Field(...,
        description="Modalidade da Reunião")
    local : Local = Field(...,
        description="Local que foi realizada a reunião. Se a modalidade for online, indique a plataforma")
    autor : Autor = Field(...,
        description="Responsável pela ATA")
    
    @field_validator("data", mode="before")
    @classmethod
    def validade_data(cls, v: Union[Tuple[int, int, int], Date]):
        if isinstance(v, tuple):
            return Date(dia=v[0], mes=v[1], ano=v[2])
        return v
    
    @field_validator("time", mode="before")
    @classmethod
    def validate_time(cls, v: Union[Tuple[int, int], Time]):
        if isinstance(v, tuple):
            return Time(horas=v[0], minutos=v[1])
        return v
    
    @field_validator("modalidade", mode="before")
    @classmethod
    def validate_modalidade(cls, v : Union[Tuple[str], Modalidade]):
        if isinstance(v, tuple):
            return Modalidade(value=v[0])
        return v

    @field_validator("local", mode="before")
    @classmethod
    def validate_local(cls, v : Union[Tuple[str], Local]):
        if isinstance(v, tuple):
            return Local(value=v[0])
        return v
    
    @field_validator("autor", mode="before")
    @classmethod
    def validade_autor(cls, v: Union[Tuple[str], Autor]):
        if isinstance(v, tuple):
            return Autor(value=v[0])
        return v

    
    @classmethod
    def expand_schema(cls):
        """Gera um JSON Schema sem $defs, expandindo os modelos aninhados."""
        schema = cls.model_json_schema()

        # Substituir as referências de $defs pelos esquemas reais dos modelos aninhados
        schema["properties"]["data"] = Date.model_json_schema()
        schema["properties"]["time"] = Time.model_json_schema()
        schema["properties"]["modalidade"] = Modalidade.model_json_schema()
        schema["properties"]["local"] = Local.model_json_schema()
        schema["properties"]["autor"] = Autor.model_json_schema()

        # Remover o bloco $defs, pois já expandimos os modelos aninhados
        schema.pop("$defs", None)
    
        return schema
    
    @classmethod
    def simple_schema(cls):
        """Gera um JSON simplificado para requisições a LLMs"""
        schema = cls.expand_schema()
        simple_json = {}

        for key, item in schema["properties"].items():
            
            if "properties" in item:  # Verifica se é um objeto aninhado
                simple_json[key] = {prop:  item["properties"][prop] for prop in item["properties"].keys()}
            else:
                simple_json[key] = "<preencher>"

        return simple_json
    
    
if __name__ == "__main__":
    print(json.dumps(Cabecalho.simple_schema(), indent=4))
