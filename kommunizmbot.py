import random

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

d = {}


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random.randint(0, 2048)})


# API-ключ созданный ранее
token = "c66136b023bae4f258d25e853cecab8a228c71a2a3b91f200ce77de838009f50f704a38df3262783da8d0"

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)

print("Бот запущен")
# Основной цикл
for event in longpoll.listen():

    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:

        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:
            
            # Сообщение от пользователя
            request = event.text

            # Каменная логика ответа
            if request == "1":
                write_msg(event.user_id, " У нас есть 2 вида пиара. Реклама и Взаимо-Пиар.")
                write_msg(event.user_id, " По всем вопросам писать ему - https://vk.com/sexy.senya")
            elif request == "2":
                write_msg(event.user_id, "Заполняй анкету - https://vk.com/ikm_meme?w=app5619682_-176556657")
            else:
                if d.get(event.user_id, 0) == 0:
                    write_msg(event.user_id,'Приветствую в нашем сообщетве')
                    d[event.user_id] = 1
                    write_msg(event.user_id,'Меню: 1.Реклама 2. Стать мемотделом')
                