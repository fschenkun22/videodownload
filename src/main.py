# Importing the necessary libraries
import time
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QThread, Signal, Slot, QSize
import sys
from downloader import Youtube_dl
from command_define import CommandFormat


class DownloadThread(QThread):
    signal_tuple = Signal(tuple)

    def __init__(self, props: CommandFormat):
        super().__init__()
        self.cmd = props.cmd
        self.url = props.url
        self.proxy = props.proxy
        print("DownloadThread", self.cmd, self.url, self.proxy)

    def run(self):
        self.start_download()

    def stop(self):
        print("this thread will be terminated!")
        self.terminate()

    def start_download(self):
        self.feedback(
            (time.time(), '<font color="#00f"> start download! </font>'))
        C = CommandFormat(self.cmd, self.url, self.proxy)
        Y = Youtube_dl(feedback=self.feedback)
        Y.downloader(C)
        self.feedback('download finished!')


    def feedback(self, data):
        self.signal_tuple.emit(data)


class MainWindow(QWidget):
    def __init__(self):
        loader = QUiLoader()
        f = QFile("main.ui")
        f.open(QFile.ReadOnly)
        f.close()
        self.ui = loader.load(f)
        # 绑定槽
        self.ui.pushButton.clicked.connect(self.on_click)
        self.ui.textEdit.append("Powered by 大海绵")
        # textEdit.append 超级链接
        self.ui.textEdit.append(
            '<a href="https://github.com/fschenkun22/videodownload">https://github.com/fschenkun22/videodownload</a>')

    def on_click(self):
        self.setup_thread()

    def setup_thread(self):
        self.ui.pushButton.setEnabled(False)
        C = CommandFormat(
            'youtube-dl',
             self.ui.lineEdit.text(),
            '127.0.0.1'
        )

        self.thread: DownloadThread = DownloadThread(C)
        self.thread.signal_tuple.connect(self.download_finished)
        self.thread.start()

    @Slot(tuple)
    def download_finished(self, data):
        print("接收到download_finished信号", data)
        self.ui.textEdit.append(str(data))
        # 如果收到的信息是download finished，那么就关闭线程
        if data == 'download finished!':
            self.ui.pushButton.setEnabled(True)
            self.thread.stop()
            self.thread.wait()


    

app = QApplication(sys.argv)
window = MainWindow()
window.ui.show()
app.exec()
