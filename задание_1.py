import sys
import math
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class Trajectory(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Визуализация движения тела, брошенного под углом к горизонту')
        self.layout = QVBoxLayout()

        self.v0_input = QLineEdit(self)
        self.v0_input.setPlaceholderText('Начальная скорость (м/с)')
        self.layout.addWidget(self.v0_input)

        self.angle_input = QLineEdit(self)
        self.angle_input.setPlaceholderText('Угол броска')
        self.layout.addWidget(self.angle_input)

        self.plot_button = QPushButton('Построить траекторию', self)
        self.plot_button.clicked.connect(self.plot_trajectory)
        self.layout.addWidget(self.plot_button)

        self.canvas = FigureCanvas(plt.figure())
        self.layout.addWidget(self.canvas)

        self.setLayout(self.layout)

    def plot_trajectory(self):
        v0 = float(self.v0_input.text())
        angle = float(self.angle_input.text())
        angle_rd = math.radians(angle)
        g = 10

        t_f = 2 * v0 * math.sin(angle_rd) / g
        t = np.linspace(0, t_f, num=100)

        x = v0 * np.cos(angle_rd) * t
        y = v0 * np.sin(angle_rd) * t - 0.5 * g * t**2

        self.canvas.figure.clear()
        ax = self.canvas.figure.add_subplot(111)
        ax.plot(x, y)
        ax.set_xlabel('Расстояние по оси X (м)')
        ax.set_ylabel('Высота по оси Y (м)')
        ax.set_title(f'Траектория движения при скорости {v0} м/с и угле {angle}°')
        self.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Trajectory()
    ex.show()
    sys.exit(app.exec_())
