import os
from pathlib import Path
import json
somestring = """
    {
        "name":"delta",
        "age":14
    }
"""
appdata = os.getenv("APPDATA")
config_dir = Path(appdata)/"Key2Click"
config_dir.mkdir(exist_ok=True)
config_file = config_dir/"shortcuts.json"
json_form = json.loads(somestring)
with open(config_file,"w") as json_file:
    json.dump(json_form,json_file,indent=2)
