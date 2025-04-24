import sys
import os
import requests
from PIL import Image, ImageDraw, ImageFont
from PyQt5 import QtCore, QtGui, QtWidgets

def get_file_path(name):
    if getattr(sys, 'frozen', None):
        basedir = sys._MEIPASS
    else:
        basedir = os.path.dirname(__file__)
    file_path = os.path.join(basedir, name)
    return file_path


def download_image(url):
    """从 URL 下载图片"""
    response = requests.get(url)
    if response.status_code == 200:
        with open('temp_image.jpg', 'wb') as f:
            f.write(response.content)
        return 'temp_image.jpg'
    return None


def add_text_to_image(image_path, text, balance):
    """在图片下方中间添加文字和余额"""
    image = Image.open(image_path)
    # 缩小图片
    new_width = 110 if balance < 30 else 150
    new_height = 110 if balance < 30 else 150
    image = image.resize((new_width, new_height), Image.LANCZOS)

    width, height = image.size

    # 创建一个新的空白区域用于添加文字
    new_height = height + 60  # 增加高度以容纳余额信息
    new_image = Image.new('RGB', (width, new_height), color=(255, 255, 255))
    new_image.paste(image, (0, 0))

    # 在新的空白区域添加文字
    draw = ImageDraw.Draw(new_image)
    size = 15 if balance < 30 else 18
    font_path = r"C:\Windows\Fonts\微软雅黑\msyh.ttc" if balance < 30 else r"C:\Windows\Fonts\微软雅黑\msyhbd.ttc"
    font = ImageFont.truetype(font_path, size)

    # 绘制赞助者名字
    left, top, right, bottom = draw.textbbox((0, 0), text, font=font)
    text_width = right - left
    text_height = bottom - top
    text_x = (width - text_width) // 2
    text_y = height + 9 if balance < 30 else height + 5
    draw.text((text_x, text_y), text, fill=(0, 0, 0), font=font)

    # 绘制余额信息
    balance_text = u"%.2f 元" % balance
    left, top, right, bottom = draw.textbbox((0, 0), balance_text, font=font)
    balance_width = right - left
    balance_height = bottom - top
    balance_x = (width - balance_width) // 2
    balance_y = text_y + text_height + 5
    draw.text((balance_x, balance_y), balance_text, fill=(0, 0, 0), font=font)

    # 保存处理后的图片
    new_image_path = 'temp_image_with_text.jpg'
    new_image.save(new_image_path)
    return new_image_path


class Ui_Dialog(object):

    def setupUi(self, Dialog):
        self.Dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(760, 523)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(30)
        Dialog.setFont(font)
        Dialog.setWindowFlags(QtCore.Qt.WindowMaximizeButtonHint | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        Dialog.setFixedSize(Dialog.width(), Dialog.height())
        Dialog.setWindowIcon(QtGui.QIcon(get_file_path("./icon.ico")))
        self.dialog = Dialog
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, -10, 741, 111))
        self.label.setObjectName("label")
        # 创建滚动区域
        self.scroll_area = QtWidgets.QScrollArea(Dialog)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setGeometry(QtCore.QRect(20, 130, 411, 371))
        self.loading_label = QtWidgets.QLabel("获取中...", self.scroll_area)
        self.loading_label.setAlignment(QtCore.Qt.AlignCenter)
        self.loading_label.setGeometry(QtCore.QRect(0, 0, 411, 371))
        self.loading_label.setFont(QtGui.QFont("微软雅黑", 18))
        self.scroll_area.setWidget(self.loading_label)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 77, 371, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(450, 90, 301, 411))
        self.label_2.setText(f'<a href="https://afdian.com/a/sun589"><img src="{get_file_path(r"./afd.png")}"></a>')
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setObjectName("label_2")
        QtCore.QTimer.singleShot(0,self.load_sponsors_list)
        QtCore.QTimer.singleShot(3500, self.allow_close)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "赞助者列表 三秒后允许关闭"))
        self.label.setText(_translate("Dialog", "如果觉得好用欢迎赞助我,有神秘大礼:))*n"))
        self.label_3.setText(_translate("Dialog", "感谢以下老板的赞助:"))

    def allow_close(self):
        self.Dialog.setWindowTitle(QtCore.QCoreApplication.translate("Dialog", "赞助者列表"))
        current_flags = self.Dialog.windowHandle().flags()
        self.Dialog.windowHandle().setFlags(current_flags | QtCore.Qt.WindowCloseButtonHint)

    def load_sponsors_list(self):
        try:
            r1 = requests.get("https://gitee.com/sun589/sponsors/raw/master/sponsors",timeout=15).text.split('\n')
            sponsors = {i.split(" ")[0]:(i.split(" ")[2],float(i.split(" ")[1])) for i in r1 if i}
            content_widget = QtWidgets.QWidget()
            content_layout = QtWidgets.QVBoxLayout(content_widget)
            current_row = QtWidgets.QHBoxLayout()
            count = 0
            for sponsor_id, (image_url, balance) in sponsors.items():
                if sponsor_id == "sun589":
                    continue
                # 下载图片
                image_path = download_image(image_url)
                if image_path:
                    # 在图片上添加文字和余额
                    new_image_path = add_text_to_image(image_path, sponsor_id, balance)

                    # 创建 QLabel 显示图片
                    pixmap = QtGui.QPixmap(new_image_path)
                    label = QtWidgets.QLabel()
                    label.setPixmap(pixmap)
                    label.setAlignment(QtCore.Qt.AlignCenter)

                    # 将 QLabel 添加到布局中
                    current_row.addWidget(label)
                    count += 1

                    # 每行显示 3 个赞助者
                    if count % 3 == 0:
                        content_layout.addLayout(current_row)
                        current_row = QtWidgets.QHBoxLayout()

            # 添加最后一行
            if current_row.count() > 0:
                content_layout.addLayout(current_row)
            self.scroll_area.setWidget(content_widget)
        except:
            self.loading_label.setText("获取失败,请检查网络连接!")
            self.loading_label.setAlignment(QtCore.Qt.AlignCenter)
            self.loading_label.setGeometry(QtCore.QRect(0, 0, 411, 371))

if __name__ == '__main__':
    QtGui.QGuiApplication.setHighDpiScaleFactorRoundingPolicy(QtCore.Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QtGui.QGuiApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    # 获取UIC窗口操作权限
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()

    # 调自定义的界面（即刚转换的.py对象）
    Ui = Ui_Dialog()
    Ui.setupUi(Dialog)

    # 显示窗口并释放资源
    Dialog.show()
    sys.exit(app.exec_())