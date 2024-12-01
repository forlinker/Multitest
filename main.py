from random import choice, shuffle
from time import *
from PyQt5.QtWidgets import QApplication,QMessageBox
app = QApplication([])
from main_window import *
from menu_window import *




class Question():
    def __init__(self,question,answer,wrong_answer1,wrong_answer2,wrong_answer3):
        self.question=question
        self.answer=answer
        self.wrong_answer1=wrong_answer1
        self.wrong_answer2=wrong_answer2
        self.wrong_answer3=wrong_answer3
        self.trys=0
        self.right_answers=0
        self.next=True

    def got_right(self):
        self.trys +=1
        self.right_answers +=1
    def got_wrong(self):
        self.trys +=1

class begining(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Оберіть предмет')
        self.resize(500,200)
        
        main_line=QVBoxLayout()
        layout = QHBoxLayout()
        layout1= QHBoxLayout()
        self.setLayout(main_line)
        text=QLabel("Оберіть предмет для тестування")
        
        text.setStyleSheet("color:black;font-weight:900;font:15px;")
        math_mode = QPushButton('Математика')
        math_mode.clicked.connect(self.math)
        math_mode.setStyleSheet("""
            QPushButton {font-weight:600;
               background-color:PaleTurquoise;
        border-radius: 10px;
        color: black;
        border: 3px solid LightSkyBlue;
                       font:20px;
        
        
            }
            QPushButton:hover {
                border: 3px solid white;
                color:white;
                           background-color: DarkTurquoise;
                }""")

        history_mode = QPushButton('Історія')
        history_mode.clicked.connect(self.history)
        history_mode.setStyleSheet("""
            QPushButton {font-weight:600;
               background-color: yellow;
        border-radius: 10px;
        color: black;
        border: 3px solid LightSkyBlue;
                       font:20px;
        
        
            }
            QPushButton:hover {
                border: 3px solid white;
                color:white;
                           background-color: DarkTurquoise;
                }""")

        layout.addWidget(math_mode)
        
        layout1.addWidget(text)
        layout.addWidget(history_mode)
        main_line.addLayout(layout1)
        main_line.addLayout(layout)

        self.show()
    def math(self):
        self.hide()
        

        def new_question():
            if len(question_list)<=0:
                
                window.setWindowTitle("2 рівень")
                if len(question_list_lvl2)<=0:
                    
                    window.setWindowTitle("3 рівень")
                    if len(question_list_lvl3)<=0:
                    
                        window.setWindowTitle("3 рівень")
                        lvl3_finished()
                        
                    else:  
                        global cur_q2
                        cur_q2 = choice(question_list_lvl3)
                        question_list_lvl3.remove(cur_q2)
                        lb_question.setText(cur_q2.question)
                        lb_right_answer.setText(cur_q2.answer)
                        shuffle(radio_buttons)

                        radio_buttons[0].setText(cur_q2.wrong_answer1)
                        radio_buttons[1].setText(cur_q2.wrong_answer2)
                        radio_buttons[2].setText(cur_q2.wrong_answer3)
                        radio_buttons[3].setText(cur_q2.answer)
                else:  
                    global cur_q1
                    cur_q1 = choice(question_list_lvl2)
                    question_list_lvl2.remove(cur_q1)
                    lb_question.setText(cur_q1.question)
                    lb_right_answer.setText(cur_q1.answer)
                    shuffle(radio_buttons)

                    radio_buttons[0].setText(cur_q1.wrong_answer1)
                    radio_buttons[1].setText(cur_q1.wrong_answer2)
                    radio_buttons[2].setText(cur_q1.wrong_answer3)
                    radio_buttons[3].setText(cur_q1.answer)
            else:
                global cur_q
                cur_q = choice(question_list)
                question_list.remove(cur_q)
                lb_question.setText(cur_q.question)
                lb_right_answer.setText(cur_q.answer)
                shuffle(radio_buttons)

                radio_buttons[0].setText(cur_q.wrong_answer1)
                radio_buttons[1].setText(cur_q.wrong_answer2)
                radio_buttons[2].setText(cur_q.wrong_answer3)
                radio_buttons[3].setText(cur_q.answer)
        def switch_menu():
            window.hide()
            menu_window.show()
            statistic_text.setText(str(tr.trys))
            n_true.setText(str(ans.right_answers))
            n_yspih.setText(str(round((ans.right_answers*100)/tr.trys)))
            sertime.setText(str(round(tr.right_answers/tr.trys,2)))
            

        def return_to_main():
            window.show()
            menu_window.hide()

        def rest():
            window.hide()
            sleep(sp_rest.value())
            window.show()


        tr=Question("1","1","1","1","1")
        ans=Question("1","1","1","1","1")
        def check_result():
            correct= radio_buttons[3].isChecked()
            
            
            if correct:
                lb_result.setText("Правильно")
                lb_right_answer.setText("")
                tr.trys+=1
                ans.right_answers+=1
                
                
            else:
                lb_result.setText("Неправильно")
                tr.trys+=1
                
            
            
                


                
        qust1 = Question("(2+x)^2","x^2 + 4x + 4","4 + 2x + x^2","x^2 + 4x + 2","4 + 4x + x")
        qust2 = Question("(1+2x)^2","1 + 4x + 4x^2","1 + 2x + 4x^2","2 + 4x + 2x^2","2 + 2x + x^2")
        qust3 = Question("(a−1)^2","a^2 – 2a + 1","a^2 + 2a – 1","(a – 1)(a + 1)","2a^2 – 2a + 1")
        qust4 = Question("(5b−1)(5b+1)","25b^2 – 1","25b^2 + 1","1 + 5b^2","5b^2 – 1")
        qust5 = Question("(−1+2t)(1+2t)","4t^2 – 1","1 – 4t^2","2t^2 + 1","2t^2 – 1")
        qust6 = Question("(7a−9)(7a+9)","49a^2 – 81","7a^2 + 81","49a^2 – 3","7a^2 – 9")

        quest1_for_lvl2=Question("""Чому дорівнює сума коренів квадратного рівняння х^2+12х+20=0?""","-12","-20","12","20")
        quest2_for_lvl2=Question("""Чому дорівнює добуток коренів квадратного рівняння x^2-7х+12=0?""","12","-12 ","7","-7")
        quest3_for_lvl2=Question("х^2+11х+q=0; x1=-1; x2 - ? ; q - ?","-10; 10 ","10; -10","11; -1","12; -12")
        quest4_for_lvl2=Question(" Рівняння х2+кх+р=0 має корені 2 і 4. Знайдіть к і р.","k=-6;p=8 ","k=6; p= -8","k=6; p= -8"," k=8; p=6")
        quest5_for_lvl2=Question("2x^2+7x+5 Знайдіть чому дорівнює дискримінант.","9 ","3","69","49")
        quest6_for_lvl2=Question("Складіть рівння за його коефіцієнтами а=6, b=10, c=-4","6x2+10x-4=0 ","-6x2-10x+4=0","6x2-10x-4=0","6x2+10x+4=0")
        quest7_for_lvl2=Question("""Знайдіть чому дорівнює сума і добуток коренів квадратного рівння х2+10х+25=0.""","-10, 25 ","10, -25","1, 25","10, 25")

        q1_forlvl3=Question("""Одна зі сторін трикутника дорівнює 7 см.Знайти висоту, проведену до неї, якщо площа дорівнює 35 см^2.""","10 см","5 см","7,5 см","2,5 см") 
        q2_forlvl3=Question("""Знайти гіпотенузу прямокутного трикутника,якщо один його катет дорівнює 6 см, а площа - 24 см^2""","10 см","12 см","7 см","4 см") 
        q3_forlvl3=Question("""Знайти площу трикутника, у якого дві сторони дорівнюють 6 см і 10 см і кут між цими сторонами 30 градусів.""","15 ","30","60","16") 
        q4_forlvl3=Question("""Знайти площу рівностороннього трикутника зі стороною 2√3.""","3√3 см^2 ","2√3 см^2","4√3 см^2","3 см^2") 




        question_list=[qust1,qust2,qust3,qust4,qust5,qust6]
        question_list_lvl2=[quest1_for_lvl2,quest2_for_lvl2,quest3_for_lvl2,quest4_for_lvl2,quest5_for_lvl2,quest6_for_lvl2,quest7_for_lvl2]
        question_list_lvl3=[q1_forlvl3,q2_forlvl3,q3_forlvl3,q4_forlvl3]
        radio_buttons=[rb_ans1,rb_ans2,rb_ans3,rb_ans4]


        new_question()

        start_time=time()
        def click_ok():
            
            
            
            if btn_next.text() == 'Відповісти':
                
                
                new_time=time()
                gb_question.hide()
                gb_answer.show()
                btn_next.setText('Наступне запитання')
                time_bt.setText(str(round(new_time-start_time)))
                tr.right_answers=new_time-start_time
                new_time=0
                
                check_result()

                

            else:
                time_bt.setText("Час:")
                gb_question.show()
                gb_answer.hide()
                btn_next.setText('Відповісти')
                new_question()
                

        def clear_all_inputline():
            quest_edit.clear()
            question_answer_enter.clear()
            question_wrong_answ1_enter.clear()
            question_wrong_answ2_enter.clear()
            question_wrong_answ3_enter.clear()
        def add_new_question():
            new_quest=Question(quest_edit.text(),question_answer_enter.text(),question_wrong_answ1_enter.text(),question_wrong_answ2_enter.text(),question_wrong_answ3_enter.text())
            question_list.append(new_quest)
            return new_quest
            clear_all_inputline()
        def button_clicked():
                dlg = QMessageBox()
                dlg.setStyleSheet("font-weight:600;color:white;background:black;border: 1px solid LightSkyBlue;font:20px;")
                dlg.setWindowTitle("Запитання додано!")
                dlg.setText("Перейдіть в тест щоб переглянути")
                button = dlg.exec()

                button == QMessageBox.StandardButton.Ok

        def lvl2_finished():
                dlg1 = QMessageBox()
                dlg1.setStyleSheet("font-weight:900;color:black;background:PaleTurquoise ;font:20px;font-family:Brush Script MT, Brush Script Std, cursive;")
                dlg1.setWindowTitle("Повідомлення")
                dlg1.setText("""Вас вітає захоплююча математична гра! 🎉 
        Ви матимете можливість пройти три рівні складності, вирішуючи завдання з логіки та обчислень.
        Кожне завдання має одну правильну відповідь, тож будьте уважні!✅ 
                Бажаємо успіху та наснаги на шляху до перемоги! 🎯💪""")
                dlg1.exec_()
        def lvl3_finished():
                dlg1 = QMessageBox()
                dlg1.setStyleSheet("font-weight:600;color:black;background:PaleTurquoise;border: 1px solid LightSkyBlue;font:20px;font-family:Brush Script MT, Brush Script Std, cursive;")
                dlg1.setWindowTitle("Завершення тесту")
                dlg1.setText("Вітаємо із завершенням тесту!Перейдіть в меню щоб побачити свій результат")
                dlg1.exec_() 

                


        btn_next.clicked.connect(click_ok)
        btn_rest.clicked.connect(rest)
        btn_menu.clicked.connect(switch_menu)
        back.clicked.connect(return_to_main)
        clear_all.clicked.connect(clear_all_inputline)
        add_quest.clicked.connect(add_new_question)
        add_quest.clicked.connect(button_clicked)
        lvl2_finished()
        window.show()
        
    def history(self):
        self.hide()
        window.setStyleSheet('background:yellow;')
        window.setWindowTitle("Тест з історії")
        def new_question():
            if len(question_list)<=0:
                
                window.setWindowTitle("2 рівень")
                if len(question_list_lvl2)<=0:
                    
                    window.setWindowTitle("3 рівень")
                    if len(question_list_lvl3)<=0:
                    
                        window.setWindowTitle("3 рівень")
                        lvl3_finished()
                        
                    else:  
                        global cur_q2
                        cur_q2 = choice(question_list_lvl3)
                        question_list_lvl3.remove(cur_q2)
                        lb_question.setText(cur_q2.question)
                        lb_right_answer.setText(cur_q2.answer)
                        shuffle(radio_buttons)

                        radio_buttons[0].setText(cur_q2.wrong_answer1)
                        radio_buttons[1].setText(cur_q2.wrong_answer2)
                        radio_buttons[2].setText(cur_q2.wrong_answer3)
                        radio_buttons[3].setText(cur_q2.answer)
                else:  
                    global cur_q1
                    cur_q1 = choice(question_list_lvl2)
                    question_list_lvl2.remove(cur_q1)
                    lb_question.setText(cur_q1.question)
                    lb_right_answer.setText(cur_q1.answer)
                    shuffle(radio_buttons)

                    radio_buttons[0].setText(cur_q1.wrong_answer1)
                    radio_buttons[1].setText(cur_q1.wrong_answer2)
                    radio_buttons[2].setText(cur_q1.wrong_answer3)
                    radio_buttons[3].setText(cur_q1.answer)
            else:
                global cur_q
                cur_q = choice(question_list)
                question_list.remove(cur_q)
                lb_question.setText(cur_q.question)
                lb_right_answer.setText(cur_q.answer)
                shuffle(radio_buttons)

                radio_buttons[0].setText(cur_q.wrong_answer1)
                radio_buttons[1].setText(cur_q.wrong_answer2)
                radio_buttons[2].setText(cur_q.wrong_answer3)
                radio_buttons[3].setText(cur_q.answer)
        def switch_menu():
            window.hide()
            menu_window.show()
            statistic_text.setText(str(tr.trys))
            n_true.setText(str(ans.right_answers))
            n_yspih.setText(str(round((ans.right_answers*100)/tr.trys)))
            sertime.setText(str(round(tr.right_answers/tr.trys,2)))
            

        def return_to_main():
            window.show()
            menu_window.hide()

        def rest():
            window.hide()
            sleep(sp_rest.value())
            window.show()


        tr=Question("1","1","1","1","1")
        ans=Question("1","1","1","1","1")
        def check_result():
            correct= radio_buttons[3].isChecked()
            
            
            if correct:
                lb_result.setText("Правильно")
                lb_right_answer.setText("")
                tr.trys+=1
                ans.right_answers+=1
                
                
            else:
                lb_result.setText("Неправильно")
                tr.trys+=1
                
            
        qust1 = Question("В якому році відбулася жовтоводська битва?","1648","1775","1654","1574")
        qust2 = Question("Яка з поданих подій відбулася в 1596?","Берестейська унія","Люблинська унія","друкування Апостола","Хотинська битва")
        qust3 = Question("""За гетьмануванням кого почалася Національно-визвольна війна 1648р?""","Б.Хмельницького","П.Дорошенка","І.Мазепи","І.Виговського")
        qust4 = Question("Гетьманство було остаточно ліквідовано у ...","1764","1778","1648","1775")
        qust5 = Question("«Паланка» — це адміністративно-територіальна одиниця","Нової (Підпільненської) Січі.","Правобережної Гетьманщини.","Лівобережної Гетьманщини.","Слобідської України.")
        qust6 = Question("""У 1734 р. царський уряд дозволив козакам заснувати Нову Січ на р. Підпільна, тому що прагнув""","використати козаків у новій російсько-турецькій війні.","залучити козаків до придушення селянських виступів.","налагодити союзницькі стосунки із Кримським ханством.","мати додатковий важіль впливу на Річ Посполиту.")

        quest1_for_lvl2=Question("1 вересня 1939 р., 22 червня 1941 р. — це дати","""початку Другої світової війни 
та Великої Вітчизняної війни.""","""укладення Мюнхенської угоди 
та пакту «Молотова-Ріббентропа».""","""включення Західної України, Бессарабії 
та Північної Буковини до складу УPCP.""","""проголошення незалежності Карпатської України 
та Акта про відновлення Української держави""")
        quest2_for_lvl2=Question("""Що є вагомим прикладом політики радянізації західних областей Української РСР у 1939–1941 рр.?""","націоналізація промисловості, торгівлі, земель великих власників","лояльне ставлення влади до священиків греко-католицької церкви","залучення «буржуазних спеціалістів» до процесу індустріалізації","налагодження співробітництва влади з українськими партіями")
        quest3_for_lvl2=Question("""Територія радянської України стала ареною збройної боротьби між СРСР і Німеччиною""","22 червня 1941 р.","30 червня 1939 р","1 вересня 1939 р.","23 серпня 1942 р.")
        quest4_for_lvl2=Question("Що стало проявом реалізації «пакту Молотова–Ріббентропа»?","вторгнення Червоної армії на територію Західної України","окупація військами Німеччини та її союзників усієї території України","агресія Угорщини проти Карпатської України","створення дистрикту «Галичина»")
        quest5_for_lvl2=Question("""Одна з найбільших танкових битв Другої світової війни в районі міст Рівно–Дубно–Броди–Луцьк відбулася в""","червні 1941 р.","квітні 1942 р.","жовтні 1944 р.","листопаді 1943 р.")
        quest6_for_lvl2=Question("""Основна боротьба загонів Української повстанської армії в 1942 р. – 1950-х рр. точилася на землях""","Західної України.","Східної України.","Південної України.","Центральної України.")
        quest7_for_lvl2=Question("""Національно-визвольна боротьба українського народу проти окупантів у роки Другої світової війни відбувалася у формі""","підпільної та партизанської боротьби проти загарбників.","страйків робітників і масових акцій громадської непокори.","участі регулярних українських армій у складі військ Антигітлерівської коаліції.","загальнонаціонального антифашистського та антирадянського повстання.")

        q1_forlvl3=Question("""Прочитайте уривок джерела.«Український народ не хоче й не буде своєю кров’ю рятувати Німеччину. Якщо Німеччина стоїть сьогодні перед смертельною небезпекою зі Сходу,то це наслідки дикунської політики німецького імперіалізму серед поневолених народів Сходу...Ми боремося за Українську державу, а не за чужий імперіалізм. Ми мусимо берегти наші сили,бо ми впевнені, що війна у своїй кінцевій фазі надасть нам державу...»Таку позицію у зверненні до українського народу в роки Другої світової війни проголосив""","Провід ОУН (Б).","уряд Української РСР.","очільник рейхскомісаріату «Україна».","керівник Українського штабу партизанського руху.") 
       
                


                
         




        question_list=[qust1,qust2,qust3,qust4,qust5,qust6]
        question_list_lvl2=[quest1_for_lvl2,quest2_for_lvl2,quest3_for_lvl2,quest4_for_lvl2,quest5_for_lvl2,quest6_for_lvl2,quest7_for_lvl2]
        question_list_lvl3=[q1_forlvl3]
        radio_buttons=[rb_ans1,rb_ans2,rb_ans3,rb_ans4]


        new_question()

        start_time=time()
        def click_ok():
            
            
            
            if btn_next.text() == 'Відповісти':
                
                
                new_time=time()
                gb_question.hide()
                gb_answer.show()
                btn_next.setText('Наступне запитання')
                time_bt.setText(str(round(new_time-start_time)))
                tr.right_answers=new_time-start_time
                new_time=0
                
                check_result()

                

            else:
                time_bt.setText("Час:")
                gb_question.show()
                gb_answer.hide()
                btn_next.setText('Відповісти')
                new_question()
                

        def clear_all_inputline():
            quest_edit.clear()
            question_answer_enter.clear()
            question_wrong_answ1_enter.clear()
            question_wrong_answ2_enter.clear()
            question_wrong_answ3_enter.clear()
        def add_new_question():
            new_quest=Question(quest_edit.text(),question_answer_enter.text(),question_wrong_answ1_enter.text(),question_wrong_answ2_enter.text(),question_wrong_answ3_enter.text())
            question_list.append(new_quest)
            return new_quest
            clear_all_inputline()
        def button_clicked():
                dlg = QMessageBox()
                dlg.setStyleSheet("font-weight:600;color:white;background:black;border: 1px solid LightSkyBlue;font:20px;")
                dlg.setWindowTitle("Запитання додано!")
                dlg.setText("Перейдіть в тест щоб переглянути")
                button = dlg.exec()

                button == QMessageBox.StandardButton.Ok

        def lvl2_finished():
                dlg1 = QMessageBox()
                dlg1.setStyleSheet("font-weight:900;color:black;background:yellow ;font:20px;font-family:Brush Script MT, Brush Script Std, cursive;")
                dlg1.setWindowTitle("Повідомлення")
                dlg1.setText("""Вас вітає розумний тест з історії! 🎉 
        Пройдіть три рівні складності та продемонструйте свої знання з історії України, вирішуючи завдання з різних тем.
        Кожне завдання має одну правильну відповідь, тож будьте уважні!✅ 
                Бажаємо успіху та наснаги на шляху до перемоги! 🎯💪""")
                dlg1.exec_()
        def lvl3_finished():
                dlg1 = QMessageBox()
                dlg1.setStyleSheet("font-weight:600;color:black;background:yellow;border: 1px solid LightSkyBlue;font:20px;font-family:Brush Script MT, Brush Script Std, cursive;")
                dlg1.setWindowTitle("Завершення тесту")
                dlg1.setText("Вітаємо із завершенням тесту!Перейдіть в меню щоб побачити свій результат")
                dlg1.exec_() 

                


        btn_next.clicked.connect(click_ok)
        btn_rest.clicked.connect(rest)
        btn_menu.clicked.connect(switch_menu)
        back.clicked.connect(return_to_main)
        clear_all.clicked.connect(clear_all_inputline)
        add_quest.clicked.connect(add_new_question)
        add_quest.clicked.connect(button_clicked)
        lvl2_finished()
        window.show()
beg=begining()
app.exec_()

































