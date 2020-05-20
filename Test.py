from PySide2.QtWidgets import *
app = QApplication([])
mainWidget = QWidget()


layout = QVBoxLayout()


label = QLabel("Ceci est un QLabel")
button = QPushButton("Ceci est un QPushButton")
date = QDateEdit()
ProgressBar = QProgressBar()


layout.addWidget(label)
layout.addWidget(button)
layout.addWidget(date)
layout.addWidget(ProgressBar)

mainWidget.setLayout(layout)


mainWidget.show()
app.exec_()
