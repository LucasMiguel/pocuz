from threading import main_thread
from PySide6 import QtGui
from PySide6 import QtWidgets
from PySide6 import QtCore
import resources

class AboutWindow(QtWidgets.QDialog):
    def __init__(self):
        super(AboutWindow, self).__init__()
        self.setObjectName("self")
        self.resize(400, 413)
        self.setMinimumSize(QtCore.QSize(400, 413))
        self.setMaximumSize(QtCore.QSize(400, 413))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setModal(True)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20, 50, 141, 131))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/images/icon_about.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(190, 80, 161, 61))
        font = QtGui.QFont("Lato", 45, QtGui.QFont.Light)        
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(250, 140, 51, 31))
        font = QtGui.QFont("Lato", 25, QtGui.QFont.Light)        
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(0, 210, 401, 71))
        font = QtGui.QFont("Lato", 15, QtGui.QFont.Light)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(0, 390, 401, 20))
        font = QtGui.QFont("Lato", 8, QtGui.QFont.Light)        
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(0, 310, 401, 20))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_10 = QtWidgets.QLabel(self)
        self.label_10.setGeometry(QtCore.QRect(0, 330, 401, 20))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_10.setOpenExternalLinks(True)
        self.label_8 = QtWidgets.QLabel(self)
        self.label_8.setGeometry(QtCore.QRect(0, 370, 401, 20))
        font = QtGui.QFont("Lato", 8, QtGui.QFont.Light)        
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, aboutWindow):
        _translate = QtCore.QCoreApplication.translate
        aboutWindow.setWindowTitle(_translate("aboutWindow", "Sobre"))
        self.label_2.setText(_translate("aboutWindow", "Pocuz"))
        self.label_3.setText(_translate("aboutWindow", "1.0"))
        self.label_4.setText(_translate("aboutWindow", "<html><head/><body><p align=\"center\">Um temporizador Pomodoro<br>multiplataformas</p></body></html>"))
        self.label_6.setText(_translate("aboutWindow", "Este programa vem com absolutamente nenhuma garantia."))
        self.label_7.setText(_translate("aboutWindow", "Criado por: Lucas Miguel"))
        self.label_10.setText(_translate("aboutWindow", "<a href=\'https://github.com/LucasMiguel\'>GitHub</a> | <a href=\'https://linkedin.com/in/lucas-42-miguel\'>Linkedin</a>"))
        self.label_8.setText(_translate("aboutWindow", "software sob a licen??a GNU General Public License v3.0 "))

