import random
import json
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QProgressBar
from PySide6.QtGui import QPixmap, QGuiApplication, QPainter, QColor
from window import MainWindow  # Импорт главного окна


class ProgressWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Загрузка...")

        # Получаем размер экрана
        screen = QGuiApplication.primaryScreen().geometry()
        screen_width = screen.width()
        screen_height = screen.height()

        # Динамический размер окна в зависимости от размера экрана
        window_width = int(screen_width * 0.5)
        window_height = int(screen_height * 0.7)

        # Устанавливаем фиксированный размер
        self.setFixedSize(window_width, window_height)

        # Отключаем возможность изменения размера
        self.setWindowFlags(self.windowFlags() | Qt.MSWindowsFixedSizeDialogHint)

        layout = QVBoxLayout()

        # Надпись с фактом
        try:
            with open("data/facts.json", "r", encoding="utf-8") as file:
                data = json.load(file)
                facts = data.get("facts", [])
                if facts:
                    fact = random.choice(facts)
                else:
                    fact = "Факты отсутствуют в файле facts.json."
        except Exception as e:
            fact = f"Ошибка при загрузке фактов: {e}"

        self.fact_label = QLabel(fact, self)
        self.fact_label.setAlignment(Qt.AlignCenter)
        self.fact_label.setWordWrap(True)  # Включаем перенос слов
        self.fact_label.setStyleSheet(f"""
            font-size: {window_width * 0.025}px; 
            margin-bottom: 10px; 
            max-width: {window_width * 0.9}px;
            padding: 0 {window_width * 0.05}px;
        """)

        # Выбираем случайное изображение
        image_paths = ["pictures/kaban.png", "pictures/koshka.png"]
        selected_image = random.choice(image_paths)

        # Изображение
        self.image_label = QLabel(self)
        original_pixmap = QPixmap(selected_image)

        # Масштабирование изображения до 80% ширины окна
        scaled_width = int(window_width * 0.8)
        scaled_height = int(original_pixmap.height() * (scaled_width / original_pixmap.width()))
        self.scaled_pixmap = original_pixmap.scaled(scaled_width, scaled_height, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # Создаем пустой пиксель для анимации
        self.reveal_pixmap = QPixmap(self.scaled_pixmap.size())
        self.reveal_pixmap.fill(QColor(0, 0, 0, 0))  # Прозрачный фон

        self.image_label.setPixmap(self.reveal_pixmap)
        self.image_label.setAlignment(Qt.AlignCenter)

        # Прогресс-бар
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setAlignment(Qt.AlignCenter)
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        self.progress_bar.setStyleSheet(f"""
            QProgressBar {{
                border: 2px solid grey;
                border-radius: {window_width * 0.01}px;
                text-align: center;
                height: {window_height * 0.03}px;
            }}
            QProgressBar::chunk {{
                background-color: #4CAF50;
                width: 10px;
            }}
        """)

        # Добавляем виджеты в layout
        layout.addWidget(self.image_label)
        layout.addWidget(self.fact_label)
        layout.addWidget(self.progress_bar)
        self.setLayout(layout)

        # Таймер для обновления прогресса и появления картинки
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(50)  # Обновление каждые 50 миллисекунд

        # Таймер для закрытия окна
        self.close_timer = QTimer(self)
        self.close_timer.timeout.connect(self.close_progress)
        self.close_timer.start(3000)  # Закрытие через 3 секунды

        self.progress_value = 0

    def update_progress(self):
        if self.progress_value < 100:
            self.progress_value += 2
            self.progress_bar.setValue(self.progress_value)

            # Постепенное открытие изображения
            self.reveal_image()

    def reveal_image(self):
        # Создаем новый пиксель-буфер
        reveal_height = int(self.scaled_pixmap.height() * (self.progress_value / 100))

        # Создаем новый пиксель с прозрачным фоном
        self.reveal_pixmap = QPixmap(self.scaled_pixmap.size())
        self.reveal_pixmap.fill(QColor(0, 0, 0, 0))  # Прозрачный фон

        # Рисуем часть оригинального изображения
        painter = QPainter(self.reveal_pixmap)
        painter.drawPixmap(0, 0, self.scaled_pixmap, 0, 0, self.scaled_pixmap.width(), reveal_height)
        painter.end()

        # Обновляем изображение
        self.image_label.setPixmap(self.reveal_pixmap)

    def close_progress(self):
        self.timer.stop()
        self.close_timer.stop()
        self.close()

        # Открываем основное окно
        self.main_window = MainWindow()
        self.main_window.show()


def main():
    app = QApplication([])

    # Запуск окна прогресса
    progress_window = ProgressWindow()
    progress_window.show()

    app.exec()


if __name__ == "__main__":
    main()