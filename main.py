#!/usr/bin/python3
#

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from form import Ui_MainWindow
import qdarktheme
import pygame
import sys,os
pygame.init()

class Window(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.n = 0
        self.setupUi(self)
        qdarktheme.setup_theme("light")
        self.setWindowTitle("Music Player")
        self.setWindowIcon(QIcon("icon.jpg"))
        self.setFixedSize(821,535)
        
        self.sound_slider.setMinimum(0)
        self.sound_slider.setMaximum(100)
        self.sound_slider.setValue(30)
        
        self.sound_slider.valueChanged.connect(self.set_sound)
        self.mylist.itemClicked.connect(self.set_file)
        
        self.play_btn.clicked.connect(self.play)
        self.pause_btn.clicked.connect(self.pause)
        self.stop_btn.clicked.connect(self.stop)
        self.select_folder.triggered.connect(self.open_folder)
        self.exit_action.triggered.connect(self.close)
        
        self.short_key()
        
        self.set_status()

    def open_folder(self):
        try:
            self.folder = QFileDialog().getExistingDirectory(self,"Select Music Folder","C:\\")
            self.mylist.clear()
            lists = os.listdir(self.folder)
            for item in lists:
                if item[-4::] == ".mp3":
                    self.mylist.addItem(item)
                else:
                    pass     
            self.label_path.setText(f"Folder: {self.folder}")
        except:
            return

    def set_file(self,item):
        try:
            item_text = item.text()
            pygame.mixer.music.load(f"{self.folder}/{item_text}")
        except Exception as err:
            print(err)
    def set_sound(self):
        value = float(self.sound_slider.value())
        pygame.mixer.music.set_volume(value)
    def change_sound(self):
        try:
            value = self.hslider.value()
            pygame.mixer.music.set_pos(value)
        except:
            return
    def play(self):
        pygame.mixer.music.play()
    def pause(self):
        pygame.mixer.music.pause()
    def stop(self):
        pygame.mixer.music.stop()
    def short_key(self):
        exit_key = QShortcut(QKeySequence("Ctrl+Q"), self)
        exit_key.activated.connect(self.close)
        exit_key2 = QShortcut(QKeySequence("Ctrl+E"), self)
        exit_key2.activated.connect(self.close)
        open_folder = QShortcut(QKeySequence("Ctrl+O"),self)
        open_folder.activated.connect(self.open_folder)
    def set_status(self):
        status = QStatusBar(self)
        status.showMessage("Music Player v1.0")
        self.setStatusBar(status)   
def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Music Player")
    app.setApplicationDisplayName("Sina Meysami")
    app.setApplicationVersion("v1")
    window = Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    # Music Player v1.0
    main()
    
