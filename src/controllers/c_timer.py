from threading import Thread
from time import strftime, gmtime, time
import time
import resources

from PySide6 import os
from PySide6.QtCore import QRunnable, Slot, QThreadPool
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
from components.notification import makeNotification

from components.sys_tray_icon import SysTrayIcon
from controllers.c_data import DataController
from screens.aboutWindow import AboutWindow
from screens.mainWindow import MainWindow
from screens.settingsWindow import SettingWindow


class MainThread(QRunnable):

    def __init__(self):
        super().__init__()
        self.data = DataController()
        self.timeCount = 0
        self.runCount = False
        self.isTimeConcentration = True
        self.isTimeBreak = False
        self.isTimeLongBreak = False
        self.concetrationCount = 1
        self.setTime(self.data.sectionsTime)
        # Instância o systrayIcon
        self.trayIcon = SysTrayIcon(self)
        # Inicia o System Tray Icon
        self.trayIcon.show()
        # Instância da janela principal
        self.mainWindow = MainWindow(self)
        # Instância da janela de preferências
        self.settingsWindow = SettingWindow(self.data, self)
        # Instância da janela de sobre
        self.aboutWindow = AboutWindow()
        # Abre uma instância da janela quando inicia a aplicação
        self.openMainWindow()
        # __init__

    @Slot()
    def run(self):
        """Função principal de contagem do tempo
        """
        while True:
            if self.runCount:
                self.timeCount = self.timeCount - 1
                # print(self.timeCount)
                self.updateTimeLabels()
                if self.timeCount == 0:                    
                    self.endTimer()
                # # Delay de 1 segundo
                time.sleep(1)
        # run

    def setTime(self, minutes):
        """Função que formata o tempo trazido das configurações para segundos, para controle do tempo

        Args:
            minutes (int): valor do tempo escolhido em minutos
        """
        self.timeCount = minutes * 60
        # setTime

    def formatTime(self):
        """Função que irá formatar os segundos em minutos   

        Returns:
            string: retorna os minutos já formatados
        """
        return strftime("%M:%S", gmtime(self.timeCount))
        # formatTime

    def playCount(self):
        """Função que irá continuar a contagem
        """
        self.runCount = True
        self.mainWindow.pauseButton.setVisible(True)
        self.mainWindow.playButton.setVisible(False)
        self.trayIcon.playTime.setVisible(False)
        self.trayIcon.pauseTime.setVisible(True)
        # playCount

    def pauseCount(self):
        """Função que irá pausar o relógio
        """
        self.runCount = False
        self.mainWindow.pauseButton.setVisible(False)
        self.mainWindow.playButton.setVisible(True)
        self.trayIcon.playTime.setVisible(True)
        self.trayIcon.pauseTime.setVisible(False)
        # pauseCount

    def resetCount(self):
        """Função que resetará o tempo de concentração ou de pausa
        """
        self.data.getData()
        if self.isTimeConcentration:
            self.setTime(self.data.sectionsTime)
        elif self.isTimeBreak:
            self.setTime(self.data.shortBreakTime)
        else:
            self.setTime(self.data.longBreakTime)
        # Atualiza a tela após 
        self.updateTimeLabels()
        # resetCount

    def endTimer(self):
        """Função que irá finalizar cada tempo
        """
        self.pauseCount()
        if (self.isTimeConcentration):
            if (self.concetrationCount != self.data.amountSections):
                msg = "Fim da concentração\nIniciar descanço!"
                self.setBreakTime()
            else:
                msg = "Fim da concentração\nIniciar descanço longo!"
                self.setLongBreakTime()
                self.concetrationCount = 0
        else:
            msg = "Fim do descanço\nIniciar concentração!"
            self.concetrationCount += 1
            self.setConcetrationTime()
        #Gera a notificação do final e do inicio do próximo ciclo
        if(self.data.notification):        
            makeNotification(msg, self)        
        self.updateScreen()
        self.updateTimeLabels()
        if(self.data.popup):
            self.openPopupWindow()
        # endTimer

    def setConcetrationTime(self):
        """Função que irá informar que é um tempo de concentração
        """
        self.data.getData()
        self.setTime(self.data.sectionsTime)
        self.isTimeConcentration = True
        self.isTimeBreak = False
        self.isTimeLongBreak = False
        self.mainWindow.serieLabel.setText("Série " +
                                           str(self.concetrationCount))
        self.mainWindow.serieLabel.setStyleSheet("color: #6A6969")
        # setConcentrationTime

    def setBreakTime(self):
        """Função que irá informar que é um tempo de pausa
        """
        self.data.getData()
        self.setTime(self.data.shortBreakTime)
        self.isTimeConcentration = False
        self.isTimeBreak = True
        self.isTimeLongBreak = False
        self.mainWindow.serieLabel.setText("Tempo de descanso")
        self.mainWindow.serieLabel.setStyleSheet("color: #79C061")
        # setBreakTime

    def setLongBreakTime(self):
        """Função que irá indicar que está em uma pausa longa
        """
        self.data.getData()
        self.setTime(self.data.longBreakTime)
        self.isTimeConcentration = False
        self.isTimeBreak = False
        self.isTimeLongBreak = True
        self.mainWindow.serieLabel.setText("Tempo de um longo descanso")
        self.mainWindow.serieLabel.setStyleSheet("color: #79C061")
        # setLongBreakTime

    def updateTimeLabels(self):
        """Função que irá atualizar a tela das janelas
        """
        self.mainWindow.timeLabel.setText(self.formatTime())
        self.trayIcon.timeLabel.setText(self.formatTime())
        # updateTimeLabels

    def updateScreen(self):
        """Função que atualiza a janela principal e do systemTrayIcon
        """
        if (self.isTimeConcentration):
            # Mudanças na janela
            self.mainWindow.concentrationMode()
            # Mudanças no system Tray Icon
            icon = QIcon(":/images/icon_32.png")
            self.trayIcon.setIcon(icon)

        else:
            # Mudanças na janela
            self.mainWindow.breakMode()
            # Mudanças no system Tray Icon
            icon = QIcon(":/images/icon_32_break.png")
            self.trayIcon.setIcon(icon)
        # updateScreen

    def openMainWindow(self):
        """Abre a janela principal
        """         
        self.setDarkMode()        
        self.mainWindow.show()                
        # openMainWindow

    def openPopupWindow(self):
        """Função que irá abrir a janela principal ao final do tempo
        """        
        if(self.mainWindow.isMinimized):
            self.mainWindow.hide()
        self.trayIcon.timeLabel.trigger()     
        # openPopupWindow

    def openSettingsWindow(self):
        """Abre a janela de preferências
        """
        # Instância da janela de preferências
        self.settingsWindow = SettingWindow(self.data, self)        
        self.setDarkMode()
        self.settingsWindow.show()
        # openSettingsWindow

    def openAboutWindow(self):
        """Função que irá abrir a janela de sobre
        """
        # Instância da janela de sobre
        self.aboutWindow = AboutWindow()
        self.setDarkMode()
        self.aboutWindow.show()
        # openAboutWindow

    def setDarkMode(self):
        self.data.getData()
        if(self.data.darkTheme):
            # MainWindow
            self.mainWindow.setStyleSheet('QMainWindow{background-color: #011627;}')            
            self.mainWindow.menuOptions.setStyleSheet(
                "QMenu{\n"
                "background-color: #011627;\n"
                "color:white;\n"            
                "}\n"
                "QMenu::item{\n"
                "color: white;\n"
                "}\n"
                "QMenu::item:selected{\n"
                "background-color: rgba(11,222,236,0.37);\n"            
                "}\n"                        
            )
            # SettingsWindow
            self.settingsWindow.setStyleSheet('QDialog{background-color: #011627;}')
            self.settingsWindow.label_2.setStyleSheet("color: #FFFFFF")
            self.settingsWindow.label_3.setStyleSheet("color: #FFFFFF")
            self.settingsWindow.label_4.setStyleSheet("color: #FFFFFF")
            self.settingsWindow.label_5.setStyleSheet("color: #FFFFFF")
            self.settingsWindow.label_6.setStyleSheet("color: #FFFFFF")
            self.settingsWindow.label_7.setStyleSheet("color: #FFFFFF")
            self.settingsWindow.label_8.setStyleSheet("color: #FFFFFF")
            self.settingsWindow.label_9.setStyleSheet("color: #FFFFFF")
            # AboutWindow
            self.aboutWindow.setStyleSheet('QDialog{background-color: #011627;}')
            self.aboutWindow.label.setStyleSheet("color: #FFFFFF")
            self.aboutWindow.label_2.setStyleSheet("color: #FFFFFF")
            self.aboutWindow.label_3.setStyleSheet("color: #FFFFFF")
            self.aboutWindow.label_4.setStyleSheet("color: #FFFFFF")
            self.aboutWindow.label_6.setStyleSheet("color: #FFFFFF")
            self.aboutWindow.label_7.setStyleSheet("color: #FFFFFF")
            self.aboutWindow.label_8.setStyleSheet("color: #FFFFFF")
            self.aboutWindow.label_10.setStyleSheet("color: #FFFFFF")          
        else:
            # MainWindow
            self.mainWindow.setStyleSheet('')            
            self.mainWindow.menuOptions.setStyleSheet('')
            # SettingsWindow
            self.settingsWindow.setStyleSheet('')            
            self.settingsWindow.label.setStyleSheet("color: #515050")
            self.settingsWindow.label_2.setStyleSheet('')
            self.settingsWindow.label_3.setStyleSheet('')
            self.settingsWindow.label_4.setStyleSheet('')
            self.settingsWindow.label_5.setStyleSheet('')
            self.settingsWindow.label_6.setStyleSheet('')
            self.settingsWindow.label_7.setStyleSheet('')
            self.settingsWindow.label_8.setStyleSheet('')
            self.settingsWindow.label_9.setStyleSheet('')
            # AboutWindow
            self.aboutWindow.setStyleSheet('')
            self.aboutWindow.label.setStyleSheet("")
            self.aboutWindow.label_2.setStyleSheet("")
            self.aboutWindow.label_3.setStyleSheet("")
            self.aboutWindow.label_4.setStyleSheet("")
            self.aboutWindow.label_6.setStyleSheet("")
            self.aboutWindow.label_7.setStyleSheet("")
            self.aboutWindow.label_8.setStyleSheet("")
            self.aboutWindow.label_10.setStyleSheet("")
        # setDarkMode

    def exitApplication(self):
        """Função que irá fechar a aplicação
        """
        os._exit(0)
    # exitApplication