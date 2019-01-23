from db import users_db
from bot import bot


def send_message_to_all_users(message: str):
    print("sfda")
    # Функция для рассылки, принимает сообщение
    if message != '':
        # Перебираем всех пользователей в бд
        for user in users_db.find():
            print(user)
            print(users_db.find())
            # Пытаемся отправить сообщение
            try:
                bot.send_message(user['chat_id'], message)
            # Если какая-то ошибка - выводим это
            except Exception as e:
                print('Something wrong')


if __name__ == '__main__':
    # Считываем сообщение с клавиатуры
    input_message = input('Введите сообщение для рассылки: ')
    send_message_to_all_users(input_message)
