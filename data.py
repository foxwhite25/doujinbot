from .nhentai import *
import ujson as json


def get_random_doujin_list(num):
    a = []
    for n in range(num):
        print(n)
        d = get_random_id()
        b = get_doujin(d)
        a.append(b.__dict__)
    return a


def get_search_doujin_list(query, num):
    b = search(query, 1, "date")
    b = b[:num]
    a = []
    for each in b:
        a.append(each.__dict__)
    return a


def list_to_forward(li):
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
    msg_list.append(msg)
    for each in doujin['pages']:
        msg_list.append(f'[CQ:image,file={each[0]}]')
    temp = '标签:\n'
    for each in doujin['tags']:
        temp += str(each[2]) + ':' + str(each[4]) + '个作品包含这个标签\n'
    msg_list.append(temp)
    return msg_list
