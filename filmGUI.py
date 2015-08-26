# -*- coding: utf-8 -*- 
# __author__ = 'jeffrey_cui'
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import FilmDialog
class testDialog(QDialog):
    def __init__(self,parent=None):
        super(testDialog,self).__init__(parent)
        self.FilmUi=FilmDialog.Ui_Dialog()
        self.FilmUi.setupUi(self)
        self.model=QStandardItemModel(1,1)
        self.model.setHeaderData(0,Qt.Horizontal,"Film Name")
        self.model.insertRow(0,QStandardItem(u"大爆炸"))
        self.FilmUi.tableView.setModel(self.model)
        self.FilmUi.tableView.setColumnWidth(0,220)
        #QPushButton("Quit1", self)
    def timeChangedEvent(self,date):
        print date.toString("yyyy-MM-dd hh:mm:ss")

app=QApplication(sys.argv)
dialog=testDialog()
dialog.show()
app.exec_()

'''class MyWidget(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidge.__init__(self,parent)
        self.setFixedSize(600, 500)
        self.quit = QtGui.QPushButton("Quit1", self)
        self.quit.setGeometry(62, 40, 75, 30)
        self.quit.setFont(QtGui.QFont("Times", 18, QtGui.QFont.Bold))
        self.connect(self.quit, QtCore.SIGNAL("clicked()"),QtGui.qApp, QtCore.SLOT("quit()"))
        self.dateEdit=QtGui.QDateEdit(QtCore.QDate.currentDate(),self)
        self.dateEdit.setStyle(QtGui.QStyleFactory.create(QtCore.QString("plastique")))
        self.dateEdit.setGeometry(20, 10, 100, 25)

        self.filmTable=QtGui.QTableView(self)
        self.filmTable.setGeometry(20, 40, 300, 200)
        #self.filmTable.setMo

app = QtGui.QApplication(sys.argv)
widget = MyWidget()
widget.show()
sys.exit(app.exec_())'''

