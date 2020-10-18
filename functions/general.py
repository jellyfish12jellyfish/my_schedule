import csv


def show(list_of_subjects, n, day, subgroup):
    week_days = {0: 'Понедельник', 1: 'Вторник', 2: 'Среда',
                 3: 'Четверг', 4: 'Пятница', 5: 'Суббота', 6: 'Воскресенье'}

    return f'''
            {subgroup}
            
            {week_days[day]}:
            {list_of_subjects[n][0]}
            {list_of_subjects[n][1]}
            {list_of_subjects[n][2]}
            {list_of_subjects[n][3]}
            {list_of_subjects[n][4]}
            '''


def get_subjects(today, n, subgroup):
    with open('student_schedule.csv') as f:
        subjects = csv.reader(f)
        subjects = list(subjects)

        # monday
        if today == 0:
            return show(subjects, n, today, subgroup)

        # tuesday
        elif today == 1:
            return show(subjects, n + 2, today, subgroup)

        # wednesday
        elif today == 2:
            return show(subjects, n + 4, today, subgroup)

        # thursday
        elif today == 3:
            return show(subjects, n + 6, today, subgroup)

        # friday
        elif today == 4:
            return show(subjects, n + 8, today, subgroup)

        # saturday
        elif today == 5:
            return show(subjects, n + 10, today, subgroup)

        # sunday or error
        else:
            return f'''
            Занятия не найдены...
            
            Скорее всего, сегодня - воскресенье.
            '''