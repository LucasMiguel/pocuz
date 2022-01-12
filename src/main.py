import threading
from PySide6 import QtGui
from PySide6 import QtWidgets
from PySide6 import QtCore
import sys


from components.sys_tray_icon import SysTrayIcon
from controllers.c_timer import ThreadCountTime
from screens.mainWindow import Ui_MainWindow


### Função principal
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    QtGui.QFontDatabase.addApplicationFont("fonts/Lato-Light.ttf")
    mainThread = ThreadCountTime(25)
    trayIcon = SysTrayIcon(mainThread)
    trayIcon.show()
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow, mainThread)
    mainThread.start()
    mainWindow.show()

    sys.exit(app.exec())
