from threading import Thread
from time import strftime, gmtime, time
import time
from components.notification import makeNotification

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

    def setLabelSeries(self, seriesLabel):
        """Função que recolherá o número da série

        Args:
            seriesLabel (label): Label com a quantidade de ciclos já passados
        """
        self.labelSeries = seriesLabel
    # setLabelSeries

    def setWindowsMode(self, concetrationMode, breakMode):
        """Função que irá pegar as funções de modo de janela para alteração no final do ciclo

        Args:
            concetrationMode (function): Função que mudará a janela para o modo de concetração
            breakMode (function): Função que irá mudar a janela para o modo de pausa
        """
        self.setConcetrationMode = concetrationMode
        self.setBreakMode = breakMode
    # setWindowsMode

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
                self.concetrationCount = 1
        else:
            msg = "Fim do descanço\nIniciar concentração!"
            self.setConcetrationTime()
            self.concetrationCount += 1
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

    # setConcentrationTime

    def setBreakTime(self):
        """Função que irá informar que é um tempo de pausa
        """
        self.setTime(self.data.shortBreakTime)
        self.isTimeConcentration = False
        self.isTimeBreak = True
        self.isTimeLongBreak = False
    # setBreakTime

    def setLongBreakTime(self):
        self.setTime(self.data.longBreakTime)
        self.isTimeConcentration = False
        self.isTimeBreak = False
        self.isTimeLongBreak = True
    # setLongBreakTime

    def updateScreen(self):
        if(self.isTimeConcentration):
            self.setConcetrationMode()
            self.labelSeries.setText("Série "+str(self.concetrationCount))
        else:
            self.setBreakMode()
    # updateScreen
