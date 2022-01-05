from pytube import YouTube
from PyQt5 import uic, QtWidgets, QtCore
from time import sleep

# Iniciando a aplicação
app = QtWidgets.QApplication([])

# Carregando as interfaces
primeira_tela = uic.loadUi('primeira_tela.ui')
segunda_tela = uic.loadUi('segunda_tela.ui')
terceira_tela = uic.loadUi('terceira_tela.ui')

# Retirando a borda da interface
primeira_tela.setWindowFlag(QtCore.Qt.FramelessWindowHint)
primeira_tela.setAttribute(QtCore.Qt.WA_TranslucentBackground)
segunda_tela.setWindowFlag(QtCore.Qt.FramelessWindowHint)
segunda_tela.setAttribute(QtCore.Qt.WA_TranslucentBackground)
terceira_tela.setWindowFlag(QtCore.Qt.FramelessWindowHint)
terceira_tela.setAttribute(QtCore.Qt.WA_TranslucentBackground)

# Mostrando a primeira tela
primeira_tela.show()

def p1():
    primeira_tela.close()
    segunda_tela.show()

def p2():
    url = segunda_tela.lineEdit.text()
    youtube = YouTube(url)
    videos = youtube.streams.get_highest_resolution()
    for c in range(101):
        sleep(0.02)
        segunda_tela.progressBar.setValue(c)
    videos.download()
    


primeira_tela.pushButton.clicked.connect(p1)
segunda_tela.pushButton.clicked.connect(p2)


app.exec()
