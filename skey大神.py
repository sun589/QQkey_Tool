#By sun589(Daniel)
# -*- coding: utf-8 -*-
"""
本软件仅供学习用途 请勿用作违法行为 后果自负!
"""

from PyQt5 import QtCore, QtWidgets
import sys
import skey大神
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PIL import Image
import requests
import re
from threading import Thread
import time
import csv
import ctypes
from webbrowser import open as webopen

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

def bkn(skey):
    #计算bkn
    t,n,o = 5381,0,len(skey)

    while n < o:
        t += (t << 5) + ord(skey[n])
        n += 1

    return t & 2147483647

def ptqrToken(qrsig):
    #计算ptqrtoken
    n,i,e = len(qrsig),0,0

    while n > i:
        e += (e << 5) + ord(qrsig[i])
        i += 1

    return 2147483647 & e

class Ui_MainWindow(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        self.uin = ''
        self.skey = ''
        self.pskey = ''
        self.cookie = ''
        font = QFont()
        font.setFamily("微软雅黑")
        MainWindow.setFont(font)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(831,567)
        MainWindow.setWindowIcon(QIcon("./icon.ico"))
        QtWidgets.QMessageBox.information(self,"警告","本软件纯免费 如果你是花钱买的火速投诉!\n本软件仅供学习用途 请勿用作违法行为 后果自负!")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 30, 221, 241))
        self.pixmap = QPixmap('二维码不存在.png')
        self.label.setPixmap(self.pixmap)
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 240, 181, 131))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 360, 181, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.get_qq)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(340, -30, 16, 631))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 111, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(380, 10, 61, 31))
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(450, 100, 271, 21))
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setFrame(True)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_2.setDragEnabled(False)
        self.lineEdit_2.setReadOnly(False)
        self.lineEdit_2.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(450, 70, 271, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(450, 130, 271, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(390, 180, 51, 16))
        self.checkBox.setObjectName("checkBox")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 170, 111, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: self.new_notice(
                    text=self.lineEdit_2.text(),q_bkn=bkn(self.skey),
                    pinned=int(self.checkBox.isChecked()),skey=self.skey,
                    pskey=self.pskey,qid=self.lineEdit.text(),uin=self.uin)
                    if self.skey else QtWidgets.QMessageBox.critical(self, "错误", "请先获取skey!")
                    if self.lineEdit_2 and self.lineEdit else QtWidgets.QMessageBox.critical(self, "错误","请先填入内容!")
                    )
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(610, 170, 111, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(lambda: self.qun_list(self.cookie,bkn(self.skey)) if self.skey else QtWidgets.QMessageBox.critical(self, "错误", "请先获取skey!"))
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(440, 230, 111, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(lambda: self.notice_list(
                    q_bkn=bkn(self.skey),skey=self.skey,
                    pskey=self.pskey,qid=self.lineEdit.text(),uin=self.uin)
                    if self.skey else QtWidgets.QMessageBox.critical(self, "错误", "请先获取skey!")
                    if self.lineEdit else QtWidgets.QMessageBox.critical(self, "错误","请先填入内容!")
                    )
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(610, 230, 111, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(lambda: self.qun_members_list(
                    bkn=bkn(self.skey),skey=self.skey,
                    pskey=self.pskey,qid=self.lineEdit.text(),uin=self.uin)
                    if self.skey else QtWidgets.QMessageBox.critical(self, "错误", "请先获取skey!")
                    if self.lineEdit else QtWidgets.QMessageBox.critical(self, "错误","请先填入内容!")
                    )
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(440, 290, 111, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(lambda: self.del_notice(
                    bkn=bkn(self.skey),skey=self.skey,
                    pskey=self.pskey,qid=self.lineEdit.text(),uin=self.uin,fid=self.lineEdit_3.text())
                    if self.skey else QtWidgets.QMessageBox.critical(self, "错误", "请先获取skey!")
                    if self.lineEdit else QtWidgets.QMessageBox.critical(self, "错误","请先填入内容!")
                    )
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(610, 290, 111, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(lambda: self.del_group_member(
                    bkn=bkn(self.skey),skey=self.skey,
                    pskey=self.pskey,qid=self.lineEdit.text(),uin=self.uin,target=self.lineEdit.text())
                    if self.skey else QtWidgets.QMessageBox.critical(self, "错误", "请先获取skey!")
                    if self.lineEdit else QtWidgets.QMessageBox.critical(self, "错误","请先填入内容!")
                    )
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(700, 490, 111, 41))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(lambda: webopen("https://github.com/sun589/QQ_Skey-"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 898, 23))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action.triggered.connect(lambda: self.help(1))
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_2.triggered.connect(lambda: self.help(2))
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menuBar.addAction(self.menu.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Skey大神"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; color:#000000;\">当前状态:</span></p><p><span style=\" font-size:11pt;\">QQ号码:</span></p><p><span style=\" font-size:11pt;\">Skey:</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "获取二维码"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/>|<br/></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#ff0000;\">Skey获取区:</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#ff0000;\">功能区:</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "发布公告"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "群号"))
        self.pushButton_3.setText(_translate("MainWindow", "群列表"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "群公告内容/QQ号"))
        self.checkBox.setText(_translate("MainWindow", "置顶"))
        self.pushButton_4.setText(_translate("MainWindow", "群公告/fid列表"))
        self.pushButton_5.setText(_translate("MainWindow", "群成员"))
        self.pushButton_6.setText(_translate("MainWindow", "删除群公告"))
        self.pushButton_7.setText(_translate("MainWindow", "删除群成员"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "群公告fid"))
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.action.setText(_translate("MainWindow", "使用帮助"))
        self.action_2.setText(_translate("MainWindow", "关于"))
        self.pushButton_8.setText(_translate("MainWindow", "打开Github主页"))

    def help(self,h):
        if h == 1:
            QtWidgets.QMessageBox.information(self, "使用帮助", """发布公告:
参数:输入框1&输入框2        
作用:发布公告              

群列表:                   
参数:无        
作用:获取所有加入的群      

群公告列表:
参数:输入框1
作用:获取已有的群里的群公告

群成员:
参数:输入框1
作用:获取已有的群里的成员

删除群公告:
参数:输入框1&输入框3
作用:删除所在群内的群公告

删除群成员:
参数:输入框1&输入框2
作用:将群内成员移除(需有管理/群主权限)
    """)
        else:
            QtWidgets.QMessageBox.about(self, "使用帮助", "作者:Daniel\n本软件仅供于学习用途 禁止用于违法行为 后果自负")

    def get_qq(self):
        self.qr()
        global flag
        flag = True
        time.sleep(1)
        flag = False
        thread1 = Thread(target=self.cookies,args=(self.ptqrtoken,self.qrsig))
        thread1.start()
    def qr(self):
        print("获取二维码中...")
        qr_res = requests.get("https://ssl.ptlogin2.qq.com/ptqrshow?appid=715030901&e=2&l=M&s=3&d=72&v=4&t=0.5703512186734734&daid=73&pt_3rd_aid=0&u1=https%3A%2F%2Fqun.qq.com%2F")
        self.qrsig = requests.utils.dict_from_cookiejar(qr_res.cookies).get('qrsig')
        self.ptqrtoken = ptqrToken(self.qrsig)
        with open("qr.jpg", 'wb') as f:
            f.write(qr_res.content)
        im = Image.open('qr.jpg')
        im = im.resize((200,200))
        im.save('qr.jpg')
        self.pixmap = QPixmap('qr.jpg')
        self.label.setPixmap(self.pixmap)
        print("二维码获取成功!")

    def new_notice(self,text, q_bkn, pinned, qid, skey, pskey, uin):
        data = {
            "qid": qid,
            "bkn": q_bkn,
            "text": text,
            "pinned": pinned,
            "type": 1,
            "settings": {"is_show_edit_card": 1, "tip_window_type": 0, "confirm_required": 1}
        }
        headers = {
            "Referer": "https://web.qun.qq.com/mannounce/edit.html?&_wv=5127",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; MI 8 Build/QKQ1.190910.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.86 MQQBrowser/6.2 TBS/046715 Mobile Safari/537.36 V1_AND_SQ_8.9.78_4548_YYB_D QQ/8.9.78.12275 NetType/WIFI WebP/0.3.0 AppId/537175315 Pixel/1080 StatusBarHeight/82 SimpleUISwitch/0 QQTheme/2099 StudyMode/0 CurrentMode/0 CurrentFontScale/1.0 GlobalDensityScale/0.9818182 AllowLandscape/false InMagicWin/0",
            "Host": "web.qun.qq.com",
            "Origin": "https://web.qun.qq.com"
        }
        Cookies = {
            "p_skey": pskey,
            "uin": str(uin),
            "skey": skey,
            "p_uin": str(uin)
        }
        requests.post(f"https://web.qun.qq.com/cgi-bin/announce/add_qun_notice?bkn={q_bkn}", params=data,headers=headers, cookies=Cookies)
        QtWidgets.QMessageBox.about(self, "提示", "发布成功!")

    def qun_list(self,cookies,bkn):
        url = 'https://qun.qq.com/cgi-bin/qun_mgr/get_group_list'
        data = {'bkn':bkn}
        qun_lis = requests.post(url,data = data,cookies = cookies).json()
        try:
            with open("qun_list.csv",'w',newline='',encoding='utf-8-sig') as f:
                csv_f = csv.writer(f)
                csv_f.writerow(["群名","群号","群主","权限"])
                l = []
                try:
                    for i in qun_lis['create']:
                        csv_f.writerow([str(i['gc'])+'\t', str(i['gn']), str(i['owner'])+'\t',"群主"])
                except Exception as e:
                    print(e)
                try:
                    for i in qun_lis['manage']:
                        csv_f.writerow([str(i['gc'])+'\t', str(i['gn']), str(i['owner'])+'\t',"管理员"])
                except Exception as e:
                    print(e)
                try:
                    for i in qun_lis['join']:
                        csv_f.writerow([str(i['gc'])+'\t', str(i['gn']), str(i['owner'])+'\t',"成员"])
                except Exception as e:
                    print(e)
                print(l)
                csv_f.writerows(l)
                f.flush()
            QtWidgets.QMessageBox.about(self,"提示","已导出至qun_list.csv文件下!")
        except PermissionError:
            QtWidgets.QMessageBox.critical(self, "错误", "请关闭正在打开qun_list.csv的文件!")
        except Exception as e:
            QtWidgets.QMessageBox.about(self, "错误", "未知错误!")
    def cookies(self,ptqtoken, qrsig):
        _translate = QtCore.QCoreApplication.translate
        while True:
            global flag
            if flag == True:
                break
            l = requests.get(
                f"https://ssl.ptlogin2.qq.com/ptqrlogin?u1=https%3A%2F%2Fqun.qq.com%2F&ptqrtoken={ptqtoken}&ptredirect=1&h=1&t=1&g=1&from_ui=1&ptlang=2052&action={time.time()}&js_ver=23111510&js_type=1&login_sig=&pt_uistyle=40&aid=715030901&daid=73&&o1vId=2c2a6e92400bf8bd544ea329f5c8b5a0&pt_js_version=v1.48.1",
                cookies={"qrsig": qrsig})
            if '二维码未失效' in l.text:
                self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; color:#000000;\">当前状态:未失效</span></p><p><span style=\" font-size:11pt;\">QQ号码:</span></p><p><span style=\" font-size:11pt;\">Skey:</span></p></body></html>"))
            elif '二维码已失效' in l.text:
                self.label_2.setText(_translate("MainWindow","<html><head/><body><p><span style=\" font-size:11pt; color:#000000;\">当前状态:已失效</span></p><p><span style=\" font-size:11pt;\">QQ号码:</span></p><p><span style=\" font-size:11pt;\">Skey:</span></p></body></html>"))
                break
            elif '二维码认证中' in l.text:
                self.label_2.setText(_translate("MainWindow","<html><head/><body><p><span style=\" font-size:11pt; color:#000000;\">当前状态:认证中</span></p><p><span style=\" font-size:11pt;\">QQ号码:</span></p><p><span style=\" font-size:11pt;\">Skey:</span></p></body></html>"))
            else:
                cookies = requests.utils.dict_from_cookiejar(l.cookies)
                uin = requests.utils.dict_from_cookiejar(l.cookies).get('uin')
                regex = re.compile(r'ptsigx=(.*?)&')
                sigx = re.findall(regex, l.text)[0]
                url = f'https://ptlogin2.qun.qq.com/check_sig?pttype=1&uin={uin}&service=ptqrlogin&nodirect=0&ptsigx={sigx}&s_url=https%3A%2F%2Fqun.qq.com%2Fmanage.html&f_url=&ptlang=2052&ptredirect=101&aid=715030901&daid=73&j_later=0&low_login_hour=0&regmaster=0&pt_login_type=3&pt_aid=0&pt_aaid=16&pt_light=0&pt_3rd_aid=0'
                r2 = requests.get(url, cookies=cookies, allow_redirects=False)
                targetCookies = requests.utils.dict_from_cookiejar(r2.cookies)
                skey = requests.utils.dict_from_cookiejar(r2.cookies).get('skey')
                pskey = requests.utils.dict_from_cookiejar(r2.cookies).get('p_skey')
                self.skey, self.uin, self.pskey = skey, uin, pskey
                self.cookie = targetCookies
                self.label_2.setText(_translate("MainWindow",f"<html><head/><body><p><span style=\" font-size:11pt; color:#000000;\">当前状态:登录成功!</span></p><p><span style=\" font-size:11pt;\">QQ号码:{self.uin}</span></p><p><span style=\" font-size:11pt;\">Skey:{self.skey}</span></p></body></html>"))
                break
            time.sleep(0.5)

    def notice_list(self, q_bkn, qid, skey, pskey, uin):
        data = {
            "qid": qid,
            "bkn": q_bkn,
            "n":"10",
            "s":"-1",
            "ni":"undefined",
            "i":"1",
            "ft":"23"
        }
        headers = {
            "Referer": "https://web.qun.qq.com/mannounce/index.html?_wv=1031&_bid=148",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; MI 8 Build/QKQ1.190910.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.86 MQQBrowser/6.2 TBS/046715 Mobile Safari/537.36 V1_AND_SQ_8.9.78_4548_YYB_D QQ/8.9.78.12275 NetType/WIFI WebP/0.3.0 AppId/537175315 Pixel/1080 StatusBarHeight/82 SimpleUISwitch/0 QQTheme/2099 StudyMode/0 CurrentMode/0 CurrentFontScale/1.0 GlobalDensityScale/0.9818182 AllowLandscape/false InMagicWin/0",
            "Host": "web.qun.qq.com",
            "Origin": "https://web.qun.qq.com"
        }
        Cookies = {
            "p_skey": pskey,
            "uin": str(uin),
            "skey": skey,
            "p_uin": str(uin)
        }
        i = 9
        notices = []
        while True:
            res = requests.post(f"https://web.qun.qq.com/cgi-bin/announce/list_announce?bkn={q_bkn}", params=data,json=data,headers=headers, cookies=Cookies).json()
            if "feeds" in res or "inst" in res:
                print(1)
                i -= 10
                print(2)
                data['s'] = i
                try:
                    for j in res['feeds']:
                        notices.append([str(j['u'])+'\t',str(j['fid']),str(j['msg']['text'])+'\t'])
                except Exception as e:
                    print(e)
                try:
                    for j in res['inst']:
                        notices.append([str(j['u'])+'\t',str(j['fid']),str(j['msg']['text'])+'\t'])
                except Exception as e:
                    print(e)
            else:
                break
        try:
            with open("notice_list.csv",'w',newline='',encoding='utf-8-sig') as f:
                csv_f = csv.writer(f)
                csv_f.writerow(['发布者','fid','内容'])
                csv_f.writerows(notices)
            QtWidgets.QMessageBox.about(self, "提示", "已保存至notice_list.csv!")
        except PermissionError:
            QtWidgets.QMessageBox.critical(self, "错误", "请关闭正在打开notice_list.csv的文件!")
        except Exception as e:
            QtWidgets.QMessageBox.about(self, "错误", "未知错误!")

    def qun_members_list(self,bkn,qid,pskey,skey,uin):
        data = {
            "st":"0",
            "start":"0",
            "end":"9",
            "sort":"1",
            "group_id":str(qid),
            "gc":str(qid)
        }
        headers = {
            "Referer": "https://web.qun.qq.com/mannounce/index.html?_wv=1031&_bid=148",
            "Host": "qun.qq.com",
            "Origin": "https://qun.qq.com"
        }
        Cookies = {
            "p_skey": pskey,
            "uin": str(uin),
            "skey": skey,
            "p_uin": str(uin),
            "ptui_loginuin":str(uin)
        }
        l = []
        start = 0
        end = 9
        while True:
            res = requests.post(f"https://qun.qq.com/cgi-bin/qun_mgr/search_group_members?bkn={bkn}&ts=1702901784527",cookies=Cookies,data=data,headers=headers).json()
            try:
                for i in res['mems']:
                    print(l,[str(i['nick'])+'\t',str(i['uin'])+'\t'])
                    if [str(i['nick'])+'\t',str(i['uin'])+'\t'] in l:
                        break
                    l.append([str(i['nick'])+'\t',str(i['uin'])+'\t'])
                start += 10
                end += 10
                data['start'],data['end'] = str(start),str(end)
            except:
                break
        try:
            with open("mem_list.csv",'w',encoding='utf-8-sig',newline='') as f:
                csv_f = csv.writer(f)
                csv_f.writerow([f'群号:{self.lineEdit.text()}\t'])
                csv_f.writerow(['名称','QQ号'])
                csv_f.writerows(l)
            QtWidgets.QMessageBox.about(self, "提示", "已保存至mem_list.csv!")
        except PermissionError:
            QtWidgets.QMessageBox.critical(self, "错误", "请关闭正在打开mem_list.csv的文件!")
        except Exception as e:
            QtWidgets.QMessageBox.about(self, "错误", "未知错误!")

    def del_notice(self,fid, bkn, qid, skey, pskey,uin):
        data = {
            "qid": qid,
            "bkn": bkn,
            "fid":fid
        }
        headers = {
            "Referer": "https://web.qun.qq.com/mannounce/index.html?_wv=1031&_bid=148",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; MI 8 Build/QKQ1.190910.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.86 MQQBrowser/6.2 TBS/046715 Mobile Safari/537.36 V1_AND_SQ_8.9.78_4548_YYB_D QQ/8.9.78.12275 NetType/WIFI WebP/0.3.0 AppId/537175315 Pixel/1080 StatusBarHeight/82 SimpleUISwitch/0 QQTheme/2099 StudyMode/0 CurrentMode/0 CurrentFontScale/1.0 GlobalDensityScale/0.9818182 AllowLandscape/false InMagicWin/0",
            "Host": "web.qun.qq.com",
            "Origin": "https://web.qun.qq.com"
        }
        Cookies = {
            "p_skey": pskey,
            "uin": str(uin),
            "skey": skey,
            "p_uin": str(uin)
        }
        requests.post(f"https://web.qun.qq.com/cgi-bin/announce/del_feed?bkn={bkn}", json=data,params=data,headers=headers, cookies=Cookies)
        QtWidgets.QMessageBox.about(self, "提示", "删除成功!")
    def del_group_member(self,bkn,skey,pskey,uin,target,qid):
        Cookies = {
            "p_skey": pskey,
            "uin": str(uin),
            "skey": skey,
            "p_uin": str(uin),
            "ptui_loginuin":str(uin)
        }
        data = {
            "ul":str(target),
            "flag":"0",
            "bkn":str(bkn),
            "gc":qid
        }
        headers = {
            "Referer": "https://web.qun.qq.com/mannounce/index.html?_wv=1031&_bid=148",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; MI 8 Build/QKQ1.190910.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.86 MQQBrowser/6.2 TBS/046715 Mobile Safari/537.36 V1_AND_SQ_8.9.78_4548_YYB_D QQ/8.9.78.12275 NetType/WIFI WebP/0.3.0 AppId/537175315 Pixel/1080 StatusBarHeight/82 SimpleUISwitch/0 QQTheme/2099 StudyMode/0 CurrentMode/0 CurrentFontScale/1.0 GlobalDensityScale/0.9818182 AllowLandscape/false InMagicWin/0",
            "Host": "qun.qq.com",
            "Origin": "https://qun.qq.com"
        }
        requests.post(f"https://qun.qq.com/cgi-bin/qun_mgr/delete_group_member?bkn={bkn}&ts=1702905613568",data=data,cookies=Cookies,headers=headers)
        QtWidgets.QMessageBox.about(self, "提示", "删除成功!")
if __name__ == '__main__':
    #获取UIC窗口操作权限
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    #调自定义的界面（即刚转换的.py对象）
    Ui = skey大神.Ui_MainWindow()
    Ui.setupUi(MainWindow)
    #显示窗口并释放资源
    MainWindow.show()
    sys.exit(app.exec_())
