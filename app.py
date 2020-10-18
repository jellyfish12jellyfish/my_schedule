from datetime import *
import os
from pytz import timezone
from vkbottle import Bot, Message
from vkbottle.keyboard import Keyboard, Text

from student import Student

ASIA = timezone('Asia/Yekaterinburg')

token = os.environ['TOKEN']
bot = Bot(token)

keyboard = Keyboard(one_time=False)
keyboard.add_row()

keyboard.add_button(Text(label="Сегодня"), color="primary")
keyboard.add_button(Text(label="Завтра"), color="positive")


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
        student.week_num = (datetime.today().now(ASIA) + timedelta(days=1)).strftime("%U")

        return student.get_schedule()

    except Exception as ex:
        print(f'> error: {ex}')
        return "Что-то пошло не так!"


if __name__ == '__main__':
    bot.run_polling()
