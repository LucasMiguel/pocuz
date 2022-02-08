
from PySide6 import QtGui
from PySide6 import QtWidgets
from PySide6.QtCore import QThreadPool
import sys



from controllers.c_timer import MainThread
from screens.mainWindow import MainWindow


### Função principal
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    # Desabilita o fechamento da janela pelo modal
    app.setQuitOnLastWindowClosed(False)    
    # Define a fonte
    QtGui.QFontDatabase.addApplicationFont("fonts/Lato-Light.ttf")
    # Instância a thread principal
    QThreadPool.globalInstance().start(MainThread(), 1)
    sys.exit(app.exec())
