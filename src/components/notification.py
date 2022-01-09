from notifypy import Notify


def makeNotification(msg, sound=False):
    """Função que irá gerar o notificação

    Args:
        msg (string): Variável que trará a mensagem da notificação
        sound (bool, optional): Informa se a notificação terá som. Defaults to False.
    """
    notification = Notify()
    notification.title = "Pocuz"
    notification.message = msg
    notification.icon = "images/icon.png"
    if sound == True:
        notification.audio = "sound/notification_sound.wav"

    notification.send()
