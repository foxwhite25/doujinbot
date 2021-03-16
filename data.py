from .nhentai import *
import random
import ujson as json


def get_random_doujin_list(num):
    hp = get_homepage(random.randint(1, 5))
    hp = random.choices(hp, k=num)
    a = []
    for n in hp:
        a.append(n.__dict__)
    return a


def get_search_doujin_list(query, num):
    b = search(query, 1, "date")
    b = random.choices(b, k=num)
    a = []
    for each in b:
        a.append(each.__dict__)
    return a


def list_to_forward(li):
    if isinstance(li, str):
        li = [li]
    temp = []
    for each in li:
        data = {
            "type": "node",
            "data": {
                "name": '小冰',
                "uin": '2854196306',
                "content": each
            }
        }
        temp.append(data)
    return temp


def get_msg_by_doujin(doujin):
    msg_list = []
    msg = f'''神秘六位数:{doujin['id']}
名字（翻译后）:{doujin['titles']['english']}
名字（原文）:{doujin['titles']['japanese']}
收藏数量:{doujin['favorites']}
'''
    msg += f'[CQ:image,file={doujin["thumbnail"]}]'
    print(msg)
    for each in doujin['pages']:
        msg_list.append(f'[CQ:image,file={each[0]}]')
    return msg_list, msg
