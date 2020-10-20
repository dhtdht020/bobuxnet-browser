from functools import partial

from PySide2.QtCore import QLine, QSize
from PySide2.QtGui import QFont, Qt, QFontMetrics
import xml.etree.ElementTree as ET
from PySide2.QtWidgets import QApplication, QMainWindow, QInputDialog, QLineEdit, QMessageBox, QSplashScreen, QLabel, \
    QListWidgetItem, QFileDialog, QListWidget, QPushButton, QFrame, QSizePolicy, QSpacerItem


def parse(context, xml):
    content = ET.fromstring(xml)

    for elem in content.findall('.//page_contents/'):
        print(elem.tag)

        if elem.tag == "heading":
            # Error Handling
            try:
                elem.attrib["bold"]
            except KeyError:
                elem.attrib["bold"] = False
            try:
                elem.attrib["size"]
            except KeyError:
                elem.attrib["size"] = "20"

            # Add heading
            add_heading(context, text=elem.text, size=elem.attrib["size"], bold=elem.attrib["bold"])

        if elem.tag == "label":
            # Error Handling
            try:
                elem.attrib["bold"]
            except KeyError:
                elem.attrib["bold"] = False
            try:
                elem.attrib["size"]
            except KeyError:
                elem.attrib["size"] = "12"

            # Add Label
            add_label(context, text=elem.text, size=elem.attrib["size"], bold=elem.attrib["bold"])

        if elem.tag == "link":
            # Error Handling
            try:
                elem.attrib["href"]
            except KeyError:
                elem.attrib["href"] = ""

            # Add link
            add_link(context, text=elem.text, location=elem.attrib["href"])

        if elem.tag == "horizontal_line":
            # Add horizontal line
            add_horizontal_line(context)

        if elem.tag == "spacer":
            # Error Handling
            try:
                elem.attrib["height"]
            except KeyError:
                elem.attrib["height"] = "20"

            # Add Spacer
            add_spacer(context, height=elem.attrib["height"])


    # print(elem)
    # print(content.find("page_header"))
    context.ui.statusbar.showMessage(f"Done!")


def add_heading(context, text="", size="20", bold=False):
    font = QFont()
    font.setPixelSize(int(size))
    if bold == "true":
        font.setBold(True)
    widget = QLabel()
    widget.setText(text)
    widget.setWordWrap(True)
    widget.setFont(font)
    widget.setTextInteractionFlags(Qt.TextSelectableByMouse)
    context.ui.WebBodyLayout.addWidget(widget)


def add_label(context, text="", size="12", bold=False):
    font = QFont()
    font.setPixelSize(int(size))
    if bold == "true":
        font.setBold(True)
    widget = QLabel()
    widget.setText(text)
    widget.setWordWrap(True)
    widget.setFont(font)
    widget.setTextInteractionFlags(Qt.TextSelectableByMouse)
    context.ui.WebBodyLayout.addWidget(widget)


def add_link(context, text="", location=""):
    widget = QPushButton(context.ui.scrollAreaWidgetContents)
    if text == "":
        widget.setText(location)
    else:
        widget.setText(f"{text} ({location})")
    #font = QFont()
    #font_metric = QFontMetrics(font)
    #button_width = font_metric.width(text)
    #widget.setMaximumSize(QSize(button_width, 16777215))
    # Align text to left
    widget.setStyleSheet("QPushButton {"
                         "text-align: left;"
                         "}")
    widget.clicked.connect(lambda context=context, location=location: click_link(context, location))
    context.ui.WebBodyLayout.addWidget(widget)


def click_link(context, location):
    context.ui.AddressBar.setText(location)
    context.navigate_button()


def add_horizontal_line(context):
    widget = QFrame()
    widget.setFrameShape(QFrame.HLine)
    widget.setFrameShadow(QFrame.Sunken)
    context.ui.WebBodyLayout.addWidget(widget)


def add_spacer(context, height="20"):
    context.ui.WebBodyLayout.addSpacing(int(height))

