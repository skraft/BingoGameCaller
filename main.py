__author__ = "Sean Kraft"

import sys
from PySide6 import QtWidgets
from manager import BingoMachine
from ui import BingoCallerUI


if __name__ == "__main__":
    bingoMachine: BingoMachine = BingoMachine()

    app = QtWidgets.QApplication([])
    manager_ui = BingoCallerUI(bingoMachine)
    manager_ui.show()
    sys.exit(app.exec())
