import os
import sys

from probe_basic.probe_basic import ProbeBasic
from qtpyvcp.plugins import getPlugin
from qtpyvcp.widgets.input_widgets.file_system import FileSystemTable
from qtpyvcp.widgets.button_widgets.mdi_button import MDIButton
from qtpyvcp.widgets.button_widgets.subcall_button import SubCallButton
from qtpyvcp.widgets.button_widgets.dialog_button import DialogButton
from qtpyvcp.widgets.input_widgets.setting_slider import VCPSettingsLineEdit, VCPSettingsPushButton, VCPSettingsSlider
from qtpyvcp.widgets.hal_widgets.hal_led import HalLedIndicator
from PyQt5 import QtCore, QtGui, QtWidgets
from linuxcnc import ini


class CustomProbeBasic(ProbeBasic):
    """Main window class for the ProbeBasic VCP.


    save this file as `custom_probebasic.py` in you config directory
    then your custom_config.yml add the `provider:` line below to the `mainwidow: section`

    ```
    windows:
      mainwindow:
        provider: custom_probebasic:CustomProbeBasic
    ```       

    """

    INI_FILE = os.environ.get("INI_FILE_NAME")
    CONFIG_DIR = os.environ.get('CONFIG_DIR')

    def __init__(self, *args, **kwargs):
        super(CustomProbeBasic, self).__init__(*args, **kwargs)
        _translate = QtCore.QCoreApplication.translate

        if self.INI_FILE is None:
            self.INI_FILE = ini_file or '/dev/null'
            os.environ['INI_FILE_NAME'] = self.INI_FILE

        if self.CONFIG_DIR is None:
            self.CONFIG_DIR = os.path.dirname(self.INI_FILE)
            os.environ['CONFIG_DIR'] = self.CONFIG_DIR

        self.ini = ini(self.INI_FILE)
        self.pin = self.ini.find('DISPLAY', 'PIN') or "1234"

        # rename the Flood button
        self.flood_button.setText("Vaccum")

        # rename the Mist button
        self.mist_button.setText("Air Blast")

        # rename REF AlL to HOME ALL buttons, for each axis config

        # since `VCPBaseWidget.rules` is a `str` and converts it to json only when need
        # we can just use str.replace

        # XYZAB
        self.ref_all_button.setText("HOME ALL")
        self.ref_all_button.rules = self.ref_all_button.rules.replace("REF ALL", "HOME ALL")

        # XYZA
        self.ref_all_button_5.setText("HOME ALL")
        self.ref_all_button_5.rules = self.ref_all_button_5.rules.replace("REF ALL", "HOME ALL")

        # XYZ
        self.ref_all_button_4.setText("HOME ALL")
        self.ref_all_button_4.rules = self.ref_all_button_4.rules.replace("REF ALL", "HOME ALL")

        self.axisactionbutton.setText("HOME Z")
        self.axisactionbutton_2.setText("HOME A")
        self.axisactionbutton_3.setText("HOME Y")
        self.axisactionbutton_4.setText("HOME B")
        self.axisactionbutton_5.setText("HOME Y")
        self.axisactionbutton_6.setText("HOME X")
        self.axisactionbutton_7.setText("HOME Z")
        self.axisactionbutton_8.setText("HOME A")
        self.axisactionbutton_9.setText("HOME X")
        self.axisactionbutton_10.setText("HOME Y")
        self.axisactionbutton_11.setText("HOME Z")
        self.axisactionbutton_12.setText("UN HOME X")
        self.axisactionbutton_13.setText("HOME X")
        self.axisactionbutton_14.setText("UN HOME Z")
        self.axisactionbutton_15.setText("UN HOME Y")
        self.ref_all_button_2.setText("UN HOME ALL")
        self.statuslabel_22.setText("HOME")
        self.statuslabel_22.setMaximumSize(43,17)
        self.statuslabel_22.setMinimumSize(43,17)

        self.facingwidget.label_172.setText("Vacuum / Air")
        self.facingwidget.coolant_input.removeItem(2)
        self.facingwidget.coolant_input.removeItem(1)
        self.facingwidget.coolant_input.addItem('VACUUM')
        self.facingwidget.coolant_input.addItem('AIR BLAST')
        self.facingwidget.coolant_input.addItem('BOTH')

        self.xycoordwidget.label_172.setText("Vacuum / Air")
        self.xycoordwidget.coolant_input.removeItem(2)
        self.xycoordwidget.coolant_input.removeItem(1)
        self.xycoordwidget.coolant_input.addItem('VACUUM')
        self.xycoordwidget.coolant_input.addItem('AIR BLAST')
        self.xycoordwidget.coolant_input.addItem('BOTH')

        self.holecirclewidget.label_172.setText("Vacuum / Air")
        self.holecirclewidget.coolant_input.removeItem(2)
        self.holecirclewidget.coolant_input.removeItem(1)
        self.holecirclewidget.coolant_input.addItem('VACUUM')
        self.holecirclewidget.coolant_input.addItem('AIR BLAST')
        self.holecirclewidget.coolant_input.addItem('BOTH')

        _file_locations = getPlugin('file_locations')
        _file_locations.local_locations.pop("Home")
        _file_locations.local_locations.pop("Desktop")
        _file_locations.local_locations.pop("NC Files")

        self.removabledevicecombobox.onRemovableDevicesChanged(_file_locations.removable_devices.value)
        recentfilecombobox_2_length = len(self.recentfilecombobox_2)
        self.recentfilecombobox_2.removeItem(recentfilecombobox_2_length-2)
        self.recentfilecombobox_2.removeItem(recentfilecombobox_2_length-2)

        recentfilecombobox_length = len(self.recentfilecombobox)
        self.recentfilecombobox.removeItem(recentfilecombobox_length-2)
        self.recentfilecombobox.removeItem(recentfilecombobox_length-2)


        self.operation.setTabVisible(2,False)
        self.operation.setTabVisible(3,False)
        self.operation.setTabVisible(4,False)
        self.tabWidget_3.setTabVisible(2,False)

        self.frame_17.setMinimumSize(QtCore.QSize(250, 300))
        self.frame_17.setMaximumSize(QtCore.QSize(250, 300))
        self.frame_17.setGeometry(QtCore.QRect(320, 80, 250, 300))

        self.frame_18.setGeometry(QtCore.QRect(320, 385, 250, 150))

        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setContentsMargins(2,2,2,2)
        self.horizontalLayout_19.setSpacing(6)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.verticalLayout_49.insertLayout(4, self.horizontalLayout_19, 0)


        self.tool_rack_button = SubCallButton(None, filename="store_tool_in_rack.ngc")
        self.tool_rack_button.setText("Store Tool in Rack")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tool_rack_button.sizePolicy().hasHeightForWidth())
        self.tool_rack_button.setSizePolicy(sizePolicy)
        self.tool_rack_button.setMinimumSize(QtCore.QSize(120, 45))
        self.tool_rack_button.setMaximumSize(QtCore.QSize(16777215, 45))
        self.tool_rack_button.setMouseTracking(True)
        self.tool_rack_button.setTabletTracking(False)
        self.tool_rack_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tool_rack_button.setObjectName("tool_rack_button")
        self.tool_rack_button.setStyleSheet("QPushButton {\n"
"    font-family: \"Bebas Kai\";\n"
"    font-size: 16pt;\n"
"}\n")
        self.horizontalLayout_19.addWidget(self.tool_rack_button)

        self.dialogbutton = DialogButton(self.frame_26)
        self.dialogbutton.setText("Shutdown System")
        self.dialogbutton.setProperty("dialogName", "shutdown")
        self.dialogbutton.setMinimumSize(QtCore.QSize(0, 40))
        self.dialogbutton.setObjectName("dialogbutton")
        self.verticalLayout_32.addWidget(self.dialogbutton)

        self.verticalLayout_32.setSpacing(11)
        self.verticalLayout_32.setContentsMargins(9,6,9,6)

        self.verticalLayout_50.setSpacing(11)

        self.mdi_entry_box_4.hide()

        self.lockScreen(self)

        self.unlock_frame = QtWidgets.QFrame(self.settings_tab)
        self.unlock_frame.setGeometry(1110, 550, 501, 80)

        self.unlock_layout = QtWidgets.QHBoxLayout(self.unlock_frame)
        self.unlock_layout.setContentsMargins(10,1,0,1)
        self.unlock_layout.setSpacing(12)
        self.unlock_layout.setObjectName("unlock_layout")

        # Create the UNLOCK button and connect it to the show_pin_dialog method
        self.unlock_button = QtWidgets.QPushButton("UNLOCK", self.unlock_frame)
        self.unlock_layout.addWidget(self.unlock_button)
        self.unlock_button.setMinimumSize(80, 40)  # Set the minimum size

        self.unlock_line_edit_number = VCPSettingsLineEdit(self.unlock_frame)
        self.unlock_line_edit_number.setObjectName("unlock_line_edit_number")
        self.unlock_line_edit_number.setMinimumHeight(31)  # Set the minimum height
        self.unlock_line_edit_number.setMaximumWidth(80)  # Set the maximum width
        self.unlock_layout.addWidget(self.unlock_line_edit_number)
        self.unlock_line_edit_number.setProperty("textFormat", _translate("Form", "{:.0f}"))
        self.unlock_line_edit_number.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.unlock_line_edit_number.setText("0000")

        self.status_led_frame = QtWidgets.QFrame(self.main_override_tool_qframe)
        self.status_led_layout = QtWidgets.QHBoxLayout(self.status_led_frame)

        self.status_led_layout.setContentsMargins(4,4,4,4)
        self.status_led_layout.setSpacing(4)
        self.status_led_frame.setGeometry(QtCore.QRect(22, 15, 393, 40))

        self.main_override_tool_qframe.setMaximumHeight(340)
        self.main_override_tool_qframe.setMinimumHeight(340)
        self.main_override_tool_qframe.setStyleSheet(".QFrame{\npadding-top:55px;\n padding-bottom:15px;\n    padding-left: 8px;\n    padding-right: 8px;\n    border-left-width: 1px;\n    border-right-width:1px;\n}")

        self.status_led_frame.setStyleSheet(".QFrame{\n    border-style: solid;\n    border-color: rgb(176, 179,172);\n    border-width: 1px;\n    border-radius: 4px;\n    background-color: rgb(90, 90, 90);\n    padding: -5px;\n}")
        self.status_spacer_item = QtWidgets.QSpacerItem(15, 20, 20, 20)
        self.status_led_layout.addItem(self.status_spacer_item)

        self.air_psi_led = HalLedIndicator(self.status_led_frame)
        self.status_led_layout.addWidget(self.air_psi_led)
        self.air_psi_led.setSizePolicy(sizePolicy)
        self.air_psi_led.setDiameter(25)
        self.air_psi_led.setMaximumWidth(25)
        self.air_psi_led.setColor(QtGui.QColor(44, 41, 255))
        self.air_psi_led.setState(False)
        self.air_psi_led.setObjectName("air_psi_led")
        self.air_psi_led.setProperty("pinBaseName", _translate("Form", "air-ps-led"))

        self.air_psi_label = QtWidgets.QLabel(self.status_led_frame)
        self.status_led_layout.addWidget(self.air_psi_label)
        self.air_psi_label.setText("Air PSI")
        self.air_psi_label.setStyleSheet("QLabel{\npadding-left:2px;    color: rgb(238, 238, 236);\n	font: 16pt \"Bebas Kai\";\n}")
        self.air_psi_label.setMaximumWidth(80)

        self.status_spacer_item2 = QtWidgets.QSpacerItem(25, 20, 20, 20)
        self.status_led_layout.addItem(self.status_spacer_item2)

        self.drawbar_led = HalLedIndicator(self.status_led_frame)
        self.status_led_layout.addWidget(self.drawbar_led)
        self.drawbar_led.setSizePolicy(sizePolicy)
        self.drawbar_led.setDiameter(25)
        self.drawbar_led.setMaximumWidth(25)
        self.drawbar_led.setColor(QtGui.QColor(44, 41, 255))
        self.drawbar_led.setState(False)
        self.drawbar_led.setObjectName("drawbar_led")
        self.drawbar_led.setProperty("pinBaseName", _translate("Form", "drawbar-led"))

        self.drawbar_label = QtWidgets.QLabel(self.status_led_frame)
        self.status_led_layout.addWidget(self.drawbar_label)
        self.drawbar_label.setText("Draw Bar")
        self.drawbar_label.setStyleSheet("QLabel{\npadding-left:2px;    color: rgb(238, 238, 236);\n	font: 16pt \"Bebas Kai\";\n}")
        self.drawbar_label.setMaximumWidth(80)

        self.status_spacer_item3 = QtWidgets.QSpacerItem(25, 20, 20, 20)
        self.status_led_layout.addItem(self.status_spacer_item3)

        self.case_air_led = HalLedIndicator(self.status_led_frame)
        self.status_led_layout.addWidget(self.case_air_led)
        self.case_air_led.setSizePolicy(sizePolicy)
        self.case_air_led.setDiameter(25)
        self.case_air_led.setMaximumWidth(25)
        self.case_air_led.setColor(QtGui.QColor(44, 41, 255))
        self.case_air_led.setState(False)
        self.case_air_led.setObjectName("case_air_led")
        self.case_air_led.setProperty("pinBaseName", _translate("Form", "case-air-led"))

        self.case_air_label = QtWidgets.QLabel(self.status_led_frame)
        self.status_led_layout.addWidget(self.case_air_label)
        self.case_air_label.setText("Spindle Purge")
        self.case_air_label.setStyleSheet("QLabel{\npadding-left:2px;    color: rgb(238, 238, 236);\n	font: 16pt \"Bebas Kai\";\n}")
        self.case_air_label.setMaximumWidth(120)

        self.status_spacer_item4 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.status_led_layout.addItem(self.status_spacer_item4)

        self.run_from_line_Num.setFocusPolicy(QtCore.Qt.ClickFocus)

        self.spacer_item = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.unlock_layout.addItem(self.spacer_item)

        self.unlock_button.clicked.connect(self.unlock_button_clicked)

        self.main_load_gcode_button.setMinimumWidth(110)
        self.main_load_gcode_button.setMaximumWidth(110)
        self.main_load_gcode_button.setEnabled(False)

        self.filesystemtable.gcodeFileSelected['bool'].connect(lambda x: self.main_load_gcode_button.setEnabled(True))

        self.filesystemtable.rootChanged.connect(lambda: self.main_folder_up_button.setEnabled(False) 
           if self.filesystemtable.model.rootPath().lower() == '/home/avidcnc/linuxcnc/nc_files/users'
           else self.main_folder_up_button.setEnabled(True))
        self.filesystemtable.gcodeFileSelected['bool'].connect(lambda x: (
           self.main_load_gcode_button.setText("SELECT FOLDER") if not x else None,
           self.main_load_gcode_button.setText("LOAD G-CODE") if x else None
        ))

        self.main_load_gcode_button.clicked.connect(lambda: ( 
            self.main_load_gcode_button.setText("LOAD G-CODE") if self.main_load_gcode_button.text() == 'SELECT FOLDER' else None
        ))

        self.recentfilecombobox.model().rowsInserted.connect(self.remove_browse_option)
        self.recentfilecombobox_2.model().rowsInserted.connect(self.remove_browse_option)

        self.filesystemtable.model.rootPathChanged.connect(lambda: (
            self.filesystemtable.clearSelection(),
            self.main_load_gcode_button.setEnabled(False)
        ))

    def remove_browse_option(self):
        for index in range(self.recentfilecombobox.count()):
            if self.recentfilecombobox.itemText(index) == 'Browse for files ...':
                recentfilecombobox_length = len(self.recentfilecombobox)
                self.recentfilecombobox.removeItem(recentfilecombobox_length - 2)
                self.recentfilecombobox.removeItem(recentfilecombobox_length - 2)
                break

        for index in range(self.recentfilecombobox_2.count()):
            if self.recentfilecombobox_2.itemText(index) == 'Browse for files ...':
                recentfilecombobox_2_length = len(self.recentfilecombobox_2)
                self.recentfilecombobox_2.removeItem(recentfilecombobox_2_length - 2)
                self.recentfilecombobox_2.removeItem(recentfilecombobox_2_length - 2)
                break

    def unlock_button_clicked(self):
        # Check the value of unlock_line_edit_number
        input_text = self.unlock_line_edit_number.text()

        if self.unlock_button.text() == "UNLOCK" and input_text == self.pin:
            # Unlock functionality
            self.unlockScreen()
            # Change button label to "Lock"
            self.unlock_button.setText("LOCK")
            self.unlock_line_edit_number.setText("0000")
            self.unlock_line_edit_number.hide()
        elif self.unlock_button.text() == "LOCK":
            # Lock functionality
            self.lockScreen()
            # Change button label back to "Unlock"
            self.unlock_button.setText("UNLOCK")
            self.unlock_line_edit_number.show()
        else:
            # Display error message
            QtWidgets.QMessageBox.warning(self, "Error", "Incorrect code entered. Please try again.")

    def lockScreen(self, *args, **kwargs):
        # hide the usb frame
        self.frame_35.hide()

        # hide the copy to usb button in file dialog
        self.copy_to_usb_2.hide()

        # hide the tool setter screen
        for child in self.widget_38.findChildren(QtWidgets.QWidget):
            child.hide()

        self.probe_tool_number.setDisabled(True)
        self.probe_tool_number.setStyleSheet("background-color: rgb(192, 192, 192);")
        self.probe_fast_fr.setDisabled(True)
        self.probe_fast_fr.setStyleSheet("background-color: rgb(192, 192, 192);")
        self.probe_slow_fr.setDisabled(True)
        self.probe_slow_fr.setStyleSheet("background-color: rgb(192, 192, 192);")

    def unlockScreen(self, *args, **kwargs):
        # hide the usb frame
        self.frame_35.show()

        # hide the copy to usb button in file dialog
        self.copy_to_usb_2.show()

        # hide the tool setter screen
        for child in self.widget_38.findChildren(QtWidgets.QWidget):
            child.show()

        self.probe_tool_number.setDisabled(False)
        self.probe_tool_number.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.probe_fast_fr.setDisabled(False)
        self.probe_fast_fr.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.probe_slow_fr.setDisabled(False)
        self.probe_slow_fr.setStyleSheet("background-color: rgb(255, 255, 255);")
