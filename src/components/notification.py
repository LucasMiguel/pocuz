from notifypy import Notify
import os
import resources


def makeNotification(msg,  mainThread):
    """Função que irá gerar o notificação

    Args:
        msg (string): Variável que trará a mensagem da notificação
        sound (bool, optional): Informa se a notificação terá som. Defaults to False.
        mainThread
    """
    if os.path.isfile('/usr/share/images/icon.png'):
        path = "/usr/share/"
    else:
        path = ""

    notification = Notify()
    notification.title = "Pocuz"
    notification.message = msg
    notification.icon = path+"images/icon.png"
    if mainThread.data.alertSound:
        notification.audio = path+"sound/notification_sound.wav"    
    notification.send()

    
