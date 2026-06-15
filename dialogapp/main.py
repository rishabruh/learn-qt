import sys

from PySide6.QtWidgets import (
    QApplication,
    QDial,
    QDialog,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
)


class Form(QDialog):
    def greetings(self):
        print(f"Hello {self.edit.text()}")

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("My Form")

        # add widget content
        self.edit = QLineEdit("Write name here...")
        self.button = QPushButton("Show greeting")

        # layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        self.button.clicked.connect(self.greetings)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()

    sys.exit(app.exec())
