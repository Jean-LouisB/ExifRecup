## Imports : -------------------

from front import MyMainWindow
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())