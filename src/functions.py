from datetime import datetime
from config import Options

class Process:
    """
    Main Class for the functions of the script
    """

    def __init__(self):
        pass

    def read_files(file_list:list)->list:
        """Function that recive a list of files to return the lines in each file

        Args:
            file_list (list): list of files to read lines from

        Returns:
            list: list of lines in each file
        """
        lines = [line for each in file_list for line in each.read().split() ]
        print(f"number of lines read: {len(lines)}")
        return lines
           
    def calulate_payment(configuration:dict , workdays_hours:list) -> dict:
        """Function that calculates the payment amount for each workday and the hours of the workdays

        Args:
            configuration (dict): configuration dictionary for the calculation of the payment amount
            workdays_hours (list): list of workdays and the hours of the workdays

        Returns:
            dict: dict with the payment amount and the details of the payment amount for each workday
        """
        total_payment =0
        day_payments =[]
        try:
            for day in workdays_hours:
                    day_name = day[0:2]
                    time = day[2:].split('-')
                    start_time = datetime.strptime(time[0], "%H:%M")
                    end_time = datetime.strptime(time[1], "%H:%M")
                    hours_delta = (end_time-start_time).total_seconds() /(60*60)
                    if hours_delta<0:
                        raise ValueError('invalid day range')
                    day_week = configuration['schedule'][day_name] 
                    daypayment = 0
                    for i in range(int(hours_delta)):
                        daypayment += configuration['payments'][day_week][start_time.hour + i]
                    day_payments.append({
                        'day_name': day_name
                        ,'start_time': start_time.hour
                        ,'end_time': end_time.hour
                        ,'day_week': day_week
                        ,'workdays_hours': workdays_hours
                        ,'response': daypayment
                    })
                    total_payment += daypayment
            return {
                'response': total_payment
                ,'response_day': day_payments
            }
        except Exception as error:
                return {
                'response': f'Error calculating day payment'
                ,'response_day': f'Error calculating day payment'
            }
            