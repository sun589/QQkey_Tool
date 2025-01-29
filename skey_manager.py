# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QDialog
import struct
import json
import os

def get_file_path(name):
    if getattr(sys, 'frozen', None):
        basedir = sys._MEIPASS
    else:
        basedir = os.path.dirname(__file__)
    file_path = os.path.join(basedir, name)
    return file_path

class CustomQuestionDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("加载方式选择")
        self.setup_ui()
        self.selected_option = None

    def setup_ui(self):
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.setFont(font)
        layout = QtWidgets.QVBoxLayout()

        # 创建按钮
        self.load_from_software_button = QtWidgets.QPushButton("从软件内加载/添加")
        self.load_from_file_button = QtWidgets.QPushButton("从文件内加载/添加")
        self.cancel_button = QtWidgets.QPushButton("取消")

        # 连接按钮的点击信号到相应的槽函数
        self.load_from_software_button.clicked.connect(self.on_load_from_software_clicked)
        self.load_from_file_button.clicked.connect(self.on_load_from_file_clicked)
        self.cancel_button.clicked.connect(self.on_cancel_clicked)

        # 将按钮添加到布局中
        layout.addWidget(self.load_from_software_button)
        layout.addWidget(self.load_from_file_button)
        layout.addWidget(self.cancel_button)

        self.setLayout(layout)

    def on_load_from_software_clicked(self):
        self.selected_option = "从软件内加载/添加"
        self.accept()

    def on_load_from_file_clicked(self):
        self.selected_option = "从文件内加载/添加"
        self.accept()

    def on_cancel_clicked(self):
        self.selected_option = "取消"
        self.reject()

class Ui_Dialog(object):

    def __init__(self, signal1=None, signal2=None):
        self.signal1,self.signal2 = signal1,signal2

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        self.centralwidget = QtWidgets.QWidget(Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        Dialog.setFont(font)
        Dialog.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint)
        Dialog.setFixedSize(312, 300)
        Dialog.setWindowIcon(QtGui.QIcon(get_file_path('icon.ico')))
        Dialog.setAcceptDrops(True)
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(30, 20, 256, 192))
        self.listWidget.setObjectName("listWidget")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(Dialog)
        self.commandLinkButton.setGeometry(QtCore.QRect(170, 220, 111, 41))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.commandLinkButton.clicked.connect(self.save_key)
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(Dialog)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(40, 220, 101, 41))
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.commandLinkButton_2.clicked.connect(self.load_key_from_file)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(166, 265, 121, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda:self.listWidget.takeItem(self.listWidget.currentRow()))
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 265, 121, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.ask_how_add_key)
        self.signal2.connect(self.add_key)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Skey管理器 双击导入skey"))
        self.commandLinkButton.setText(_translate("Dialog", "保存至..."))
        self.commandLinkButton_2.setText(_translate("Dialog", "加载Key"))
        self.pushButton.setText(_translate("Dialog", "删除选中的skey"))
        self.pushButton_2.setText(_translate("Dialog", "添加skey"))

    def load_key_from_file(self, add=False):
        filepath, type = QtWidgets.QFileDialog.getOpenFileName(self.centralwidget, "文件选择", "/",'skey文件(*.qktkey)')
        if not filepath:
            return
        with open(filepath,'rb') as f:
            packed_data = f.read()
        unpacked_data = []
        offset = 0
        try:
            while offset < len(packed_data):
                # 读取JSON字符串的长度
                str_len = struct.unpack('>I', packed_data[offset:offset + 4])[0]
                offset += 4

                # 读取JSON字符串
                json_str = packed_data[offset:offset + str_len].decode()
                offset += str_len

                # 将JSON字符串转换为字典
                unpacked_data.append(json.loads(json_str))
        except:
            QtWidgets.QMessageBox.critical(self.centralwidget, '错误', '文件格式错误')
            return
        if not add:
            self.listWidget.clear()
        for key in unpacked_data:
            self.add_key(key)

    def ask_how_add_key(self):
        dialog = CustomQuestionDialog()
        dialog.exec_()
        if dialog.selected_option == '从软件内加载/添加':
            self.signal1.emit(0)
            return
        elif dialog.selected_option == '从文件内加载/添加':
            self.load_key_from_file(True)
            return
        else:
            return

    def save_key(self):
        keys = [self.listWidget.item(i).data(QtCore.Qt.UserRole) for i in range(self.listWidget.count())]
        filepath, type = QtWidgets.QFileDialog.getSaveFileName(self.centralwidget, "文件保存", "/", 'skey文件(*.qktkey)')
        if not filepath:
            return
        try:
            with open(filepath,'wb') as f:
                json_strings = [json.dumps(d) for d in keys]
                content = b''.join(struct.pack('>I', len(s)) + s.encode() for s in json_strings)
                f.write(content)
        except:
            QtWidgets.QMessageBox.critical(self.centralwidget, '错误', '保存失败')
            return
        QtWidgets.QMessageBox.information(self.centralwidget, '提示', '保存成功')

    def add_key(self, data:dict):
        if data['uin']:
            item = QtWidgets.QListWidgetItem()
            item.setData(QtCore.Qt.UserRole, data)
            item.setData(QtCore.Qt.DisplayRole, str(data['uin']))
            self.listWidget.addItem(item)

if __name__ == '__main__':
    class EmittingSignal(QtCore.QObject):
        signal = QtCore.pyqtSignal(tuple)
        signal2 = QtCore.pyqtSignal(int)
    signal = EmittingSignal()
    app = QtWidgets.QApplication(sys.argv)
    dialog = QDialog()
    ui = Ui_Dialog(signal.signal, signal.signal2)
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())