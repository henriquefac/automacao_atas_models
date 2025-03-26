from enum import StrEnum
from pydantic import BaseModel, Field, field_validator
import json

class ModalidadeEnum(StrEnum):
    HIBRIDO = "hibrido"
    ONLINE = "online"
    PRESENCIAL = "presencial"  # Corrigido erro de digitação

class Modalidade(BaseModel):
    value: str = Field(..., 
        description="Tipo de modalidade da reunião.",
        exemples=["online", "hibrido", "presencial"])

    @field_validator("value", mode="before")
    @classmethod
    def validar_modalidade(cls, v):
        if isinstance(v, str):
            v = v.lower() 
        
        try:
            ModalidadeEnum(v)
        except:
            raise ValueError(f"'{v}' não é uma modalidade válida")
            
        return v

if __name__ == "__main__":
    Modalidade(value="Hibrido")
