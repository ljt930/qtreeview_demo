#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2010 Riverbank Computing Limited.
## Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).
## All rights reserved.
##
## This file is part of the examples of PyQt.
##
## $QT_BEGIN_LICENSE:BSD$
## You may use this file under the terms of the BSD license as follows:
##
## "Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are
## met:
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above copyright
##     notice, this list of conditions and the following disclaimer in
##     the documentation and/or other materials provided with the
##     distribution.
##   * Neither the name of Nokia Corporation and its Subsidiary(-ies) nor
##     the names of its contributors may be used to endorse or promote
##     products derived from this software without specific prior written
##     permission.
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
## $QT_END_LICENSE$
##
#############################################################################

from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui

# try:
#     import simpletreemodel_rc3
# except ImportError:
#     import simpletreemodel_rc2


class TreeItem(object):

    def __init__(self, data=None, parent=None):
        self.parentItem = parent
        self.itemData = data
        # self.value = list(data.values())
        self.childItems = []
        self.childIds = {}

        # self.itemUid = data['parentBizOrgId']
        # self.itemId = data['bizOrgId']
        # self.displayName = data['bizOrgName']

    def appendChild(self, item):
        self.childItems.append(item)

    def getAllChilds(self):
        return self.childItems

    def child(self, row):
        return self.childItems[row]

    def childCount(self):
        return len(self.childItems)

    def columnCount(self):
        # return len(self.itemData)
        return 1
    def data(self, column):
        try:
            # return (self.getItemName(),self.getItemId(),self.getItemUid(),self.getItemCode())[column]
            return self.itemData
        except IndexError:
            return None

    def parent(self):
        return self.parentItem

    def row(self):
        if self.parentItem:
            return self.parentItem.childItems.index(self)

        return 0

    def itemdata(self):
        return self.itemData

    def remove(self, itme):
        # print(itme.itemData['bizOrgName'],self.childItems)
        # print("itme",itme)
        self.childItems.remove(itme)



class departmentTreeItem(TreeItem):

    def __init__(self, data=None, parent=None):
        super(departmentTreeItem, self).__init__(data)
        self.parentItem = parent
        self.itemData = data
        # self.value = list(data.values())
        self.childItems = []
        self.childIds = {} ###ID-item的字典

    def appendChild(self, item):
        """
        ##添加子节点item
        :param item:
        :return:
        """
        ##添加一个ID-item的字典--self.childIds，方便根据ID查找到其item
        self.childIds[item.getItemId()] = item

        self.childItems.append(item)
    def data(self, column):
        try:
            return self.getItemName()
        except IndexError:
            return None
    def columnCount(self):
        # return len(self.itemData)
        return 1

    def moveChildItmes(self, items, newparent):
        for item in items:

            self.remove(item)
            item.parentItem = newparent
            newparent.appendChild(item)
            # self.remove(item)
        pass

    def findParentItmeFromUID(self,uid):
        """
        ##根据目标节点的父ID、在该层节点中所有的ID-子节点字典中，查找到相同ID，找到对应的item
        :param uid: 源节点的父ID，
        :return: Item
        """
        return self.childIds.get(uid)

    def findChildItmesFromId(self, id):
        """
        ##根据目标节点ID，在该层节点中查找所有子节点的父ID与目标节点ID相同的item
        :param id: 根据目标节点ID
        :return: 子节点Item
        """
        #获取该层节点中，所有的子节点
        childs = self.getAllChilds()

        # items = [ child for child in childs if child.itemData['parentBizOrgId'] == id]#
        items = []
        ##该层子item的父ID，与目标节点ID相同的，则为目标节点的子节点，添加到items中
        for child in childs:
            if child.getItemUid() == id:
                items.append(child)
        return items

    def getType(self):
        return 'department'

    def getItemId(self):
        if self.itemData:
            return self.itemData['bizOrgId']

    def getItemName(self):
        if self.itemData:
            return self.itemData['bizOrgName']

    def getItemUid(self):
        if self.itemData:
            return self.itemData['parentBizOrgId']
    def getItemCode(self):
        if self.itemData:
            return self.itemData['bizOrgCode']

class userItem(TreeItem):
    def __init__(self, data, parent=None):
        super(userItem,self).__init__(data)
        self.parentItem = parent
        self.itemData = data
        self.value = list(data.values())
        self.childItems = []
        self.childIds = {}

    def appendChild(self, item):

        self.childItems.append(item)
    def data(self, column):
        try:
            # return (self.getItemName(),self.getItemId(),self.getItemUid(),self.getItemCode())[column]
            return self.getItemName()
        except IndexError:
            return None

    def getType(self):
        return 'user'
    def getItemId(self):
        return self.itemData['userID']

    def getItemName(self):
        return self.itemData['realName']

    def getItemUid(self):
        return self.itemData['bizOrgId']
    def getItemCode(self):
        return self.itemData['loginName']

class TreeModel(QtCore.QAbstractItemModel):
    def __init__(self, parent=None):
        super(TreeModel, self).__init__(parent)
        self.departmet_map = dict()
        _dep_head = {'bizOrgId':'bizOrgId','bizOrgName':'head','parentBizOrgId':'parentBizOrgId','bizOrgCode':'bizOrgCode'}
        self.rootItem = departmentTreeItem()

    def columnCount(self, parent=None, *args, **kwargs):
        # return 1
        if parent.isValid():
            return parent.internalPointer().columnCount()
        else:
            return self.rootItem.columnCount()

    def data(self, index, role=None):

        if not index.isValid():
            return None

        if role != QtCore.Qt.DisplayRole:
            return None

        item = index.internalPointer()

        return item.data(index.column())
    def setData(self, index, data, role=None):

        # 编辑后更新模型中的数据 View中编辑后，View会调用这个方法修改Model中的数据
        if index.isValid() and data:
            col = index.column()
            print(col)
            # if 0 < col < len(self.headers):
            # self.beginResetModel()
            item = index.internalPointer()
            print(data)
            # item.itemData['bizOrgName'] = data
            # if CONVERTS_FUNS[col]:  # 必要的时候执行数据类型的转换
            #     self.datas[index.row()][col] = CONVERTS_FUNS[col](value)
            # else:
            #     self.datas[index.row()][col] = value
            self.dirty = True
            self.dataChanged.emit(index,index)
            return True
        return False

    def flags(self, index):
        # if not index.isValid():
        #     return QtCore.Qt.NoItemFlags
        #
        # return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable
        if not index.isValid():
            return QtCore.Qt.ItemIsEnabled
        ###QtCore.Qt.ItemIsEditable #可编辑
        return  QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled

    def headerData(self, section, orientation, role=None):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.rootItem.data(section)

        return None

    def index(self, row, column, parent=None, *args, **kwargs):
        if not self.hasIndex(row, column, parent):
            return QtCore.QModelIndex()

        if not parent.isValid():
            parentItem = self.rootItem
        else:
            parentItem = parent.internalPointer()

        childItem = parentItem.child(row)
        if childItem:
            return self.createIndex(row, column, childItem)
        else:
            return QtCore.QModelIndex()

    def parent(self, index=None):
        if not index.isValid():
            return QtCore.QModelIndex()

        childItem = index.internalPointer()
        parentItem = childItem.parent()

        if parentItem == self.rootItem:
            return QtCore.QModelIndex()

        return self.createIndex(parentItem.row(), 0, parentItem)

    def rowCount(self, parent=None, *args, **kwargs):
        # if parent.column() > 0:
        #     return 0

        if not parent.isValid():
            parentItem = self.rootItem
        else:
            parentItem = parent.internalPointer()

        return parentItem.childCount()
    def getIndexFromItem(self,childItem):

        if childItem:
            row = childItem.row()
            return self.createIndex(row, 0, childItem)
        else:
            return QtCore.QModelIndex()

    def getItemFromIndex(self,index):
        if index :
            return index.internalPointer()

    def getItemFromUid(self,uid):
        return self.getItemFromIndex(self.departmet_map.get(uid))

    def supportedDropActions(self):
        return QtCore.Qt.CopyAction | QtCore.Qt.MoveAction

    def mimeTypes(self):
        return ['text']

    def mimeData(self, indexes, QModelIndex=None):
        item = self.getItemFromIndex(indexes[0])
        print(item.itemData['bizOrgName'])
        mimedata = QtCore.QMimeData()
        mimedata.setData('text',b"t")
        mimedata.setImageData(indexes[0])
        return mimedata

    def dropMimeData(self, data, action, row, column, parent):
        # indexe = data.data('QModelIndex')
        sou_item = self.getItemFromIndex(data.imageData())
        print("s:",sou_item.itemData['bizOrgName'])

        obj_item = self.getItemFromIndex(parent)
        print(obj_item.itemData['bizOrgName'])

        # index = self.index(self, row, column)
        # item = self.getItemFromIndex(index)
        sou_item.parentItem.moveChildItmes((sou_item,), obj_item)
        sou_item.itemData['parentBizOrgId'] = obj_item.itemData['bizOrgId']
        self.modelReset.emit()
        return True
        pass

    def dropEvent(self, e):
        # self.setText(e.mimeData().text())prin
        print("111",e.mimeData().text())

    def setupData(self,deparmentdata_l,userdata_d):
        self.deparmentdata_l = deparmentdata_l
        self.userdata_d = userdata_d
        self.__initDepartmentData()

    def __initDepartmentData(self):

        for deparmentdata in self.deparmentdata_l:
            bizOrgId = deparmentdata['bizOrgId']
            parentBizOrgId = deparmentdata['parentBizOrgId']

            _parentitem = self.getItemFromUid(parentBizOrgId)

            if _parentitem is None :
                new_item = departmentTreeItem(deparmentdata, self.rootItem)
                self.rootItem.appendChild(new_item)

            else:
                # self.initModelData((dep_data,), _parentitem)
                new_item = departmentTreeItem(deparmentdata, _parentitem)
                # print(_parentitem.itemData)
                _parentitem.appendChild(new_item)

            self.departmet_map[bizOrgId] = self.getIndexFromItem(new_item)

            self.__initUserData(new_item,bizOrgId)

            itmes = self.rootItem.findChildItmesFromId(bizOrgId)

            if itmes:
                # for item in itmes:
                #     print(dep_data['bizOrgName'], ':itmes:', item.itemData)
                self.rootItem.moveChildItmes(itmes, new_item)

            # if new_item is None:
            #     new_item = parent


    def __initUserData(self, new_item, orgid):
        if self.userdata_d:
            userdata_l = self.userdata_d.get(orgid)
            if userdata_l:
                for user in userdata_l:
                    new_user = userItem(user, new_item)
                    new_item.appendChild(new_user)

def suid(emun):
    return emun['parentBizOrgId']




if __name__ == '__main__':
    import sys
    import json
    import user_data
    # u = user_data.user()
    # userdata = u.getUser4A()
    with open('deparment.json','r',encoding='utf8') as fp:
        json_in = fp.read().replace('\\', '')
        department = json.loads(json_in,encoding='utf8')
    # jo = jsonParserOper.jsonOper()
    # data = jo.getjsondict('depm')

    t_data = department["deptDatas"]
    # t_data = [{'bizOrgId':'0016','bizOrgName':'dp0016','parentBizOrgId':'001'},
    #           {'bizOrgId': '0017', 'bizOrgName': 'dp0017', 'parentBizOrgId': '001'},
    #           {'bizOrgId': '001', 'bizOrgName': 'dp001', 'parentBizOrgId': '1'},
    #           {'bizOrgId': '1', 'bizOrgName': '1', 'parentBizOrgId': '0'},
    #           {'bizOrgId': '00171', 'bizOrgName': '00171', 'parentBizOrgId': '0017'},
    #           {'bizOrgId': '0021', 'bizOrgName': 'dp0021', 'parentBizOrgId': '002'},
    #           {'bizOrgId': '002', 'bizOrgName': 'dp002', 'parentBizOrgId': '2'},
    #           {'bizOrgId': '0023', 'bizOrgName': 'dp0023', 'parentBizOrgId': '002'},
    #           {'bizOrgId': '00211', 'bizOrgName': '00211', 'parentBizOrgId': '0021'}
    #           ]

    # t_data.sort(key=suid)
    # print(t_data)
    app = QtWidgets.QApplication(sys.argv)

    # f = QtCore.QFile(':/default.txt')
    # f.open(QtCore.QIODevice.ReadOnly)
    # f.close()
    model = TreeModel()
    model.setupData(t_data,{})

    view = QtWidgets.QTreeView()
    view.setModel(model)
    view.setHeaderHidden(True)

    view.setItemsExpandable(True)
    view.resizeColumnToContents(0)
    view.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
    view.setWindowTitle("Simple Tree Model")
    view.show()
    sys.exit(app.exec_())
