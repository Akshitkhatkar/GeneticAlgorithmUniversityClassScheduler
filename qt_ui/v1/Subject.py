# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subject.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(716, 553)
        Dialog.setMinimumSize(QtCore.QSize(716, 553))
        Dialog.setMaximumSize(QtCore.QSize(716, 553))
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEditName = QtWidgets.QLineEdit(Dialog)
        self.lineEditName.setObjectName("lineEditName")
        self.gridLayout.addWidget(self.lineEditName, 0, 1, 1, 1)
        self.lineEditHours = QtWidgets.QLineEdit(Dialog)
        self.lineEditHours.setObjectName("lineEditHours")
        self.gridLayout.addWidget(self.lineEditHours, 0, 4, 1, 1)
        self.lblName = QtWidgets.QLabel(Dialog)
        self.lblName.setObjectName("lblName")
        self.gridLayout.addWidget(self.lblName, 0, 0, 1, 1)
        self.lblHours = QtWidgets.QLabel(Dialog)
        self.lblHours.setObjectName("lblHours")
        self.gridLayout.addWidget(self.lblHours, 0, 3, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioYes = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioYes.setObjectName("radioYes")
        self.horizontalLayout_2.addWidget(self.radioYes)
        self.radioNo = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioNo.setObjectName("radioNo")
        self.horizontalLayout_2.addWidget(self.radioNo)
        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 2)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radioLec = QtWidgets.QRadioButton(self.groupBox)
        self.radioLec.setObjectName("radioLec")
        self.horizontalLayout_3.addWidget(self.radioLec)
        self.radioLab = QtWidgets.QRadioButton(self.groupBox)
        self.radioLab.setObjectName("radioLab")
        self.horizontalLayout_3.addWidget(self.radioLab)
        self.gridLayout.addWidget(self.groupBox, 1, 3, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        self.tableSchedule = QtWidgets.QTableView(Dialog)
        self.tableSchedule.setObjectName("tableSchedule")
        self.verticalLayout.addWidget(self.tableSchedule)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnFinish = QtWidgets.QPushButton(Dialog)
        self.btnFinish.setObjectName("btnFinish")
        self.horizontalLayout.addWidget(self.btnFinish)
        self.btnCancel = QtWidgets.QPushButton(Dialog)
        self.btnCancel.setObjectName("btnCancel")
        self.horizontalLayout.addWidget(self.btnCancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Subject"))
        self.lblName.setText(_translate("Dialog", "Name"))
        self.lblHours.setText(_translate("Dialog", "Hours/Week"))
        self.groupBox_2.setTitle(_translate("Dialog", "Divisible Schedule"))
        self.radioYes.setText(_translate("Dialog", "Yes"))
        self.radioNo.setText(_translate("Dialog", "No"))
        self.groupBox.setTitle(_translate("Dialog", "Type"))
        self.radioLec.setText(_translate("Dialog", "Lecture"))
        self.radioLab.setText(_translate("Dialog", "Laboratory"))
        self.btnFinish.setText(_translate("Dialog", "Finish"))
        self.btnCancel.setText(_translate("Dialog", "Cancel"))

