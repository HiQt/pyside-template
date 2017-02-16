from PySide.QtGui import QWidget
from ui.AnotherWidget_ui import Ui_Form


class AnotherWidget(QWidget, Ui_Form):
    def __init__(self, *args, **kwargs):
        super(AnotherWidget, self).__init__(*args, **kwargs)

        self.setupUi(self)
