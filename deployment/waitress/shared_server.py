"""
    This class should create whole project
    In main thread we keep tray icon with settings button & methods
    In second thread we keep core HTTP server

    On exit, we will kill whole process
    On open folder we will open Windows Explorer with data folder

    Change path is more difficult, I should think about it more

    ~~~~ If you're reading this, you also can just buy me a coffee <3
"""
from threading import Thread

import pystray

from deployment.waitress.tray_menu import TrayMenu
from src.app import create_app
from src.config import Config

import PIL.Image
from waitress import serve


class SharedServer:
    def __init__(self):
        self.__exec_path = "C:\\Users\\danil\\pets\\shared-server"  # str(os.path.dirname(sys.executable))
        self.__config = Config(self.__exec_path)
        self.__tray_menu = TrayMenu(self.__config)
        self.__service_thread = Thread(target=self.__init_service)
        self.__icon = self.__init_tray_icon()

    def __init_tray_icon(self) -> pystray.Icon:
        """
        Open icon with next buttons:
        * Open folder
        * Change path
        * Exit
        :return: None
        """
        opened_icon = PIL.Image.open(self.__exec_path + "\\views\\static\\icon.jpg")
        icon = pystray.Icon(
            name="Shared Server",
            title="Shared Server",
            icon=opened_icon,
            menu=pystray.Menu(
                pystray.MenuItem("Open folder", self.__tray_menu.on_open_folder),
                pystray.MenuItem("Change folder", self.__tray_menu.on_change_path),
                pystray.MenuItem("Exit", self.__tray_menu.on_exit)
            )
        )
        return icon

    def __init_service(self) -> None:
        """
        Initialize a web server
        :return: None
        """
        app = create_app(self.__config)
        serve(app, host=self.__config.host, port=self.__config.port, threads=1)

    def run(self):
        self.__service_thread.start()
        self.__icon.run()


if __name__ == "__main__":
    shared_server = SharedServer()
    shared_server.run()
