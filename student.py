from datetime import datetime, date
from pytz import timezone
from functions.cfg import *
from functions.general import *

ASIA = timezone('Asia/Yekaterinburg')


class Student:

    def __init__(self, student_id):
        self.id = student_id
        self.today = datetime.today().now(ASIA).weekday()
        self.week_num = date.today().isocalendar()[1]

    def get_schedule(self):
        error = "Вы не состоите в списке студентов :("
        if int(self.week_num) % 2 == 0:
            if self.id in FIRST_SUBGROUP:
                args = [N1, 'Числитель - 1 подгруппа']
            elif self.id in SECOND_SUBGROUP:
                args = [N2, 'Числитель - 2 подгруппа']
            else:
                return error

            return get_subjects(self.today, *args)

        else:
            if self.id in FIRST_SUBGROUP:
                args = [D1, 'Знаменатель - 1 подгруппа']
            elif self.id in SECOND_SUBGROUP:
                args = [D2, 'Знаменатель - 2 подгруппа']
            else:
                return error

            return get_subjects(self.today, *args)
