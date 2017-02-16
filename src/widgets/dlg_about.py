from PySide.QtGui import QDialog
from ui.DlgAbout_ui import Ui_Dialog
from app_info import APP_INFO


class DlgAbout(QDialog, Ui_Dialog):
    def __init__(self, *args, **kwargs):
        super(DlgAbout, self).__init__(*args, **kwargs)

        self.setupUi(self)

        self.label.setText("""
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
        ))
