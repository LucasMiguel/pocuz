from threading import main_thread
from PySide6 import QtGui
from PySide6 import QtWidgets
from PySide6 import QtCore

from controllers.c_data import DataController


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, mainTread):
        self.mainThread = mainTread
        self.data = DataController()
        # Estilo dos botões grandes na concentração
        self.concentStyleButtonBig = str(
            "QPushButton{\n"
            "background-color: rgb(230, 54, 53);\n"
            "border-radius: 35px;\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color: #EE5C5B;\n"
            "}\n"
        )
        # Estilo dos botões grandes na pausa
        self.breakStyleButtonBig = str(
            "QPushButton{\n"
            "background-color: rgb(103, 183, 76);\n"
            "border-radius: 35px;\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color: #79C061;\n"
            "}\n"
        )
        # Estilo dos botãos pequenos na concentração
        self.concentStyleButtonSmall = str(
            "QPushButton{\n"
            "background-color:rgb(230, 54, 53);\n"
            "border-radius: 22px;\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color: #EE5C5B;\n"
            "}\n"
        )
        # Estilo dos botões pequenos na pausa
        self.breakStyleButtonSmall = str(
            "QPushButton{\n"
            "background-color: rgb(103, 183, 76);\n"
            "border-radius: 22px;\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color: #79C061;\n"
            "}\n"
        )
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(400, 413)
        MainWindow.setMinimumSize(QtCore.QSize(400, 413))
        MainWindow.setMaximumSize(QtCore.QSize(400, 413))
        font = QtGui.QFont()
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("../Imagens/Icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        MainWindow.setWindowIcon(icon)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        ## TIME LABEL =======================================================================================
        self.timeLabel = QtWidgets.QLabel(self.centralwidget)
        self.timeLabel.setGeometry(QtCore.QRect(70, 80, 261, 121))
        font = QtGui.QFont("Lato", 60, QtGui.QFont.Light)
        self.timeLabel.setFont(font)
        self.timeLabel.setStyleSheet("color: #E63635")
        self.timeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.timeLabel.setObjectName("timeLabel")
        ## SERIE LABEL ======================================================================================
        self.serieLabel = QtWidgets.QLabel(self.centralwidget)
        self.serieLabel.setGeometry(QtCore.QRect(170, 190, 61, 18))
        self.serieLabel.setStyleSheet("color:#E63635")
        self.serieLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.serieLabel.setObjectName("serieLabel")
        ##PLAY BUTTON =======================================================================================
        self.playButton = QtWidgets.QPushButton(self.centralwidget)
        self.playButton.setGeometry(QtCore.QRect(165, 240, 70, 70))
        self.playButton.setStyleSheet(self.concentStyleButtonBig)
        self.playButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap("images/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.playButton.setIcon(icon1)
        self.playButton.setIconSize(QtCore.QSize(50, 50))
        self.playButton.setFlat(True)
        self.playButton.setObjectName("playButton")
        self.playButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.playButton.clicked.connect(self.handlePlay)
        ##PAUSE BUTTON ======================================================================================
        self.pauseButton = QtWidgets.QPushButton(self.centralwidget)
        self.pauseButton.setVisible(False)
        self.pauseButton.setGeometry(QtCore.QRect(165, 240, 70, 70))
        self.pauseButton.setStyleSheet(self.concentStyleButtonBig)
        self.pauseButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(
            QtGui.QPixmap("images/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.pauseButton.setIcon(icon4)
        self.pauseButton.setIconSize(QtCore.QSize(45, 45))
        self.pauseButton.setFlat(True)
        self.pauseButton.setObjectName("pauseButton")
        self.pauseButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pauseButton.clicked.connect(self.handlePause)
        ## CONCETRATION BUTTON ====================================================================================
        self.concetrationButton = QtWidgets.QPushButton(self.centralwidget)
        self.concetrationButton.setVisible(False)
        self.concetrationButton.setGeometry(QtCore.QRect(80, 250, 45, 45))
        self.concetrationButton.setStyleSheet(self.concentStyleButtonSmall)
        self.concetrationButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap("images/concentration.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.concetrationButton.setIcon(icon2)
        self.concetrationButton.setIconSize(QtCore.QSize(24, 24))
        self.concetrationButton.setFlat(True)
        self.concetrationButton.setObjectName("concetrationButton")
        self.concetrationButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.concetrationButton.clicked.connect(self.handleConcetration)
        ## BREAK BUTTON ====================================================================================
        self.breakButton = QtWidgets.QPushButton(self.centralwidget)
        self.breakButton.setGeometry(QtCore.QRect(80, 250, 45, 45))
        self.breakButton.setStyleSheet(self.breakStyleButtonSmall)
        self.breakButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(
            QtGui.QPixmap("images/break.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.breakButton.setIcon(icon3)
        self.breakButton.setIconSize(QtCore.QSize(26, 26))
        self.breakButton.setFlat(True)
        self.breakButton.setObjectName("breakButton")
        self.breakButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.breakButton.clicked.connect(self.handleBreak)
        ## UNDO BUTTON ====================================================================================
        self.undoButton = QtWidgets.QPushButton(self.centralwidget)
        self.undoButton.setGeometry(QtCore.QRect(270, 250, 45, 45))
        self.undoButton.setStyleSheet(self.concentStyleButtonSmall)
        self.undoButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(
            QtGui.QPixmap("images/undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.undoButton.setIcon(icon5)
        self.undoButton.setIconSize(QtCore.QSize(20, 20))
        self.undoButton.setFlat(True)
        self.undoButton.setObjectName("undoButton")
        self.undoButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        ## MENU BUTTON ====================================================================================
        self.menuButton = QtWidgets.QPushButton(self.centralwidget)
        self.menuButton.setGeometry(QtCore.QRect(360, 380, 50, 30))
        self.menuButton.setText("")
        self.menuButton.setStyleSheet(
            "QPushButton{\n"
            "background-color: transparent;\n"
            "border: none"
            "}\n"
            "QPushButton:hover{\n"
            "background-color: transparent;\n"
            "border: none"
            "}\n"
            ""
        )
        icon6 = QtGui.QIcon()
        icon6.addPixmap(
            QtGui.QPixmap("images/menu_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.menuButton.setIcon(icon6)
        self.menuButton.setIconSize(QtCore.QSize(35, 35))
        self.menuButton.setFlat(True)
        self.menuButton.setObjectName("menuButton")
        self.menuButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menuButton.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.menuButton.customContextMenuRequested.connect(self.onContextMenu)
        self.menuOptions = QtWidgets.QMenu()
        restartCicle = self.menuOptions.addAction("Recomeçar Ciclo")
        settings = self.menuOptions.addAction("Preferências")
        about = self.menuOptions.addAction("Sobre")
        self.menuOptions.addSeparator()
        exit = self.menuOptions.addAction("Sair")
        self.menuButton.setMenu(self.menuOptions)
        ## ================================================================================================
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # Envia a label para edição
        self.mainThread.parseTimeLabel(self.timeLabel)

    def onContextMenu(self, point):
        """Função que mostrará o context menu do botão de menu

        Args:
            point ([type]): Local de abertura
        """
        self.menuOptions.exec_(self.button.mapToGlobal(point))

    def handlePlay(self):
        """Função que irá controlar o botão de play

        Args:
            type (int): Define se é play na concentração ou descanso | 1 = concentração || 2 = descanso
        """
        self.playButton.setVisible(False)
        self.pauseButton.setVisible(True)
        self.mainThread.play()

    def handlePause(self):
        """Função que ir á controlar o botão de pause

        Args:
            type (int): Define se é pause na concentração ou descanso | 1 = concentração || 2 = descanso
        """
        self.pauseButton.setVisible(False)
        self.playButton.setVisible(True)
        self.mainThread.pause()

    def handleConcetration(self):
        self.concetrationButton.setVisible(False)
        self.breakButton.setVisible(True)

    def handleBreak(self):
        self.breakButton.setVisible(False)
        self.concetrationButton.setVisible(True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pocuz"))
        self.timeLabel.setText(_translate("MainWindow", str(self.mainThread.timeCount)))
        self.serieLabel.setText(_translate("MainWindow", "Série 1"))
