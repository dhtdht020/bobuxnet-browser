import os
import sys
import re
from functools import partial

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QInputDialog, QLineEdit, QMessageBox, QSplashScreen, QLabel, \
    QListWidgetItem, QFileDialog, QListWidget
import requests

import xmlparser

import gui.ui_web

# Get resource when frozen with PyInstaller
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


# G U I
class MainWindow(gui.ui_web.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = gui.ui_web.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.WebBodyLayout.setAlignment(Qt.AlignTop)
        self.history = []
        self.ui.ElementDock.close()
        self.connect_things()

    def connect_things(self):
        self.ui.NavigateButton.clicked.connect(partial(self.navigate_button))
        self.ui.actionReturn.triggered.connect(self.back_button)
        self.ui.actionElement_View.triggered.connect(self.open_elementview)

    def navigate_button(self):
        url = self.ui.AddressBar.text()
        self.history.append(url)
        self.navigate()

    def navigate(self):
        self.clear_page()
        url = self.ui.AddressBar.text()
        if url.endswith("/") is False:
            url = url + "/"

        self.ui.ElementList.clear()

        # Get hostname (**hostname**.tld/path)
        regex_hostname = re.compile(r'([^.]+)')
        hostname = re.search(regex_hostname, url).group(1)

        # Get tld (hostname.**tld**/path)
        regex_tld = re.compile(r'(?<=\.)(.*?)(?=/)')
        tld = re.search(regex_tld, url).group(1)

        # Get path (hostname.tld/**path**)
        print(url)
        regex_path = re.compile(r'(?<=/).*')
        path = re.search(regex_path, url).group(0)[:-1]

        if path == "":
            path = "index.xml"

        print(hostname)
        print(tld)
        print(path)

        self.ui.statusbar.showMessage(f"Loading {hostname}.{tld}..")
        self.repaint()

        # Get index
        request = requests.get(f"https://raw.githubusercontent.com/dhtdht020/bobuxnet-sites/main/"
                     f"{tld}/{hostname}/{path}")
        if request.status_code == 200:
            xmlparser.parse(self, request.text)
        else:
            xmlparser.add_heading(self, f"Can't connect to {url}!")
            xmlparser.add_label(self, "This URL either does not exist, or BobuxNet is down. :(")
            xmlparser.add_spacer(self, "50")
            xmlparser.add_link(self, "Try Again", url)
            xmlparser.add_link(self, "Go Back", self.previous_page())

    def clear_page(self):
        for i in reversed(range(self.ui.WebBodyLayout.count())):
            try:
                self.ui.WebBodyLayout.itemAt(i).widget().setParent(None)
            except AttributeError:
                item = self.ui.WebBodyLayout.itemAt(i)
                self.ui.WebBodyLayout.removeItem(item)

    def previous_page(self):
        if len(self.history) > 0:
            page = self.history[-2]
            print(self.history)
            self.history.remove(self.history[-1])
            return page
        else:
            return ""

    def back_button(self):
        try:
            self.ui.AddressBar.setText(self.previous_page())
            self.navigate()
        except IndexError:
            self.ui.statusbar.showMessage("There's nothing to go back to!")

    def open_elementview(self):
        self.ui.ElementDock.show()


if __name__ == "__main__":
    app = QApplication()

    window = MainWindow()
    window.show()
    app.exec_()
