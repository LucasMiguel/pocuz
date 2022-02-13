import PyInstaller.__main__

PyInstaller.__main__.run([
    'src/main.py',
    '--windowed',
    '-icon="images/icon.ico"',
    '--paths="env/lib/python3.10/site-packages/"',
    '--name="pocuz"'
])