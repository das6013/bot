import vk_api
import bs4
from bs4 import BeautifulSoup
import random
import lxml
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import requests
hi=['привет','ку','hi']
hi1=['привет!','ку!','hi!']
poka=['пока','прощай','до встречи']
poka1=['пока!','прощай!','до встречи!']

vk_session = vk_api.VkApi(token="5e62498d90d23127fd30580b3d79536ea9ecfda9b3fec309a56998cad7c5aacb25818977100ab093fd1b1")
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session,"201547143")
for event in longpoll.listen(): #Проверка действий
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.type == VkBotEventType.MESSAGE_NEW:  # последняя строчка
            # проверяем не пустое ли сообщение нам пришло
            if event.obj.text != '':
                # проверяем пришло сообщение от пользователя или нет
                if event.from_user:
                    if event.obj.text.lower() in hi:
                        vk.messages.send(
                        user_id=event.obj.from_id,
                        random_id=get_random_id(),
                        message=hi1[random.randint(0,2)])
                if event.obj.text.lower()=="time":
                    link = 'https://time100.ru/'
                    kek = requests.get(link).text
                    soup = BeautifulSoup(kek, 'lxml')
                    block = soup.find('div', {'class': 'time'}).text
                    vk.messages.send(
                        user_id=event.obj.from_id,
                        random_id=get_random_id(),
                        message="Moscow time:"+" "+str(block))
                elif event.obj.text.lower()=="анекдот":
                    link = 'https://anekdot-z.ru/random-anekdot'
                    kek = requests.get(link).text
                    soup = BeautifulSoup(kek, 'lxml')
                    block = soup.find('div', {'class': 'anekdot-content'}).find('p').text
                    vk.messages.send(
                        user_id=event.obj.from_id,
                        random_id=get_random_id(),
                        message=block)
                elif event.obj.text.lower() in poka:
                    vk.messages.send(
                        user_id=event.obj.from_id,
                        random_id=get_random_id(),
                        message=poka1[random.randint(0,2)])







