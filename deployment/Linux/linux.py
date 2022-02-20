import PyInstaller.__main__

PyInstaller.__main__.run([
    '../../src/main.py',   
    '--onefile', 
    # Incluindo o banco de dados
    '--add-data=../../data/data.json:data',
    # Incluindo arquivos de imagem
    '--add-binary=../../images/break.png:images',
    '--add-binary=../../images/concentration.png:images',
    '--add-binary=../../images/icon_32_break.png:images',
    '--add-binary=../../images/icon_32.png:images',
    '--add-binary=../../images/icon_about.png:images',
    '--add-binary=../../images/icon.ico:images',
    '--add-binary=../../images/icon.png:images',
    '--add-binary=../../images/menu_button.png:images',
    '--add-binary=../../images/pause.png:images',
    '--add-binary=../../images/play.png:images',
    '--add-binary=../../images/undo.png:images',
    # Incluindo o som da notificação
    '--add-binary=../../sound/notification_sound.wav:sound',
    # Inlcuindo a fonte
    '--add-binary=../../fonts/Lato-Light.ttf:fonts',
    '--paths=../../env/lib/python3.10/site-packages/',    
    '--name=pocuz'
])