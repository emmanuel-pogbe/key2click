#JavaScript Object Notation
import json
#load method loads a python file
#loads method loads a string

#dump method converts data to json file
#dumps method converts data to json string
#json.dump(data, file_name, indent = 2)
states = '''
    {
        "states": [
            {
            "name": "Alabama",
            "abbreviation": "AL"
            },
            {
            "name": "Alaska",
            "abbreviation": "AK"
            },
            {
            "name": "Arizona",
            "abbreviation": "AZ"
            }
        ]
    }
'''
data = json.loads(states)
del data.get("states")[-1]
my_string = json.dumps(data,indent=2)
print(my_string)