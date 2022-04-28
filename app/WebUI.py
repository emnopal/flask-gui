import PyQt5.QtCore as core
import PyQt5.QtWidgets as core_widgets
import PyQt5.QtWebEngineWidgets as web_widgets
import PyQt5.QtGui as gui

from threading import Thread
from app import CustomWebEnginePage
from app import DEFAULT_HOST, DEFAULT_PORT, IS_DEBUG, APP_NAME


class WebUI(object):

    def __init__(self, app, using_win32=False, icon_path=None, width=None, height=None):

        self.flask_app = app
        self.flask_thread = Thread(
            target=self._run_flask,
            args=(DEFAULT_HOST, DEFAULT_PORT, IS_DEBUG(), using_win32)
        )
        self.flask_thread.daemon = True
        self.debug = IS_DEBUG()

        self.using_win32 = using_win32

        self.url = f"http://{DEFAULT_HOST}:{DEFAULT_PORT}"
        self.app = core_widgets.QApplication([])
        self.app.setWindowIcon(gui.QIcon(icon_path))
        self.app.setApplicationName(APP_NAME)
        self.view = web_widgets.QWebEngineView(self.app.activeModalWidget())
        self.page = CustomWebEnginePage(self.view)
        self.view.setPage(self.page)

    def run(self):
        self.run_flask()
        self.run_gui()

    def run_flask(self):
        self.flask_thread.start()

    def run_gui(self):
        self.view.load(core.QUrl(self.url))
        change_setting = self.view.page().settings().setAttribute
        settings = web_widgets.QWebEngineSettings
        change_setting(settings.LocalStorageEnabled, True)
        change_setting(settings.PluginsEnabled, True)
        self.view.showMaximized()
        self.app.exec_()

    def _run_flask(self):
        print(DEFAULT_HOST)
        if self.using_win32:
            import pythoncom
            pythoncom.CoInitialize()
        self.flask_app.run(debug=IS_DEBUG(), host=DEFAULT_HOST, port=DEFAULT_PORT, use_reloader=False)
