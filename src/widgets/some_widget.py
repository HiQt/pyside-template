from PySide.QtGui import QWidget
from ui.SomeWidget_ui import Ui_Form


class SomeWidget(QWidget, Ui_Form):
    def __init__(self, *args, **kwargs):
        super(SomeWidget, self).__init__(*args, **kwargs)

        self.setupUi(self)
