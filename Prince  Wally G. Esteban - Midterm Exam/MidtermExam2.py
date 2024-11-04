import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout

class Button(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Midterm in OOP')
        self.x = 200
        self.y = 200
        self.width = 400
        self.height = 200
        
        self.setGeometry(self.x, self.y, self.width, self.height)

        self.labels = ["Enter your Fullname:"]
        
        
        self.entries = {}

        layout = QVBoxLayout()

        for label in self.labels:
            h_layout = QHBoxLayout()
            lbl = QLabel(label)
            entry = QLineEdit()
            h_layout.addWidget(lbl)
            h_layout.addWidget(entry)
            layout.addLayout(h_layout)
            self.entries[label] = entry

        self.show_button = QPushButton("Click to Display your Fullname",self)
        self.result_entry = QLineEdit()
        self.result_entry.setReadOnly(True)
        self.show_button.setStyleSheet("color: red;")

        h_layout_result = QHBoxLayout()
        h_layout_result.addWidget(self.show_button)
        h_layout_result.addWidget(self.result_entry)
        layout.addLayout(h_layout_result)

        
        self.show_button.clicked.connect(self.display)
        layout.addWidget(self.show_button)

        self.setLayout(layout)


    def display(self):
        fullname = self.entries["Enter your Fullname:"].text()
        self.result_entry.setText(fullname)
        self.result_entry.setStyleSheet("color: red;")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Button()
    ex.show()
    sys.exit(app.exec_())
