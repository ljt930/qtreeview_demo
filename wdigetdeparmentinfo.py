#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 23:41
# @Author  : Aries
# @Site    : 
# @File    : wdigetdeparmentinfo.py
# @Software: PyCharm

import sys
from UI.UI_widget_departemtinfo import Ui_DepartmentInfo
from PyQt5 import QtWidgets


class DepartemtInfo(QtWidgets.QWidget, Ui_DepartmentInfo):
    def __init__(self,parent=None):
        super(DepartemtInfo,self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    tools = DepartemtInfo()
    tools.show()
    sys.exit(app.exec_())

