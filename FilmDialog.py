# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FilmDialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(593, 428)
        self.horizontalLayoutWidget = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 160, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_date = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_date.setObjectName(_fromUtf8("label_date"))
        self.horizontalLayout.addWidget(self.label_date)
        self.dateEdit = QtGui.QDateEdit(self.horizontalLayoutWidget)
        self.dateEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.horizontalLayout.addWidget(self.dateEdit)
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 251, 371))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_movielist = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_movielist.setObjectName(_fromUtf8("label_movielist"))
        self.verticalLayout.addWidget(self.label_movielist)
        self.tableView = QtGui.QTableView(self.verticalLayoutWidget)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.verticalLayout.addWidget(self.tableView)
        self.label_movieimage = QtGui.QLabel(Dialog)
        self.label_movieimage.setGeometry(QtCore.QRect(300, 30, 46, 13))
        self.label_movieimage.setText(_fromUtf8(""))
        self.label_movieimage.setObjectName(_fromUtf8("label_movieimage"))
        self.horizontalLayoutWidget.raise_()
        self.label_date.raise_()
        self.verticalLayoutWidget.raise_()
        self.label_movieimage.raise_()

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.label_date, QtCore.SIGNAL(_fromUtf8("linkActivated(QString)")), self.dateEdit.selectAll)
        QtCore.QObject.connect(self.dateEdit, QtCore.SIGNAL(_fromUtf8("dateTimeChanged(QDateTime)")), Dialog.timeChangedEvent)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Hot Movie", None))
        self.label_date.setText(_translate("Dialog", "Date:", None))
        self.label_movielist.setText(_translate("Dialog", "Movie List:", None))
