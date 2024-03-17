#для начала скопируй сюда интерфейс "Умных заметок" и проверь его работу

#затем запрограммируй демо-версию функционала
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QInputDialog, QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout, QFormLayout
import json

app = QApplication([])
window = QWidget()
window.resize(900, 600)
window.setWindowTitle('Умные заметки')
notes = []
note = {    
    "Добро пожаловать!":
    {
        "текст": "В этом приложении можно создавать заметки с тегами...",
        "теги": ["умные заметки",
        "инструкция"]
    }   
}

with open ('Data.json', 'w', encoding = 'utf-8') as file:
    json.dump(note, file)



label_note = QLabel("Заметка:")
text_field = QTextEdit()

button1 = QPushButton("Создать заметку")
button2 = QPushButton("Удалить заметку")
button3 = QPushButton("Сохранить заметку")
button4 = QPushButton("Добавить к заметке")
button5 = QPushButton("Открепить от заметки")
button6 = QPushButton("Искать заметку по тегу")

notes_list = QListWidget()

layout_main = QVBoxLayout()
layout_note = QHBoxLayout()

layout_main.addWidget(label_note)
layout_main.addWidget(text_field)

# layout_buttons1 = QHBoxLayout()
# layout_buttons1.addWidget(button1)
# layout_buttons1.addWidget(button2)

layout_buttons2 = QHBoxLayout()
layout_buttons2.addWidget(button3)

notes_label = QLabel('Список заметок')
layout_int = QVBoxLayout()
layout_int.addWidget(notes_label)
layout_int.addWidget(notes_list)

layout_int.addWidget(button1)
layout_int.addWidget(button2)
layout_int.addWidget(button3)


tag_label = QLabel('Список тегов')
tags_list = QListWidget()
layout_int.addWidget(tag_label)
layout_int.addWidget(tags_list)

tag_field = QLineEdit('')
tag_field.setPlaceholderText('Введите тег...')
layout_int.addWidget(tag_field)

layout_int.addWidget(button4)
layout_int.addWidget(button5)
layout_int.addWidget(button6)

layout_note.addLayout(layout_main, stretch = 2)
layout_note.addLayout(layout_int, stretch = 1)
window.setLayout(layout_note)

def show_note():
    note_name = notes_list.selectedItems()[0].text()
    for note in notes:
        if note_name == note[0]:
            text_field.setText(note[1])
            tags_list.clear()
            tags_list.addItems(note[2])

def add_note():
    note_name, result = QInputDialog.getText(window, 'Добавить заметку', 'Название заметки:')
    if result and note_name != '':
        note = list()
        note = [note_name, '', []]
        notes.append(note)
        notes_list.addItem(note[0])
        tags_list.addItems(note[2])
        filename = str(len(notes)-1)+'txt'
        with open(filename, 'w') as file:
            file.write(note[0]+ '\n')

def save_note():
    if notes_list.selectedItems():
        key = notes_list.selectedItems()[0].text()
        i = 0
        for note in notes:
            if note[0] == key:
                note[1] = text_field.toPlainText()
                filename = str(i)+'.txt'
                with open(filename,'w') as file:
                    file.write(note[0] + '\n')
                    file.write(note[1] + '\n') 
                    for tag in note[2]:
                        file.write(tag+' ')
                    file.write('\n')
            i += 1

button1.clicked.connect(add_note)
button3.clicked.connect(save_note)

notes_list.itemClicked.connect(show_note)

window.show()

name = 0
note = []
while True:
    filename = str(name)+'txt'
    try:
        with open (filename, 'w', encoding = 'utf-8') as file:
            for line in file:
                line = line.replace('\n','')
                note.append(line)
            tags = note[2].split()
            note[2] = tags
            notes.append(note)
            note = []
            name += 1
        
    except IOError:
        break
    
for note in notes:
    list_notes.addItem(note[0])

app.exec_()





