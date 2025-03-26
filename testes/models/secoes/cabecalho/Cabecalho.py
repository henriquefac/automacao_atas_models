from dataclasses import dataclass
from utils.Date import Date
from utils.Time import Time
from utils.Modalidade import Modalidade
from utils.Local import Local
from utils.Autor import Autor

from dataclasses import is_dataclass, fields
from typing import Dict, Any, get_origin, get_args

import json

def generate_schema(cls) -> Dict[str, Any]:
    scheme = {}
    
    if is_dataclass(cls):
        annotations = {field.name: field.type for field in fields(cls)}
    else:
        annotations = getattr(cls, "__annotations__", {})
        
    for field_name, field_type in annotations.items():
        origin = get_origin(field_type)  
        args = get_args(field_type)
        
        if origin:  
            
            compound_field = origin.__name__
            list_args = [generate_schema(arg) if hasattr(arg, "__annotations__") and len(arg.__annotations__) > 0  
                        else arg.__name__ for arg in args]

            compound_field = compound_field + "[" + ",".join(list_args) + "]"
            scheme[field_name] = compound_field
            continue
        
        
        if hasattr(field_type, "__annotations__"):
            scheme[field_name] = generate_schema(field_type)
        else:
            scheme[field_name] = cls.description if field_name == "description" else field_type.__name__  
            
    
    return scheme  


@dataclass
class Cabecalho():
    data : Date
    horario : Time
    modalidade : Modalidade
    local : Local
    autor : Autor
    
    description : str = "Cabecalho da ATA, contendo informacoes sobre: data, horario, modalidade, local e autor da ATA"
    
    @classmethod
    def cabecalho(cls, data : Date, horario : Time, modalidade : Modalidade
                  , local : Local, autor : Autor):
        return cls(data, horario, modalidade, local, autor)
    
    @staticmethod
    def getData(dia : int, mes : int, ano : int):
        return Date.date(dia, mes, ano)
    
    @staticmethod
    def getHorario(horas : int, minutos : int):
        return Time.time(horas, minutos)
    
    @staticmethod
    def getModalidade(modalidade : int):
        return Modalidade.modalidade(modalidade)
    
    @staticmethod
    def getLocal(local):
        return Local.local(local)
    
    @staticmethod
    def getAutor(autor):
        return Autor.autor(autor)
    
if __name__ == "__main__":
    print(json.dumps(generate_schema(Cabecalho), indent=5))