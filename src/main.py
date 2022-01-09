from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
import sys


from components.sys_tray_icon import SysTrayIcon
from screens.mainWindow import Ui_MainWindow


    
### Função principal
if __name__ == "__main__":
    app = QApplication([])
    trayIcon = SysTrayIcon()
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    sys.exit(app.exec())

 


