#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 22:34
# @Author  : Aries
# @Site    : 
# @File    : orgedit.py
# @Software: PyCharm

import sys
from UI.UI_orgedittool import Ui_Form
from PyQt5 import QtWidgets
import json
import wdigetgetuserinfo
import wdigetdeparmentinfo
import sip

class OrgEdit(QtWidgets.QWidget, Ui_Form):
    """b
    #方法二：先把ui文件转换成py文件。
    再通过继承 ui中的类Ui_MainWindow，直接初始化
    """

    def __init__(self):
        super(OrgEdit, self).__init__()
        self.setupUi(self)
        self.__inittree()
        self.__init_info()



    def __inittree(self):
        import orgtreemodel
        import user_data
        # u = user_data.user()
        # userdata = u.getUser4A()
        userdata = {}
        with open('deparment.json', 'r', encoding='utf8') as fp:
            json_in = fp.read().replace('\\', '')
            deparment = json.loads(json_in, encoding='utf8')
        t_data = deparment["deptDatas"]

        self.verticalLayout_tree = QtWidgets.QVBoxLayout(self.widget_treeview_org)
        self.verticalLayout_tree.setContentsMargins(0, 0, 0, 0)
        model = orgtreemodel.TreeModel()
        model.setupData(t_data,userdata)


        view = QtWidgets.QTreeView(self.widget_treeview_org)
        view.setModel(model)
        view.setHeaderHidden(True)
        view.setItemsExpandable(True)
        view.resizeColumnToContents(0)
        self.verticalLayout_tree.addWidget(view)


        view.clicked.connect(self.showinfo)
    def __init_info(self):
        self.verticalLayout_info = QtWidgets.QVBoxLayout(self.widget_info)
        self.verticalLayout_info.setContentsMargins(0, 0, 0, 0)
        self.spacerItem = QtWidgets.QSpacerItem(0, 200, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.w_info = wdigetdeparmentinfo.DepartemtInfo(self.widget_info)
        self.verticalLayout_info.addWidget(self.w_info)
        self.spacerItem = QtWidgets.QSpacerItem(0, 200, QtWidgets.QSizePolicy.Minimum,
                                                QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_info.addItem(self.spacerItem)


    def showinfo(self,index):
        item = index.internalPointer()
        _type = item.getType()
        if _type == 'department':
            self.verticalLayout_info.removeWidget(self.w_info)
            self.verticalLayout_info.removeItem(self.spacerItem)
            self.w_info.deleteLater()
            # sip.delete(self.w_info)
            # sip.delete(self.spacerItem)
            print(self.w_info)

            # print(item.itemData)
            self.w_info = wdigetdeparmentinfo.DepartemtInfo(self.widget_info)
            self.verticalLayout_info.addWidget(self.w_info)
            # self.spacerItem = QtWidgets.QSpacerItem(0, 200, QtWidgets.QSizePolicy.Minimum,
            #                                         QtWidgets.QSizePolicy.Expanding)
            self.verticalLayout_info.addItem(self.spacerItem)

            self.w_info.lineEdit_Name.setText(item.getItemName())
            self.w_info.lineEdit_bizOrgId.setText(item.getItemId())
            self.w_info.lineEdit_bizOrgCode.setText(item.getItemCode())
            self.w_info.lineEdit_parentBizOrgId.setText(item.getItemUid())
        else:
            self.verticalLayout_info.removeWidget(self.w_info)
            self.verticalLayout_info.removeItem(self.spacerItem)
            sip.delete(self.w_info)
            sip.delete(self.spacerItem)
            print(item.itemData)
            self.w_info = wdigetgetuserinfo.UserInfo(self.widget_info)
            self.verticalLayout_info.addWidget(self.w_info)
            self.spacerItem = QtWidgets.QSpacerItem(0, 200, QtWidgets.QSizePolicy.Minimum,
                                                    QtWidgets.QSizePolicy.Expanding)
            self.verticalLayout_info.addItem(self.spacerItem)

            self.w_info.lineEdit_Name.setText(item.getItemName())
            self.w_info.lineEdit_bizOrgId.setText(item.getItemId())

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    tools = OrgEdit()
    tools.show()
    sys.exit(app.exec_())