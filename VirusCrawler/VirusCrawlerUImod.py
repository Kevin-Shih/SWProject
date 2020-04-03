from __future__ import unicode_literals
import json
from PyQt5 import QtCore, QtGui, QtWidgets
from VirusCrawlerCode import crawler
from VirusCrawlerUI import Ui_Flight


class Flight(QtWidgets.QMainWindow):
    def __init__(self):
        super(Flight, self).__init__()
#        self.craw = crawler()
#        self.driver = webdriver.Chrome(executable_path='C:\Code\VirusCrawler\venv\Lib\site-packages\selenium\webdriver\remote\chromedriver.exe')
        json_file = json.loads(crawler())
#        json_file = open(self.craw, "r", encoding='utf-8')
        self.FData = json.load(json_file, encoding='utf-8')
        print(self.FData["1"][0])
        json_file.close()
        self.ui = Ui_Flight()
        self.ui.setupUi(self)
        self.ui.flighttable.hide()
        self.ui.search.hide()
        self.ui.textEdit.hide()
        self.ui.retranslateUi(Fl)
        _translate = QtCore.QCoreApplication.translate
        for i in range(100):
            for j in range(8):
                self.ui.item = QtWidgets.QTableWidgetItem()
                self.ui.flighttable.setItem(i, j, self.ui.item)
        for i in range(3):
            for j in range(8):
                self.ui.item = self.ui.flighttable.item(i, j)
                self.ui.item.setText(_translate("Flight", self.FData[str(i)][j]))

        self.ui.flighttable.itemActivated.connect(itemActivated_event)
 #       self.ui.search.clicked.connect(self.handleButton)   #search button ( not completed

def itemActivated_event(item):
    json_file = open("C:\Code\VirusCrawler\jsonfiles\FlightUrl","r",encoding='utf-8')
    Flight.FData = json.load(json_file)
    json_file.close()
    if item.text() == '亞州航空' or item.text() == '中華航空' or item.text() == '馬來西亞':
        QtGui.QDesktopServices.openUrl(QtCore.QUrl(Flight.FData[item.text()]))
    else:
        print(item.text())

#    def handleButton(self):     # search function (not completed
#        items = self.ui.flighttable.findItems(self.ui.textedit.text(), QtCore.Qt.MatchExactly)
#        if items:
#            results = '\n'.join('row %d column %d' % (item.row() + 1, item.column() + 1) for item in items)
#        else:
#            results = 'Found Nothing'
#        QtGui.QMessageBox.information(self, 'Search Results', results)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Fl = QtWidgets.QWidget()
#    ui = Ui_Flight()     #original
    Fl = Flight()
#    Fl.ui.setupUi(Fl)
    Fl.show()
    sys.exit(app.exec_())
