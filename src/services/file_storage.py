from src.config import Config


class FileStorageService:
    def __init__(self, config: Config):
        self.__files = []
        self.__folder: str = config.directory_path

    @property
    def files(self) -> list:
        return self.__files

    def file(self, filename: str) -> str:
        return self.__folder + filename
