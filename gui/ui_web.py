# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'web.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(736, 398)
        self.actionReturn = QAction(MainWindow)
        self.actionReturn.setObjectName(u"actionReturn")
        self.actionElement_View = QAction(MainWindow)
        self.actionElement_View.setObjectName(u"actionElement_View")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.TopBar = QFrame(self.centralwidget)
        self.TopBar.setObjectName(u"TopBar")
        self.TopBar.setMaximumSize(QSize(16777215, 40))
        self.TopBar.setStyleSheet(u"QFrame[accessibleName=\"TopBar\"] {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.983, y2:0.954545, stop:0 rgba(142, 187, 255, 255), stop:1 rgba(170, 255, 255, 255));\n"
"}")
        self.TopBar.setFrameShape(QFrame.NoFrame)
        self.TopBar.setFrameShadow(QFrame.Plain)
        self.TopBar.setLineWidth(0)
        self.horizontalLayout = QHBoxLayout(self.TopBar)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Money = QLabel(self.TopBar)
        self.Money.setObjectName(u"Money")

        self.horizontalLayout.addWidget(self.Money)

        self.AddressBar = QLineEdit(self.TopBar)
        self.AddressBar.setObjectName(u"AddressBar")
        self.AddressBar.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.AddressBar)

        self.NavigateButton = QPushButton(self.TopBar)
        self.NavigateButton.setObjectName(u"NavigateButton")
        self.NavigateButton.setMinimumSize(QSize(0, 21))
        self.NavigateButton.setMaximumSize(QSize(16777215, 75))

        self.horizontalLayout.addWidget(self.NavigateButton)


        self.verticalLayout.addWidget(self.TopBar)

        self.WebContents = QScrollArea(self.centralwidget)
        self.WebContents.setObjectName(u"WebContents")
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.WebContents.sizePolicy().hasHeightForWidth())
        self.WebContents.setSizePolicy(sizePolicy)
        self.WebContents.setFrameShape(QFrame.NoFrame)
        self.WebContents.setFrameShadow(QFrame.Plain)
        self.WebContents.setLineWidth(0)
        self.WebContents.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 602, 317))
        sizePolicy1 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy1)
        self.WebBodyLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.WebBodyLayout.setObjectName(u"WebBodyLayout")
        self.WebContents.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.WebContents)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 736, 21))
        self.menuPage = QMenu(self.menubar)
        self.menuPage.setObjectName(u"menuPage")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.ElementDock = QDockWidget(MainWindow)
        self.ElementDock.setObjectName(u"ElementDock")
        self.ElementDock.setMinimumSize(QSize(130, 38))
        self.ElementDock.setFeatures(QDockWidget.DockWidgetClosable)
        self.ElementDock.setAllowedAreas(Qt.LeftDockWidgetArea)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout_2 = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.ElementList = QTreeWidget(self.dockWidgetContents)
        self.ElementList.setObjectName(u"ElementList")
        sizePolicy2 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ElementList.sizePolicy().hasHeightForWidth())
        self.ElementList.setSizePolicy(sizePolicy2)
        self.ElementList.setRootIsDecorated(True)
        self.ElementList.setWordWrap(True)
        self.ElementList.setHeaderHidden(True)

        self.verticalLayout_2.addWidget(self.ElementList)

        self.ElementDock.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.LeftDockWidgetArea, self.ElementDock)

        self.menubar.addAction(self.menuPage.menuAction())
        self.menuPage.addAction(self.actionReturn)
        self.menuPage.addAction(self.actionElement_View)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"BobuxNet Browser", None))
        self.actionReturn.setText(QCoreApplication.translate("MainWindow", u"Return", None))
#if QT_CONFIG(shortcut)
        self.actionReturn.setShortcut(QCoreApplication.translate("MainWindow", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.actionElement_View.setText(QCoreApplication.translate("MainWindow", u"Element View", None))
#if QT_CONFIG(accessibility)
        self.TopBar.setAccessibleName(QCoreApplication.translate("MainWindow", u"TopBar", None))
#endif // QT_CONFIG(accessibility)
        self.Money.setText(QCoreApplication.translate("MainWindow", u"0 BOBUX", None))
        self.AddressBar.setText(QCoreApplication.translate("MainWindow", u"hello.com", None))
        self.AddressBar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Shop Address..", None))
        self.NavigateButton.setText(QCoreApplication.translate("MainWindow", u"Navigate", None))
        self.menuPage.setTitle(QCoreApplication.translate("MainWindow", u"Page", None))
        self.ElementDock.setWindowTitle(QCoreApplication.translate("MainWindow", u"Elements", None))
        ___qtreewidgetitem = self.ElementList.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Element", None));
    # retranslateUi

