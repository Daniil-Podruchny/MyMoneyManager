from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
from DB import money_manager_db


class MplWidget(QTabWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)

        self.money_manager_db = money_manager_db.MoneyManagerDb()
        self.draw_diagram()
        

    def draw_diagram(self):
        category_dict = self.money_manager_db.getCostsAndCategories()

        self.canvas = FigureCanvas(Figure())

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)

        self.canvas.ax = self.canvas.figure.add_subplot()
        self.canvas.ax.pie(list(category_dict.values()), labels=list(category_dict))
        self.canvas.ax.axis("equal")
        self.setLayout(vertical_layout)


