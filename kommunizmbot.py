import random

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

d = {}


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random.randint(0, 2048)})


# API-���� ��������� �����
token = "c66136b023bae4f258d25e853cecab8a228c71a2a3b91f200ce77de838009f50f704a38df3262783da8d0"

# ������������ ��� ����������
vk = vk_api.VkApi(token=token)

# ������ � �����������
longpoll = VkLongPoll(vk)

print("��� �������")
# �������� ����
for event in longpoll.listen():

    # ���� ������ ����� ���������
    if event.type == VkEventType.MESSAGE_NEW:

        # ���� ��� ����� ����� ��� ����( �� ���� ����)
        if event.to_me:
            
            # ��������� �� ������������
            request = event.text

            # �������� ������ ������
            if request == "1":
                write_msg(event.user_id, " � ��� ���� 2 ���� �����. ������� � ������-����.")
                write_msg(event.user_id, " �� ���� �������� ������ ��� - https://vk.com/sexy.senya")
            elif request == "2":
                write_msg(event.user_id, "�������� ������ - https://vk.com/ikm_meme?w=app5619682_-176556657")
            else:
                if d.get(event.user_id, 0) == 0:
                    write_msg(event.user_id,'����������� � ����� ���������')
                    d[event.user_id] = 1
                    write_msg(event.user_id,'����: 1.������� 2. ����� ����������')
                