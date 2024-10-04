import json

from model import StatusPage

schema = StatusPage.model_json_schema()

with open("generated_schema.json", "w") as out_file:
    out_file.write(json.dumps(schema, indent=2))
