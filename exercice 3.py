from PySide2.QtWidgets import *
from  PySide2.QtGui import *

class Window(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        self.setFixedSize(400,300)
        self.setWindowTitle("IHM")
        self.setWindowIcon(QIcon("flag.png"))

        self.layout = QVBoxLayout()

        self.label = QLabel("Hello World!")
        self.label.setAlignment(Qt.AlignCenter)

        self.progressbar = QProgressBar()
        self.progressbar.setValue(50)

        self.edit = QLineEdit()

        self.button1 = QPushButton("Click me!")
        self.button1.setToolTip("Well done!")


        self.layout.addWidget(self.label)
        self.layout.addWidget(self.progressbar)
        self.layout.addWidget(self.edit)
        self.layout.addWidget(self.button1)


        self.setLayout(self.layout)

if __name__ == "__main__":
    app = QApplication([])
    win = Window()
    win.show()
    app.exec_()

