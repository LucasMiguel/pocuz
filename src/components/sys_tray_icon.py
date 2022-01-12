from PySide6 import QtWidgets
from PySide6.QtGui import QIcon
import sys

class SysTrayIcon(QtWidgets.QSystemTrayIcon):
    def __init__(self, mainTread):
        super().__init__()
        self.mainTread = mainTread
        icon = QIcon("images/icon_32.png")
        menu = QtWidgets.QMenu()
        time = menu.addAction("25:00")
        time.triggered.connect(self.openMainWindow)
        play = menu.addAction("Play")
        play.triggered.connect(self.playCount)
        pause = menu.addAction("Pause")
        pause.triggered.connect(self.pauseCount)
        exitAction = menu.addAction("exit")
        exitAction.triggered.connect(sys.exit)
        
        self.tray = QtWidgets.QSystemTrayIcon()
        self.tray.setIcon(icon)
        self.tray.setContextMenu(menu)
        self.tray.setToolTip("25:00")
        self.tray.show()

    def openMainWindow(self):
        print("Coisa")
    def playCount(self):
        self.mainTread.play()
    def pauseCount(self):
        self.mainTread.pause()
        