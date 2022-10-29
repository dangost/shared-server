import os

ENV_DATA_FOLDER = "SHARED_DATA_FOLDER"
ENV_SERVER_HOST = "SHARED_SERVER_HOST"
ENV_SERVER_PORT = "SHARED_SERVER_PORT"


class Config:
    def __init__(self, exec_path: str = ""):
        self.__directory_path = ""
        self.directory_path = os.getenv(ENV_DATA_FOLDER, exec_path + '\\data')
        self.host = os.getenv(ENV_SERVER_HOST, "0.0.0.0")
        self.port = int(os.getenv(ENV_SERVER_PORT, 8888))
        self.killing_delay = 0.1

    @property
    def directory_path(self) -> str:
        return self.__directory_path

    @directory_path.setter
    def directory_path(self, directory_path) -> None:
        if os.path.exists(directory_path):
            if os.path.isdir(directory_path):
                self.__directory_path = directory_path
        else:
            os.mkdir(directory_path)
            self.__directory_path = directory_path
