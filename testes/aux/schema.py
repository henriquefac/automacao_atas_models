from dataclasses import is_dataclass, fields
from typing import Dict, Any, get_origin, get_args

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