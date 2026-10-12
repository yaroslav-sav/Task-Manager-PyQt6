import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, \
    QHBoxLayout, QTextEdit, QRadioButton, QCheckBox, QPushButton

app = QApplication(sys.argv)

window = QMainWindow()
window.resize(800, 600)

window.setWindowTitle("Task Manager")

central = QWidget()
window.setCentralWidget(central)

main_layout = QVBoxLayout(central)

task_name_layout = QHBoxLayout()
text_task_name = QLabel("Task:")
task_name_input = QLineEdit()
task_name_layout.addWidget(text_task_name)
task_name_layout.addWidget(task_name_input)
main_layout.addLayout(task_name_layout)

desc_task_layout = QVBoxLayout()
text_desc_task = QLabel("About:")
task_desc_input = QTextEdit()
desc_task_layout.addWidget(text_desc_task)
desc_task_layout.addWidget(task_desc_input)
main_layout.addLayout(desc_task_layout)

priority_layout = QVBoxLayout()
text_priority = QLabel("Priority:")
radio_layout = QHBoxLayout()
is_low = QRadioButton("Low")
is_medium = QRadioButton("Medium")
is_high = QRadioButton("High")
radio_layout.addWidget(is_low)
radio_layout.addWidget(is_medium)
radio_layout.addWidget(is_high)
priority_layout.addWidget(text_priority)
priority_layout.addLayout(radio_layout)
main_layout.addLayout(priority_layout)

checkBox_layout = QVBoxLayout()
is_important = QCheckBox("Important")
is_notify = QCheckBox("Send notification")
checkBox_layout.addWidget(is_important)
checkBox_layout.addWidget(is_notify)
main_layout.addLayout(checkBox_layout)

create_button = QPushButton("Create task")
main_layout.addWidget(create_button)

status_layout = QHBoxLayout()
text_status = QLabel("Status: ")
status = QLabel("Ready")
status_layout.addWidget(text_status)
status_layout.addWidget(status)
main_layout.addLayout(status_layout)

result_text = QLabel("Result:")
main_layout.addWidget(result_text)
result = QLabel("-")
main_layout.addWidget(result)

clear_button = QPushButton("Clear")
main_layout.addWidget(clear_button)

def create_task():
    name_task = task_name_input.text().strip()
        
    if not name_task:
        result.setText("Нельзя добавить задачу без названия")
        return
        
    desc_task = task_desc_input.toPlainText().strip()
        
    if is_low.isChecked():
        level = "Low"
    elif is_medium.isChecked():
        level = "Medium"
    elif is_high.isChecked():
        level = "High"
    else:
        level = "-"
        
    notify = "Yes" if is_notify.isChecked() else "No" 
    important = "Yes" if is_important.isChecked() else "No"
        
    status.setText("Task created")
        
    result.setText(
        f"Task: {name_task}\n" 
        f"About: {desc_task}\n" 
        f"Level: {level}\n" 
        f"Important: {important}\n" 
        f"Send notification: {notify}"
    )    
        

def clear_task():
    task_name_input.setText("")
    task_desc_input.setText("")
    
    is_low.setChecked(False)
    is_medium.setChecked(False)
    is_high.setChecked(False)
    
    is_important.setChecked(False)
    is_notify.setChecked(False)
    
    status.setText("Ready")
    result.setText("-")
    
    
create_button.clicked.connect(create_task)
clear_button.clicked.connect(clear_task)


window.show()
app.exec()