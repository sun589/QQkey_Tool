# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import subprocess

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(252, 72)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        Dialog.setFont(font)
        Dialog.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint)
        Dialog.setFixedSize(Dialog.width(), Dialog.height())
        Dialog.setWindowIcon(QtGui.QIcon("./icon.ico"))
        self.centralwidget = QtWidgets.QWidget(Dialog)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 30, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda:self.write_host(0))
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 30, 91, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda:self.write_host(1))
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(21, 7, 131, 16))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "QQKey漏洞修复器"))
        self.pushButton.setText(_translate("Dialog", "修复"))
        self.pushButton_2.setText(_translate("Dialog", "恢复"))
        with open('C:\Windows\System32\drivers\etc\hosts') as f:
            content = f.read()
        self.label.setText(_translate("Dialog", f"当前状态:{'已修复' if '0.0.0.0 localhost.ptlogin2.qq.com' in content else '未修复'}"))

    def write_host(self,choose):
        _translate = QtCore.QCoreApplication.translate
        if choose == 0:
            with open('C:\Windows\System32\drivers\etc\hosts',encoding='utf-8') as f:
                content = f.read()
            with open('C:\Windows\System32\drivers\etc\hosts','w+',encoding='utf-8') as f:
                if '0.0.0.0 localhost.ptlogin2.qq.com' not in content:
                    f.write(content+'\n0.0.0.0 localhost.ptlogin2.qq.com')
                else:
                    f.write(content)
        else:
            with open('C:\Windows\System32\drivers\etc\hosts',encoding='utf-8') as f:
                content = f.readlines()
            try:
                with open('C:\Windows\System32\drivers\etc\hosts','w+',encoding='utf-8') as f:
                    for i in range(0,len(content)):
                        if '0.0.0.0 localhost.ptlogin2.qq.com' in content[i]:
                            del content[i]
                    f.write(''.join(content))
            except Exception as e:
                print(repr(e))
        subprocess.call("ipconfig /flushdns",creationflags=subprocess.CREATE_NO_WINDOW)
        with open('C:\Windows\System32\drivers\etc\hosts') as f:
            content = f.read()
        self.label.setText(_translate("Dialog",
                                      f"当前状态:{'已修复' if '0.0.0.0 localhost.ptlogin2.qq.com' in content else '未修复'}"))
        QtWidgets.QMessageBox.information(self.centralwidget,"提示","操作完成!")


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