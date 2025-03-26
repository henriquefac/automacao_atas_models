from pydantic import BaseModel, Field, model_validator
import json

class Individuo(BaseModel):
    name: str = Field(..., description="Nome do Indivíduo")
    cargo: str = Field(..., description="Cargo ou função")

    @model_validator(mode="before")
    @classmethod
    def update_description(cls, values):
        """Atualiza a descrição do campo 'name' com base na classe filha."""
        if cls.__name__ != "Individuo":  # Evita modificar a classe base
            values["name"] = Field(..., description=f"Nome do participante {cls.__name__}")
        return values

class Presente(Individuo):
    name: str = Field(..., description="Nome do participante presente")

class Convidado(Individuo):
    name: str = Field(..., description="Nome do participante convidado")

class Ausente(Individuo):
    name: str = Field(..., description="Nome do participante ausente")
    
if __name__ == "__main__":
    print(json.dumps(Presente.model_json_schema(), indent=4))
    print(json.dumps(Convidado.model_json_schema(), indent=4))
    print(json.dumps(Ausente.model_json_schema(), indent=4)) 