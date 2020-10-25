import csv


def show(list_of_subjects, n, day, subgroup):
    week_days = {0: 'Понедельник', 1: 'Вторник', 2: 'Среда',
                 3: 'Четверг', 4: 'Пятница', 5: 'Суббота', 6: 'Воскресенье'}

    return f'''{subgroup}\n\n{week_days[day]}:\n{list_of_subjects[n][0]}\n{list_of_subjects[n][1]}\n{list_of_subjects[n][2]}\n{list_of_subjects[n][3]}\n{list_of_subjects[n][4]}\n'''


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
            return f'''Воскресенье: выходной день :)'''
