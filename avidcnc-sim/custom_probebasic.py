import os

from probe_basic.probe_basic import ProbeBasic
from qtpyvcp.plugins import getPlugin
#from qtpy.QtWidgets import QTableView
from qtpyvcp.widgets.input_widgets.file_system import FileSystemTable

#class TableType(object):
#    Local = 0
#    Remote = 1

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

#    def custom_showEvent(self, event=None):
#        root_path = self.model.rootPath()
#        #self.rootChanged.emit(root_path)
#        isroot = os.path.ismount(root_path)
#        islink = False
#        if root_path == '/home/avidcnc/linuxcnc/nc_files/USERS':
#          islink = True
#        print('ROOT:')
#        print(root_path)
#        print(islink)
#        self.atDeviceRoot.emit(isroot or islink)

#    def custom_onRootPathChanged(self, path):
#        #self.atDeviceRoot.emit(os.path.ismount(path))
#        isroot = os.path.ismount(path)
#        islink = False
#        if path == '/home/avidcnc/linuxcnc/nc_files/USERS':
#          islink = True
#        print('CHANGED:')
#        print(path)
#        print(islink)
#        self.atDeviceRoot.emit(isroot or islink)



