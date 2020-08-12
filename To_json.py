import json
import functools

def to_json(ine):
    @functools.wraps(ine)
    def wrapped(*args,**kwargs):
        json_formatted_str = json.dumps(ine(*args,**kwargs))
        return(json_formatted_str)
    return(wrapped)




@to_json
def get_data():
    return {
        'data': 42
    }

#For commit
