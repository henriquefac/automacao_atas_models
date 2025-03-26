from dataclasses import dataclass

@dataclass
class Autor():
    value : str 
    description : str = "Nome do autor responsavel pela ATA"
    
    @classmethod
    def autor(cls, autor:str):
        return cls(autor)
    
    def get(self):
        return self.get