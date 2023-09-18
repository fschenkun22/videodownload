"""
downloader module for downloading files from the internet

"""

from command_define import CommandFormat


class FileDownloader:
    """
     abstract class for downloading files from the internet

    """

    def downloader(self) -> CommandFormat :
        pass


class Youtube_dl(FileDownloader):
    """
    Youtube_dl class for downloading files from the internet

    """

    def __init__(self):
        super().__init__()

    def downloader(self, CommandFormat):
        self.cmd = CommandFormat.cmd
        self.url = CommandFormat.addr
        self.proxy = CommandFormat.proxy

        print (self.cmd, self.url, self.proxy)



if __name__ == "__main__":
    cmd = "youtube-dl"
    url = "https://www.youtube.com/watch?v=4zH8aT3PHKM"
    proxy = "127.0.0.1"
    command = CommandFormat(cmd, url, proxy)
    downloader = Youtube_dl()
    downloader.downloader(command)
