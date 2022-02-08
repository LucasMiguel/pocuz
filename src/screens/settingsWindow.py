from threading import main_thread
from PySide6 import QtGui
from PySide6 import QtWidgets
from PySide6 import QtCore

class SettingWindow(QtWidgets.QDialog):
    def __init__(self, data, mainThread):
        self.data = data
        self.mainThread = mainThread        
        super(SettingWindow, self).__init__()
        self.setObjectName("self")
        self.resize(400, 413)
        self.setMinimumSize(QtCore.QSize(400, 413))
        self.setMaximumSize(QtCore.QSize(400, 413))        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setModal(True)
        # ===== LABELS =======================================================================
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20, 40, 321, 18))
        font = QtGui.QFont("Lato", 12, QtGui.QFont.Light)       
        self.label.setFont(font)
        self.label.setStyleSheet("color: #A9A9A9")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 191, 18))       
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #FFFFFF")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 281, 18))        
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #FFFFFF")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(20, 170, 281, 18))        
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: #FFFFFF")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(20, 210, 281, 18))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: #FFFFFF")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(20, 290, 281, 18))
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: #FFFFFF")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(20, 250, 281, 18))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: #FFFFFF")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self)
        self.label_8.setGeometry(QtCore.QRect(20, 330, 281, 18))
        self.label_8.setStyleSheet("color: #FFFFFF")
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        # ==== SPINS ==============================================================================
            # === CONCENTRATION ===================================================================
        self.spinBoxConcentration = QtWidgets.QSpinBox(self)
        self.spinBoxConcentration.setGeometry(QtCore.QRect(310, 80, 45, 27))
        font = QtGui.QFont()
        font.setFamily("Lato")
        self.spinBoxConcentration.setFont(font)
        self.spinBoxConcentration.setMinimum(1)
        self.spinBoxConcentration.setMaximum(60)
        self.spinBoxConcentration.setObjectName("spinBoxConcentration")
        self.spinBoxConcentration.setValue(data.sectionsTime)
        self.spinBoxConcentration.valueChanged.connect(lambda value: self.fieldChange(self.spinBoxConcentration))
            # === BREAK ===========================================================================
        self.spinBoxBreak = QtWidgets.QSpinBox(self)
        self.spinBoxBreak.setGeometry(QtCore.QRect(310, 120, 45, 27))
        font = QtGui.QFont()
        font.setFamily("Lato")
        self.spinBoxBreak.setFont(font)
        self.spinBoxBreak.setMinimum(1)
        self.spinBoxBreak.setMaximum(99)
        self.spinBoxBreak.setObjectName("spinBoxBreak")
        self.spinBoxBreak.setValue(self.data.shortBreakTime)
        self.spinBoxBreak.valueChanged.connect(lambda value: self.fieldChange(self.spinBoxBreak))
            # === LONG BREAK =======================================================================
        self.spinBoxLongBreak = QtWidgets.QSpinBox(self)
        self.spinBoxLongBreak.setGeometry(QtCore.QRect(310, 160, 45, 27))
        font = QtGui.QFont()
        font.setFamily("Lato")
        self.spinBoxLongBreak.setFont(font)
        self.spinBoxLongBreak.setMinimum(1)
        self.spinBoxLongBreak.setMaximum(99)
        self.spinBoxLongBreak.setObjectName("spinBoxLongBreak")
        self.spinBoxLongBreak.setValue(self.data.longBreakTime)
        self.spinBoxLongBreak.valueChanged.connect(lambda value: self.fieldChange(self.spinBoxLongBreak))
            # === SERIE COUNT =======================================================================
        self.spinBoxSeriesCount = QtWidgets.QSpinBox(self)
        self.spinBoxSeriesCount.setGeometry(QtCore.QRect(310, 200, 45, 27))
        font = QtGui.QFont()
        font.setFamily("Lato")
        self.spinBoxSeriesCount.setFont(font)
        self.spinBoxSeriesCount.setMinimum(1)
        self.spinBoxSeriesCount.setMaximum(99)
        self.spinBoxSeriesCount.setObjectName("spinBoxSeriesCount")
        self.spinBoxSeriesCount.setValue(self.data.amountSections)
        self.spinBoxSeriesCount.valueChanged.connect(lambda value: self.fieldChange(self.spinBoxSeriesCount))
        # ===== CHECKBOX ===================================================================================
            #  ==== NOTIFICATION ===========================================================================
        self.checkBoxNotification = QtWidgets.QCheckBox(self)
        self.checkBoxNotification.setGeometry(QtCore.QRect(310, 240, 21, 24))
        self.checkBoxNotification.setText("")
        self.checkBoxNotification.setObjectName("checkBoxNotification")
        self.checkBoxNotification.setChecked(self.data.notification)
        self.checkBoxNotification.isChecked
        self.checkBoxNotification.stateChanged.connect(lambda value: self.fieldChange(self.checkBoxNotification))
            #  ==== NOTIFICATION SOUND =====================================================================
        self.checkBoxNotificationSound = QtWidgets.QCheckBox(self)
        self.checkBoxNotificationSound.setGeometry(QtCore.QRect(310, 280, 21, 24))
        self.checkBoxNotificationSound.setText("")
        self.checkBoxNotificationSound.setObjectName("checkBoxNotificationSound")
        self.checkBoxNotificationSound.setChecked(self.data.alertSound)
        self.checkBoxNotificationSound.stateChanged.connect(lambda value: self.fieldChange(self.checkBoxNotificationSound))
            #  ==== DARK THEME =============================================================================
        self.checkBoxDarkTheme = QtWidgets.QCheckBox(self)
        self.checkBoxDarkTheme.setGeometry(QtCore.QRect(310, 320, 21, 24))
        self.checkBoxDarkTheme.setText("")
        self.checkBoxDarkTheme.setObjectName("checkBoxDarkTheme")
        self.checkBoxDarkTheme.setChecked(self.data.darkTheme)
        self.checkBoxDarkTheme.stateChanged.connect(lambda value: self.fieldChange(self.checkBoxDarkTheme))

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, SettingWindow):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Pocuz - Preferências"))
        self.label.setText(_translate("self", "As alterações serão efetuadas no próximo ciclo."))
        self.label_2.setText(_translate("self", "Comprimento da série (min)"))
        self.label_3.setText(_translate("self", "Comprimento da do intervalo curto (min)"))
        self.label_4.setText(_translate("self", "Comprimento da do intervalo longo (min)"))
        self.label_5.setText(_translate("self", "Sessões até o intervalo longo"))
        self.label_6.setText(_translate("self", "Notificação sonora"))
        self.label_7.setText(_translate("self", "Notificação"))
        self.label_8.setText(_translate("self", "Tema Dark"))
    

    def fieldChange(self, field):
        """Função que irá atualizar os dados quando a um campo mudar o estado

        Args:
            field (Field): O valor do campo que foi alterado
        """
        if(field == self.spinBoxConcentration):
            self.data.sectionsTime = field.value()
        elif (field == self.spinBoxBreak):
            self.data.shortBreakTime = field.value()
        elif (field == self.spinBoxLongBreak):
            self.data.longBreakTime = field.value()
        elif(field == self.spinBoxSeriesCount):
            self.data.amountSections = field.value()
        elif(field == self.checkBoxNotification):
            self.data.notification = field.isChecked()
        elif(field == self.checkBoxNotificationSound):
            self.data.alertSound = field.isChecked()
        else:
            self.data.darkTheme = field.isChecked()
        # Atualiza os dados
        self.data.setData()
        self.mainThread.setDarkMode()
        # fieldChange