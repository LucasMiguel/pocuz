from threading import Thread
from time import strftime, gmtime, time
import time
from components.notification import makeNotification
from PySide6.QtGui import QIcon

from controllers.c_data import DataController


class MainThread(Thread):

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

    # __init__

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
                # Delay de 1 segundo
                # time.sleep(1)
                time.sleep(0.2)

    # run

    def setTime(self, minutes):
        """Função que formata o tempo trazido das configurações para segundos, para controle do tempo

        Args:
            minutes (int): valor do tempo escolhido em minutos
        """
        self.timeCount = minutes * 60

    # setTime

    def setLabelTrayIcon(self, timeLabelTray):
        """Função que irá trazer a referência da label do trayIcon

        Args:
            labelTime (Referência): Referência ao campo que será atualizado
        """
        self.timeLabelTray = timeLabelTray

    # setLabelTrayIcon

    def setWindow(self, mainWindow):
        """Função que irá setar a janela principal

        Args:
            mainWindow (Ref QMainWindow): Referência da Janela principal
        """
        self.mainWindow = mainWindow

    # setWindow

    def setTrayIcon(self, trayIcon):
        """Função que recebe a instância do trayIcon

        Args:
            trayIcon (Ref QTrayIcon): Referência da Instância do TrayIcon
        """
        self.trayIcon = trayIcon

    # setTrayIcon

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
        if self.isTimeConcentration:
            self.setTime(self.data.sectionsTime)
        elif self.isTimeBreak:
            self.setTime(self.data.shortBreakTime)
        else:
            self.setTime(self.data.longBreakTime)
    # resetCount

    def endTimer(self):
        """Função que irá finalizar cada tempo
        """
        self.runCount = False
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
        makeNotification(msg, self.data.alertSound)
        self.updateScreen()
        self.updateTimeLabels()

    # endTimer

    def setConcetrationTime(self):
        """Função que irá informar que é um tempo de concentração
        """
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
        self.setTime(self.data.shortBreakTime)
        self.isTimeConcentration = False
        self.isTimeBreak = True
        self.isTimeLongBreak = False
        self.mainWindow.serieLabel.setText("Tempo de descanso")
        self.mainWindow.serieLabel.setStyleSheet("color: #79C061")

    # setBreakTime

    def setLongBreakTime(self):
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
            icon = QIcon("images/icon_32.png")
            self.trayIcon.setIcon(icon)

        else:
            # Mudanças na janela
            self.mainWindow.breakMode()
            # Mudanças no system Tray Icon
            icon = QIcon("images/icon_32_break.png")
            self.trayIcon.setIcon(icon)

    # updateScreen
