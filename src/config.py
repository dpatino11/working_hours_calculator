from utils import get_project_root


class Options:
    """
    Main class for the configuration of the project
    """

    def __init__(self):
        pass

    def parse(self, args=None):
        """Function tht recibes the args of the main run and opens each file 

        Args:
            args (_type_, optional): args from the main run. Defaults to None.
        """
        project_root = get_project_root()
        self.data_input = [
            open(f"{project_root}/input/{each}", "r")for each in args]
        print(f'number of files recived: {len(self.data_input)}')

    def config(self):
        """Functions that configure the payments system
        """
        self.payments_config= {
            'payments': {
                'WEEK_DAY': {
                    0: 25, 1: 25, 2: 25, 3: 25, 4: 25, 5: 25, 6: 25, 7: 25, 8: 25, 9: 18, 10: 18, 11: 18, 12: 18, 13: 18, 14: 18, 15: 18, 16: 18, 17: 18, 18: 20, 19: 20, 20: 20, 21: 20, 22: 20, 23: 20
                }, 'WEEKEND_DAY': {
                    0: 30, 1: 30, 2: 30, 3: 30, 4: 30, 5: 30, 6: 30, 7: 30, 8: 30, 9: 18, 10: 20, 11: 20, 12: 20, 13: 20, 14: 20, 15: 20, 16: 20, 17: 20, 18: 25, 19: 25, 20: 25, 21: 25, 22: 25, 23: 25
                }
            }, 'schedule': {
                'MO': 'WEEK_DAY', 'TU': 'WEEK_DAY', 'WE': 'WEEK_DAY', 'TH': 'WEEK_DAY', 'FR': 'WEEK_DAY', 'SA': 'WEEKEND_DAY', 'SU': 'WEEKEND_DAY'
            }
        }
        print(f'config payments done:')
 
