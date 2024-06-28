from datetime import datetime, timedelta, date


def get_week_dates(dateVar, week):
    """
    weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
                    0          1        2           3           4           5           6       
    """
    init_day = dateVar.weekday()
    if init_day == 0:
        start_date = datetime.strptime(f'{dateVar.year}-{week}-1', "%Y-%W-%w")
        end_date = start_date + timedelta(days = 4)
        return start_date, end_date
    elif init_day == 1: 
        start_date = datetime.strptime(f'{dateVar.year}-{week}-2', "%Y-%W-%w")
        end_date = start_date + timedelta(days = 3)
        return start_date, end_date
    elif init_day == 2: 
        start_date = datetime.strptime(f'{dateVar.year}-{week}-3', "%Y-%W-%w")
        end_date = start_date + timedelta(days = 2)
        return start_date, end_date
    elif init_day == 3:
        start_date = datetime.strptime(f'{dateVar.year}-{week}-4', "%Y-%W-%w")
        end_date = start_date + timedelta(days = 1)
        return start_date, end_date
    elif init_day == 4:
        start_date = datetime.strptime(f'{dateVar.year}-{week}-5', "%Y-%W-%w")
        end_date = start_date + timedelta(days = 0)
        return start_date, end_date
    else:
        return None, None

def create_file(company, dateVar, yearVar):
    current_week = dateVar.isocalendar()[1]

    # file 1
    start_date, end_date = get_week_dates(dateVar, current_week)
    if not start_date == None and not end_date == None: 
        week_str = f'{company}--{yearVar}__week{current_week}_{start_date.strftime("%d%b")}-{end_date.strftime("%d%b")}'
        file_name = f'{week_str}.txt'
        print(file_name)   

    # other files
    for week in range(current_week+1, 53):
        day_offset = (week - 1) * 7
        first_week_day = date(dateVar.year, 1, 1) + timedelta(days=day_offset)

        start_date, end_date = get_week_dates(first_week_day, week)
        week_str = f'{company}--{yearVar}__week{week}_{start_date.strftime("%d%b")}-{end_date.strftime("%d%b")}'
        file_name = f'{week_str}.txt'

        with open(file_name, 'w') as file:
            file.write('Sumary of the week: '+ week_str)
        print(f'File "{file_name}" criated.')

if __name__ == "__main__":
    _company = "<company name>"
    _today = datetime.today()
    """
        Specific day use i.e.:
        _today = datetime.strptime("2024-4-5", '%Y-%m-%d').date()
    """
    _year = date.today().year

    create_file(_company, _today, _year)

