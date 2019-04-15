import os
from pathlib import Path
import json

convert_dir = '/convert'  # Location for input files

path = Path(os.path.dirname(__file__))
content_path = Path(os.path.dirname(__file__) + convert_dir)

dict_object = dict()

with open('modules.json', 'w') as data:
    data.write("{\n")

    for d, s, f in os.walk(content_path):
        for file in f:
            if '.gitignore' not in file:
                name = file.split(".")[0]
                html = os.path.join(d, file)                
                
                with open(html, 'r') as html:
                    dict_object[name] = html.read()
                    
                    data.write('    "{}": {{\n'.format(name))
                    data.write('        "scope": "html",\n')
                    data.write('        "prefix": "{}",\n'.format(name))
                    data.write('        "body": {},\n'.format(json.dumps(dict_object[name])))
                    data.write('        "description": "{}"\n    }},\n'.format(name))

    data.write("\n}")

print(f'All good.')