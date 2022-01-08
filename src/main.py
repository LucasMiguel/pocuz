from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
import sys
import os
from plyer import notification

from components.sys_tray_icon import SysTrayIcon


    
### Função principal
if __name__ == "__main__":
    app = QApplication([])
    trayIcon = SysTrayIcon() 
    notification.notify(
    title = "Pocuz",
    message = "Mensagem",
    app_icon = r'images/icon',
    timeout = 10
    )
    sys.exit(app.exec())

 


