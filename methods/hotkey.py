from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt

class hotkey:
    def keyPressEvent(self, event):
        key = event.key()
        key_map = {
            Qt.Key.Key_0: '0', Qt.Key.Key_1: '1', Qt.Key.Key_2: '2', Qt.Key.Key_3: '3',
            Qt.Key.Key_4: '4', Qt.Key.Key_5: '5', Qt.Key.Key_6: '6', Qt.Key.Key_7: '7',
            Qt.Key.Key_8: '8', Qt.Key.Key_9: '9', Qt.Key.Key_Plus: '+', Qt.Key.Key_Minus: '-',
            Qt.Key.Key_Asterisk: '*', Qt.Key.Key_Slash: '/', Qt.Key.Key_ParenLeft: '(',
            Qt.Key.Key_ParenRight: ')', Qt.Key.Key_Period: '.', Qt.Key.Key_Backspace: '←',
            Qt.Key.Key_C: 'C', Qt.Key.Key_Enter: '=', Qt.Key.Key_Return: '=', Qt.Key.Key_Percent: '%'
        }

        additional_keys = {
            Qt.Key.Key_S: 'sin', Qt.Key.Key_O: 'cos', Qt.Key.Key_T: 'tan',
            Qt.Key.Key_L: 'log', Qt.Key.Key_AsciiCircum: '^', Qt.Key.Key_Q: 'sqrt',
            Qt.Key.Key_I: '∫', Qt.Key.Key_D: 'd/dx', Qt.Key.Key_X: 'x', Qt.Key.Key_Y: 'y',
        }

        key_map.update(additional_keys)

        if key in key_map:
            current_tab = self.tab_widget.currentWidget()
            input_line = current_tab.findChild(QLineEdit)
            self.on_button_click(key_map[key], input_line)