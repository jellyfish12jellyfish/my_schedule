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
        print(self.today, self.week_num)

        if int(self.week_num) % 2 == 0:
            if self.id in FIRST_SUBGROUP:
                return get_subjects(self.today, N1, subgroup='Числитель - 1 подгруппа')
            elif self.id in SECOND_SUBGROUP:
                return get_subjects(self.today, N2, subgroup='Числитель - 2 подгруппа')
            else:
                return "Вы не состоите в списке студентов :("

        else:
            if self.id in FIRST_SUBGROUP:
                return get_subjects(self.today, D1, subgroup='Знаменатель - 1 подгруппа')
            elif self.id in SECOND_SUBGROUP:
                return get_subjects(self.today, D2, subgroup='Знаменатель - 2 подгруппа')
            else:
                return "Вы не состоите в списке студентов :("
