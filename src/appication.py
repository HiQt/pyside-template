import sys
from PySide import QtGui, QtCore
from widgets.main_window import MainWindow


class _AppData(QtCore.QObject):
    """Simple container for global app state and global Signals"""
    pass


AppData = _AppData()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()

    sys.exit(app.exec_())
