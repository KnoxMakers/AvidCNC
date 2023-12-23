import os

from probe_basic.probe_basic import ProbeBasic
from qtpyvcp.plugins import getPlugin
from qtpyvcp.widgets.input_widgets.file_system import FileSystemTable
from qtpyvcp.widgets.button_widgets.mdi_button import MDIButton
from qtpyvcp.widgets.button_widgets.subcall_button import SubCallButton
from qtpyvcp.widgets.button_widgets.dialog_button import DialogButton
from PyQt5 import QtCore, QtGui, QtWidgets


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
    def __init__(self, *args, **kwargs):
        super(CustomProbeBasic, self).__init__(*args, **kwargs)

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
        recentfilecombobox_length = len(self.recentfilecombobox_2)
        self.recentfilecombobox_2.removeItem(recentfilecombobox_length-2)
        self.recentfilecombobox_2.removeItem(recentfilecombobox_length-2)

        self.filesystemtable.atDeviceRoot['bool'].connect(self.main_folder_up_button.setDisabled) # type: ignore

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
