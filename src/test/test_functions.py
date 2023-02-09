import pytest
from functions import Process

@pytest.mark.parametrize(['input', 'config_dict', 'expected'], [
    [['MO10:00-12:00', 'TU10:00-12:00', 'TH07:00-03:00', 'SA14:00-18:00', 'SU20:00-21:00']
    ,{'payments': {
            'WEEK_DAY': {
                0: 25, 1: 25, 2: 25, 3: 25, 4: 25, 5: 25, 6: 25, 7: 25, 8: 25, 9: 18, 10: 18, 11: 18, 12: 18, 13: 18, 14: 18, 15: 18, 16: 18, 17: 18, 18: 20, 19: 20, 20: 20, 21: 20, 22: 20, 23: 20
            }, 'WEEKEND_DAY': {
                0: 30, 1: 30, 2: 30, 3: 30, 4: 30, 5: 30, 6: 30, 7: 30, 8: 30, 9: 18, 10: 20, 11: 20, 12: 20, 13: 20, 14: 20, 15: 20, 16: 20, 17: 20, 18: 25, 19: 25, 20: 25, 21: 25, 22: 25, 23: 25
            }
        }
        ,'schedule': {
            'MO': 'WEEK_DAY', 'TU': 'WEEK_DAY', 'WE': 'WEEK_DAY', 'TH': 'WEEK_DAY', 'FR': 'WEEK_DAY', 'SA': 'WEEKEND_DAY', 'SU': 'WEEKEND_DAY'
        }
    }
    ,{'response': 227, 'response_day': [{'day_name': 'MO', 'start_time': 10, 'end_time': 12, 'day_week': 'WEEK_DAY', 'workdays_hours': ['MO10:00-12:00', 'TU10:00-12:00', 'TH01:00-03:00', 'SA14:00-18:00', 'SU20:00-21:00'], 'response': 36}, {'day_name': 'TU', 'start_time': 10, 'end_time': 12, 'day_week': 'WEEK_DAY', 'workdays_hours': ['MO10:00-12:00', 'TU10:00-12:00', 'TH01:00-03:00', 'SA14:00-18:00', 'SU20:00-21:00'], 'response': 36}, {'day_name': 'TH', 'start_time': 1, 'end_time': 3, 'day_week': 'WEEK_DAY', 'workdays_hours': ['MO10:00-12:00', 'TU10:00-12:00', 'TH01:00-03:00', 'SA14:00-18:00', 'SU20:00-21:00'], 'response': 50}, {'day_name': 'SA', 'start_time': 14, 'end_time': 18, 'day_week': 'WEEKEND_DAY', 'workdays_hours': ['MO10:00-12:00', 'TU10:00-12:00', 'TH01:00-03:00', 'SA14:00-18:00', 'SU20:00-21:00'], 'response': 80}, {'day_name': 'SU', 'start_time': 20, 'end_time': 21, 'day_week': 'WEEKEND_DAY', 'workdays_hours': ['MO10:00-12:00', 'TU10:00-12:00', 'TH01:00-03:00', 'SA14:00-18:00', 'SU20:00-21:00'], 'response': 25}]}],
    ["should not pass"
    ,{'payments': {
            'WEEK_DAY': {
                0: 25, 1: 25, 2: 25, 3: 25, 4: 25, 5: 25, 6: 25, 7: 25, 8: 25, 9: 18, 10: 18, 11: 18, 12: 18, 13: 18, 14: 18, 15: 18, 16: 18, 17: 18, 18: 20, 19: 20, 20: 20, 21: 20, 22: 20, 23: 20
            }, 'WEEKEND_DAY': {
                0: 30, 1: 30, 2: 30, 3: 30, 4: 30, 5: 30, 6: 30, 7: 30, 8: 30, 9: 18, 10: 20, 11: 20, 12: 20, 13: 20, 14: 20, 15: 20, 16: 20, 17: 20, 18: 25, 19: 25, 20: 25, 21: 25, 22: 25, 23: 25
            }
        }
        ,'schedule': {
            'MO': 'WEEK_DAY', 'TU': 'WEEK_DAY', 'WE': 'WEEK_DAY', 'TH': 'WEEK_DAY', 'FR': 'WEEK_DAY', 'SA': 'WEEKEND_DAY', 'SU': 'WEEKEND_DAY'
        }
    }
    ,{'response': f'Error calculating day payment',
                        'response_day': f'Error calculating day payment'}],
    #[['MO18:00-12:00', 'TU10:00-12:00'],  {'response': f'Error calculating day payment','response_day': f'Error calculating day payment'}],
    #[['KO18:00-12:00'],  {'response': f'Error calculating day payment','response_day': f'Error calculating day payment'}],
])
def test_calculate_payment(input, config_dict, expected):
    response =Process().calulate_payment(config_dict, input)
    assert response == expected
