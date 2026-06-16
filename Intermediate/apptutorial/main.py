# This Python file uses the following encoding: utf-8
import sys
import json
import urllib

#from PySide6.QtWidgets import QApplication
from PySide6.QtQuick import QQuickView
from PySide6.QtCore import QStringListModel
from PySide6.QtGui import QGuiApplication


if __name__ == "__main__":
    url = "https://country.io/names.json"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read().decode('utf-8'))

    data_list = list(data.values())
    data_list.sort()

    app = QGuiApplication(sys.argv)
    view = QQuickView()
    view.setResizeMode(QQuickView.ResizeMode.SizeRootObjectToView)

    model = QStringListModel()
    model.setStringList(data_list)
    view.setInitialProperties({"myModel": model})

    view.engine().addImportPath(sys.path[0])
    view.loadFromModule("App", "Main")

    if view.status() == QQuickView.Status.Error:
        sys.exit(-1)
    view.show()

    app.exec()
    del view