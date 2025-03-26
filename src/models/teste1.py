from pydantic import BaseModel, Field
import json

class Endereco(BaseModel):
    rua: str = Field(..., description="Nome da rua")
    numero: int = Field(..., description="Número do endereço")

class Pessoa(BaseModel):
    nome: str = Field(..., description="Nome da pessoa")
    idade: int = Field(..., description="Idade da pessoa", ge=0)
    endereco: dict = Field(..., description="Endereço da pessoa")  # 🔹 Mudança importante

    @classmethod
    def expand_schema(cls):
        """Expande manualmente as classes aninhadas para evitar $defs."""
        schema = cls.model_json_schema()
        schema["properties"]["endereco"] = Endereco.model_json_schema()  # 🔹 Expande endereço manualmente
        return schema

if __name__ == "__main__":
    schema_sem_refs = Pessoa.expand_schema()  # 🔹 Usa a função para remover $defs
    print(json.dumps(schema_sem_refs, indent=4, ensure_ascii=False))    