import json
import base64


def json_to_base64(json_data):
    # Convierte el JSON a una cadena
    json_str = json.dumps(json_data)

    # Codifica la cadena JSON a Base64
    base64_data = base64.b64encode(json_str.encode('utf-8'))

    # Decodifica la representación de bytes a una cadena legible
    base64_str = base64_data.decode('utf-8')

    return base64_str


#path = './pe-fesa-gm-gmtm-explore-dev-c750746c0fad.json'
path = './versatile-art-391814-f8de69376fbd.json'
# open json file
with open(path) as json_file:
    json_data = json.load(json_file)

    # Convierte el JSON a Base64
    base64_str = json_to_base64(json_data)
    # Imprime el resultado
    print(base64_str)
