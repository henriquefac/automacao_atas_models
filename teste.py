from automacao_atas_models import Ata, participantes
import json
print(json.dumps(participantes.Presente.model_json_schema(), indent=4))
