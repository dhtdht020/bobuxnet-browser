import os
import sys
from functools import partial

from PySide2.QtCore import QLine, QSize
from PySide2.QtGui import QFont, Qt, QFontMetrics, QIcon
import xml.etree.ElementTree as ET
from PySide2.QtWidgets import QApplication, QMainWindow, QInputDialog, QLineEdit, QMessageBox, QSplashScreen, QLabel, \
    QListWidgetItem, QFileDialog, QListWidget, QPushButton, QFrame, QSizePolicy, QSpacerItem, QTreeWidgetItem


# Get resource when frozen with PyInstaller
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


def parse(context, xml):
    content = ET.fromstring(xml)

    for elem in content.findall('.//page_contents/'):
        # Add to element view
        elementview_item = QTreeWidgetItem()
        elementview_item.setText(0, elem.tag)

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
            try:
                elem.attrib["alignment"]
            except KeyError:
                elem.attrib["alignment"] = "left"

            # Add heading
            add_heading(context, text=elem.text,
                        size=elem.attrib["size"],
                        bold=elem.attrib["bold"],
                        alignment=elem.attrib["alignment"])

            # Add info to element list
            text_child = QTreeWidgetItem()
            text_child.setText(0, f'"{elem.text}"')
            text_child.setIcon(0, QIcon(resource_path("./gui/assets/elements/type/text.png")))

            bold_child = QTreeWidgetItem()
            bold_child.setText(0, f"Bold: {str(elem.attrib['bold'])}")
            bold_child.setIcon(0, QIcon(resource_path("./gui/assets/elements/type/bold.png")))

            size_child = QTreeWidgetItem()
            size_child.setText(0, f"Size: {str(elem.attrib['size'])}")
            size_child.setIcon(0, QIcon(resource_path("./gui/assets/elements/type/font_size.png")))

            alignment_child = QTreeWidgetItem()
            alignment_child.setText(0, f"Alignment: {str(elem.attrib['alignment'])}")
            alignment_child.setIcon(0, QIcon(resource_path("./gui/assets/elements/type/alignment.png")))

            elementview_item.setIcon(0, QIcon(resource_path("./gui/assets/elements/heading.png")))
            elementview_item.addChildren([text_child, bold_child, size_child, alignment_child])

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
            try:
                elem.attrib["alignment"]
            except KeyError:
                elem.attrib["alignment"] = "left"

            # Add Label
            add_label(context,
                      text=elem.text,
                      size=elem.attrib["size"],
                      bold=elem.attrib["bold"],
                      alignment=elem.attrib["alignment"])

            # Add info to element list
            text_child = QTreeWidgetItem()
            text_child.setText(0, f'"{elem.text}"')
            text_child.setIcon(0, QIcon(resource_path("./gui/assets/elements/type/text.png")))

            bold_child = QTreeWidgetItem()
            bold_child.setText(0, f"Bold: {str(elem.attrib['bold'])}")
            bold_child.setIcon(0, QIcon(resource_path("./gui/assets/elements/type/bold.png")))

            size_child = QTreeWidgetItem()
            size_child.setText(0, f"Size: {str(elem.attrib['size'])}")
            size_child.setIcon(0, QIcon(resource_path("./gui/assets/elements/type/font_size.png")))

            alignment_child = QTreeWidgetItem()
            alignment_child.setText(0, f"Alignment: {str(elem.attrib['alignment'])}")
            alignment_child.setIcon(0, QIcon(resource_path("./gui/assets/elements/type/alignment.png")))

            elementview_item.setIcon(0, QIcon(resource_path("./gui/assets/elements/label.png")))
            elementview_item.addChildren([text_child, bold_child, size_child, alignment_child])

        if elem.tag == "link":
            # Error Handling
            try:
                elem.attrib["href"]
            except KeyError:
                elem.attrib["href"] = ""
            try:
                elem.attrib["alignment"]
            except KeyError:
                elem.attrib["alignment"] = "left"

            # Add link
            add_link(context, text=elem.text, location=elem.attrib["href"], alignment=elem.attrib["alignment"])

            # Add info to element list
            location_child = QTreeWidgetItem()
            location_child.setText(0, f"Location: {str(elem.attrib['href'])}")
            location_child.setIcon(0, QIcon(resource_path("./gui/assets/elements/type/link.png")))

            alignment_child = QTreeWidgetItem()
            alignment_child.setText(0, f"Alignment: {str(elem.attrib['alignment'])}")
            alignment_child.setIcon(0, QIcon(resource_path("./gui/assets/elements/type/alignment.png")))

            elementview_item.setIcon(0, QIcon(resource_path("./gui/assets/elements/link.png")))
            elementview_item.addChildren([location_child, alignment_child])

        if elem.tag == "horizontal_line":
            # Add horizontal line
            add_horizontal_line(context)
            elementview_item.setIcon(0, QIcon(resource_path("./gui/assets/elements/horizontal_line.png")))

        if elem.tag == "spacer":
            # Error Handling
            try:
                elem.attrib["height"]
            except KeyError:
                elem.attrib["height"] = "20"

            # Add Spacer
            add_spacer(context, height=elem.attrib["height"])

            # Add info to element view
            elementview_item.setIcon(0, QIcon(resource_path("./gui/assets/elements/spacer.png")))
            height_child = QTreeWidgetItem()
            height_child.setText(0, f"Height: {str(elem.attrib['height'])}")
            height_child.setIcon(0, QIcon(resource_path("./gui/assets/elements/type/height.png")))

            elementview_item.addChildren([height_child])

        context.ui.ElementList.addTopLevelItem(elementview_item)

    # print(elem)
    # print(content.find("page_header"))
    context.ui.statusbar.showMessage(f"Done!")


def add_heading(context, text="", size="20", bold=False, alignment="left"):
    font = QFont()
    font.setPixelSize(int(size))
    if bold == "true":
        font.setBold(True)
    widget = QLabel()
    widget.setText(text)

    if alignment == "left":
        widget.setAlignment(Qt.AlignLeft)
    elif alignment == "right":
        widget.setAlignment(Qt.AlignRight)
    elif alignment == "center":
        widget.setAlignment(Qt.AlignCenter)

    widget.setWordWrap(True)
    widget.setFont(font)
    widget.setTextInteractionFlags(Qt.TextSelectableByMouse)
    context.ui.WebBodyLayout.addWidget(widget)


def add_label(context, text="", size="12", bold=False, alignment="left"):
    font = QFont()
    font.setPixelSize(int(size))
    if bold == "true":
        font.setBold(True)
    widget = QLabel()
    widget.setText(text)

    if alignment == "left":
        widget.setAlignment(Qt.AlignLeft)
    elif alignment == "right":
        widget.setAlignment(Qt.AlignRight)
    elif alignment == "center":
        widget.setAlignment(Qt.AlignCenter)

    widget.setWordWrap(True)
    widget.setFont(font)
    widget.setTextInteractionFlags(Qt.TextSelectableByMouse)
    context.ui.WebBodyLayout.addWidget(widget)


def add_link(context, text="", location="", alignment="left"):
    widget = QPushButton(context.ui.scrollAreaWidgetContents)
    if text == "":
        widget.setText(location)
    else:
        widget.setText(f"{text} ({location})")
        widget.setCursor(Qt.PointingHandCursor)

        # Set Stylesheet
        widget.setStyleSheet(
            f"""
            QPushButton {{
                text-align: {alignment};
                background-color: transparent;
                border : 0px solid #0000EE;
                color: #0000EE;
                border-bottom: 1px solid #0000EE;
            }}

            QPushButton:pressed {{
                background-color: transparent;
                border : 0px solid #ff0000;
                color: #ff0000;
                border-bottom: 1px solid #ff0000;
            }}
            """
        )

    # font = QFont()
    # font_metric = QFontMetrics(font)
    # button_width = font_metric.width(text)
    # widget.setMaximumSize(QSize(button_width, 16777215))
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
