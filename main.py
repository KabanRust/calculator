from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QProgressBar
from PySide6.QtGui import QPixmap
from window import MainWindow  # Импорт главного окна


class ProgressWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Загрузка...")
        self.setFixedSize(800, 600)

        layout = QVBoxLayout()

        # Изображение
        self.image_label = QLabel(self)
        self.pixmap = QPixmap("kaban.png")  # Укажите корректный путь к изображению
        self.image_label.setPixmap(self.pixmap)
        self.image_label.setAlignment(Qt.AlignCenter)

        # Прогресс-бар
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setAlignment(Qt.AlignCenter)
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)

        layout.addWidget(self.image_label)
        layout.addWidget(self.progress_bar)
        self.setLayout(layout)

        # Таймер для обновления прогресса
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(50)  # Обновление каждые 50 миллисекунд

        # Таймер для закрытия окна
        self.close_timer = QTimer(self)
        self.close_timer.timeout.connect(self.close_progress)
        self.close_timer.start(5000)  # Закрытие через 5 секунд

        self.progress_value = 0

    def update_progress(self):
        """Обновляет прогресс-бар."""
        if self.progress_value < 100:
            self.progress_value += 2
            self.progress_bar.setValue(self.progress_value)

    def close_progress(self):
        """Закрывает окно прогресса и открывает главное окно."""
        self.timer.stop()
        self.close_timer.stop()
        self.close()

        # Открываем основное окно
        self.main_window = MainWindow()
        self.main_window.show()


def main():
    """Точка входа в приложение."""
    app = QApplication([])

    # Запуск окна прогресса
    progress_window = ProgressWindow()
    progress_window.show()

    app.exec()


if __name__ == "__main__":
    main()
