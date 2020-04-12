# -*- coding: utf-8 -*-


# 插件被加载时的
import requests


def on_load(server, old_module):
    server.add_help_message('§2[Welcomer]', ' §5联系作者 Hanbings 3219065882@qq.com')

# 获取进入游戏消息
def on_player_joined(server, player):
    seed_color_sub_title(server, player, '欢迎', get_text(), 'white', 'yellow')


# 获取每日一句
def get_text():
    req = requests.get('https://v1.hitokoto.cn/?c=f&encode=text')
    return req.text


# title轮子

# 封装发送标题（在屏幕中间显示）
def seed_title(server, playerName, message):
    server.execute("title" + " " + playerName + " " + "title" + " " + "{\"text\":\"" + message + "\"}")


# 封装带颜色的标题（在屏幕中间显示）
def seed_color_title(server, playerName, message, color):
    server.execute(
        "title" + " " + playerName + " " + "title" + " " + "{\"text\":\"" + message + "\",\"color\":\"" + color + "\"}")


# 封装带子标题的标题（在屏幕中间显示）
def seed_sub_title(server, playerName, message, subMessage):
    server.execute("title" + " " + playerName + " " + "subtitle" + " " + "{\"text\":\"" + subMessage + "\"}")
    server.execute("title" + " " + playerName + " " + "title" + " " + "{\"text\":\"" + message + "\"}")


# 封装带颜色和子标题的标题（在屏幕中间显示）
def seed_color_sub_title(server, playerName, message, subMessage, color, subColor):
    server.execute("title" + " " + playerName + " " + "subtitle" + " " + "{\"text\":\"" + subMessage + "\",\"color\":\""
                   + subColor + "\"}")
    server.execute("title" + " " + playerName + " " + "title" + " " + "{\"text\":\"" + message + "\",\"color\":\""
                   + color + "\"}")
