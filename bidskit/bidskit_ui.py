# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bidskit.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1165, 826)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.dicomdirButton = QtWidgets.QPushButton(self.groupBox)
        self.dicomdirButton.setObjectName("dicomdirButton")
        self.gridLayout.addWidget(self.dicomdirButton, 0, 0, 1, 1)
        self.dicomdirText = QtWidgets.QLineEdit(self.groupBox)
        self.dicomdirText.setReadOnly(True)
        self.dicomdirText.setObjectName("dicomdirText")
        self.gridLayout.addWidget(self.dicomdirText, 0, 1, 1, 1)
        self.sourcedirLabel = QtWidgets.QLabel(self.groupBox)
        self.sourcedirLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sourcedirLabel.setObjectName("sourcedirLabel")
        self.gridLayout.addWidget(self.sourcedirLabel, 1, 0, 1, 1)
        self.sourcedirText = QtWidgets.QLineEdit(self.groupBox)
        self.sourcedirText.setReadOnly(True)
        self.sourcedirText.setObjectName("sourcedirText")
        self.gridLayout.addWidget(self.sourcedirText, 1, 1, 1, 1)
        self.derivdirLabel = QtWidgets.QLabel(self.groupBox)
        self.derivdirLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.derivdirLabel.setObjectName("derivdirLabel")
        self.gridLayout.addWidget(self.derivdirLabel, 2, 0, 1, 1)
        self.derivdirText = QtWidgets.QLineEdit(self.groupBox)
        self.derivdirText.setReadOnly(True)
        self.derivdirText.setObjectName("derivdirText")
        self.gridLayout.addWidget(self.derivdirText, 2, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_2)
        self.tableWidget.setRowCount(6)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 6, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(24)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setSortIndicatorShown(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.horizontalLayout.addWidget(self.tableWidget)
        self.BIDSTree = QtWidgets.QTreeView(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BIDSTree.sizePolicy().hasHeightForWidth())
        self.BIDSTree.setSizePolicy(sizePolicy)
        self.BIDSTree.setObjectName("BIDSTree")
        self.BIDSTree.header().setSortIndicatorShown(True)
        self.horizontalLayout.addWidget(self.BIDSTree)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setMinimumSize(QtCore.QSize(0, 64))
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_4.setMinimumSize(QtCore.QSize(200, 0))
        self.pushButton_4.setMaximumSize(QtCore.QSize(200, 16777215))
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_2.setMinimumSize(QtCore.QSize(200, 0))
        self.pushButton_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_3.setMinimumSize(QtCore.QSize(200, 0))
        self.pushButton_3.setMaximumSize(QtCore.QSize(200, 16777215))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.verticalLayout.addWidget(self.groupBox_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1165, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionDICOMDirMenu = QtWidgets.QAction(MainWindow)
        self.actionDICOMDirMenu.setObjectName("actionDICOMDirMenu")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionDICOMDirButton = QtWidgets.QAction(MainWindow)
        self.actionDICOMDirButton.setObjectName("actionDICOMDirButton")
        self.menuFile.addAction(self.actionDICOMDirMenu)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.actionQuit.triggered.connect(MainWindow.close)
        self.dicomdirButton.clicked.connect(self.actionDICOMDirButton.trigger)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BIDSKit"))
        self.groupBox.setTitle(_translate("MainWindow", "Directories"))
        self.dicomdirButton.setText(_translate("MainWindow", "DICOM Directory"))
        self.sourcedirLabel.setText(_translate("MainWindow", "Source Directory"))
        self.derivdirLabel.setText(_translate("MainWindow", "Derivatives Directory"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Conversion and Structure"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Original Series"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Purpose"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Task"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Acquisition"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Run"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Direction"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Sequence"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "Localizer"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "anat"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "-"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("MainWindow", "-"))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.item(0, 5)
        item.setText(_translate("MainWindow", "-"))
        item = self.tableWidget.item(0, 6)
        item.setText(_translate("MainWindow", "gre"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "T1w"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("MainWindow", "anat"))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("MainWindow", "-"))
        item = self.tableWidget.item(1, 3)
        item.setText(_translate("MainWindow", "-"))
        item = self.tableWidget.item(1, 4)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.item(1, 5)
        item.setText(_translate("MainWindow", "-"))
        item = self.tableWidget.item(1, 6)
        item.setText(_translate("MainWindow", "T1w"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("MainWindow", "T2w"))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("MainWindow", "anat"))
        item = self.tableWidget.item(2, 2)
        item.setText(_translate("MainWindow", "-"))
        item = self.tableWidget.item(2, 3)
        item.setText(_translate("MainWindow", "-"))
        item = self.tableWidget.item(2, 4)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.item(2, 5)
        item.setText(_translate("MainWindow", "-"))
        item = self.tableWidget.item(2, 6)
        item.setText(_translate("MainWindow", "T2w"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("MainWindow", "Rest1"))
        item = self.tableWidget.item(3, 1)
        item.setText(_translate("MainWindow", "func"))
        item = self.tableWidget.item(3, 2)
        item.setText(_translate("MainWindow", "rest"))
        item = self.tableWidget.item(3, 3)
        item.setText(_translate("MainWindow", "-"))
        item = self.tableWidget.item(3, 4)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.item(3, 5)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.item(3, 6)
        item.setText(_translate("MainWindow", "bold"))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("MainWindow", "FmapAP"))
        item = self.tableWidget.item(4, 1)
        item.setText(_translate("MainWindow", "fmap"))
        item = self.tableWidget.item(4, 2)
        item.setText(_translate("MainWindow", "-"))
        item = self.tableWidget.item(4, 3)
        item.setText(_translate("MainWindow", "-"))
        item = self.tableWidget.item(4, 4)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.item(4, 5)
        item.setText(_translate("MainWindow", "AP"))
        item = self.tableWidget.item(4, 6)
        item.setText(_translate("MainWindow", "epi"))
        item = self.tableWidget.item(5, 0)
        item.setText(_translate("MainWindow", "FmapPA"))
        item = self.tableWidget.item(5, 1)
        item.setText(_translate("MainWindow", "fmap"))
        item = self.tableWidget.item(5, 2)
        item.setText(_translate("MainWindow", "-"))
        item = self.tableWidget.item(5, 3)
        item.setText(_translate("MainWindow", "-"))
        item = self.tableWidget.item(5, 4)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.item(5, 5)
        item.setText(_translate("MainWindow", "PA"))
        item = self.tableWidget.item(5, 6)
        item.setText(_translate("MainWindow", "epi"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.groupBox_3.setTitle(_translate("MainWindow", "Actions"))
        self.pushButton_4.setText(_translate("MainWindow", "Scan DICOM Directory"))
        self.pushButton_2.setText(_translate("MainWindow", "Convert to BIDS"))
        self.pushButton_3.setText(_translate("MainWindow", "Validate BIDS"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionDICOMDirMenu.setText(_translate("MainWindow", "Select DICOM Directory"))
        self.actionDICOMDirMenu.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionDICOMDirButton.setText(_translate("MainWindow", "DICOMDirButton"))

