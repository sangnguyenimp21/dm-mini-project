import json
from os.path import exists
 
def read_sidebar_fields(path = 'sidebar.json'):
    file_exists = exists(path)
    if not file_exists:
        return []
    f = open(path)
    data = json.load(f)
    return data['Fields']