from functions import Process

class Project:
    """
    
    """
    def __init__(self, options):
        self.options = options
        self.process = Process()

    def calculate_payment(self)->list:
        """_summary_

        Returns:
            list: _description_
        """
        data_to_calculate_payment = Process.read_files(self.options.data_input)
        total_data = []
        for data in data_to_calculate_payment:
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
        return total_data
            
