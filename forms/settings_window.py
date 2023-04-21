from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QGridLayout, QLabel, QPushButton, QSlider, QVBoxLayout, QSpinBox

from logic.settings import Settings


class SettingsWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Настройки")
        self.setFixedSize(300, 200)

        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)

        self.level_label = QLabel("Уровень:")
        self.level_label.setFont(font)
        self.level_slider = QSlider(Qt.Horizontal)
        self.level_slider.setRange(1, 2)
        self.level_slider.setValue(Settings.level_number)
        self.level_slider.setTickInterval(1)
        self.level_slider.setTickPosition(QSlider.TicksBelow)
        self.level_slider.valueChanged.connect(self.change_level)

        self.cell_size_label = QLabel("Размер ячейки:")
        self.cell_size_label.setFont(font)
        self.cell_size_spinbox = QSpinBox()
        self.cell_size_spinbox.setRange(50, 100)
        self.cell_size_spinbox.setValue(Settings.cell_size)
        self.cell_size_spinbox.setSingleStep(10)
        self.cell_size_spinbox.valueChanged.connect(self.change_size)

        self.ok_button = QPushButton("OK")
        self.ok_button.setFont(font)
        self.ok_button.clicked.connect(self.accept)
        self.ok_button.setFlat(True)
        self.ok_button.setStyleSheet("border:none; background-color: none;")
        self.ok_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cancel_button = QPushButton("Отмена")
        self.cancel_button.setFont(font)
        self.cancel_button.clicked.connect(self.reject)
        self.cancel_button.setFlat(True)
        self.cancel_button.setStyleSheet("border:none; background-color: none;")
        self.cancel_button.setFocusPolicy(QtCore.Qt.NoFocus)


        layout = QGridLayout()
        layout.addWidget(self.level_label, 0, 0)
        layout.addWidget(self.level_slider, 0, 1)
        layout.addWidget(self.cell_size_label, 1, 0)
        layout.addWidget(self.cell_size_spinbox, 1, 1)

        button_layout = QVBoxLayout()
        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.cancel_button)

        layout.addLayout(button_layout, 2, 0, 1, 2)

        self.setLayout(layout)

    def change_size(self, value):
        Settings.change_size(value)

    def change_level(self, value):
        Settings.change_level(value)

