#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/22 23:53
# @Author  : Aries
# @Site    : 
# @File    : wdigetgetuserinfo.py
# @Software: PyCharm
import sys
from UI.UI_widget_userinfo import Ui_UserInfo
from PyQt5 import QtWidgets


class UserInfo(QtWidgets.QWidget, Ui_UserInfo):
    def __init__(self,parent=None):
        super(UserInfo,self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    tools = UserInfo()
    tools.show()
    sys.exit(app.exec_())