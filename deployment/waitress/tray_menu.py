import os
import signal
import time
import subprocess
from threading import Thread

from src.config import Config


class TrayMenu:
    def __init__(self, config: Config):
        self.__config = config

    def on_open_folder(self):
        self.__run_explorer_subprocess()

    def __run_explorer_subprocess(self):
        Thread(target=subprocess.run, args=[['explorer', self.__config.directory_path]]).start()

    def on_change_path(self):
        # todo
        pass

    def on_exit(self):
        pid = os.getpid()
        time.sleep(self.__config.killing_delay)
        os.kill(pid, signal.SIGINT)
