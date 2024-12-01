from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QGroupBox,\
QButtonGroup, QRadioButton, QPushButton, QLabel, QSpinBox, QApplication

from PyQt5.QtCore import Qt

window = QWidget()
window.setStyleSheet('background:PaleTurquoise;font-family:Brush Script MT, Brush Script Std, cursive;font-weight:900;')
window.setWindowTitle("Основи арифметики 1 рівень")
btn_menu = QPushButton('Меню')
btn_menu.setStyleSheet("""
            QPushButton {font-weight:600;
               background-color: black;
        border-radius: 10px;
        color: white;
        border: 3px solid LightSkyBlue;
        
        
            }
            QPushButton:hover {
                border: 3px solid white;
                color:white;
                           background-color: DarkTurquoise;
                }
           """)

btn_rest = QPushButton('Відпочити')
btn_rest.setStyleSheet("""
            QPushButton {font-weight:600;
               background-color: black;
        border-radius: 10px;
        color: white;
        border: 3px solid LightSkyBlue;
        
        
            }
            QPushButton:hover {
                border: 3px solid white;
                color:white;
                           background-color: DarkTurquoise;
                }
           """)

btn_next = QPushButton('Відповісти')
btn_next.setStyleSheet("""
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
                }
           """)

rb_ans1 = QRadioButton(" ")

rb_ans1.setStyleSheet("color:black;font-weight:600;font:20px;")
rb_ans2 = QRadioButton("")
rb_ans2.setStyleSheet("color:black;font-weight:600;font:20px;")

rb_ans3 = QRadioButton("")
rb_ans3.setStyleSheet("color:black;font-weight:600;font:20px;")
rb_ans4 = QRadioButton("")
rb_ans4.setStyleSheet("color:black;font-weight:600;font:20px;")

RadioGroup = QButtonGroup()


RadioGroup.addButton(rb_ans1)

RadioGroup.addButton(rb_ans2)

RadioGroup.addButton(rb_ans3)

RadioGroup.addButton(rb_ans4)


lb_question = QLabel('Яблуко')
lb_question.setAlignment(Qt.AlignVCenter)
lb_question.setWordWrap(True)
lb_question.setStyleSheet("color:black;font-weight:600;font:35px;")
lb_rest = QLabel('с.')
lb_rest.setStyleSheet("color:black;font-weight:600;")
lb_result = QLabel('Правильно')
lb_result.setAlignment(Qt.AlignVCenter)
lb_result.setStyleSheet("color:black;font-weight:600;font:30px;")
lb_right_answer = QLabel('apple')
lb_right_answer.setAlignment(Qt.AlignVCenter)
lb_right_answer.setStyleSheet("color:black;font-weight:600;font:20px;")
N=10
sp_rest = QSpinBox()
sp_rest.setStyleSheet("color:black;font-weight:600;")
sp_rest.setValue(N)
gb_question = QGroupBox('Варіанти відповідей')
gb_question.setStyleSheet("color:black;font-weight:600;font:15px;border: 3px solid black")
time_bt=QLabel("Час:")
time_bt.setStyleSheet("color:black;font-weight:900;font:22px;")

rb_v1 = QVBoxLayout()

rb_v2 = QVBoxLayout()

rb_h1 = QHBoxLayout()


rb_v1.addWidget(rb_ans1)

rb_v1.addWidget(rb_ans2)

rb_v2.addWidget(rb_ans3)

rb_v2.addWidget(rb_ans4)
rb_h1.addLayout(rb_v1)
rb_h1.addLayout(rb_v2)

gb_question.setLayout(rb_h1)

gb_answer = QGroupBox()
v1 = QVBoxLayout()
v1.addWidget(lb_result)
v1.addWidget(lb_right_answer)
gb_answer.setLayout(v1)

h1_main = QHBoxLayout()

h2_main = QHBoxLayout()

h3_main = QHBoxLayout()

h4_main = QHBoxLayout()

v1_main = QVBoxLayout()


h1_main.addWidget (btn_menu)

h1_main.addStretch (1)

h1_main.addWidget (btn_rest)
h1_main.addWidget (sp_rest)
h1_main.addWidget (lb_rest)
h2_main.addWidget(lb_question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

h3_main.addWidget(gb_answer)
h3_main.addWidget(gb_question)
gb_answer.hide()
h4_main.addStretch (1)
h4_main.addWidget (btn_next, 65)
h4_main.addWidget (time_bt, 15)
h4_main.addStretch (1)

v1_main.addLayout (h1_main, stretch=1)

v1_main.addLayout (h2_main, stretch=2)

v1_main.addLayout (h3_main, stretch=8)


v1_main.addLayout (h4_main)
v1_main.setSpacing(5)
window.setLayout(v1_main)
window.resize(1280,600)

