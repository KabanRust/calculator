from PyQt6.QtWidgets import QApplication
from window import MainWindow


def main():
    app = QApplication([])

    # Создаем главное окно
    main_window = MainWindow()

    # Отображаем окно
    main_window.show()

    # Запускаем приложение
    app.exec()

if __name__ == "__main__":
    main()
