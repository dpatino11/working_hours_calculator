from functions import Process

class Project:
    """
    Main class for working hours project
    """
    def __init__(self, options):
        self.options = options
        self.process = Process()

    def calculate_payment(self)->list:
        """main function that recibes the input files in the options class, reads each line in the files and calculates the pyment for each line
        Returns:
            list: list of the details for the calculation of each line in the multiple files
        """
        data_to_calculate_payment = Process.read_files(self.options.data_input)
        total_data = []
        for data in data_to_calculate_payment:
            try:
                name = data.split('=')[0]
                workdays_hours = data.split('=')[1].split(',')
                final_payment = Process.calulate_payment(self.options.payments_config,  workdays_hours)
                print(f"the payment for {name} is {final_payment['response']}")
                total_data.append({
                    'name': name
                    ,'workdays_hours': workdays_hours
                    ,'total_payment': final_payment['response']
                    ,'response_day': final_payment['response_day']
                })
            except:
                print(f"error in line {data}")
                total_data.append({
                    'name': data
                    ,'workdays_hours': 'error in line'
                    ,'total_payment': 'error in line'
                    ,'response_day': 'error in line'
                })
        return total_data
            
