import sys
import imp
import random
from PyQt5 import QtCore, QtGui, uic,QtWidgets


qtCreatorFile = "C://Users//Wyf//Desktop//songci.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.random_button.clicked.connect(self.randomdemo)


    def randomdemo(self):
        cipai = [2, 2, '，', 2, 2, 1, '，', 2, 2, 2, '。', 2, 2, 2, '，', 2, 2, 2, '，', 2, 2, 2, '。', 2, 2, 2, '，', 2, 2, 2,
                 '。']
        string = ''
        for i in cipai:
            if type(i) == int:
                if i == 1:
                    file = open('E://learning//1.txt', 'r', encoding='utf-8')
                    ran_num = random.randint(0, 150)
                    temp = file.readlines()[ran_num].replace('\n', '')[2:3]
                    string = string + temp
                    file.close()
                if i == 2:
                    file = open('E://learning//2.txt', 'r', encoding='utf-8')
                    ran_num = random.randint(0, 150)
                    temp = file.readlines()[ran_num].replace('\n', '')[2:4]
                    string = string + temp
                    file.close()
            else:
                string = string + i
        self.songci_text.setText(string)



if __name__ == "__main__":

       app = QtWidgets.QApplication(sys.argv)
       window = MyApp()
       window.show()
       sys.exit(app.exec_())
