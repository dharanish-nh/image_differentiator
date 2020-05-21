

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QIcon
class Ui_Dialog(object):
    def setupUi(self,Dialog):

        Dialog.setObjectName("Dialog")
        Dialog.resize(550, 300)
        Dialog.setWindowFlags(Dialog.windowFlags()|QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowMaximizeButtonHint)
        self.frame = QtWidgets.QFrame(Dialog)

        self.frame.resize(550, 300)
        self.frame.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.frame.setAutoFillBackground(True)
        self.frame.setStyleSheet("background-color: rgb(200, 200, 200)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setStyleSheet("background-color: rgb(250, 250, 250)")
        self.lineEdit.setGeometry(QtCore.QRect(100, 20, 341, 21))
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_3 = QtWidgets.QTextEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 90, 510, 200))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setStyleSheet("color: rgb(250, 0, 0)")

        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 20, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 50, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(450, 50, 75, 23))

        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(532, 270, 20, 20))
        self.pushButton_5.setStyleSheet("background-color: rgb(0, 250, 100)")
        self.pushButton_5.setObjectName("pushButton_5")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setStyleSheet("background-color: rgb(250, 250, 250)")
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 50, 341, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "IMAGE DIFFERENTIATOR"))
        Dialog.setWindowIcon(QIcon('intersection.png'))
        self.pushButton.setText(_translate("Dialog", "IMAGE1"))
        self.pushButton_2.setText(_translate("Dialog", "CHECK"))
        self.pushButton_3.setText(_translate("Dialog", "IMAGE2"))
        self.pushButton_4.setText(_translate("Dialog", "SAVE"))
        self.pushButton_5.setText(_translate("Dialog", "©"))

