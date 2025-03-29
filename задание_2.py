import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class OscPlot(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle('График гармонического колебания')
        layout = QVBoxLayout()

        self.amp_in = QLineEdit(self)
        self.amp_in.setPlaceholderText('Амплитуда (м)')
        layout.addWidget(self.amp_in)

        self.freq_in = QLineEdit(self)
        self.freq_in.setPlaceholderText('Частота (Гц)')
        layout.addWidget(self.freq_in)

        self.phase_in = QLineEdit(self)
        self.phase_in.setPlaceholderText('Фаза (градусы)')
        layout.addWidget(self.phase_in)

        plot_btn = QPushButton('Построить', self)
        plot_btn.clicked.connect(self.draw_plot)
        layout.addWidget(plot_btn)

        self.canvas = FigureCanvas(plt.figure())
        layout.addWidget(self.canvas)
        self.setLayout(layout)

    def draw_plot(self):
        amp = float(self.amp_in.text())
        freq = float(self.freq_in.text())
        phase = float(self.phase_in.text())

        t = np.linspace(0, 10, 1000)
        y = amp * np.cos(2 * np.pi * freq * t + np.radians(phase))

        self.canvas.figure.clear()
        ax = self.canvas.figure.add_subplot(111)
        ax.plot(t, y)
        ax.set_xlabel('Время (с)')
        ax.set_ylabel('Смещение (м)')
        ax.set_title(f'A={amp} м, f={freq} Гц, φ={phase}°')
        self.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = OscPlot()
    window.show()
    sys.exit(app.exec_())
