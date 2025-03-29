import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class CoolApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle('Ньютоновское охлаждение')
        layout = QVBoxLayout()

        self.temp0_in = QLineEdit(self)
        self.temp0_in.setPlaceholderText('Начальная температура (°C)')
        layout.addWidget(self.temp0_in)

        self.env_in = QLineEdit(self)
        self.env_in.setPlaceholderText('Температура среды (°C)')
        layout.addWidget(self.env_in)

        self.k_in = QLineEdit(self)
        self.k_in.setPlaceholderText('Коэффициент (1/с)')
        layout.addWidget(self.k_in)

        btn = QPushButton('Построить', self)
        btn.clicked.connect(self.plot_cooling)
        layout.addWidget(btn)

        self.canvas = FigureCanvas(plt.figure())
        layout.addWidget(self.canvas)
        self.setLayout(layout)

    def plot_cooling(self):
        t0 = float(self.temp0_in.text())
        env = float(self.env_in.text())
        k = float(self.k_in.text())

        t = np.linspace(0, 10, 1000)
        temp = env + (t0 - env) * np.exp(-k * t)
        
        self.canvas.figure.clear()
        ax = self.canvas.figure.add_subplot(111)
        ax.plot(t, temp)
        ax.set_xlabel('Время (с)')
        ax.set_ylabel('Температура (°C)')
        ax.set_title(f'{t0}°C, {env}°C, k={k}')
        self.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = CoolApp()
    win.show()
    sys.exit(app.exec_())
