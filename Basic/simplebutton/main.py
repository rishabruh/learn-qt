import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QPushButton


# Greetings
@Slot()
def sayHello():
    print("Button clicked, Hello!")

app = QApplication(sys.argv)
button = QPushButton("Click me")
button.clicked.connect(sayHello)
button.show()
app.exec()