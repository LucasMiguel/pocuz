from notifypy import Notify


def makeNotification(msg,  mainThread):
    """Função que irá gerar o notificação

    Args:
        msg (string): Variável que trará a mensagem da notificação
        sound (bool, optional): Informa se a notificação terá som. Defaults to False.
        mainThread
    """
    notification = Notify()
    notification.title = "Pocuz"
    notification.message = msg
    notification.icon = "images/icon.png"
    if mainThread.data.alertSound:
        notification.audio = "sound/notification_sound.wav"
    notification.send()
    
