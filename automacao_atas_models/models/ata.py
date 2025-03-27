from pydantic import BaseModel, Field, field_validator
import json

from .secoes import Cabecalho, Participantes, Pautas

# criar classe da ata de reunião, par criar o json


class Ata(BaseModel):
    cabecalho : Cabecalho = Field(..., description="Cabecalho da Ata")
    participantes : Participantes = Field(..., description="Participantes da reunião: presentes, convidados e ausentes")
    pautas : Pautas = Field(..., description="Pautas associadas a unidade proponente")    


if __name__ == "__main__":
    print(json.dumps(Cabecalho.simple_schema(), indent=4))
    print("="*40)
    print(json.dumps(Participantes.simple_schema(), indent=4))
    print("="*40)
    print(json.dumps(Pautas.simple_schema(), indent=4))