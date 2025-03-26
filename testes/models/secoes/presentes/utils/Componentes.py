from dataclasses import dataclass

@dataclass
class Nome:
    value: str
    
    description : str = "Nome do indivíduo"
    
@dataclass
class Cargo:
    value: str
    
    description: str = "Cargo do indivíduo"

@dataclass
class Individuo:
    nome: Nome
    cargo: Cargo
    
    description: str = "Indivíduo referente a reunião"