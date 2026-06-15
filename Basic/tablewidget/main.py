import sys

from PySide6.QtGui import QColor
from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem

# simple data model
colors = [
    ("Red", "#FF0000"),
    ("Green", "#00FF00"),
    ("Blue", "#0000FF"),
    ("Black", "#000000"),
    ("White", "#FFFFFF"),
    ("Electric Green", "#41CD52"),
    ("Dark Blue", "#222840"),
    ("Yellow", "#F9E56d"),
]


def getRGBfromHEX(code):
    codeHEX = code.replace("#", "")
    rgb = tuple(int(codeHEX[i : i + 2], 16) for i in (0, 2, 4))
    return QColor.fromRgb(rgb[0], rgb[1], rgb[2])


app = QApplication()

table = QTableWidget()
table.setRowCount(len(colors))
table.setColumnCount(len(colors[0]) + 1)
table.setHorizontalHeaderLabels(["Name", "Hex Code", "Color"])

for i, (name, code) in enumerate(colors):
    itemName = QTableWidgetItem(name)
    itemCode = QTableWidgetItem(code)
    itemColor = QTableWidgetItem()
    itemColor.setBackground(getRGBfromHEX(code))
    table.setItem(i, 0, itemName)
    table.setItem(i, 1, itemCode)
    table.setItem(i, 2, itemColor)

table.show()
sys.exit(app.exec())
