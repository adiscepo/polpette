from random import randint
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtCore import QTimer 

"""
Petit script permettant de mesurer le temps de parole de chaque personne

"""

class Polpette(QWidget):
    def __init__(self, participants):
        super().__init__()
        self.participants = participants
        self.timer_val = [0 for p in self.participants]
        self.label = [QLabel() for p in self.participants]
        self.current_speaker = -1
        self.timer = QTimer(self)
        color = ["90F1EF", "FFD6E0", "FFEF9F", "C1FBA4", "7BF1A8"]
        self.setGeometry(500, 550, 200, 50*len(self.participants))

        self.setWindowTitle("Polpette")
        self.layoutV = QVBoxLayout()
        self.layoutH = [QHBoxLayout() for p in self.participants]
        for i, elem in enumerate(self.layoutH):
            self.label[i].setText('0')
            self.label[i].setGeometry(75, 100, 250, 70) 
            self.label[i].setStyleSheet("border : 2px solid #{}; font-family: 'Monospace'".format(color[randint(0, len(color)-1)]))  
            elem.addWidget(self.label[i])

            button = QPushButton(self.participants[i])
            button.clicked.connect(lambda x, i=i: self.start_timer(i))
            
            elem.addWidget(button)
            self.layoutV.addLayout(elem)
        
        self.timer.timeout.connect(self.set_time)
        # pause =  QPushButton("Pause")
        # pause.pressed.connect(self.pause_timer)
        # self.layoutV.addWidget(pause)
        self.setLayout(self.layoutV)
        self.show()
    
    def start_timer(self, i):
        if (self.current_speaker == -1):
            self.timer.start(100)
        if (i < len(self.participants)):
            if i != self.current_speaker:
                print("Ok {} commence a parler".format(i))
                self.current_speaker = i
            else:
                self.pause_timer()

    def set_time(self):
        if (self.current_speaker != -1): # Si timer pas en pause
            self.timer_val[self.current_speaker] += 1/10
            self.label[self.current_speaker].setText("{:.1f}".format(self.timer_val[self.current_speaker]))
    
    def pause_timer(self):
        self.current_speaker = -1

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Le programme se lance avec `python3 main.py participant_1 participant_2 ... participant_n`")
        exit(1)
    
    participants = sys.argv[1:].copy()
    app = QApplication(sys.argv)
    window = Polpette(participants)
    app.exec()
