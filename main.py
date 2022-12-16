import sys
from PyQt5 import QtWidgets
from Windows import main_menu


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = main_menu.MainMenu()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()