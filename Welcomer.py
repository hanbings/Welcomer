# -*- coding: utf-8 -*-

# 插件被加载时的
import requests

from plugins.TitleAPI import seed_sub_title, ChatColor


# 写入帮助
def on_load(server, old_module):
    server.logger.info('[Welcomer] 欢迎插件已启用')
    server.add_help_message('§l[Welcomer]', ' §6用!!welcomer 查看插件信息')


# 获取进入游戏消息
def on_player_joined(server, player):
    message = get_text()
    seed_sub_title(server, player, '欢迎', message)
    server.execute("tell" + " " + player + " " + message)


# 接受指令
def on_info(server, info):
    tempInfo = str(info)
    if '!!welcomer' in tempInfo:
        if check_player_if_not_command(info):
            server.say("§l[Welcomer] §6联系作者 Hanbings 3219065882@qq.com")
            server.say("§l[Welcomer] §6所有语句均来自于一言开发者平台")
            server.say("§l[Welcomer] §6一言开发者平台 https://developer.hitokoto.cn/")


# 获取每日一句
def get_text():
    req = requests.get('https://v1.hitokoto.cn/?encode=text')
    return req.text


# 判断指令是不是处于聊天语句最前方
def check_player_if_not_command(info):
    if str(info.content).index('!!welcomer') == 0:
        return True
    else:
        return False



