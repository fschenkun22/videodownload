# Importing the necessary libraries
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QThread, Signal, Slot, QSize
import sys


class DownloadThread(QThread):
    signal_tuple = Signal(tuple)

    def __init__(self):
        super().__init__()
        print("DownloadThread")
        # 关闭当前线程
        self.run()

    def run (self):
        # 下载文件
        print("run")
        self.feedback("开始下载文件")

    def feedback(self, data):
        self.signal_tuple.emit(data)


class MainWindow(QWidget):
    def __init__(self):
        loader = QUiLoader()
        f = QFile("src/main.ui")
        f.open(QFile.ReadOnly)
        f.close()
        self.ui = loader.load(f)
        # 绑定槽
        self.ui.pushButton.clicked.connect(self.on_click)
        self.ui.textEdit.append("Hello World!")

    def on_click(self):
        self.setup_thread()

    def setup_thread(self):
        # 禁用按键
        self.ui.pushButton.setEnabled(False)
        # 创建线程
        self.thread = DownloadThread()
        # 绑定信号
        self.thread.signal_tuple.connect(self.download_finished)
        # 启动线程
        self.thread.start()

    @Slot(tuple)
    def download_finished(self, data):
        print("接收到download_finished信号", data)
        


app = QApplication(sys.argv)
window = MainWindow()
window.ui.show()
app.exec()
