from pathlib import Path
import json
def get_project_root() -> Path:
    """function that returns the project root
            
        Returns:
            str: project root
    """
    return Path(__file__).parent.parent

def write_json_output(file_path, dict) :
    """function that writes json output in the output folder
    """
    with open(file_path, "w") as outfile:
        json.dump(dict, outfile)