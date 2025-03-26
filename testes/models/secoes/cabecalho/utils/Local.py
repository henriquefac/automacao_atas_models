from dataclasses import dataclass


@dataclass
class Local():
    value : str
    description : str = "Local da reunião. Se modalidade for Hibrida ou Online, informe plataforma"
    
    @classmethod
    def local(cls, local: str):
        return cls(local)
    
    def get(self):
        return self.value
