import random
from threading import Thread
from playsound import playsound
from PyQt5.QtWidgets import  QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    
    def __init__(self) -> None:
        self.uscore = 0
        self.cscore = 0
        music_thread = Thread(target=self.play_music())
        music_thread.daemon = True
        music_thread.start()
        

    def play_music(self):
        music_file = "assets/background.mp3"
        try:
            playsound(music_file, block=False)
        except:
            pass

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1048, 681)
        MainWindow.setStyleSheet("background-color: rgb(44, 136, 176);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.yourscore = QtWidgets.QLabel(self.centralwidget)
        self.yourscore.setGeometry(QtCore.QRect(180, 60, 161, 61))
        self.yourscore.setObjectName("yourscore")
        self.star1 = QtWidgets.QLabel(self.centralwidget)
        self.star1.setGeometry(QtCore.QRect(120, 120, 55, 51))
        self.star1.setStyleSheet("background-image: url(:/star/star.png);")
        self.star1.setText("")
        #self.star1.setPixmap(QtGui.QPixmap(":/star/star.png"))
        self.star1.setScaledContents(True)
        self.star1.setObjectName("star1")
        self.star2 = QtWidgets.QLabel(self.centralwidget)
        self.star2.setGeometry(QtCore.QRect(200, 120, 55, 51))
        self.star2.setStyleSheet("background-image: url(:/star/star.png);")
        self.star2.setText("")
        #self.star2.setPixmap(QtGui.QPixmap(":/star/star.png"))
        self.star2.setScaledContents(True)
        self.star2.setObjectName("star2")
        self.star3 = QtWidgets.QLabel(self.centralwidget)
        self.star3.setGeometry(QtCore.QRect(280, 120, 55, 51))
        self.star3.setStyleSheet("background-image: url(:/star/star.png);")
        self.star3.setText("")
        #self.star3.setPixmap(QtGui.QPixmap(":/star/star.png"))
        self.star3.setScaledContents(True)
        self.star3.setObjectName("star3")
        self.computerscore = QtWidgets.QLabel(self.centralwidget)
        self.computerscore.setGeometry(QtCore.QRect(810, 60, 211, 61))
        self.computerscore.setObjectName("computerscore")
        self.cstar3 = QtWidgets.QLabel(self.centralwidget)
        self.cstar3.setGeometry(QtCore.QRect(930, 120, 55, 51))
        self.cstar3.setStyleSheet("background-image: url(:/star/star.png);")
        self.cstar3.setText("")
        #self.cstar3.setPixmap(QtGui.QPixmap(":/star/star.png"))
        self.cstar3.setScaledContents(True)
        self.cstar3.setObjectName("cstar3")
        self.cstar1 = QtWidgets.QLabel(self.centralwidget)
        self.cstar1.setGeometry(QtCore.QRect(770, 120, 55, 51))
        self.cstar1.setStyleSheet("background-image: url(:/star/star.png);")
        self.cstar1.setText("")
        #self.cstar1.setPixmap(QtGui.QPixmap(":/star/star.png"))
        self.cstar1.setScaledContents(True)
        self.cstar1.setObjectName("cstar1")
        self.cstar2 = QtWidgets.QLabel(self.centralwidget)
        self.cstar2.setGeometry(QtCore.QRect(850, 120, 55, 51))
        self.cstar2.setStyleSheet("background-image: url(:/star/star.png);")
        self.cstar2.setText("")
        #self.cstar2.setPixmap(QtGui.QPixmap(":/star/star.png"))
        self.cstar2.setScaledContents(True)
        self.cstar2.setObjectName("cstar2")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(330, 10, 441, 51))
        self.Title.setObjectName("Title")
        self.uchoise = QtWidgets.QLabel(self.centralwidget)
        self.uchoise.setGeometry(QtCore.QRect(100, 430, 201, 71))
        self.uchoise.setObjectName("uchoise")
        self.rock = QtWidgets.QPushButton(self.centralwidget)
        self.rock.setGeometry(QtCore.QRect(10, 250, 121, 141))
        self.rock.setStyleSheet("QPushButton{\n"
                                "border-image: url(:/rock/rock.png);\n"
                                "background-color: rgb(188, 18, 255);\n"
                                "}\n"
                                "QPushButton:hover{\n"
                                "background: rgba(0, 0, 0,0);\n"
                                "}")
        self.rock.setText("")
        self.rock.setObjectName("rock")
        self.paper = QtWidgets.QPushButton(self.centralwidget)
        self.paper.setGeometry(QtCore.QRect(160, 250, 121, 141))
        self.paper.setStyleSheet("QPushButton{\n"
                                 "border-image: url(:/paper/paper.png);\n"
                                 "background-color: rgb(255, 255, 255);\n"
                                 "}\n"
                                 "QPushButton:hover{\n"
                                 "background: rgba(0, 0, 0,0);\n"
                                 "}")
        self.paper.setText("")
        self.paper.setObjectName("paper")
        self.scissors = QtWidgets.QPushButton(self.centralwidget)
        self.scissors.setGeometry(QtCore.QRect(300, 250, 121, 141))
        self.scissors.setStyleSheet("QPushButton{\n"
                                    "border-image: url(:/scissors/scissors.png);\n"
                                    "background-color: rgb(255, 85, 0);\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                    "background: rgba(0, 0, 0,0);\n"
                                    "}")
        self.scissors.setText("")
        self.scissors.setObjectName("scissors")
        self.compick = QtWidgets.QLabel(self.centralwidget)
        self.compick.setGeometry(QtCore.QRect(790, 440, 171, 51))
        self.compick.setObjectName("compick")
        self.comchoise = QtWidgets.QLabel(self.centralwidget)
        self.comchoise.setGeometry(QtCore.QRect(790, 230, 171, 171))
        self.comchoise.setStyleSheet("background-image: url(:/rps/rock-paper-scissors.png);")
        self.comchoise.setText("")
        self.comchoise.setPixmap(QtGui.QPixmap(":/rps/rock-paper-scissors.png"))
        self.comchoise.setScaledContents(True)
        self.comchoise.setObjectName("comchoise")
        self.gamestatus = QtWidgets.QLabel(self.centralwidget)
        self.gamestatus.setGeometry(QtCore.QRect(420, 430, 281, 151))
        
        self.gamestatus.setText("")
        
        self.gamestatus.setScaledContents(True)
        self.gamestatus.setObjectName("gamestatus")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.rock.clicked.connect(lambda: self.action("rock"))
        self.paper.clicked.connect(lambda: self.action("paper"))
        self.scissors.clicked.connect(lambda: self.action("scissors"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.yourscore.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Your Score</span></p></body></html>"))
        self.computerscore.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Computer Score</span></p></body></html>"))
        self.Title.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; font-style:italic; text-decoration: underline;\">Rock Paper Scissors Game</span></p></body></html>"))
        self.uchoise.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Take your pick</span></p></body></html>"))
        self.compick.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">computer pick</span></p></body></html>"))

    def action(self, user_choice):
        computer_choice = random.choice(["rock", "paper", "scissors"])
        if computer_choice == "rock" :
            self.comchoise.setPixmap(QtGui.QPixmap(":/rock/rock.png"))
            self.comchoise.setStyleSheet("border-image: url(:/rock/rock.png);\n""background-color: rgb(178, 58, 255);")
        elif computer_choice == "paper":
            self.comchoise.setPixmap(QtGui.QPixmap(":/paper/paper.png"))
            self.comchoise.setStyleSheet("border-image: url(:/paper/paper.png);\n""background-color: rgb(255, 255, 255);")
        elif computer_choice == "scissors":
            self.comchoise.setPixmap(QtGui.QPixmap(":/scissors/scissors.png"))
            self.comchoise.setStyleSheet("border-image: url(:/scissors/scissors.png);\n""background-color: rgb(255, 85, 0);")
        
        if user_choice == computer_choice:
                playsound("assets/tie.mp3")
        elif user_choice == "rock":
            if computer_choice == "scissors":
                self.uscore += 1
            else:
                self.cscore += 1
        elif user_choice == "paper":
                if computer_choice == "rock":
                  self.uscore += 1
                else:
                    self.cscore += 1
        elif user_choice == "scissors":
                if computer_choice == "paper":
                    self.uscore += 1
                else:
                    self.cscore += 1
        self.update_score(self.cscore,self.uscore)

    def update_score(self,c_score,u_score):
        
        if c_score >0:
              self.cstar1.setPixmap(QtGui.QPixmap(":/star/star.png"))
        if c_score >1:
              self.cstar2.setPixmap(QtGui.QPixmap(":/star/star.png"))
        if c_score > 2:
              self.cstar3.setPixmap(QtGui.QPixmap(":/star/star.png"))
              self.declare_result('x') 
        if u_score >= 1:
              self.star1.setPixmap(QtGui.QPixmap(":/star/star.png"))
        if u_score >= 2:
              self.star2.setPixmap(QtGui.QPixmap(":/star/star.png"))
        if u_score >= 3:
              self.star3.setPixmap(QtGui.QPixmap(":/star/star.png"))
              self.declare_result('u')    

    def declare_result(self,winner):
        if winner == 'u':
             self.gamestatus.setPixmap(QtGui.QPixmap(":/win/winner.jpg"))
             self.play_again_dialog()
        else:
             self.gamestatus.setPixmap(QtGui.QPixmap("://loser/lose.jpg"))
             self.play_again_dialog()


    def play_again_dialog(self):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Play Again?")
        msg_box.setText("Do you want to play again?")
        play_again_btn = msg_box.addButton("Play Again", QMessageBox.YesRole)
        exit_btn = msg_box.addButton("Exit", QMessageBox.NoRole)
        msg_box.setDefaultButton(play_again_btn)
    
        msg_box.exec_() 
    
        if msg_box.clickedButton() == play_again_btn:
            self.uscore = 0
            self.cscore = 0
            self.cstar1.clear()
            self.cstar2.clear()
            self.cstar3.clear()
            self.star1.clear()
            self.star2.clear()
            self.star3.clear()
            self.gamestatus.clear()
        elif msg_box.clickedButton() == exit_btn :
            exit()
        else:
             exit()

        


from assets import resources


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
