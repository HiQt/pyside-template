from PySide import QtGui
from ui.MainWindow_ui import Ui_MainWindow
from dlg_about import DlgAbout
from app_info import APP_INFO


class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setupUi(self)

        self.setWindowTitle(APP_INFO.APP_NAME)
        self.setWindowIcon(QtGui.QIcon(":/icons/icon.ico"))

        self.actionAbout.triggered.connect(self.actionAbout_triggered)
        self.actionAbout_Qt.triggered.connect(self.actionAbout_Qt_triggered)

    def actionAbout_triggered(self):
        QtGui.QMessageBox.about(
            self,
            APP_INFO.APP_NAME,
            """
            <h1>{APP_NAME}</h1>
            <br>
            Author:  {APP_AUTHOR}<br>
            Version: {Major}.{Minor}.{Revision}<br>
            """.format(
                APP_NAME=APP_INFO.APP_NAME,
                APP_AUTHOR=APP_INFO.APP_AUTHOR,
                Major=APP_INFO.APP_VERSION.Major,
                Minor=APP_INFO.APP_VERSION.Minor,
                Revision=APP_INFO.APP_VERSION.Revision
            )
        )

    def actionAbout_Qt_triggered(self):
        QtGui.QMessageBox.aboutQt(self)
