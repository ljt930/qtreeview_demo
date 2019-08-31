# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_departemtinfo.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DepartmentInfo(object):
    def setupUi(self, DepartmentInfo):
        DepartmentInfo.setObjectName("DepartmentInfo")
        DepartmentInfo.resize(387, 367)
        self.verticalLayout = QtWidgets.QVBoxLayout(DepartmentInfo)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_bizOrgId = QtWidgets.QLabel(DepartmentInfo)
        self.label_bizOrgId.setObjectName("label_bizOrgId")
        self.gridLayout.addWidget(self.label_bizOrgId, 1, 0, 1, 1)
        self.lineEdit_parentBizOrgId = QtWidgets.QLineEdit(DepartmentInfo)
        self.lineEdit_parentBizOrgId.setObjectName("lineEdit_parentBizOrgId")
        self.gridLayout.addWidget(self.lineEdit_parentBizOrgId, 2, 1, 1, 1)
        self.lineEdit_bizOrgCode = QtWidgets.QLineEdit(DepartmentInfo)
        self.lineEdit_bizOrgCode.setObjectName("lineEdit_bizOrgCode")
        self.gridLayout.addWidget(self.lineEdit_bizOrgCode, 3, 1, 1, 1)
        self.label_bizOrgId_3 = QtWidgets.QLabel(DepartmentInfo)
        self.label_bizOrgId_3.setObjectName("label_bizOrgId_3")
        self.gridLayout.addWidget(self.label_bizOrgId_3, 3, 0, 1, 1)
        self.lineEdit_bizOrgId = QtWidgets.QLineEdit(DepartmentInfo)
        self.lineEdit_bizOrgId.setObjectName("lineEdit_bizOrgId")
        self.gridLayout.addWidget(self.lineEdit_bizOrgId, 1, 1, 1, 1)
        self.label_bizOrgId_2 = QtWidgets.QLabel(DepartmentInfo)
        self.label_bizOrgId_2.setObjectName("label_bizOrgId_2")
        self.gridLayout.addWidget(self.label_bizOrgId_2, 2, 0, 1, 1)
        self.lineEdit_Name = QtWidgets.QLineEdit(DepartmentInfo)
        self.lineEdit_Name.setObjectName("lineEdit_Name")
        self.gridLayout.addWidget(self.lineEdit_Name, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(DepartmentInfo)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(DepartmentInfo)
        QtCore.QMetaObject.connectSlotsByName(DepartmentInfo)

    def retranslateUi(self, DepartmentInfo):
        _translate = QtCore.QCoreApplication.translate
        DepartmentInfo.setWindowTitle(_translate("DepartmentInfo", "Form"))
        self.label_bizOrgId.setText(_translate("DepartmentInfo", "bizOrgId:"))
        self.label_bizOrgId_3.setText(_translate("DepartmentInfo", "bizOrgCode:"))
        self.label_bizOrgId_2.setText(_translate("DepartmentInfo", "parentBizOrgId:"))
        self.label.setText(_translate("DepartmentInfo", "Name:"))

