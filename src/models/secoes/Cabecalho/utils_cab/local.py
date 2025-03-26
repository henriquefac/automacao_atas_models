from pydantic import BaseModel, Field, field_validator
import json
class Local(BaseModel):
    value : str = Field(..., description="Local da reunião. Se modalidade for Hibrida ou Online, informe plataforma")


    @field_validator("value")
    @classmethod
    def validate_local(cls, value: str) -> str:
        """Valida se o valor informado para local é uma string válida."""
        if not isinstance(value, str):
            raise ValueError("O local deve ser uma string.")
        
        if not value.strip(): 
            raise ValueError("O local da reunião não pode estar vazio.")

        return value

if __name__ == "__main__":
    print(json.dumps(Local.model_json_schema(), indent=4, ensure_ascii=False))