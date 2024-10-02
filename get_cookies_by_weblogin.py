# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
import sys
import base64
import os

def get_file_path(name):
    if getattr(sys, 'frozen', None):
        basedir = sys._MEIPASS
    else:
        basedir = os.path.dirname(__file__)
    file_path = os.path.join(basedir, name)
    return file_path

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.cookies = {}
        Dialog.setObjectName("Dialog")
        Dialog.resize(761, 612)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        Dialog.setFont(font)
        Dialog.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint)
        Dialog.setFixedSize(Dialog.width(), Dialog.height())
        Dialog.setWindowIcon(QtGui.QIcon(get_file_path("./icon.ico")))
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(30, 445, 191, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.webpage = QtWebEngineWidgets.QWebEngineView(Dialog)
        self.webpage.setGeometry(30, 18, 701, 411)
        self.webpage.setObjectName("qtweb")
        self.webpage.page().profile().cookieStore().cookieAdded.connect(self.cookie_added)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(450, 440, 281, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.get_cookies)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 440, 211, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.change_page)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(410, 490, 321, 101))
        self.textEdit.setReadOnly(False)
        self.textEdit.setObjectName("textEdit")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(100, 570, 301, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 570, 81, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 490, 81, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 490, 301, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 517, 81, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 517, 301, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 543, 81, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(100, 543, 301, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Cookies获取器"))
        self.comboBox.setItemText(0, _translate("Dialog", "QQ空间"))
        self.comboBox.setItemText(1, _translate("Dialog", "QQ群"))
        self.comboBox.setItemText(2, _translate("Dialog", "QQ VIP"))
        self.pushButton.setText(_translate("Dialog", "获取Cookies"))
        self.pushButton_2.setText(_translate("Dialog", "进入页面"))
        self.label.setText(_translate("Dialog", "Key配置码:"))
        self.label_2.setText(_translate("Dialog", "QQ号:"))
        self.label_3.setText(_translate("Dialog", "Skey:"))
        self.label_4.setText(_translate("Dialog", "P_skey:"))
        html_content = """
<html>
<head>
    <title>My Web Page</title>
    <style>
    .container {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
    }
    </style>
</head>
<body>
  <div class="container">
    <h1>请选择需要登录的网站!</h1>
  </div>
</body>
</html>
        """
        self.webpage.setHtml(html_content)

    def change_page(self):
        html_content = """
        <html>
        <head>
            <title>My Web Page</title>
            <style>
            .container {
              position: absolute;
              top: 50%;
              left: 50%;
              transform: translate(-50%, -50%);
            }
            </style>
        </head>
        <body>
          <div class="container">
            <h1>加载中...</h1>
          </div>
        </body>
        </html>
                """
        self.webpage.setHtml(html_content)
        urls = ["https://xui.ptlogin2.qq.com/cgi-bin/xlogin?proxy_url=https%3A//qzs.qq.com/qzone/v6/portal/proxy.html&daid=5&&hide_title_bar=1&low_login=0&qlogin_auto_login=1&no_verifyimg=1&link_target=blank&appid=549000912&style=22&target=self&s_url=https%3A%2F%2Fqzs.qq.com%2Fqzone%2Fv5%2Floginsucc.html%3Fpara%3Dizone&pt_qr_app=%E6%89%8B%E6%9C%BAQQ%E7%A9%BA%E9%97%B4&pt_qr_link=https%3A//z.qzone.com/download.html&self_regurl=https%3A//qzs.qq.com/qzone/v6/reg/index.html&pt_qr_help_link=https%3A//z.qzone.com/download.html&pt_no_auth=0",
                "https://xui.ptlogin2.qq.com/cgi-bin/xlogin?pt_disable_pwd=1&appid=715030901&hide_close_icon=1&daid=73&pt_no_auth=1&s_url=https%3A%2F%2Fqun.qq.com%2F",
                "https://xui.ptlogin2.qq.com/cgi-bin/xlogin?appid=8000201&style=20&s_url=https%3A%2F%2Fvip.qq.com%2Floginsuccess.html&maskOpacity=60&daid=18&target=self"]
        index = self.comboBox.currentIndex()
        self.cookies = {}
        self.webpage.load(QtCore.QUrl(urls[index]))

    def get_cookies(self):
        # 获取当前页面的Cookie
        if self.cookies:
            if 'qzone' in self.webpage.url().toString(): g_tk = self.get_g_tk(self.cookies['p_skey'])
            else: g_tk = ''
            data = {
                "uin": self.cookies['uin'],
                "skey": self.cookies['skey'],
                "pskey": self.cookies['p_skey'],
                "cookie": self.cookies,
                "g_tk": g_tk,
                "login_url": ""
            }
            print(data)
            self.textEdit.setText('; '.join([f"{key}={value}" for key, value in self.cookies.items()]))
            self.lineEdit_2.setText(self.cookies['uin'])
            self.lineEdit_3.setText(self.cookies['skey'])
            self.lineEdit_4.setText(self.cookies['p_skey'])
            self.lineEdit.setText(base64.b64encode(str(data).replace("'",'"').encode('utf-8')).decode('utf-8'))

    def get_g_tk(self,p_skey):
        if 'qun' in self.webpage.url().toString():
            return ''
        t = 5381
        for i in p_skey:
            t += (t << 5) + ord(i)
        return t & 2147483647

    def cookie_added(self, cookie):
        self.cookies[cookie.name().data().decode('utf-8')] = cookie.value().data().decode('utf-8')
        if 'skey' not in self.cookies:
            self.cookies = {}
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