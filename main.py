#!/usr/bin/python3
#

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
import pygame
import sys
pygame.init()
width = 401
height = 371
class Window(QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        loadUi("./Form/form.ui",self)
        
        self.setWindowTitle("Music Player")
        self.setGeometry(500,200,width,height)
        self.setFixedSize(width,height)
        
        self.play_btn.clicked.connect(self.play)
        self.pause_btn.clicked.connect(self.pause)
        self.stop_btn.clicked.connect(self.stop)
        self.openfile_action.triggered.connect(self.open_file)
        self.exit_action.triggered.connect(self.close)
        self.about_action.triggered.connect(self.about)
        
        self.short_key()
        
        self.setstatus = QStatusBar()
        self.setstatus.showMessage("Music Player v1.0")
        self.setStatusBar(self.setstatus)
    def open_file(self):
        try:
            file = QFileDialog().getOpenFileName(self,caption="Open File",filter="Mp3 File (*.mp3)")
            self.file_name = file[0]
            self.music_label.setText(self.file_name)
            pygame.mixer.music.load(self.file_name)
            
        except (Exception,):
            pass
    def play(self):
        pygame.mixer.music.play()
    def pause(self):
        pygame.mixer.music.pause()
    def stop(self):
        pygame.mixer.music.stop()
    def about(self):
        text = """Developer: Sina Meysami
Version: v1.0
Github: https://github.com/mrprogrammer2938
Instagram: https://instagram.com/sina.coder
Twitter: https://twitter.com/Sinameysami
"""
        width = 401
        height = 371
        dlg = QDialog()
        dlg.setWindowTitle("Music-Player/About")
        dlg.setGeometry(920,200,width,height)
        dlg.setFixedSize(width,height)
        textbox = QTextEdit(dlg)
        textbox.setText(text)
        textbox.setFont(QFont("Arial",20))
        textbox.setReadOnly(True)
        textbox.setStyleSheet("background-color: white;color: black;")
        textbox.resize(401,371)
        rev = dlg.exec_()
    def short_key(self):
        exit_key = QShortcut(QKeySequence("Ctrl+Q"), self)
        exit_key.activated.connect(self.close)
        exit_key2 = QShortcut(QKeySequence("Ctrl+E"), self)
        exit_key2.activated.connect(self.close)
        open_file = QShortcut(QKeySequence("Ctrl+O"),self)
        open_file.activated.connect(self.open_file)
        
def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Music Player")
    app.setApplicationDisplayName("Music Player")
    app.setApplicationVersion("v1.0")
    window = Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    # Music Player v1.0
    main()
    