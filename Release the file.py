import os

try:
    os.makedirs('config')
    os.makedirs('System')
    os.makedirs('modlues')
    os.makedirs('traceback')

    clean_py = r'''import os
import time

print('要清理的文件夹:')
print('__pycache__(pyc文件缓存)')
print('log(日志文件夹)')
print('traceback(错误报告文件)')
time.sleep(1)
clean_list = ['__pycache__','log','traceback']
for i in clean_list:
    print(f'removeing... {i}')
    try:
        os.mkdir(i)
    except FileExistsError:
        File = os.listdir(f'{i}\\')
        for Files in File:
            print(f'removeing...{Files}')
            os.remove(f'{i}\\'+Files)
        os.rmdir(f'{i}')
        if i != '__pycache__':
            print('makedir... ' + i)
            os.mkdir(f'{i}')
        else:
            pass
print('程序执行完毕...')'''

    print('clean.py文件已定义完毕，准备写入...[001]')

    with open('clean.py','w+',encoding='UTF-8') as f:
        f.write(clean_py)

    print('写入完毕![001]')

    Random_name_py = r'''"""
From System.py
===
Random Name
===
"""
import sys
import random
import art
import time
import os
import string
import tkinter as tk
from tkinter import messagebox

def main():
    first = []
    second = []
    third = []
    read_all = ['first.txt','second.txt','third.txt']
    for read in read_all:
        with open(f'.\\Random_named\\{read}','r',encoding='UTF-8') as f:
            read_ = f.read()
            if read == 'first.txt':
                first = read_.split('\n')
            elif read == 'second.txt':
                second = read_.split('\n')
            elif read == 'third.txt':
                third = read_.split('\n')
    print('网易随机取名系统启动中...')
    time.sleep(2)
    while True:
        text = 'Press "quit" to Exit,Press "ten" to output ten,else continue'
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        print()
        input_= input('>>>')
        if input_ == 'quit':
            print('command:quit')
            break
        elif input_ == 'ten':
            for i in range(10):
                RandomName = ''
                RandomName =  str(random.choice(first)) + str(random.choice(second)) + str(random.choice(third))
                for char in RandomName:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.01)
                print()
        else:
            RandomName = ''
            RandomName =  str(random.choice(first)) + str(random.choice(second)) + str(random.choice(third))
            for char in RandomName:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)
            print()
    if __name__ == '__main__':
        pass
    else:
        exit()'''

    print('Random_name.py文件已定义完毕，准备写入...[002]')

    with open('System\\Random_name.py','w+',encoding='UTF-8') as f:
        f.write(Random_name_py)

    print('写入完毕![002]')

    Game_py = r'''"""
From System.py
===
Small Game
===
"""

import string,random

class Game(object):
    def __init__(self,big,small):
        self.small = small
        self.big = big
    @staticmethod
    def random_text(small,big):
        str_text = string.ascii_letters
        list_text = []
        for char in str_text:
            list_text.append(char)
        str_text = random.sample(str_text,random.randint(small,big))
        print(''.join(str_text))
        return ''.join(str_text)'''

    print('Game.py文件已定义完毕，准备写入...[003]')

    with open('System\\Game.py','w+',encoding='UTF-8') as f:
        f.write(Game_py)

    print('写入完毕![003]')

    Windows_bat = r'''pip install sys
pip install art
pip install time
pip install webbrowser
pip install os
pip install string
pip install subprocess
pip install logging
pip install send2trash
pip install tkinter'''

    print('install modlue.bat文件已定义完毕，准备写入...[004]')

    with open('System\\install modlue.bat','w+',encoding='UTF-8') as f:
        f.write(Windows_bat)

    print('写入完毕![004]')

    os.makedirs('Account number')
    os.makedirs('Account number\\System User')
    with open('Account number\\System User\\System Version Number.txt','w+',encoding='UTF-8') as f:
        f.write('1.6.0')
    with open('Account number\\list.txt','w+',encoding='UTF-8') as f:
        f.write("['System user']")
    os.makedirs('log')
    os.makedirs('Random_named')
    first = r'''开心的
快乐的
渺小的
失望的
聪明的
智慧的
矮矮的
瘦瘦的
简单的
生动的
美丽的'''
    second = r'''小朋友
村民
钻石块
原木
木棍
书本
小鸡
小牛
末地烛
鞘翅
末影人
小青蛙
足球'''
    third = r'''跳舞
打篮球
写作业
看电视
看书
喝水
踢足球
打乒乓球
学习
吃饭
写作文
玩游戏
做运动
上课
复习
写作业'''
    with open('Random_named\\first.txt','w+',encoding='UTF-8') as f:
        f.write(first)
    with open('Random_named\\second.txt','w+',encoding='UTF-8') as f:
        f.write(second)
    with open('Random_named\\third.txt','w+',encoding='UTF-8') as f:
        f.write(third)

    install = r'''import sys
import random
import art
import time
import os
import tkinter as tk
from tkinter import messagebox

def main():
    art.tprint('YJDOSsystem')

    install = tk.Tk()
    install.title('YJDOSsystem--install')
    install.geometry('500x300')

    def next_1():
        def clr():
            messagebox.showinfo(title='HI',message='安装完毕!')
            with open('.\\name.txt','w+',encoding='UTF-8') as f:
                f.write(name_entry.get())
            with open('.\\password.txt','w+',encoding='UTF-8') as f:
                write_ = ''
                for char in password_entry.get():
                    cache = ord(char) + len(password_entry.get())
                    write_ += chr(cache)
                f.write(write_)
            os.system('dir C:\\WINDOWS\\System32')
            sys.exit()
        print('你同意了YJDOSsystem条款，即将进行下一步...')
        install_2 = tk.Tk()
        install_2.title('YJDOSsystem--install')
        name_text = tk.Label(install_2,text='name').grid(row=0)
        password_text = tk.Label(install_2,text='password').grid(row=1)
        name_entry = tk.Entry(install_2)
        password_entry = tk.Entry(install_2,show='*')
        name_entry.grid(row=0,column=1)
        password_entry.grid(row=1,column=1)
        tk.Button(install_2,text='Over',command=clr).grid(row=2,column=0,pady=10)
    tiaokuan = """                            YJDOSsystem条款
    1.不可搬运
    2.由KkyijvkK个人编写，无其他指导
    3.不可改版，由个人改版后发生的一切错误或其他事件由修改人承担，与编写者无关
    4.不可盗用
    5.下一步意味着你已阅读并同意此条款
    6.仅供娱乐"""

    tk.Label(install,text='YJDOSsystem安装程序').pack()
    next_1_true = False
    def Button_pack():
        tk.Button(install,text='我已阅读并同意YJDOSsystem条款，下一步',command=next_1).pack()
    tiku = tk.Text(install,height=8)

    tiku.insert('insert',tiaokuan)

    tiku.pack()

    next_1_False = input('输入True以下一步....\n-->')

    if next_1_False == 'True' or next_1_False == 'true':
        Button_pack()

    install.mainloop()
'''

    print('install_import.py文件已定义完毕，准备写入...[005]')

    with open('System\\install_import.py','w+',encoding='UTF-8') as f:
        f.write(install)

    print('写入完毕![005]')

    Analysis_module = r'''"""
Analysis module(path:.\\modlues\\*.md)
"""

def Analysis_module(path = str()):
    """How does it work? Something like this:

    >>> import Analysis_module

    >>> Analysis_module.Analysis_module('modlues\\YJGOSSystem.md')

    'calc'"""
    try:
        with open(path,'r',encoding='UTF-8') as f:
            Read = f.read()
    except FileNotFoundError:
        return 'The File is undefined'
    Split = Read.split(':')
    if Split[0] == 'import':
        if Split[1] == 'YJGOSSystem.calc':
            return 'calc'
        else:
            return 'The module is not defined'
    else:
        return 'The command is undefined'
'''

    print('Analysis_module.py文件已定义完毕，准备写入...[006]')

    with open('System\\Analysis_module.py','w+',encoding='UTF-8') as f:
        f.write(Analysis_module)

    print('写入完毕![006]')

    Buckup = r"""import shutil

def BUCKUP():
    path = input('请输入备份路径:')

    try:
        shutil.copytree('.','..\\Buckup\\')
    except FileExistsError:
        print('[Buckup.py] 上层工作目录已有Buckup文件夹,请删除或切换YJGOSSystem文件夹的路径后再尝试...')
        shutil.rmtree('..\\Buckup')
        exit()
    try:
        shutil.move('..\\Buckup',path)
    except shutil.Error:
        print('[Buckup.py] 输入的备份目录已有Buckup文件夹,请删除后再尝试...')
        shutil.rmtree('..\\Buckup')
        exit()

    print('备份完毕！备份在System/Buckup文件夹中')"""

    print('Buckup.py文件已定义完毕，准备写入...[007]')

    with open('System\\Buckup.py','w+',encoding='UTF-8') as f:
        f.write(Buckup)

    print('写入完毕![007]')

    Import_module_items = r"""import os
import shutil

def list_(modluedir = str()):
    '''
    How does it work? Something like this:

    >>> import Import_module_items as imi

    >>> Return_list = imi.list(modluedir = "modlues\\")

    >>> Return_list

    ['learn_calc']
    '''

    return os.listdir(modluedir)

def make(name = str(),icon_path = str(),how_do = str()):
    if os.path.exists('modlues'):
        os.makedirs(f'modlues\\{name}')
        os.makedirs(f'modlues\\{name}\\do')
        os.makedirs(f'modlues\\{name}\\image')
        with open(f'modlues\\{name}\\main.md','w+',encoding='UTF-8') as f:
            f.write(f'name-->{name}\nicon_image-->modlues\\{name}\\image\\icon.png\nhow_do-->modlues\\{name}\\do\\do_main.txt')
        with open(f'modlues\\{name}\\do\\do_main.txt','w+',encoding='UTF-8') as f:
            if how_do == '':
                f.write(f'''name-->{name}
icon_image-->modlues\\{name}c\\image\\icon.png
how_do-->modlues\\{name}\\do\\do_main.txt''')
            else:
                f.write(how_do)
        shutil.copy(icon_path,f'modlues\\{name}\\image\\icon.png')
        return True
    raise Exception('not found "modlues" dir')
"""
    
    print('Import_module_items.py文件已定义完毕，准备写入...[008]')
    
    with open('System\\Import_module_items.py','w+',encoding='UTF-8') as f:
        f.write(Import_module_items)

    print('写入完毕![008]')

    command_list = r"""exit
idc
idc_OP
Changelog
Random_name
calc
Buckup
user
web
text_playgame
UserName
PasswordSet
clean
with
reopen
time
cmd_dir /s
config"""
    print('command_list.txt文件已定义完毕，准备写入...[009]')
    
    with open('command_list.txt','w+',encoding='UTF-8') as f:
        f.write(command_list)

    print('写入完毕![009]')

    Progress_bar = r"""import time

class Toolong(Exception): pass

class Progress_bar(object):
    def __init__(self,speed=0.1,style='-'):
        self.speed = speed
        self.style = style
        self.titlestyle = ''
        self.index = 0
    def print_(self):
        if len(self.style) > 1: raise Toolong(f'The displayed characters are too long, this will cause an error in the display, please reduce the string first (please try "{self.style[0]}")')
        self.index = 0
        for i in range(100):
            self.index += 1
            print('/{0:*<110s}/        {1:<3s}%/100%'.format(self.style * (i + 1),str(self.index)),end='\r')
            time.sleep(self.speed)
        print('\n')"""
    
    with open('System\\Progress_bar.py','w+',encoding='UTF-8') as f:
        f.write(Progress_bar)

    print('写入完毕![010]')

except FileExistsError:
    print('你已经释放过文件了!')
