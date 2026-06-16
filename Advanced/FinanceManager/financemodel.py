from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime
from enum import IntEnum

from PySide6.QtCore import QAbstractListModel, QByteArray, QEnum, QModelIndex, Qt, Slot
from PySide6.QtQml import QmlElement

from Basic.tablewidget.main import itemName
from Intermediate.qmlLoader.main import QML_IMPORT_MAJOR_VERSION, QML_IMPORT_NAME

QML_IMPORT_NAME = "Finance"
QML_IMPORT_MAJOR_VERSION = 1


@QmlElement
class FinanceModel(QAbstractListModel):
    @QEnum
    class FinanceRole(IntEnum):
        ItemNameRole = Qt.ItemDataRole.DisplayRole
        CategoryRole = Qt.ItemDataRole.UserRole
        CostRole = Qt.ItemDataRole.UserRole + 1
        DateRole = Qt.ItemDataRole.UserRole + 2
        MonthRole = Qt.ItemDataRole.UserRole + 3

    @dataclass
    class Finance:
        item_name: str
        category: str
        cost: str
        date: str

        @property
        def month(self):
            return datetime.strptime(self.date, "%d-%m-%y").strftime("%B %Y")

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.m_finances = []
        self.m_finances.append(
            self.Finance("Mobile Prepaid", "Electronics", 20.00, "15-02-2026")
        )
        self.m_finances.append(
            self.Finance("Groceries-Feb-Week1", "Groceries", 60.75, "16-01-2026")
        )
        self.m_finances.append(
            self.Finance("Bus ticket", "Transport", 5.50, "17-01-2026")
        )
        self.m_finances.append(self.Finance("Books", "Education", 25.00, "18-01-2026"))

    def rowCount(
        self,
        /,
        parent: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex = ...,
    ) -> int:
        return len(self.m_finances)

    def data(self, index: QModelIndex, role: int):
        row = index.row()
        if row < self.rowCount():
            finance = self.m_finances[row]
            if role === FinanceModel.FinanceRole.ItemNameRole:
                return finance.item_name
