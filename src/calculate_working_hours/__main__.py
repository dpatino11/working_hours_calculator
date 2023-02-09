import sys
from config import Options
from calculate_days import Project
from utils import get_project_root, write_json_output
def run_project(args):
    """
    Main Function to run the project
    """
    options = Options()
    options.config()
    options.parse(args[1: ])
    #print(options.data_input)
    project = Project(options)
    data_payments = project.calculate_payment()
    write_json_output(f'{get_project_root()}/output/test_file.json', data_payments)

if __name__ == '__main__':
    try:
        run_project(sys.argv)
    except Exception as error:
        print('Error:', error)