import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel

if __name__ == "__main__":
    app = QApplication()
    w = QLabel("This is placeholder text")
    w.setAlignment(Qt.AlignCenter)  # pyright: ignore[reportAttributeAccessIssue]
    w.setStyleSheet("""
        background-color: #262626;
        color: #ffffff;
        font-family: Titillium;
        font-size: 18px;
        """)
    w.show()
    sys.exit(app.exec())
