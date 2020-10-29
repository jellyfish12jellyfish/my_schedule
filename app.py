from datetime import *
import os
from pytz import timezone
from vkbottle import Bot, Message
from vkbottle.keyboard import Keyboard, Text
from functions import cfg

from student import Student

ASIA = timezone('Asia/Yekaterinburg')

USERS_IDS = cfg.FIRST_SUBGROUP + cfg.SECOND_SUBGROUP
WHITE_LIST = [443285989, 497524684, 236635200, 306226901]

token = os.environ['TOKEN']
bot = Bot(token)

keyboard = Keyboard(one_time=False)
keyboard.add_row()

keyboard.add_button(Text(label="Сегодня"), color="primary")
keyboard.add_button(Text(label="Завтра"), color="positive")


@bot.on.message(text="-help")
async def show_help(ans: Message):
    await ans(
        '-c ваше_сообщение_участникам (доступ ограничен);\n\nесли возникли проблемы, наберите админу: '
        '"-iss описание_вашей_проблемы";')


@bot.on.message(text="-iss <issue>")
async def show_ad(ans, issue):
    user = await bot.api.users.get(user_ids=ans.from_id)
    await bot.api.messages.send(user_ids=cfg.ADMIN, random_id=0,
                                message=f'У {user[0].first_name} {user[0].last_name} проблема:\n\n{issue}')


@bot.on.message(text=["-c <msg>", "-с <msg>"])
async def show_ad(ans, msg):
    if ans.from_id not in WHITE_LIST:
        return "К сожалению, у вас нет доступа к данной команде :("
    user = await bot.api.users.get(user_ids=ans.from_id)
    await bot.api.messages.send(user_ids=USERS_IDS, random_id=0,
                                message=f'Объявление от {user[0].first_name}:\n{msg}')


@bot.on.message(text=['клаву', '-к', '-k', 'клавиатуру, пожалуйста'], lower=True)
async def wrapper(ans: Message):
    await ans('Держите.', keyboard=keyboard.generate())


@bot.on.message(text=["расписание", "Сегодня"], lower=True)
async def get_today_schedule(ans: Message):
    try:
        student = Student(ans.from_id)
        return student.get_schedule()

    except Exception as ex:
        print(f'> error: {ex}')
        return "Что-то пошло не так!"


@bot.on.message(text=["Завтра"], lower=True)
async def get_tomorrow_schedule(ans: Message):
    try:
        student = Student(ans.from_id)
        student.today = (datetime.today().now(ASIA) + timedelta(days=1)).weekday()
        # student.week_num = (datetime.today().now(ASIA) + timedelta(days=1)).strftime("%U")
        student.week_num = (date.today() + timedelta(days=1)).isocalendar()[1]

        return student.get_schedule()

    except Exception as ex:
        print(f'> error: {ex}')
        return "Что-то пошло не так!"


@bot.on.message(text='')
async def on_unexpected_msg(ans: Message):
    await ans('Команда не найдена, попробуйте набрать: -help')


if __name__ == '__main__':
    bot.run_polling()
