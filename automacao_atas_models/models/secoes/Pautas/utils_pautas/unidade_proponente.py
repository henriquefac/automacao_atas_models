from pydantic import BaseModel, Field, field_validator

class UnidadeProponente(BaseModel):
    unidade: str = Field(..., description="Nome da unidade proponente.")
    pautas: list[str] = Field(..., description="Lista de pautas da unidade proponente.")

