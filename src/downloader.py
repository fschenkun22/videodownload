"""
downloader module for downloading files from the internet

"""

import subprocess
import time
from command_define import CommandFormat
import os


class FileDownloader:
    """
     abstract class for downloading files from the internet

    """

    def downloader(self) -> None:
        pass


class Youtube_dl(FileDownloader):
    """
    Youtube_dl class for downloading files from the internet

    """

    def __init__(self,feedback):
        super().__init__()
        self.feedback = feedback


    def downloader(self, C: CommandFormat):
        self.cmd = C.cmd
        self.url = C.url
        self.proxy = C.proxy
        self.feedback('开始下载：'+self.url)
        print('downloader开始下载', self.cmd, self.url, self.proxy)
        print(os.getcwd()+'\\bin\\youtbe-dl.exe')
        self.feedback(os.system(os.getcwd()+'\\bin\\youtube-dl.exe'+ ' ' + self.url)) 
        print('downloader下载完成')
        

      



if __name__ == "__main__":
    cmd = "youtube-dl"
    url = "https://www.youtube.com/watch?v=rtmGjjHEK-g"
    proxy = "127.0.0.1"
    command = CommandFormat(cmd, url, proxy)
    downloader = Youtube_dl()
    downloader.downloader(command)
