import sys
from pathlib import Path

from PySide6.QtGui import QGuiApplication
from PySide6.QtQuick import QQuickView

if __name__ == "__main__":
    app = QGuiApplication()
    view = QQuickView()
    view.engine().addImportPath(str(Path(__file__).resolve().parent.parent))
    view.loadFromModule("App", "Main")
    view.setResizeMode(QQuickView.ResizeMode.SizeRootObjectToView)
    view.show()
    ex = app.exec()
    del view
    sys.exit(ex)
