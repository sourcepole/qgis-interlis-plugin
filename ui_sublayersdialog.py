# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_sublayersdialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SublayersDialog(object):
    def setupUi(self, SublayersDialog):
        SublayersDialog.setObjectName("SublayersDialog")
        SublayersDialog.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(SublayersDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.mSublayersTreeWidget = QtWidgets.QTreeWidget(SublayersDialog)
        self.mSublayersTreeWidget.setRootIsDecorated(False)
        self.mSublayersTreeWidget.setItemsExpandable(False)
        self.mSublayersTreeWidget.setObjectName("mSublayersTreeWidget")
        self.mSublayersTreeWidget.headerItem().setText(0, "1")
        self.gridLayout.addWidget(self.mSublayersTreeWidget, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(SublayersDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(SublayersDialog)
        self.buttonBox.accepted.connect(SublayersDialog.accept)
        self.buttonBox.rejected.connect(SublayersDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SublayersDialog)

    def retranslateUi(self, SublayersDialog):
        _translate = QtCore.QCoreApplication.translate
        SublayersDialog.setWindowTitle(_translate("SublayersDialog", "Interlis sublayers"))

