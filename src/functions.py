from datetime import datetime
from config import Options

class Process:

    def __init__(self):
        pass

    def read_files(file_list:list)->list:
        """_summary_

        Args:
            file_list (list): _description_

        Returns:
            list: _description_
        """
        lines = [line for each in file_list for line in each.read().split() ]
        print(f"number of lines read: {len(lines)}")
        return lines
           
    def calulate_payment(configuration:dict , workdays_hours:list) -> str:
        """_summary_

        Args:
            configuration (Options): _description_
            workdays_hours (list): _description_

        Returns:
            str: _description_
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
            