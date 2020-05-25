from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QTabWidget,
    QGridLayout,
    QCheckBox,
    QGroupBox,
    QLabel,
    QPushButton,
    QRadioButton,
    QMessageBox,
    QLineEdit,
    QFileDialog,
    QListWidget,
    QListWidgetItem,
    QSpinBox,
    QDesktopWidget,
    QDialogButtonBox,
    QDialog,
)
from PyQt5 import QtCore
import string
import keyboard
import sys
import Style.windows as windows
from utils import start_thirdparty, hotkey_delete_request
import ressources
import win32gui
from time import sleep
from Settings import Settings
from Listener import Listener
from kthread import KThread


class MainWindow(QMainWindow):
    def __init__(self, settings, listener):
        super().__init__()
        self.settings = settings
        self.listener = listener
        self.setWindowTitle('Eule.py')
        self.table_widget = TableWidget(self)
        self.setCentralWidget(self.table_widget)
        self.locate_to_center()

        self.status_thread = KThread(target=self.set_status)
        self.status_thread.start()

    def locate_to_center(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

    def set_status(self):
        while True:
            self.table_widget.main_page_tab.diablo_hooked.setChecked(
                win32gui.FindWindow('D3 Main Window Class', 'Diablo III')
            )
            sleep(1)

    def closeEvent(self, event):
        self.settings.save()
        self.listener.thread.terminate()
        self.listener.image_recognition_thread.terminate()
        self.status_thread.terminate()
        sys.stdout = sys.__stdout__
        super().closeEvent(event)


class TableWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.settings = parent.settings
        self.listener = parent.listener
        self.layout = QGridLayout(self)

        self.tabs = QTabWidget()
        self.main_page_tab = MainPage(parent)
        self.hotkey_tab = HotkeyTab(parent)
        self.abbrevation_tab = AbbrevationTab(parent)
        self.settings_tab = SettingsTab(parent)

        self.tabs.addTab(self.main_page_tab, 'Main Page')
        self.tabs.addTab(self.hotkey_tab, 'Hotkeys')
        self.tabs.addTab(self.abbrevation_tab, 'Abbrevations')
        self.tabs.addTab(self.settings_tab, 'Settings')

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)


class MainPage(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self)
        self.layout = QGridLayout(self)
        self.settings = parent.settings
        self.listener = parent.listener

        self.image = QLabel(self)
        # Add the image
        self.layout.addWidget(self.image, 0, 0, 1, 0)

        self.diablo_hooked = QCheckBox(self)
        self.diablo_hooked.setText('Diablo hooked')
        self.diablo_hooked.setDisabled(True)
        self.layout.addWidget(self.diablo_hooked, 1, 0)

        self.eule_paused = QCheckBox(self)
        self.eule_paused.setText('Eule paused')
        self.eule_paused.setDisabled(True)
        self.layout.addWidget(self.eule_paused, 1, 1)
        # Add to Listener, so he can change
        self.listener.gui_paused = self.eule_paused

        button = QPushButton(self)
        button.setText('Start Third Party')
        button.clicked.connect(lambda: start_thirdparty(self.settings.paths))
        self.layout.addWidget(button, 1, 2)

        label = QLabel(self)
        label.setText(
            '<a href="https://github.com/VocalTrance/Eule.py">Github / Help</a>'
        )
        label.setOpenExternalLinks(True)
        self.layout.addWidget(label, 1, 3, QtCore.Qt.AlignRight)

        self.setLayout(self.layout)


class HotkeyTab(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.layout = QGridLayout(self)
        self.settings = parent.settings
        self.listener = parent.listener

        self.buttons = {}

        general = QGroupBox(self)
        general_layout = QGridLayout(general)
        general.setTitle('General')
        self.layout.addWidget(general, 0, 0)

        ###################################

        label = QLabel(general)
        label.setText('Spam Right Click')
        general_layout.addWidget(label, 0, 0)

        button = QPushButton(general)
        self.buttons['right_click'] = button
        button.setText(self.settings.hotkeys['right_click'])
        button.clicked.connect(lambda: self.set_hotkey('right_click'))
        general_layout.addWidget(button, 0, 1)

        label = QLabel(general)
        label.setText('Spam Left Click')
        general_layout.addWidget(label, 1, 0)

        button = QPushButton(general)
        self.buttons['left_click'] = button
        button.setText(self.settings.hotkeys['left_click'])
        button.clicked.connect(lambda: self.set_hotkey('left_click'))
        general_layout.addWidget(button, 1, 1)

        label = QLabel(general)
        label.setText('Normalize Difficulty')
        general_layout.addWidget(label, 2, 0)

        button = QPushButton(general)
        self.buttons['lower_difficulty'] = button
        button.setText(self.settings.hotkeys['lower_difficulty'])
        button.clicked.connect(lambda: self.set_hotkey('lower_difficulty'))
        general_layout.addWidget(button, 2, 1)

        label = QLabel(general)
        label.setText('Swap Armor')
        general_layout.addWidget(label, 3, 0)

        button = QPushButton(general)
        self.buttons['swap_armor'] = button
        button.setText(self.settings.hotkeys['swap_armor'])
        button.clicked.connect(lambda: self.set_hotkey('swap_armor'))
        general_layout.addWidget(button, 3, 1)

        radio = QRadioButton(general)
        radio.setText('Cains')
        radio.clicked.connect(lambda: self.radio_clicked('cains'))
        radio.setChecked(self.settings.special['armor_swap_amount'] == 3)
        general_layout.addWidget(radio, 4, 0)

        radio = QRadioButton(general)
        radio.setText('Bounty DH')
        radio.clicked.connect(lambda: self.radio_clicked('bounty_dh'))
        radio.setChecked(self.settings.special['armor_swap_amount'] == 2)
        general_layout.addWidget(radio, 4, 1)

        label = QLabel(general)
        label.setText('Pause Eule')
        general_layout.addWidget(label, 5, 0)

        button = QPushButton(general)
        self.buttons['pause'] = button
        button.setText(self.settings.hotkeys['pause'])
        button.clicked.connect(lambda: self.set_hotkey('pause'))
        general_layout.addWidget(button, 5, 1)

        porting = QGroupBox(self)
        porting_layout = QGridLayout(porting)
        porting.setTitle('Porting')
        self.layout.addWidget(porting, 1, 0, -1, 1)

        ######################

        label = QLabel(porting)
        label.setText('Port to A1 Town')
        porting_layout.addWidget(label, 0, 0)

        button = QPushButton(porting)
        self.buttons['port_a1'] = button
        button.setText(self.settings.hotkeys['port_a1'])
        button.clicked.connect(lambda: self.set_hotkey('port_a1'))
        porting_layout.addWidget(button, 0, 1)

        label = QLabel(porting)
        label.setText('Port to A2 Town')
        porting_layout.addWidget(label, 1, 0)

        button = QPushButton(porting)
        self.buttons['port_a2'] = button
        button.setText(self.settings.hotkeys['port_a2'])
        button.clicked.connect(lambda: self.set_hotkey('port_a2'))

        porting_layout.addWidget(button, 1, 1)

        label = QLabel(porting)
        label.setText('Port to A3 / A4 Town')
        porting_layout.addWidget(label, 2, 0)

        button = QPushButton(porting)
        self.buttons['port_a3'] = button

        button.setText(self.settings.hotkeys['port_a3'])
        button.clicked.connect(lambda: self.set_hotkey('port_a3'))

        porting_layout.addWidget(button, 2, 1)

        label = QLabel(porting)
        label.setText('Port to A5 Town')
        porting_layout.addWidget(label, 3, 0)

        button = QPushButton(porting)
        self.buttons['port_a5'] = button
        button.setText(self.settings.hotkeys['port_a5'])
        button.clicked.connect(lambda: self.set_hotkey('port_a5'))
        porting_layout.addWidget(button, 3, 1)

        label = QLabel(porting)
        label.setText('Port to Pool')
        porting_layout.addWidget(label, 4, 0)

        button = QPushButton(porting)
        self.buttons['port_pool'] = button
        button.setText(self.settings.hotkeys['port_pool'])
        button.clicked.connect(lambda: self.set_hotkey('port_pool'))
        porting_layout.addWidget(button, 4, 1)

        greater_rift = QGroupBox(self)
        greater_rift_layout = QGridLayout(greater_rift)
        greater_rift.setTitle('Greater Rift')
        self.layout.addWidget(greater_rift, 0, 1)

        ####################

        label = QLabel(greater_rift)
        label.setText('Open Grift')
        greater_rift_layout.addWidget(label, 0, 0)

        button = QPushButton(greater_rift)
        self.buttons['open_gr'] = button

        button.setText(self.settings.hotkeys['open_gr'])
        button.clicked.connect(lambda: self.set_hotkey('open_gr'))
        greater_rift_layout.addWidget(button, 0, 1)

        label = QLabel(greater_rift)
        label.setText('Upgrade Gem')
        greater_rift_layout.addWidget(label, 1, 0)

        button = QPushButton(greater_rift)
        self.buttons['upgrade_gem'] = button
        button.setText(self.settings.hotkeys['upgrade_gem'])
        button.clicked.connect(lambda: self.set_hotkey('upgrade_gem'))
        greater_rift_layout.addWidget(button, 1, 1)

        checkbox = QCheckBox(greater_rift)
        checkbox.setText('Empowered')
        checkbox.stateChanged.connect(lambda: self.checkbox_clicked('empowered'))
        checkbox.setChecked(self.settings.special['empowered'])
        greater_rift_layout.addWidget(checkbox, 2, 0)

        label = QLabel(greater_rift)
        label.setText('Leave Game')
        greater_rift_layout.addWidget(label, 3, 0)

        button = QPushButton(greater_rift)
        self.buttons['leave_game'] = button

        button.setText(self.settings.hotkeys['leave_game'])
        button.clicked.connect(lambda: self.set_hotkey('leave_game'))
        greater_rift_layout.addWidget(button, 3, 1)

        after_rift = QGroupBox(self)
        after_rift_layout = QGridLayout(after_rift)
        after_rift.setTitle('After Rift')
        self.layout.addWidget(after_rift, 1, 1)

        ######################

        label = QLabel(after_rift)
        label.setText('Salvage')
        after_rift_layout.addWidget(label, 0, 0)

        button = QPushButton(after_rift)
        self.buttons['salvage'] = button
        button.setText(self.settings.hotkeys['salvage'])
        button.clicked.connect(lambda: self.set_hotkey('salvage'))
        after_rift_layout.addWidget(button, 0, 1)

        label = QLabel(after_rift)
        label.setText('Drop Inventory')
        after_rift_layout.addWidget(label, 1, 0)

        button = QPushButton(after_rift)
        self.buttons['drop_inventory'] = button
        button.setText(self.settings.hotkeys['drop_inventory'])
        button.clicked.connect(lambda: self.set_hotkey('drop_inventory'))
        after_rift_layout.addWidget(button, 1, 1)

        label = QLabel(after_rift)
        label.setText('Spare Columns')
        after_rift_layout.addWidget(label, 2, 0)

        spinbox = QSpinBox(after_rift)
        spinbox.setMinimum(0)
        spinbox.setMaximum(10)
        spinbox.setValue(self.settings.special['spare_columns'])
        spinbox.valueChanged.connect(self.spinbox_changed)
        after_rift_layout.addWidget(spinbox, 2, 1)

        label = QLabel(after_rift)
        label.setText('Gamble')
        after_rift_layout.addWidget(label, 3, 0)

        button = QPushButton(after_rift)
        self.buttons['gamble'] = button
        button.setText(self.settings.hotkeys['gamble'])
        button.clicked.connect(lambda: self.set_hotkey('gamble'))
        after_rift_layout.addWidget(button, 3, 1)

        cube_converter = QGroupBox(self)
        cube_converter_layout = QGridLayout(cube_converter)
        cube_converter.setTitle('Cube Converter')
        self.layout.addWidget(cube_converter, 2, 1)

        ######################

        label = QLabel(cube_converter)
        label.setText('Convert 1-Slot')
        cube_converter_layout.addWidget(label, 0, 0)

        button = QPushButton(cube_converter)
        self.buttons['cube_conv_sm'] = button
        button.setText(self.settings.hotkeys['cube_conv_sm'])
        button.clicked.connect(lambda: self.set_hotkey('cube_conv_sm'))
        cube_converter_layout.addWidget(button, 0, 1)

        label = QLabel(cube_converter)
        label.setText('Convert 2-Slot')
        cube_converter_layout.addWidget(label, 1, 0)

        button = QPushButton(cube_converter)
        self.buttons['cube_conv_lg'] = button

        button.setText(self.settings.hotkeys['cube_conv_lg'])
        button.clicked.connect(lambda: self.set_hotkey('cube_conv_lg'))

        cube_converter_layout.addWidget(button, 1, 1)

        checkbox = QCheckBox(cube_converter)
        checkbox.setText('SoL Converting')
        checkbox.clicked.connect(lambda: self.checkbox_clicked('fast_convert'))
        checkbox.setChecked(self.settings.special['fast_convert'])
        cube_converter_layout.addWidget(checkbox, 2, 0)

        label = QLabel(cube_converter)
        label.setText('Reforge / Convert Set')
        cube_converter_layout.addWidget(label, 3, 0)

        button = QPushButton(cube_converter)
        self.buttons['reforge'] = button
        button.setText(self.settings.hotkeys['reforge'])
        button.clicked.connect(lambda: self.set_hotkey('reforge'))

        cube_converter_layout.addWidget(button, 3, 1)

        self.setLayout(self.layout)

    def set_hotkey(self, hotkey):
        self.listener.stop()
        sender = self.sender()
        input = keyboard.read_hotkey(suppress=False)
        if input != 'esc':
            if hotkey_delete_request(input):
                self.settings.hotkeys[hotkey] = ''
                self.buttons[hotkey].setText('')
            else:
                reply = QMessageBox.question(
                    self, 'Save Hotkey?', f'New Hotkey: {input}.\n Save Hotkey?'
                )
                if reply == QMessageBox.Yes:
                    for k, hk in self.settings.hotkeys.items():
                        if hk == input:
                            self.settings.hotkeys[k] = ''
                            self.buttons[k].setText('')
                    self.settings.hotkeys[hotkey] = input
                    sender.setText(input)
        if not self.listener.paused:
            self.listener.start()
        # TODO: Wenn man seinen Pause key deleted
        elif self.settings.hotkeys['pause']:
            keyboard.add_hotkey(self.settings.hotkeys['pause'], self.listener.pause)

    def checkbox_clicked(self, value):
        self.listener.stop()
        sender = self.sender()
        if value == 'empowered':
            settings.special['empowered'] = sender.isChecked()
        elif value == 'fast_convert':
            settings.special['fast_convert'] = sender.isChecked()

        if not self.listener.paused:
            self.listener.start()
        # TODO: Wenn man seinen Pause key deleted
        elif self.settings.hotkeys['pause']:
            keyboard.add_hotkey(self.settings.hotkeys['pause'], self.listener.pause)

    def radio_clicked(self, value):
        self.listener.stop()
        if value == 'cains':
            self.settings.special['armor_swap_amount'] = 3
        elif value == 'bounty_dh':
            self.settings.special['armor_swap_amount'] = 2

        if not self.listener.paused:
            self.listener.start()
        elif self.settings.hotkeys['pause']:
            keyboard.add_hotkey(self.settings.hotkeys['pause'], self.listener.pause)

    def spinbox_changed(self):
        self.listener.stop()

        self.settings.special['spare_columns'] = self.sender().value()

        if not self.listener.paused:
            self.listener.start()
        elif self.settings.hotkeys['pause']:
            keyboard.add_hotkey(self.settings.hotkeys['pause'], self.listener.pause)


class AbbrevationTab(QWidget):
    def __init__(self, elder):
        super().__init__()
        self.elder = elder
        self.layout = QGridLayout(self)
        self.settings = elder.settings
        self.listener = elder.listener

        checkbox = QCheckBox(self)
        checkbox.setText('Abbrevations enabled')
        checkbox.setChecked(self.settings.special['abbrevations_enabled'])
        checkbox.clicked.connect(self.checkbox_clicked)
        self.layout.addWidget(checkbox)

        abbrevations = QGroupBox(self)
        abbrevations.setTitle('Current Abbrevations')
        abbrevations_layout = QGridLayout(abbrevations)
        self.layout.addWidget(abbrevations)

        self.abbrevations_list = QListWidget(abbrevations)
        self.abbrevations_list.setSelectionMode(QListWidget.SingleSelection)
        for abbrevation, msg in self.settings.abbrevations.items():
            # Add the new Item to QListWidget
            custom_widget = CustomListWidget(abbrevation, msg)
            item = QListWidgetItem(self.abbrevations_list)
            item.abbrevation = abbrevation
            item.msg_line_edit = custom_widget.msg_edit

            self.abbrevations_list.addItem(item)
            item.setSizeHint(custom_widget.minimumSizeHint())
            self.abbrevations_list.setItemWidget(item, custom_widget)
        abbrevations_layout.addWidget(self.abbrevations_list, 0, 0, 1, 0)

        button = QPushButton(abbrevations)
        button.setText('Save')
        button.clicked.connect(self.update_abbrevations)
        abbrevations_layout.addWidget(button, 1, 0)

        button = QPushButton(abbrevations)
        button.setText('Add new')
        button.clicked.connect(self.add_item)
        abbrevations_layout.addWidget(button, 1, 1)

        button = QPushButton(abbrevations)
        button.setText('Remove selected')
        button.clicked.connect(self.remove_selected_item)
        abbrevations_layout.addWidget(button, 1, 2)

        self.layout.addWidget(abbrevations)

    def checkbox_clicked(self):
        self.listener.stop()
        sender = self.sender()

        self.settings.special['abbrevations_enabled'] = sender.isChecked()

        if not self.listener.paused:
            self.listener.start()
        # TODO: Wenn man seinen Pause key deleted
        elif self.settings.hotkeys['pause']:
            keyboard.add_hotkey(self.settings.hotkeys['pause'], self.listener.pause)

    def update_abbrevations(self):
        self.listener.stop()

        new_abbrevations = {}
        for i in range(self.abbrevations_list.count()):
            item = self.abbrevations_list.item(i)
            abbrevation = item.abbrevation
            msg = item.msg_line_edit.text()
            new_abbrevations[abbrevation] = msg
        self.settings.abbrevations = new_abbrevations

        if not self.listener.paused:
            self.listener.start()
        # TODO: Wenn man seinen Pause key deleted
        elif self.settings.hotkeys['pause']:
            keyboard.add_hotkey(self.settings.hotkeys['pause'], self.listener.pause)

    def remove_selected_item(self):
        if self.abbrevations_list.selectedItems():
            item = self.abbrevations_list.selectedItems()[0]
            self.abbrevations_list.takeItem(self.abbrevations_list.row(item))

    def add_item(self):
        dlg = AddItemDialog(self)
        if dlg.exec_():
            abbrevation = dlg.abbrevation_edit.text()
            msg = dlg.msg_edit.text()

            # Add the new Item to QListWidget
            custom_widget = CustomListWidget(abbrevation, msg)
            item = QListWidgetItem(self.abbrevations_list)
            item.abbrevation = abbrevation
            item.msg_line_edit = custom_widget.msg_edit

            self.abbrevations_list.addItem(item)
            item.setSizeHint(custom_widget.minimumSizeHint())
            self.abbrevations_list.setItemWidget(item, custom_widget)


class SettingsTab(QWidget):
    def __init__(self, elder):
        super().__init__()
        self.elder = elder
        self.layout = QGridLayout(self)
        self.settings = elder.settings
        self.listener = elder.listener

        paths = QGroupBox(self)
        paths.setTitle('Paths')
        paths_layout = QGridLayout(paths)
        self.layout.addWidget(paths)

        label = QLabel(paths)
        label.setText('Fiddler Path')
        paths_layout.addWidget(label, 0, 0, 1, 1)

        self.fiddler_path = QLineEdit(paths)
        self.fiddler_path.setText(self.settings.paths['Fiddler'])
        self.fiddler_path.setDisabled(True)
        paths_layout.addWidget(self.fiddler_path, 0, 1, 1, 1)

        button = QPushButton(paths)
        button.setText('...')
        button.clicked.connect(lambda: self.set_path('fiddler'))
        paths_layout.addWidget(button, 0, 2, 1, 1)

        label = QLabel(paths)
        label.setText('TurboHUD Path')
        paths_layout.addWidget(label, 1, 0, 1, 1)

        self.turbohud_path = QLineEdit(paths)
        self.turbohud_path.setText(self.settings.paths['TurboHUD'])
        self.turbohud_path.setDisabled(True)
        paths_layout.addWidget(self.turbohud_path, 1, 1, 1, 1)

        button = QPushButton(paths)
        button.setText('...')
        button.clicked.connect(lambda: self.set_path('turbohud'))
        paths_layout.addWidget(button, 1, 2, 1, 1)

        label = QLabel(paths)
        label.setText('pHelper Path')
        paths_layout.addWidget(label, 2, 0, 1, 1)

        self.phelper_path = QLineEdit(paths)
        self.phelper_path.setText(self.settings.paths['pHelper'])
        self.phelper_path.setDisabled(True)
        paths_layout.addWidget(self.phelper_path, 2, 1, 1, 1)

        button = QPushButton(paths)
        button.setText('...')
        button.clicked.connect(lambda: self.set_path('phelper'))
        paths_layout.addWidget(button, 2, 2, 1, 1)

        image_recognition = QGroupBox(self)
        image_recognition.setTitle('Auto Stuff (Image Recognition)')
        image_recognition_layout = QGridLayout(image_recognition)
        self.layout.addWidget(image_recognition, 0, 1)

        checkbox = QCheckBox(image_recognition)
        checkbox.setText('Auto start Game')
        checkbox.setChecked(self.settings.special['auto_start'])
        checkbox.clicked.connect(lambda: self.checkbox_clicked('auto_start'))
        image_recognition_layout.addWidget(checkbox, 0, 0)

        checkbox = QCheckBox(image_recognition)
        checkbox.setText('Auto open Rift / Grift')
        checkbox.setChecked(self.settings.special['auto_open'])
        checkbox.clicked.connect(lambda: self.checkbox_clicked('auto_open'))
        image_recognition_layout.addWidget(checkbox, 1, 0)

        radio = QRadioButton(image_recognition)
        radio.setText('Rift')
        radio.setChecked(self.settings.special['auto_open_option'] == 'rift')
        radio.clicked.connect(lambda: self.radio_clicked('rift'))
        image_recognition_layout.addWidget(radio, 2, 0)

        radio = QRadioButton(image_recognition)
        radio.setText('Grift')
        radio.setChecked(self.settings.special['auto_open_option'] == 'grift')
        radio.clicked.connect(lambda: self.radio_clicked('grift'))
        image_recognition_layout.addWidget(radio, 2, 1)

        checkbox = QCheckBox(image_recognition)
        checkbox.setText('Auto accept Grift')
        checkbox.setChecked(self.settings.special['auto_accept_gr'])
        checkbox.clicked.connect(lambda: self.checkbox_clicked('auto_accept_gr'))
        image_recognition_layout.addWidget(checkbox, 3, 0)

        checkbox = QCheckBox(image_recognition)
        checkbox.setText('Auto upgrade Gem')
        checkbox.setChecked(self.settings.special['auto_upgrade_gem'])
        checkbox.clicked.connect(lambda: self.checkbox_clicked('auto_upgrade_gem'))
        image_recognition_layout.addWidget(checkbox, 4, 0)

        checkbox = QCheckBox(image_recognition)
        checkbox.setText('Auto gamble')
        checkbox.setChecked(self.settings.special['auto_gamble'])
        checkbox.clicked.connect(lambda: self.checkbox_clicked('auto_gamble'))
        image_recognition_layout.addWidget(checkbox, 5, 0)

        poolspots = QGroupBox(self)
        poolspots.setTitle('Poolspots')
        poolspots_layout = QGridLayout(poolspots)
        self.layout.addWidget(poolspots, 1, 0)

        self.poolspot_list = QListWidget(poolspots)
        self.poolspot_list.setSelectionMode(QListWidget.MultiSelection)
        for act, ps in ressources.poolspots().items():
            for poolspot in ps:
                item = QListWidgetItem(self.poolspot_list)
                item.setText(
                    f'Act {act}: {string.capwords(poolspot.replace("_", " "))}'
                )
                item.poolspot = poolspot
                if poolspot in self.settings.poolspots:
                    item.setSelected(True)
        self.poolspot_list.itemSelectionChanged.connect(self.update_poolspots)
        poolspots_layout.addWidget(self.poolspot_list)

        # button = QPushButton(poolspots)
        # button.setText('Save')
        # button.clicked.connect(self.update_poolspots)
        # poolspots_layout.addWidget(button)

        gamble_item = QGroupBox(self)
        gamble_item.setTitle('Gamble Item')
        gamble_item_layout = QGridLayout(gamble_item)
        self.layout.addWidget(gamble_item, 1, 1)

        self.gamble_item_list = QListWidget(gamble_item)
        self.gamble_item_list.setSelectionMode(QListWidget.SingleSelection)
        for _item in ressources.items():
            item = QListWidgetItem(self.gamble_item_list)
            item.setText(string.capwords(_item.replace('_', ' ')))
            item.item = _item
            if _item == self.settings.special['gamble_item']:
                item.setSelected(True)
        self.gamble_item_list.itemSelectionChanged.connect(self.update_gamble_item)
        gamble_item_layout.addWidget(self.gamble_item_list)

        self.setLayout(self.layout)

    def set_path(self, path):
        exe = str(
            QFileDialog.getOpenFileName(
                self, 'Select Executables', '', 'Executables (*.exe)'
            )[0]
        )
        if exe:
            if path == 'fiddler':
                self.settings.paths['Fiddler'] = exe
                self.fiddler_path.setText(exe)
            elif path == 'turbohud':
                self.settings.paths['TurboHUD'] = exe
                self.turbohud_path.setText(exe)
            elif path == 'phelper':
                self.settings.paths['pHelper'] = exe
                self.phelper_path.setText(exe)

    def update_poolspots(self):
        self.listener.stop()

        selected_spots = []
        for i in range(self.poolspot_list.count()):
            item = self.poolspot_list.item(i)
            if item.isSelected():
                selected_spots.append(item.poolspot)
        self.settings.poolspots = selected_spots

        if not self.listener.paused:
            self.listener.start()
        # TODO: Wenn man seinen Pause key deleted
        elif self.settings.hotkeys['pause']:
            keyboard.add_hotkey(self.settings.hotkeys['pause'], self.listener.pause)

    def update_gamble_item(self):
        self.listener.stop()

        selected_item = self.gamble_item_list.selectedItems()[0]
        self.settings.special['gamble_item'] = selected_item.item

        if not self.listener.paused:
            self.listener.start()
        # TODO: Wenn man seinen Pause key deleted
        elif self.settings.hotkeys['pause']:
            keyboard.add_hotkey(self.settings.hotkeys['pause'], self.listener.pause)

    def checkbox_clicked(self, value):
        sender = self.sender()
        self.settings.special[value] = sender.isChecked()

    def radio_clicked(self, value):
        self.settings.special['auto_open_option'] = value


class CustomListWidget(QWidget):
    def __init__(self, abbrevation, msg):
        super().__init__()
        self.row = QGridLayout(self)
        self.row.setSpacing(50)
        self.msg_edit = QLineEdit(msg)
        self.row.addWidget(QLabel(abbrevation), 0, 0)
        self.row.addWidget(self.msg_edit, 0, 1)

        self.setLayout(self.row)


class AddItemDialog(QDialog):
    def __init__(self, parent):
        super().__init__()
        self.setWindowTitle('Add a new Abbrevation')
        self.layout = QGridLayout(self)

        label = QLabel(self)
        label.setText('Abbrevation')
        self.layout.addWidget(label, 0, 0)

        self.abbrevation_edit = QLineEdit(self)
        self.layout.addWidget(self.abbrevation_edit, 0, 1)

        label = QLabel(self)
        label.setText('Replacement Text')
        self.layout.addWidget(label, 1, 0)

        self.msg_edit = QLineEdit(self)
        self.layout.addWidget(self.msg_edit, 1, 1)

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.layout.addWidget(self.buttonBox, 2, 1)

        self.setLayout(self.layout)


if __name__ == '__main__':
    settings = Settings()
    listener = Listener(settings)
    app = QApplication(sys.argv)
    win = MainWindow(settings, listener)
    mw = windows.ModernWindow(win)

    # for pyinstaller
    """
    from PyQt5.QtGui import QIcon

    wd = sys._MEIPASS
    file_path = os.path.join(wd, './Style/frameless.qss')
    with open(file_path) as stylesheet:
        mw.setStyleSheet(stylesheet.read())
    icon_path = os.path.join(wd, './owl.ico')
    mw.setWindowIcon(QIcon(icon_path))
    """
    # Normal
    with open('./Style/frameless.qss') as stylesheet:
        mw.setStyleSheet(stylesheet.read())

    mw.show()
    sys.exit(app.exec_())


"""
    def item_changed(self, item):
        self.listener.stop()
        print('Before:')
        print(self.settings.poolspots)
        if item.isSelected():
            self.settings.poolspots.append(item.poolspot)
        else:
            try:
                self.settings.poolspots.remove(item.poolspot)
            except ValueError:
                # TODO
                print('Poolspot war inkonsistent.')
        print('After:')
        print(self.settings.poolspots)

        if not self.listener.paused:
            self.listener.start()
        # TODO: Wenn man seinen Pause key deleted
        elif self.settings.hotkeys['pause']:
            keyboard.add_hotkey(self.settings.hotkeys['pause'], self.listener.pause)
"""
