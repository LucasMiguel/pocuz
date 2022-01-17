from threading import Thread
from time import strftime, gmtime, time
import time

from controllers.c_data import DataController


class MainThread(Thread):

    def __init__(self):
        super().__init__()
        self.data = DataController()
        self.timeCount = 0
        self.runCount = False
        self.timeConcentration = True
        self.timeBreak = False
        self.longBreak = False
        self.amountSeries = 1
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
                    self.runCount = False                
                # Delay de 1 segundo
                time.sleep(1)
    # run

    def setTime(self, minutes):
        """Função que formata o tempo trazido das configurações para segundos, para controle do tempo

        Args:
            minutes (int): valor do tempo escolhido em minutos
        """
        self.timeCount = minutes * 60
    # setTime

    def setLabelWindow(self, timeLabelWindow):
        """Função que irá trazer a referência da label da janela

        Args:
            labelTime (Referência): Referência ao campo que será atualizado
        """
        self.timeLabelWindow = timeLabelWindow
    # setLabelWindow

    def setLabelTrayIcon(self, timeLabelTray):
        """Função que irá trazer a referência da label do trayIcon

        Args:
            labelTime (Referência): Referência ao campo que será atualizado
        """
        self.timeLabelTray = timeLabelTray
    # setLabelTrayIcon

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
    # playCount
    
    def pauseCount(self):
        """Função que irá pausar o relógio
        """
        self.runCount = False
    # pauseCount

    def updateTimeLabels(self):     
        """Função que irá atualizar a tela das janelas
        """
        self.timeLabelWindow.setText(self.formatTime())
        self.timeLabelTray.setText(self.formatTime())
    # updateTimeLabels

