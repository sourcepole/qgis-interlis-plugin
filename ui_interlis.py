# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_interlis.ui'
#
# Created: Fri Mar 11 15:39:31 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Interlis(object):
    def setupUi(self, Interlis):
        Interlis.setObjectName(_fromUtf8("Interlis"))
        Interlis.resize(522, 270)
        self.gridLayout_2 = QtGui.QGridLayout(Interlis)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 2, 1, 1, 1)
        self.tabWidget = QtGui.QTabWidget(Interlis)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.transfertab = QtGui.QWidget()
        self.transfertab.setObjectName(_fromUtf8("transfertab"))
        self.gridLayout = QtGui.QGridLayout(self.transfertab)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.mImdGroupBox = gui.QgsCollapsibleGroupBoxBasic(self.transfertab)
        self.mImdGroupBox.setEnabled(True)
        self.mImdGroupBox.setProperty("collapsed", True)
        self.mImdGroupBox.setObjectName(_fromUtf8("mImdGroupBox"))
        self.gridLayout_3 = QtGui.QGridLayout(self.mImdGroupBox)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.mModelFileButton = QtGui.QPushButton(self.mImdGroupBox)
        self.mModelFileButton.setObjectName(_fromUtf8("mModelFileButton"))
        self.gridLayout_3.addWidget(self.mModelFileButton, 0, 3, 1, 1)
        self.mImportEnumsButton = QtGui.QPushButton(self.mImdGroupBox)
        self.mImportEnumsButton.setEnabled(False)
        self.mImportEnumsButton.setObjectName(_fromUtf8("mImportEnumsButton"))
        self.gridLayout_3.addWidget(self.mImportEnumsButton, 3, 2, 1, 1)
        self.mModelLineEdit = QtGui.QLineEdit(self.mImdGroupBox)
        self.mModelLineEdit.setObjectName(_fromUtf8("mModelLineEdit"))
        self.gridLayout_3.addWidget(self.mModelLineEdit, 0, 1, 1, 2)
        self.mModelFileLabel = QtGui.QLabel(self.mImdGroupBox)
        self.mModelFileLabel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.mModelFileLabel.setObjectName(_fromUtf8("mModelFileLabel"))
        self.gridLayout_3.addWidget(self.mModelFileLabel, 0, 0, 1, 1)
        self.mCreateSchemaButton = QtGui.QPushButton(self.mImdGroupBox)
        self.mCreateSchemaButton.setEnabled(False)
        self.mCreateSchemaButton.setObjectName(_fromUtf8("mCreateSchemaButton"))
        self.gridLayout_3.addWidget(self.mCreateSchemaButton, 3, 1, 1, 1)
        self.gridLayout.addWidget(self.mImdGroupBox, 2, 0, 1, 5)
        self.mDataFileLabel = QtGui.QLabel(self.transfertab)
        self.mDataFileLabel.setObjectName(_fromUtf8("mDataFileLabel"))
        self.gridLayout.addWidget(self.mDataFileLabel, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 1, 1, 1)
        self.cbDbConnections = QtGui.QComboBox(self.transfertab)
        self.cbDbConnections.setEnabled(False)
        self.cbDbConnections.setObjectName(_fromUtf8("cbDbConnections"))
        self.gridLayout.addWidget(self.cbDbConnections, 4, 3, 1, 2)
        self.mModelAutoLoadCheckBox = QtGui.QCheckBox(self.transfertab)
        self.mModelAutoLoadCheckBox.setChecked(True)
        self.mModelAutoLoadCheckBox.setObjectName(_fromUtf8("mModelAutoLoadCheckBox"))
        self.gridLayout.addWidget(self.mModelAutoLoadCheckBox, 1, 0, 1, 2)
        self.mDataFileButton = QtGui.QPushButton(self.transfertab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mDataFileButton.sizePolicy().hasHeightForWidth())
        self.mDataFileButton.setSizePolicy(sizePolicy)
        self.mDataFileButton.setObjectName(_fromUtf8("mDataFileButton"))
        self.gridLayout.addWidget(self.mDataFileButton, 0, 4, 1, 1)
        self.mQgisLayer = QtGui.QCheckBox(self.transfertab)
        self.mQgisLayer.setChecked(True)
        self.mQgisLayer.setObjectName(_fromUtf8("mQgisLayer"))
        self.gridLayout.addWidget(self.mQgisLayer, 4, 0, 1, 1)
        self.mDataLineEdit = QtGui.QLineEdit(self.transfertab)
        self.mDataLineEdit.setObjectName(_fromUtf8("mDataLineEdit"))
        self.gridLayout.addWidget(self.mDataLineEdit, 0, 1, 1, 3)
        self.mDestQgisLayerCheckBox = QtGui.QLabel(self.transfertab)
        self.mDestQgisLayerCheckBox.setObjectName(_fromUtf8("mDestQgisLayerCheckBox"))
        self.gridLayout.addWidget(self.mDestQgisLayerCheckBox, 4, 2, 1, 1)
        self.tabWidget.addTab(self.transfertab, _fromUtf8(""))
        self.settingstab = QtGui.QWidget()
        self.settingstab.setObjectName(_fromUtf8("settingstab"))
        self.gridLayout_5 = QtGui.QGridLayout(self.settingstab)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.frame_2 = QtGui.QFrame(self.settingstab)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.gridLayout_8 = QtGui.QGridLayout(self.frame_2)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.cbResetData = QtGui.QCheckBox(self.frame_2)
        self.cbResetData.setChecked(True)
        self.cbResetData.setObjectName(_fromUtf8("cbResetData"))
        self.gridLayout_8.addWidget(self.cbResetData, 4, 1, 1, 1)
        self.cbStrokeCurve = QtGui.QCheckBox(self.frame_2)
        self.cbStrokeCurve.setChecked(True)
        self.cbStrokeCurve.setObjectName(_fromUtf8("cbStrokeCurve"))
        self.gridLayout_8.addWidget(self.cbStrokeCurve, 5, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem2, 6, 1, 1, 1)
        self.mIlisMetaUrlLineEdit = QtGui.QLineEdit(self.frame_2)
        self.mIlisMetaUrlLineEdit.setObjectName(_fromUtf8("mIlisMetaUrlLineEdit"))
        self.gridLayout_8.addWidget(self.mIlisMetaUrlLineEdit, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.frame_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_8.addWidget(self.label_4, 1, 0, 1, 1)
        self.cbSkipFailures = QtGui.QCheckBox(self.frame_2)
        self.cbSkipFailures.setChecked(True)
        self.cbSkipFailures.setObjectName(_fromUtf8("cbSkipFailures"))
        self.gridLayout_8.addWidget(self.cbSkipFailures, 3, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.frame_2)
        self.label_3.setEnabled(False)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_8.addWidget(self.label_3, 2, 0, 1, 1)
        self.mRepoUrlLineEdit = QtGui.QLineEdit(self.frame_2)
        self.mRepoUrlLineEdit.setEnabled(False)
        self.mRepoUrlLineEdit.setObjectName(_fromUtf8("mRepoUrlLineEdit"))
        self.gridLayout_8.addWidget(self.mRepoUrlLineEdit, 2, 1, 1, 1)
        self.gridLayout_5.addWidget(self.frame_2, 1, 0, 1, 1)
        self.tabWidget.addTab(self.settingstab, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 3)
        self.buttonBox = QtGui.QDialogButtonBox(Interlis)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_2.addWidget(self.buttonBox, 2, 2, 1, 1)
        self.mImportButton = QtGui.QPushButton(Interlis)
        self.mImportButton.setEnabled(False)
        self.mImportButton.setObjectName(_fromUtf8("mImportButton"))
        self.gridLayout_2.addWidget(self.mImportButton, 2, 0, 1, 1)
        self.mModelFileLabel.setBuddy(self.mModelLineEdit)
        self.mDataFileLabel.setBuddy(self.mDataLineEdit)
        self.mDestQgisLayerCheckBox.setBuddy(self.cbDbConnections)
        self.label_4.setBuddy(self.mIlisMetaUrlLineEdit)
        self.label_3.setBuddy(self.mRepoUrlLineEdit)

        self.retranslateUi(Interlis)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Interlis.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Interlis.reject)
        QtCore.QObject.connect(self.mModelAutoLoadCheckBox, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.mImdGroupBox.setCollapsed)
        QtCore.QMetaObject.connectSlotsByName(Interlis)

    def retranslateUi(self, Interlis):
        Interlis.setWindowTitle(_translate("Interlis", "Interlis", None))
        self.mImdGroupBox.setTitle(_translate("Interlis", "Lokales Modell", None))
        self.mModelFileButton.setText(_translate("Interlis", "...", None))
        self.mImportEnumsButton.setText(_translate("Interlis", "Enums importieren", None))
        self.mModelFileLabel.setText(_translate("Interlis", "IlisMeta Modell:", None))
        self.mCreateSchemaButton.setText(_translate("Interlis", "DB-Tabellen anlegen", None))
        self.mDataFileLabel.setText(_translate("Interlis", "Transferfile:", None))
        self.mModelAutoLoadCheckBox.setText(_translate("Interlis", "Modell automatisch laden", None))
        self.mDataFileButton.setText(_translate("Interlis", "...", None))
        self.mQgisLayer.setText(_translate("Interlis", "QGIS Layer", None))
        self.mDestQgisLayerCheckBox.setText(_translate("Interlis", "PostGIS:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.transfertab), _translate("Interlis", "Import", None))
        self.cbResetData.setText(_translate("Interlis", "Daten ersetzen", None))
        self.cbStrokeCurve.setText(_translate("Interlis", "Kurven segmentieren", None))
        self.mIlisMetaUrlLineEdit.setText(_translate("Interlis", "http://interlis.sourcepole.ch/wps", None))
        self.label_4.setText(_translate("Interlis", "IlisMeta Lookup:", None))
        self.cbSkipFailures.setText(_translate("Interlis", "Import-Fehler überspringen", None))
        self.label_3.setText(_translate("Interlis", "Model Repositories:", None))
        self.mRepoUrlLineEdit.setText(_translate("Interlis", "http://models.interlis.ch/", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settingstab), _translate("Interlis", "Einstellungen", None))
        self.mImportButton.setText(_translate("Interlis", "Import", None))

from qgis import gui