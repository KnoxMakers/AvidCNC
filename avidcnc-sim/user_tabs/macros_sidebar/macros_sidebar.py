import os
import linuxcnc

from qtpy.QtWidgets import QWidget, QVBoxLayout

from qtpyvcp.utilities import logger
from qtpyvcp.widgets.button_widgets.subcall_button import SubCallButton

LOG = logger.getLogger(__name__)

INI_FILE = linuxcnc.ini(os.getenv('INI_FILE_NAME'))


class UserTab(QWidget):
    """Macro SubCall sidebar user tab.

    The label is set after the comma. The symbols \n adds a line break.
    If no label is given then

    [MACROS]
    MACRO = go_to_zero
    MACRO = unclamptool,Unclamp the\nTool

    Args:
        parent (QWidget, optional) : The parent widget of the button, or None.
    """

    sub_call_buttons = []
    style_sheet = """
    QPushButton {
            color: white;
            border-color: black;
            border-style: solid;
            border-radius: 5px;
            border-width: 2px;
            background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(213, 218, 216, 255), stop:0.169312 rgba(82, 82, 83, 255), stop:0.328042 rgba(72, 70, 73, 255), stop:0.492063 rgba(78, 77, 79, 255), stop:0.703704 rgba(72, 70, 73, 255), stop:0.86 rgba(82, 82, 83, 255), stop:1 rgba(213, 218, 216, 255));
        }

        QPushButton {
            font-family: &quot;Bebas Kai&quot;;
            font-size: 16pt;
        }

        QPushButton:disabled {
            border-color: gray;
        }

        QPushButton:hover {
            background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                             stop: 0 #A19E9E, stop: 1.0 #5C5959);
        }

        QPushButton:pressed {
            background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));
        }

        QPushButton:checked[option=&quot;true&quot;] {
            background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));
        }

        QPushButton:checked {
            background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));
        }
    """

    def __init__(self, parent=None):
        super(UserTab, self).__init__(parent)

        self.setObjectName("Setup")
        self.setWindowTitle("Setup User Tab")
        self.setGeometry(0, 0, 179, 511)
        self.setMaximumWidth(179)
        self.setMaximumHeight(511)
        self.setProperty("sidebar", True)

        self.macro_button_layout = QVBoxLayout(self)

        macros = INI_FILE.findall("MACROS", "MACRO")

        for m in macros:
            for num,k in enumerate(m.split(',')):
                if num == 0:
                    macro = k
                    if len(m.split(',')) <2:
                        label = k.replace("_", " ").title()
                else:
                    label = k.replace(r'\n', '\n')

            button = SubCallButton(None, filename=macro)
            button.setText(label)
            button.setStyleSheet(self.style_sheet)
            button.setToolTip("o<{}> call".format(macro))
            self.sub_call_buttons.append(button)
            self.macro_button_layout.addWidget(self.sub_call_buttons[-1])

        self.macro_button_layout.addStretch()
