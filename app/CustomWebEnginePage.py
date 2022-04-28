import PyQt5.QtWebEngineWidgets as web_widgets
import PyQt5.QtGui as gui

class CustomWebEnginePage(web_widgets.QWebEnginePage):
    def createWindow(self, _type):
        page = CustomWebEnginePage(self)
        page.urlChanged.connect(self.open_browser)
        return page

    def open_browser(self, url):
        page = self.sender()
        gui.QDesktopServices.openUrl(url)
        page.deleteLater()
