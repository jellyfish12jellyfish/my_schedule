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
        self.error = "Вы не состоите в списке студентов :("

    def __check_id(self, flag1=None, flag2=None):
        if self.id in FIRST_SUBGROUP:
            args = [flag1, 'Числитель - 1 подгруппа']
        elif self.id in SECOND_SUBGROUP:
            args = [flag2, 'Числитель - 2 подгруппа']
        else:
            return self.error

        return get_subjects(self.today, *args)

    def get_schedule(self):
        if int(self.week_num) % 2 == 0:
            self.__check_id(N1, N2)
            # if self.id in FIRST_SUBGROUP:
            #     args = [N1, 'Числитель - 1 подгруппа']
            # elif self.id in SECOND_SUBGROUP:
            #     args = [N2, 'Числитель - 2 подгруппа']
            # else:
            #     return self.error
            #
            # return get_subjects(self.today, *args)

        else:
            self.__check_id(D1, D2)
