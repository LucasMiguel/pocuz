from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
import json
import sys

from components.sys_tray_icon import SysTrayIcon
from controllers.c_data import DataController


    
### Função principal
if __name__ == "__main__":
    app = QApplication([])
    trayIcon = SysTrayIcon() 

    sys.exit(app.exec())

 


