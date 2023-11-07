import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QSlider, QCheckBox, QPushButton, QHBoxLayout
from PyQt5.QtGui import QIcon, QFont, QPalette, QColor
import random
import string
import pyperclip

class PasswordGeneratorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Generator")
        self.setGeometry(100, 100, 400, 400)
        self.setWindowIcon(QIcon("lock.png"))

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        # Set an interactive background color
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(184, 184, 148))  # Change the color as needed
        self.setPalette(palette)

        slider_layout = QHBoxLayout()

        self.min_length_label = QLabel("Min Length: 4")
        self.min_length_label.setFont(QFont("Times New Roman", 12))
        slider_layout.addWidget(self.min_length_label)

        self.length_slider = QSlider()
        self.length_slider.setOrientation(1)  # Vertical slider
        self.length_slider.setRange(4, 32)
        self.length_slider.setValue(16)
        self.length_slider.setTickInterval(4)  # Increment by 4
        self.length_slider.setTickPosition(QSlider.TicksAbove)
        slider_layout.addWidget(self.length_slider)

        self.max_length_label = QLabel("Max Length: 32")
        self.max_length_label.setFont(QFont("Times New Roman", 12))
        slider_layout.addWidget(self.max_length_label)

        self.layout.addLayout(slider_layout)

        self.length_display_label = QLabel("Selected Length: 16")
        self.length_display_label.setFont(QFont("Times New Roman", 16))
        self.layout.addWidget(self.length_display_label)

        self.lowercase_checkbox = QCheckBox("Include Lowercase")
        self.lowercase_checkbox.setFont(QFont("Times New Roman", 12))
        self.layout.addWidget(self.lowercase_checkbox)

        self.uppercase_checkbox = QCheckBox("Include Uppercase")
        self.uppercase_checkbox.setFont(QFont("Times New Roman", 12))
        self.layout.addWidget(self.uppercase_checkbox)

        self.number_checkbox = QCheckBox("Include Numbers")
        self.number_checkbox.setFont(QFont("Times New Roman", 12))
        self.layout.addWidget(self.number_checkbox)

        self.symbol_checkbox = QCheckBox("Include Symbols")
        self.symbol_checkbox.setFont(QFont("Times New Roman", 12))
        self.layout.addWidget(self.symbol_checkbox)

        self.generate_button = QPushButton("Generate Password")
        self.generate_button.setFont(QFont("Times New Roman", 14))
        self.generate_button.setStyleSheet("background-color: #5c5c3d; color: #FFFFFF;")
        self.generate_button.clicked.connect(self.generate_password)
        self.layout.addWidget(self.generate_button)

        self.result_label = QLabel("")
        self.result_label.setFont(QFont("Times New Roman", 18))
        self.layout.addWidget(self.result_label)

        self.central_widget.setLayout(self.layout)

        self.length_slider.valueChanged.connect(self.update_min_max_labels)

    def update_min_max_labels(self):
        min_length = self.length_slider.minimum()
        max_length = self.length_slider.maximum()
        self.min_length_label.setText(f"Min Length: {min_length}")
        self.max_length_label.setText(f"Max Length: {max_length}")
        selected_length = self.length_slider.value()
        self.length_display_label.setText(f"Selected Length: {selected_length}")

    def generate_password(self):
        length = self.length_slider.value()
        use_lower = self.lowercase_checkbox.isChecked()
        use_upper = self.uppercase_checkbox.isChecked()
        use_number = self.number_checkbox.isChecked()
        use_symbol = self.symbol_checkbox.isChecked()

        characters = ""
        if use_lower:
            characters += string.ascii_lowercase
        if use_upper:
            characters += string.ascii_uppercase
        if use_number:
            characters += string.digits
        if use_symbol:
            characters += string.punctuation

        if not characters:
            self.result_label.setText("Select at least one option")
        else:
            password = "password is : "+''.join(random.choice(characters) for _ in range(length))
            self.result_label.setText(password)

            # Copy generated password to clipboard
            pyperclip.copy(password)

def main():
    app = QApplication(sys.argv)

    window = PasswordGeneratorApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
