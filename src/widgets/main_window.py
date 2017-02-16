from PySide.QtGui import QMainWindow, QIcon
from ui.MainWindow_ui import Ui_MainWindow
from dlg_about import DlgAbout
from app_info import APP_INFO


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setupUi(self)

        self.setWindowTitle(APP_INFO.APP_NAME)
        self.setWindowIcon(QIcon(":/icons/icon.ico"))

        self.actionAbout.triggered.connect(self.actionAbout_triggered)

    def actionAbout_triggered(self):
        dlg = DlgAbout(self)
        dlg.exec_()
