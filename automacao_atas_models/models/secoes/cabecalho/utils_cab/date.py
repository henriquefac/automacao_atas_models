from pydantic import BaseModel, Field, field_validator
import json


class Date(BaseModel):
    dia: int = Field(..., description="Dia da Reunião", ge=1, le=31)
    mes: int = Field(..., description="Mês da Reunião", ge=1, le=12)
    ano: int = Field(..., description="Ano da Reunião", ge=1)
    
    
    @field_validator("dia", mode="after")
    @classmethod
    def validar_dia(cls, dia: int, values) -> int:
        mes = values.get("mes")
        ano = values.get("ano")
        
        if mes and ano:
            if mes in {1,3,5,7,8,10,12}:
                dias_no_mes = 31
            elif mes in {4, 6, 9, 11}:
                dias_no_mes = 30
            else:
                dias_no_mes = 29 if cls.is_bissexto(ano) else 28
            if not (1 <= dia <= dias_no_mes):
                raise ValueError(f"Data inválida: {dia}/{mes}/{ano} não existe!")
            
        return dia
    @staticmethod
    def is_bissexto(ano: int) -> bool:
        """Verifica se um ano é bissexto."""
        return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
    
if __name__ == "__main__":
    print(json.dumps(Date.model_json_schema(), indent=4))