
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QButtonGroup, QApplication, QWidget, QLabel, QVBoxLayout, QMessageBox, QRadioButton,QHBoxLayout, QPushButton, QGroupBox)
from random import shuffle, randint
#класс Вопрос
class Question():
    def __init__(
        self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

#создание приложения и главного окна
app = QApplication([])
main_win = QWidget()
main_win.resize(400, 400)
main_win.setWindowTitle('Memory Card')
main_win.total = 0
main_win.score = 0
#надпись
text = QLabel('Вопрос')
#кнопка
btn = QPushButton('Ответить')

#создание группы
RB = QGroupBox('Варианты ответов')
ans_1 = QRadioButton('ответ1')
ans_2 = QRadioButton('ответ2')
ans_3 = QRadioButton('ответ3')
ans_4 = QRadioButton('ответ4')


line_1 = QVBoxLayout()
line_2 = QVBoxLayout()
line_k = QHBoxLayout()
line_1.addWidget(ans_1)
line_1.addWidget(ans_2)
line_2.addWidget(ans_3)
line_2.addWidget(ans_4)
line_k.addLayout(line_1)
line_k.addLayout(line_2)
RB.setLayout(line_k)

line_t = QHBoxLayout()
line_rb = QHBoxLayout()
line_b = QHBoxLayout()

line_t.addWidget(text)
line_rb.addWidget(RB)
line_b.addWidget(btn)

main_line = QVBoxLayout()

main_line.addLayout(line_t)
main_line.addLayout(line_rb)
main_line.addLayout(line_b)



AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('Правильно/Неправильно')
lb_Correct = QLabel('Правильный ответ')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft |  Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter)
AnsGroupBox.setLayout(layout_res)

line_rb.addWidget(AnsGroupBox)

RadioGroup = QButtonGroup()
RadioGroup.addButton(ans_1)
RadioGroup.addButton(ans_2)
RadioGroup.addButton(ans_3)
RadioGroup.addButton(ans_4)

AnsGroupBox.hide()

def show_result():
    RB.hide()
    AnsGroupBox.show()
    btn.setText('Следующий вопрос')

def question_func():
    AnsGroupBox.hide()
    RB.show()
    btn.setText('Ответить')
    RadioGroup.setExclusive(False)
    ans_1.setChecked(False)
    ans_2.setChecked(False)
    ans_3.setChecked(False)
    ans_4.setChecked(False)
    RadioGroup.setExclusive(True)




ans = [ans_1, ans_2, ans_3, ans_4]
def ask(q: Question):
    shuffle(ans)
    ans[0].setText(q.right_answer)
    ans[1].setText(q.wrong1)
    ans[2].setText(q.wrong2)
    ans[3].setText(q.wrong3)
    
    text.setText(q.question)
    lb_Correct.setText(q.right_answer)
    question_func()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def checked_answer():
    if ans[0].isChecked():
        show_correct('Правильно')

    if ans[1].isChecked() or ans[2].isChecked() or ans[3].isChecked():
        show_correct('Неправильно')
    print('Статистика всего вопросов:',main_win.total)
    print('Правильных ответов', main_win.score)
    print('Рейтинг:', round(main_win.score/main_win.total*100, 2))

question_list = []
question_list.append(Question('Госдарственный язык Португалии','Португальский','Английский','Испанский','Французкий'))

question_list.append(Question('Сколько длилась столетняя война','116 лет','100 лет','120 лет','118 лет'))

question_list.append(Question('Кто создал фэйсбук','Марк Цукерберг','Эндрю Босуорт','Дэвид Венер','не знаю'))

question_list.append(Question('','','','',''))



def next_question():
    if len(question_list) > 0:
        main_win.total += 1
        cur_question = randint(0, len(question_list) - 1)
        q = question_list[cur_question]
        ask(q)
        if main_win.total >0:
            question_list.remove(question_list[cur_question])
        
    else:
        print('Тест завершён')
        text.setText('Тест завершен')
        lb_Result.setText('Ваш рейтинг: ' + str(round(main_win.score/main_win.total*100, 2)))
        lb_Correct.setText('Правильных ответов: ' +str( main_win.score) + ' из '+ str(main_win.total))
        btn.hide()

def click_OK():
    if btn.text() == 'Ответить':
        checked_answer()
    else:
        next_question()
    


main_win.cur_question = -1


btn.clicked.connect(click_OK)
next_question()
main_win.setLayout(main_line)
main_win.show()
app.exec_()