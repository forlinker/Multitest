from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QGroupBox,\
QButtonGroup, QRadioButton, QPushButton, QLabel, QSpinBox, QApplication,QLineEdit

from PyQt5.QtCore import Qt

menu_window = QWidget()
menu_window.setWindowTitle('Меню')
menu_window.setStyleSheet('background:black;')
enter_question=QLabel("Введіть запитання:")
enter_question.setStyleSheet("color:white;font-weight:900;font:15px;")
quest_edit=QLineEdit()
quest_edit.setStyleSheet("color:white;font-weight:900;font:15px;")
question_answer=QLabel("Введіть вірну відповідь:")
question_answer.setStyleSheet("color:white;font-weight:900;font:15px;")
question_answer_enter=QLineEdit()
question_answer_enter.setStyleSheet("color:white;font-weight:900;font:15px;")

question_wrong_answ1=QLabel("Введіть першу хибну відповідь:")
question_wrong_answ1.setStyleSheet("color:white;font-weight:900;font:15px;")
question_wrong_answ1_enter=QLineEdit()
question_wrong_answ1_enter.setStyleSheet("color:white;font-weight:900;font:15px;")

question_wrong_answ2=QLabel("Введіть другу хибну відповідь:")
question_wrong_answ2.setStyleSheet("color:white;font-weight:900;font:15px;")
question_wrong_answ2_enter=QLineEdit()
question_wrong_answ2_enter.setStyleSheet("color:white;font-weight:900;font:15px;")

question_wrong_answ3=QLabel("Введіть третю хибну відповідь:")
question_wrong_answ3.setStyleSheet("color:white;font-weight:900;font:15px;")
question_wrong_answ3_enter=QLineEdit()
question_wrong_answ3_enter.setStyleSheet("color:white;font-weight:900;font:15px;")

add_quest=QPushButton("Додати запитання")
add_quest.setStyleSheet("""
            QPushButton {font-weight:600;
               background-color: black;
        border-radius: 10px;
        color: white;
        border: 3px solid LightSkyBlue;
                       font:20px;
        
        
            }
            QPushButton:hover {
                border: 3px solid white;
                color:white;
                           background-color: DarkTurquoise;
                }""")
clear_all=QPushButton("Очистити")
clear_all.setStyleSheet("""
            QPushButton {font-weight:600;
               background-color: black;
        border-radius: 10px;
        color: white;
        border: 3px solid LightSkyBlue;
                       font:20px;
        
        
            }
            QPushButton:hover {
                border: 3px solid white;
                color:white;
                           background-color: DarkTurquoise;
                }""")


statistic=QLabel("Статистика")
statistic.setStyleSheet("color:white;font-weight:900;font:25px;")
text_statistic_text=QLabel("Разів відповіли:")
text_statistic_text.setStyleSheet("color:white;font-weight:900;font:15px;")
text_n_true=QLabel("Вірних відповідей:")
text_n_true.setStyleSheet("color:white;font-weight:900;font:15px;")
text_n_yspih=QLabel("Успішність(%):")
text_n_yspih.setStyleSheet("color:white;font-weight:900;font:15px;")
text_sertime=QLabel("Ср. час / запитання:")
text_sertime.setStyleSheet("color:white;font-weight:900;font:15px;")

statistic_text=QLabel()
statistic_text.setStyleSheet("color:white;font-weight:900;font:15px;")
n_true=QLabel()
n_true.setStyleSheet("color:white;font-weight:900;font:15px;")
n_yspih=QLabel()
n_yspih.setStyleSheet("color:white;font-weight:900;font:15px;")
sertime=QLabel()
sertime.setStyleSheet("color:white;font-weight:900;font:15px;")

back=QPushButton("Назад")
back.setStyleSheet("""
            QPushButton {font-weight:600;
               background-color: black;
        border-radius: 10px;
        color: white;
        border: 3px solid LightSkyBlue;
                       font:20px;
        
        
            }
            QPushButton:hover {
                border: 3px solid white;
                color:white;
                           background-color: DarkTurquoise;
                }""")

c1_main=QHBoxLayout()
c2_main=QHBoxLayout()
c3_main=QHBoxLayout()
c4_main=QHBoxLayout()
c5_main=QHBoxLayout()
c6_main=QHBoxLayout()
c7_main=QHBoxLayout()
c8_main=QHBoxLayout()
c9_main=QHBoxLayout()
c10_main=QHBoxLayout()
main_line=QVBoxLayout()


c1_main.addWidget(enter_question)
c1_main.addWidget(quest_edit)

c2_main.addWidget(question_answer)
c2_main.addWidget(question_answer_enter)

c3_main.addWidget(question_wrong_answ1)
c3_main.addWidget(question_wrong_answ1_enter)

c4_main.addWidget(question_wrong_answ2)
c4_main.addWidget(question_wrong_answ2_enter)

c5_main.addWidget(question_wrong_answ3)
c5_main.addWidget(question_wrong_answ3_enter)

c6_main.addWidget(add_quest)
c6_main.addWidget(clear_all)

c7_main.addWidget(text_statistic_text)
c7_main.addWidget(statistic_text)

c8_main.addWidget(text_n_true)
c8_main.addWidget(n_true)

c9_main.addWidget(text_n_yspih)
c9_main.addWidget(n_yspih)

c10_main.addWidget(text_sertime)
c10_main.addWidget(sertime)
main_line.addLayout(c1_main)
main_line.addLayout(c2_main)
main_line.addLayout(c3_main)
main_line.addLayout(c4_main)
main_line.addLayout(c5_main)
main_line.addLayout(c6_main)


main_line.addWidget(statistic,5)
main_line.addLayout(c7_main)
main_line.addLayout(c8_main)
main_line.addLayout(c9_main)
main_line.addLayout(c10_main)
main_line.addWidget(back)

menu_window.setLayout(main_line)
menu_window.resize(550, 450)