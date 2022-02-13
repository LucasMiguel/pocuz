import PyInstaller.__main__

PyInstaller.__main__.run([
    '../src/main.py',
    '--paths=../env/lib/python3.10/site-packages/',    
    '--name=pocuz'
])