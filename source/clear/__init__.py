import time
from mcdreforged.api.all import *

creeper = False

def on_load(server: PluginServerInterface, prev_module):
    # 注册帮助命令
    server.register_help_message('!!clear creeper', '弄死苦力怕')
    server.register_help_message('!!clear item', '清除掉落物')

    # 注册命令
    server.register_command(
        Literal('!!clear')
        .then(Literal('creeper').runs(clear_creeper))
        .then(Literal('item').runs(clear_item))
    )
    
    server.register_command(
        Literal('!!switch')
        .then(Literal('creeper').runs(switch_creeper))
    )

    auto_clear_item(server)

def clear_creeper(source: CommandSource):
    global creeper
    if creeper == False:
        source.reply('你没有权限使用这个指令')
        return
    
    source.get_server().execute('kill @e[type=creeper]')
    source.get_server().say('§a已清除所有苦力怕')

@new_thread('clear_item')
def clear_item(source: CommandSource):
    for i in range(3, 0, -1):
        source.get_server().say(f'§cWARNING!!! {i}秒后清除掉落物')
        time.sleep(1)
    source.get_server().execute('kill @e[type=item]')
    source.get_server().say('§a已清除所有掉落物')

def switch_creeper(source: CommandSource):
    global creeper
    if source.get_permission_level() < 3:
        source.reply('你没有权限使用这个指令')
        return
    
    creeper = not creeper
    source.reply(f'creeper: {creeper}')

@new_thread('auto_clear_item')
def auto_clear_item(server: PluginServerInterface):
    while True:
        time.sleep(50)

        for i in range(10, 5, -1):
            server.say(f'§bWARNING!!! {i}秒后清除掉落物')
            time.sleep(1)
        for i in range(5, 3, -1):
            server.say(f'§6WARNING!!! {i}秒后清除掉落物')
            time.sleep(1)
        for i in range(3, 0, -1):
            server.say(f'§cWARNING!!! {i}秒后清除掉落物')
            time.sleep(1)

        server.execute('kill @e[type=item]')
        server.say('§a已清除所有掉落物')