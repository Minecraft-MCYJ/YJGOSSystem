"""
*_encoding_* *_Python_*
*_by_* *_MCYJ_*
*_Version_* *_1.6.0_*
"""

import sys, art, time, webbrowser, os, subprocess, logging, re, pyautogui, threading, _tkinter
import System.install_import as ins
import System.Game as Game
import System.Random_name as Random_name
import System.Buckup as bu
import System.Import_module_items as imi
import System.Progress_bar as pb
import traceback as trk
import tkinter as tk
from tkinter import messagebox as msg

try:
    run = tk.Tk()
    run.geometry('700x700')
    run.title('Loading System...')
    run.config(bg='Black')
    icon = tk.PhotoImage(file='Assert\\YJGOSSystem_Icon.png')
    run.iconphoto(True, icon)

    def reopen():
        global root_
        logging.info('system-command-reopen')
        root_.destroy()
        try:
            if os.path.exists('system.py') == True: os.system(f'python {os.path.abspath('.') + '\\system.py'}')
            else: os.system(os.path.abspath('.') + '\\system.exe')
        except:
            print('啊？没有system.py或者system.exe你是怎么运行这个程序的？难道你把文件改名了？')

    def destory():
        global run
        time.sleep(2)
        run.destroy()

    D = threading.Thread(target=destory)

    def Setup():
        tra = tk.Tk()
        tra.title(':)    BlueScreen')
        w = tra.winfo_screenwidth()
        h = tra.winfo_screenheight()
        tra.geometry("%dx%d" % (w, h))
        tra.config(bg='Blue')

        def fo():
            time.sleep(1)
            tra.attributes('-fullscreen', True)

        def de():
            tra.destroy()

        tk.Label(tra, text='：）', font=('Lucida Console', 70), bg='Blue').grid(row=0, column=0)
        tk.Label(tra, text='As you can see, the blue screen is up, it\'s just that this feature is not finished.',
                 font=('Lucida Console', 13), bg='Blue').grid(row=1, column=0)
        tk.Label(tra, text='I   Can\'t    Help    You  !', font=('Lucida Console', 20), bg='Blue').grid(row=2, column=0)
        tk.Label(tra,
                 text='温馨提示：这是个玩笑，您的PC没得一点问题，想要关掉这个窗口，你需要先点击这个窗口，然后按下Alt+F4，或者点击这个按钮',
                 font=('Lucida Console', 15), bg='Blue').grid(row=3, column=0)
        tk.Button(tra, text='关闭', command=de, bg='Blue').grid(row=3, column=1)

        foc = threading.Thread(target=fo)
        foc.start()

        tra.mainloop()
        sys.exit()

    tk.Label(image=icon).pack()
    tk.Label(text='Press this button to join the Setup Program.').pack()
    tk.Button(text='This', command=Setup).pack()

    D.start()

    run.mainloop()

    def traceback_errors(window, showtext=str()):
        tk.Label(window, text=showtext).pack()
        return 'Debugging system running...'


    def SELF_TEST():
        def DE():
            self_test.destroy()

        class Self_test(object):
            def exists_(path): return os.path.exists(path)

        exists_Errorlist = []
        exists_list = ['Account number', 'Account number\\System User', 'Account number\\list.txt',
                       'Account number\\System User\\System Version Number.txt', 'log', 'modlues', 'Random_named',
                       'Random_named\\first.txt', 'Random_named\\second.txt', 'Random_named\\third.txt']
        for i in exists_list:
            Return = Self_test.exists_(i)
            if Return == True:
                pass
            else:
                exists_Errorlist.append(i)
        show_text = ''
        if len(exists_Errorlist) == 0:
            show_text = 'Not Found Errors!'
        else:
            show_text = 'Errors:' + str(len(exists_Errorlist))
        self_test = tk.Tk()
        self_test.geometry('500x300')
        self_test.title('self-test')

        tk.Label(self_test, text=show_text, bg='Red').pack()
        tk.Button(self_test, text='OVER', command=DE).pack()

        if show_text == 'Not Found Errors!':
            pass
        else:
            TEXT = tk.Text(self_test, height=len(exists_Errorlist))
            TEXT.pack()
            for e in exists_Errorlist: TEXT.insert(tk.END, e)

        self_test.mainloop()


    try:
        with open('config\\self-test', 'r', encoding='UTF-8') as f:
            CONFIG_SELF_TEST = f.read()
    except:
        CONFIG_SELF_TEST = None

    if CONFIG_SELF_TEST == 'self-test -f':
        pass
    else:
        SELF_TEST()
        print('自检测试已完毕')

    pattern_imc = r'imc (\w)+'

    try:
        try:
            with open('name.txt', 'r', encoding='UTF-8') as f:
                UserName = f.read()
            with open('password.txt', 'r', encoding='UTF-8') as f:
                UserPassword = f.read()
        except FileNotFoundError:
            print('检测到未执行登陆程序，已自动导入!')
            ins.main()


        def idc_(Permissions='Regular users'):
            while True:
                idc = input(f'<{os.path.abspath(".")} -{Permissions}> ')
                imc = re.search(pattern_imc, idc, re.I)
                try:
                    IMC = imc.group(0)
                    IMC = IMC[4:]
                except AttributeError:
                    if imc == None:
                        if idc == 'Permissions - hoist':
                            Permissions = 'administrator'
                            return (f'您的权限已提升至{Permissions}')
                        elif idc == 'exit':
                            break
                        elif idc == 'self-test':
                            print('已开启自检测试...')
                            SELF_TEST()
                        elif idc == '':
                            pass
                        elif idc == 'ipo':
                            input_name = input('Please input your want name:')
                            icon_path = input('Please input your want icon path:')
                            how_do = input('Please input your want do:')
                            return (f'info:{imi.make(name=input_name, icon_path=icon_path, how_do=how_do)}')
                        else:
                            return (idc + '不是可运行的命令!')
                else:
                    UUID = ''
                    UUID += '0b'
                    for word in IMC: UUID += str(bin(ord(word))[2:])
                    print('Looking in indexes: https://www.bilibili.com/video/BV1GJ411x7h7/')
                    time.sleep(1)
                    print('Collecting', IMC)
                    time.sleep(2)
                    print('  Using cached https://www.bilibili.com/video/BV1GJ411x7h7/', IMC, '/', UUID,
                          f' ({len(UUID)}Kib)', sep='')
                    time.sleep(0.5)
                    print('Installing collected packages:', IMC)
                    pbar = pb.Progress_bar(speed=len(UUID) / 100)
                    pbar.print_()
                    print('\nSuccessfully installed', IMC)
                    imi.make(name=IMC, icon_path='Assert\\YJGOSSystem_Icon.png')


        logging.basicConfig(level=logging.DEBUG, filename='log\\system.log', filemode='a',
                            format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

        logging.info('system-open')

        with open('Account number\\System User\\System Version Number.txt', 'r', encoding='UTF-8') as f:
            System_Version = f.read()
        try:
            with open(f'..\\Changelog\\{System_Version}\\options.txt', 'r', encoding='UTF-8') as f:
                Changelog = f.read()
        except FileNotFoundError:
            Changelog = '没有更新日志'


        def Password_SR(UserPassword_=str()):
            time.sleep(2)
            YSZFC = input('请输入密码:')
            for char in UserPassword_:
                str3 = ord(char) - len(YSZFC)
                UserPassword_ += chr(str3)
            PYMM = UserPassword_[len(YSZFC):]
            if YSZFC == PYMM:
                print('密码输入正确!')
                logging.info('Password-ok')
            else:
                print('密码输入错误!')
                logging.critical(f'Password-mistake  input:{YSZFC}')
                Password_SR(UserPassword_=UserPassword)
            return YSZFC


        try:
            with open('config\\Password', 'r', encoding='UTF-8') as f:
                CONFIG_PASSWORD = f.read()
        except:
            CONFIG_PASSWORD = None

        if CONFIG_PASSWORD == 'Password -f':
            pass
        else:
            YSZFC = Password_SR(UserPassword_=UserPassword)

        root = True
        art.tprint('YJDOSsystem')
        now_time = time.localtime()
        now_time = f'{now_time[0]} {now_time[1]} {now_time[2]}-{now_time[3]}:{now_time[4]}:{now_time[5]}'
        print(f'你好！{UserName}')
        print('当前时间:', now_time)


        def command_(command):
            if command == 'exit':
                logging.info('system-command-exit')
                sys.exit()
            elif command == 'idc':
                idc_()
                return (
                    '你现在打开了idc(Install the debugging command)安装调试命令,说明你已经确定你的操作不会失误,如操作不当可能会删除整个YJGOSSystem系统...')
            elif command == 'idc_OP':
                idc_(Permissions='administrator')
                return (
                    '你现在以管理员模式打开了idc(Install the debugging command)安装调试命令,说明你已经确定你的操作不会失误,如操作不当可能会删除整个YJGOSSystem系统...')
            elif command == 'Changelog':
                return (Changelog)
            elif command == 'Random_name':
                logging.info('system-command-Random_name')
                Random_name.main()
            elif command == 'calc':
                logging.info('system-command-calc')
                subprocess.Popen('calc.exe')
            elif command == 'Buckup':
                bu.BUCKUP()
            elif command == 'user':
                logging.info('system-command-user')
                user = tk.Tk(className='User')
                user.geometry('500x300')

                def listuser():
                    logging.info('system-command-user-listuser')
                    with open('.\\Account number\\list.txt', 'r', encoding='UTF-8') as f:
                        GetAllUser = f.read()
                        msg.showinfo(title='User', message=GetAllUser)

                tk.Label(text='SetUserSystem').pack()
                tk.Button(user, text='listuser', command=listuser).pack()
            elif command == 'web':
                logging.info('system-command-web')
                print('web程序启动中..')
                time.sleep(1)
                wait_list = ['|', '/', '-', '\\', '|']
                for i in range(10):
                    for wait in wait_list:
                        print(f'\r{wait}', end='')
                        time.sleep(0.1)
                print()
                web_input = input('请输入web网址:')
                logging.info(f'system-command-web  web:{web_input}')
                webbrowser.open(web_input)
            elif command == 'text_playgame':
                logging.info('system-command-text_playgame')
                while True:
                    text_random = Game.Game(big=7, small=5)
                    text_playgame = text_random.random_text(big=7, small=5)
                    input_ = input('请输入上面的随机字母(exit为退出):')
                    if input_ == 'exit':
                        break
                    else:
                        if input_ == text_playgame:
                            continue
                        else:
                            return ('输入错误!')
            elif command == 'UserName':
                logging.info('system-command-UserName')
                return (f'UserName:{UserName}')
            elif command == 'PasswordSet':
                OldPassword = input('Please enter your old password:')
                if OldPassword == UserPassword:
                    NewPassword = input('Please enter your new password:')
                    with open('.\\password.txt', 'w+', encoding='UTF-8') as f:
                        write_ = ''
                        for char in NewPassword:
                            cache = ord(char) + len(NewPassword)
                            write_ += chr(cache)
                        f.write(write_)
                    logging.info(f'system-command-PasswordSet  Old:{OldPassword}   New:{NewPassword}')
                else:
                    pass
            elif command == 'clean':
                return ('请执行放在System\\clean.py的文件...(保持system.py程序关闭状态)')
            elif command == 'with':
                logging.info('system-command-with')
                print('''with--文件操作(你可以从下列选择中选择一个进行操作)
                    1.read(读取)
                    2.write(写入)''')
                with_all_first = [
                    'read',
                    'write'
                ]
                while True:
                    mode_with_first = input('-->')
                    if mode_with_first in with_all_first:
                        if mode_with_first == with_all_first[0]:
                            print('mode:read')
                            logging.info('system-command-with-mode:read')
                            file_path = input('文件路径-->')
                            try:
                                with open(file_path, 'r', encoding='UTF-8') as f:
                                    print('加载中...')
                                    pbar = pb.Progress_bar(speed=0.01)
                                    pbar.print_()
                                    print('\nFileText:')
                                    read_text = f.read()
                                    logging.info(f'system-command-with-mode:read  File:{file_path}')
                                    for char in read_text:
                                        sys.stdout.write(char)
                                        sys.stdout.flush()
                                    return ('\n')
                            except:
                                logging.error('system-command-with-mode:read-FileNotinTheComputer')
                                return ('[002]Error:FileNotinTheComputer')
                        elif mode_with_first == with_all_first[1]:
                            print('mode:write')
                            logging.info('system-command-with-mode:write')
                            file_path = input('文件路径-->')
                            file_text = input('写入内容-->')
                            logging.info(f'system-command-with-mode:write- File:{file_path}  Write:{file_text}')
                            pbar = pb.Progress_bar(speed=0.01)
                            pbar.print_()
                            print('\n')
                            try:
                                with open(file_path, 'w+', encoding='UTF-8') as f:
                                    f.write(file_text)
                            except:
                                logging.error('system-command-with-mode:write-PathError')
                                return ('路径错误!')
                            else:
                                logging.info(f'system-command-with-mode:write File:{file_path}')
                                for char in file_text:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                return ('成功写入:\n')
                        else:
                            break
                    else:
                        break
            elif command == 'reopen':
                reopen()
            elif command == 'time':
                logging.info('system-command-time')
                now_time = time.localtime()
                return (
                '当前时间:', f'{now_time[0]} {now_time[1]} {now_time[2]}-{now_time[3]}:{now_time[4]}:{now_time[5]}   ')
            elif command == 'cmd_dir /s':
                logging.info('system-command-cmd_dir /s')
                os.system('color a')
                os.system('dir C:\\WINDOWS\\System32\\')
                return ('你发现了彩蛋!')
            elif command == 'config':
                setconfig = input('>>>')
                if setconfig == 'Password -f':
                    with open('config\\Password', 'w+') as f:
                        f.write('Password -f')
                        print('Attribute: Password is disabled(Password -f)')
                        return 'Attribute: Password Enabled(Password -f)'
                if setconfig == 'Password -t':
                    with open('config\\Password', 'w+') as f:
                        f.write('Password -t')
                        print('Attribute: Password Enabled(Password -t)')
                        return 'Attribute: Password Enabled(Password -t)'
                if setconfig == 'self-test -f':
                    with open('config\\self-test', 'w+') as f:
                        f.write('self-test -f')
                        print('Attribute: self-test is disabled(self-test -f)')
                        return 'Attribute: self-test Enabled(self-test -f)'
                if setconfig == 'self-test -t':
                    with open('config\\self-test', 'w+') as f:
                        f.write('self-test -t')
                        print('Attribute: self-test Enabled(self-test -t)')
                        return 'Attribute: self-test Enabled(self-test -t)'
            elif command == '':
                return False
            else:
                logging.error(f'system-command-Error  Command:{command}')
                return ('Command:Error')


        class Console(tk.Frame):
            def __init__(self, master=None):
                super().__init__(master)

                def exit_():
                    sys.exit()

                self.output = tk.Text(self, height=24, font=("Consolas", 10))
                self.output.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
                self.input = tk.Entry(self, font=("Consolas", 10))
                self.input.pack(side=tk.BOTTOM, fill=tk.X, padx=5, pady=5, ipady=5, expand=1)
                self.input.focus_set()
                self.input.bind("<Return>", self.handle_input)
                self.pack(fill=tk.BOTH, expand=1)
                self.menu = tk.Menu(master)

                def exit__():
                    os.system('Shutdown -s -t 5')

                def reopen_():
                    os.system('Shutdown -r -t 5')

                def TFP():
                    TF = msg.askquestion(title='设置-输入密码', message='输入密码开关')
                    if TF == 'yes':
                        with open('config\\Password', 'w+') as f:
                            f.write('Password -t')
                            print('Attribute: Password Enabled(Password -t)')
                    if TF == 'no':
                        with open('config\\Password', 'w+') as f:
                            f.write('Password -f')
                            print('Attribute: Password is disabled(Password -f)')

                def TFS():
                    TF = msg.askquestion(title='设置-自检测试', message='自检测试开关')
                    if TF == 'yes':
                        with open('config\\self-test', 'w+') as f:
                            f.write('self-test -t')
                            print('Attribute: self-test Enabled(self-test -t)')
                    if TF == 'no':
                        with open('config\\self-test', 'w+') as f:
                            f.write('self-test -f')
                            print('Attribute: self-test is disabled(self-test -f)')

                master['menu'] = self.menu
                self.systemmenu = tk.Menu(self.menu)
                self.menu.add_cascade(label='YJGOS', menu=self.systemmenu)
                self.systemmenu.add_command(label='重启', command=reopen)
                self.systemmenu.add_separator()
                self.systemmenu.add_command(label='关机', command=exit_)

                self.setupmenu = tk.Menu(self.menu)
                self.menu.add_cascade(label='设置', menu=self.setupmenu)
                self.setupmenu.add_command(label='输入密码', command=TFP)
                self.setupmenu.add_separator()
                self.setupmenu.add_command(label='自检测试', command=TFS)

                self.windowsmenu = tk.Menu(self.menu)
                self.menu.add_cascade(label='系统', menu=self.windowsmenu)
                self.windowsmenu.add_command(label='五秒后重启', command=reopen_)
                self.windowsmenu.add_separator()
                self.windowsmenu.add_command(label='五秒后关机', command=exit__)

            def write(self, text):
                self.output.insert(tk.END, text)
                self.output.see(tk.END)

            def handle_input(self, event):
                command = self.input.get()
                self.input.delete(0, tk.END)
                ret = command_(command)
                if ret != False:
                    self.write(f"\n>>>{command}\n")
                    self.write(ret)
                else:
                    self.write(f"\n>>>{command}")


        if __name__ == "__main__":
            root_ = tk.Tk()
            root_.geometry("800x600")
            root_.title("YJGOSSystem")
            console = Console(root_)
            console.write("YJGOSSystem DOS\n")
            root_.attributes("-fullscreen", True)


            def cl():
                time.sleep(0.25)
                pyautogui.click()
                root_.attributes("-fullscreen", False)
                pyautogui.hotkey(['ctrlleft', 'space'])


            cl_ = threading.Thread(target=cl)
            cl_.start()
            root_.mainloop()
    except KeyboardInterrupt:
        print('你按下了Ctrl+C,从而产生了此错误...')
        logging.critical('KeyboardInterrupt')
        with open('traceback\\traceback.log', 'w+', encoding='UTF-8') as f:
            f.write(trk.format_exc())
        sys.exit()
    except EOFError:
        print('你按下了Ctrl+Z并按下了Enter键,从而产生了此错误...')
        logging.critical('EOFError')
        with open('traceback\\traceback.log', 'w+', encoding='UTF-8') as f:
            f.write(trk.format_exc())
        sys.exit()
    except _tkinter.TclError:
        pass

except:
    trk_ = trk.format_exc()
    if 'SystemExit' in trk_:
        pass
    else:
        with open('traceback\\traceback.log', 'w+', encoding='UTF-8') as f:
            f.write(trk_)
        print('发生错误，已将Traceback错误代码存入traceback\\traceback.log文件中')
