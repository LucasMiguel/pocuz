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
        menu = QtWidgets.QMenu()
        self.timeLabel = menu.addAction(self.mainThread.formatTime())
        self.timeLabel.triggered.connect(self.openMainWindow)
        play = menu.addAction("Play")
        play.triggered.connect(self.playCount)
        pause = menu.addAction("Pause")
        pause.triggered.connect(self.pauseCount)
        exitAction = menu.addAction("Sair")
        exitAction.triggered.connect(self.exitApplication)
        
        self.setIcon(icon)
        self.setContextMenu(menu)
        self.show()
        

        # Cria o Trigger para o click duplo no icone
        self.activated.connect(self.iconActivated)

        # Passa a label para alteração
        self.mainThread.setTrayIcon(self)
        self.mainThread.setWindow(self.mainWindow)
    # __init__

    def iconActivated(self, reason):
        """Função que irá abrir uma nova janela caso clique duas vezes no icone
        """
        if reason == QtWidgets.QSystemTrayIcon.DoubleClick:
            self.mainWindow.show()
    # iconActivated

    def openMainWindow(self):
        """Função que irá abrir uma nova instância da janela principal
        """
        self.mainWindow.show()
    # openMainWindow

    def playCount(self):
        """Função que irá começar a contagem do tempo
        """
        self.mainThread.playCount()
        self.mainWindow.pauseButton.setVisible(True)
        self.mainWindow.playButton.setVisible(False)
    # playCount

    def pauseCount(self):
        """Função que irá pausar a contagem do tempo
        """
        self.mainThread.pauseCount()
        self.mainWindow.pauseButton.setVisible(False)
        self.mainWindow.playButton.setVisible(True)
    # pauseCount

    def exitApplication(self):
        """Função que irá fechar a aplicação
        """
        os._exit(0)
    # exitApplication
    
        