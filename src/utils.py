from pathlib import Path
import json
def get_project_root() -> Path:
    """_summary_
            
        Returns:
            str: _description_
    """
    
    return Path(__file__).parent.parent

def write_json_output(file_path, dict) :
    """_summary_
            
        Returns:
            str: _description_
    """
    with open(file_path, "w") as outfile:
        json.dump(dict, outfile)
    return True