# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_userinfo.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_UserInfo(object):
    def setupUi(self, UserInfo):
        UserInfo.setObjectName("UserInfo")
        UserInfo.resize(273, 173)
        self.verticalLayout = QtWidgets.QVBoxLayout(UserInfo)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(UserInfo)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_Name = QtWidgets.QLineEdit(UserInfo)
        self.lineEdit_Name.setObjectName("lineEdit_Name")
        self.gridLayout.addWidget(self.lineEdit_Name, 0, 1, 1, 1)
        self.label_bizOrgId_2 = QtWidgets.QLabel(UserInfo)
        self.label_bizOrgId_2.setObjectName("label_bizOrgId_2")
        self.gridLayout.addWidget(self.label_bizOrgId_2, 1, 0, 1, 1)
        self.lineEdit_userId = QtWidgets.QLineEdit(UserInfo)
        self.lineEdit_userId.setObjectName("lineEdit_userId")
        self.gridLayout.addWidget(self.lineEdit_userId, 1, 1, 1, 1)
        self.label_bizOrgId_3 = QtWidgets.QLabel(UserInfo)
        self.label_bizOrgId_3.setObjectName("label_bizOrgId_3")
        self.gridLayout.addWidget(self.label_bizOrgId_3, 2, 0, 1, 1)
        self.lineEdit_loginName = QtWidgets.QLineEdit(UserInfo)
        self.lineEdit_loginName.setObjectName("lineEdit_loginName")
        self.gridLayout.addWidget(self.lineEdit_loginName, 2, 1, 1, 1)
        self.label_bizOrgId = QtWidgets.QLabel(UserInfo)
        self.label_bizOrgId.setObjectName("label_bizOrgId")
        self.gridLayout.addWidget(self.label_bizOrgId, 3, 0, 1, 1)
        self.lineEdit_bizOrgId = QtWidgets.QLineEdit(UserInfo)
        self.lineEdit_bizOrgId.setObjectName("lineEdit_bizOrgId")
        self.gridLayout.addWidget(self.lineEdit_bizOrgId, 3, 1, 1, 1)
        self.label_baseOrgName = QtWidgets.QLabel(UserInfo)
        self.label_baseOrgName.setObjectName("label_baseOrgName")
        self.gridLayout.addWidget(self.label_baseOrgName, 4, 0, 1, 1)
        self.lineEdit_baseOrgName = QtWidgets.QLineEdit(UserInfo)
        self.lineEdit_baseOrgName.setObjectName("lineEdit_baseOrgName")
        self.gridLayout.addWidget(self.lineEdit_baseOrgName, 4, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(UserInfo)
        QtCore.QMetaObject.connectSlotsByName(UserInfo)

    def retranslateUi(self, UserInfo):
        _translate = QtCore.QCoreApplication.translate
        UserInfo.setWindowTitle(_translate("UserInfo", "Form"))
        self.label.setText(_translate("UserInfo", "Name:"))
        self.label_bizOrgId_2.setText(_translate("UserInfo", "userId:"))
        self.label_bizOrgId_3.setText(_translate("UserInfo", "loginName:"))
        self.label_bizOrgId.setText(_translate("UserInfo", "bizOrgId:"))
        self.label_baseOrgName.setText(_translate("UserInfo", "bbaseOrgName:"))

