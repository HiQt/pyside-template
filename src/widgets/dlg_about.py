from PySide.QtGui import QDialog
from ui.DlgAbout import Ui_Dialog
from app_info import APP_INFO


class DlgAbout(QDialog, Ui_Dialog):
    def __init__(self, *args, **kwargs):
        super(DlgAbout, self).__init__(*args, **kwargs)

        self.setupUi(self)

        self.label.setText("""
        <h1>{APP_NAME}</h1>
        <br>
        Author:  {APP_AUTHOR}<br>
        Version: {MAJOR}.{MINOR}.{REVISION}<br>
        """.format(
            APP_NAME=APP_INFO.APP_NAME,
            APP_AUTHOR=APP_INFO.APP_AUTHOR,
            MAJOR=APP_INFO.APP_VERSION.MAJOR,
            MINOR=APP_INFO.APP_VERSION.MINOR,
            REVISION=APP_INFO.APP_VERSION.REVISION
        ))
