from automacao_atas_models import Ata
import json
print(json.dumps(Ata.model_json_schema(), indent=4))