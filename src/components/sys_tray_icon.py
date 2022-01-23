import os
from PySide6 import QtWidgets
from PySide6.QtGui import QIcon

from screens.mainWindow import MainWindow

class SysTrayIcon(QtWidgets.QSystemTrayIcon):
    def __init__(self, mainThread):
        super().__init__()
        self.mainThread = mainThread

        self.mainWindow = MainWindow(self.mainThread)

        icon = QIcon("images/icon_32.png")
        self.menu = QtWidgets.QMenu()
        self.timeLabel = self.menu.addAction(self.mainThread.formatTime())
        self.timeLabel.triggered.connect(self.mainThread.openMainWindow)        
        self.playTime = self.menu.addAction("Iniciar tempo")
        self.playTime.triggered.connect(self.mainThread.playCount)
        self.pauseTime = self.menu.addAction("Pausar tempo")
        self.pauseTime.triggered.connect(self.mainThread.pauseCount)
        self.pauseTime.setVisible(False)
        self.resetTime = self.menu.addAction("Reiniciar ciclo")
        self.resetTime.triggered.connect(self.mainThread.resetCount)
        self.menu.addSeparator()
        self.subMenu = QtWidgets.QMenu()
        self.subMenu.setTitle("Recomeçar Ciclo")        
        self.startConcentratio = self.subMenu.addAction("Começar concetração")
        self.startConcentratio.triggered.connect(
            lambda checked: self.jumpToCicles(1))
        self.startShortBreak = self.subMenu.addAction("Começar descanso")
        self.startShortBreak.triggered.connect(
            lambda checked: self.jumpToCicles(2))
        self.srtatLongBreak = self.subMenu.addAction("Começar descanso longo")
        self.srtatLongBreak.triggered.connect(
            lambda checked: self.jumpToCicles(3))
        self.menu.addMenu(self.subMenu)
        self.settings = self.menu.addAction("Preferências")
        self.settings.triggered.connect(self.mainThread.openSettingsWindow)
        self.menu.addSeparator()
        exitAction = self.menu.addAction("Sair")
        exitAction.triggered.connect(self.mainThread.exitApplication)
        
        self.setIcon(icon)
        self.setContextMenu(self.menu)
        self.show()
        

        # Cria o Trigger para o click duplo no icone
        self.activated.connect(self.iconActivated)

    # __init__

    def iconActivated(self, reason):
        """Função que irá abrir uma nova janela caso clique duas vezes no icone
        """
        if reason == QtWidgets.QSystemTrayIcon.DoubleClick:
            self.mainWindow.show()
    # iconActivated


    def jumpToCicles(self, type):
        """Função que irá pular para um ciclo específico

        Args:
            type (int): Indica qual o tipo do ciclo == 1 = Concentração | 2 = Pausa | 3 = Pausa Longa
        """
        if(type == 1):
            self.mainThread.setConcetrationTime()
        elif(type == 2):
            self.mainThread.setBreakTime()
        else:
            self.mainThread.setLongBreakTime()
        self.mainThread.updateScreen()
        self.mainThread.updateTimeLabels()
        self.mainThread.playCount()
    # jumpToCicles
   
    
        