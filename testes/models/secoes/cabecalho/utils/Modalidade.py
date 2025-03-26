from dataclasses import dataclass



class Hibrido():
    def value(self) -> str:
        return "Hibrido"

class Online():
    def value(self) -> str:
        return "Online"

class Presencial():
    def value(self) -> str:
        return "Presencial"

@dataclass
class Modalidade():
    value : Presencial | Online | Hibrido
    description : str = "Modalidade da reunião. Pode ser Presencial, Hibrido ou Online"
    
    @classmethod
    def modalidade(cls, modalidade: int) -> 'Modalidade':
        if modalidade == 0:
            value = Presencial()
        elif modalidade == 1:
            value = Online()
        elif modalidade == 2:
            value = Hibrido()
        else:
            raise ValueError(f"Não há modalide para o seguinte indice fornecido: {modalidade}")
        
        return cls(value) 
    
    def get(self):
        return self.value.value()
