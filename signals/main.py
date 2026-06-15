import sys
from pydoc import text

from PySide6.QtWidgets import QApplication, QLineEdit, QPushButton, QToolButton


def function():
    print("The function has been called.")


app = QApplication()
button = QPushButton("Call function")
button.clicked.connect(function)
button.show()

button2 = QToolButton()
textbox = QLineEdit()
button2.clicked.connect(textbox.clear)
button2.show()

sys.exit(app.exec())
