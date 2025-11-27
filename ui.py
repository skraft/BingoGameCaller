"""A UI that allows the user to pull bingo numbers one at a time and
review the previously pulled numbers in organized columns."""

__author__ = "Sean Kraft"


from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout,QPushButton, QWidget, QLabel, QTreeWidget, QTreeWidgetItem
from manager import BingoMachine


class BingoCallerUI(QMainWindow):
    UI_NAME = "Bingo Caller"

    def __init__(self, bingo_machine: BingoMachine):
        super().__init__()

        self.bingo_machine: BingoMachine = bingo_machine

        self.setObjectName("BingoCaller")
        self.setWindowTitle(self.UI_NAME)

        self.new_game: bool = True

        self.btn_next_number: QPushButton = None
        self.lbl_number: QLabel = None
        self.tre_b_letters: QTreeWidget = None
        self.tre_i_letters: QTreeWidget = None
        self.tre_n_letters: QTreeWidget = None
        self.tre_g_letters: QTreeWidget = None
        self.tre_o_letters: QTreeWidget = None

        self.number_font = QFont()
        self.number_font.setPointSize(32)
        self.table_font = QFont()
        self.table_font.setPointSize(16)

        self.build_ui()

    def build_ui(self):
        self.resize(566, 720)

        # main widget and layout
        wdg_main = QWidget()
        self.setCentralWidget(wdg_main)
        lyo_main = QVBoxLayout(wdg_main)
        lyo_main.setContentsMargins(15, 12, 15, 15)
        lyo_main.setSpacing(9)

        self.btn_next_number = QPushButton("Start Game")
        self.btn_next_number.setMinimumHeight(50)
        self.btn_next_number.clicked.connect(self.on_next_number)
        lyo_main.addWidget(self.btn_next_number)

        self.lbl_number = QLabel("")
        self.lbl_number.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.lbl_number.setFont(self.number_font)
        lyo_main.addWidget(self.lbl_number)

        lyo_pulled_numbers = QHBoxLayout()
        lyo_main.addLayout(lyo_pulled_numbers)

        self.tre_b_letters = QTreeWidget()
        self.tre_b_letters.setColumnCount(1)
        self.tre_b_letters.setHeaderLabels(["B"])
        self.tre_b_letters.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        header = self.tre_b_letters.header()
        header.setDefaultAlignment(Qt.AlignmentFlag.AlignHCenter)
        header.setFont(self.number_font)
        lyo_pulled_numbers.addWidget(self.tre_b_letters)

        self.tre_i_letters = QTreeWidget()
        self.tre_i_letters.setColumnCount(1)
        self.tre_i_letters.setHeaderLabels(["I"])
        self.tre_i_letters.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        header = self.tre_i_letters.header()
        header.setDefaultAlignment(Qt.AlignmentFlag.AlignHCenter)
        header.setFont(self.number_font)
        lyo_pulled_numbers.addWidget(self.tre_i_letters)

        self.tre_n_letters = QTreeWidget()
        self.tre_n_letters.setColumnCount(1)
        self.tre_n_letters.setHeaderLabels(["N"])
        self.tre_n_letters.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        header = self.tre_n_letters.header()
        header.setDefaultAlignment(Qt.AlignmentFlag.AlignHCenter)
        header.setFont(self.number_font)
        lyo_pulled_numbers.addWidget(self.tre_n_letters)

        self.tre_g_letters = QTreeWidget()
        self.tre_g_letters.setColumnCount(1)
        self.tre_g_letters.setHeaderLabels(["G"])
        self.tre_g_letters.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        header = self.tre_g_letters.header()
        header.setDefaultAlignment(Qt.AlignmentFlag.AlignHCenter)
        header.setFont(self.number_font)
        lyo_pulled_numbers.addWidget(self.tre_g_letters)

        self.tre_o_letters = QTreeWidget()
        self.tre_o_letters.setColumnCount(1)
        self.tre_o_letters.setHeaderLabels(["O"])
        self.tre_o_letters.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        header = self.tre_o_letters.header()
        header.setDefaultAlignment(Qt.AlignmentFlag.AlignHCenter)
        header.setFont(self.number_font)
        lyo_pulled_numbers.addWidget(self.tre_o_letters)

        btn_reset_game = QPushButton("Reset Game")
        btn_reset_game.clicked.connect(self.on_reset_game)
        lyo_main.addWidget(btn_reset_game)

    def on_next_number(self):
        """Displays the next number and adds it to the appropriate number column."""
        # get the next number from the bingo machine
        if self.new_game:
            self.btn_next_number.setText("Next Number")
            self.new_game = False

        try:
            number: int = self.bingo_machine.select_number()

            # update the label
            self.lbl_number.setText(self.bingo_machine.add_letter(number))

            # add the number to the appropriate pulled numbers column
            item = QTreeWidgetItem()
            item.setData(0, Qt.ItemDataRole.DisplayRole, number)
            item.setFont(0, self.table_font)

            if number < 16:
                self.tre_b_letters.addTopLevelItem(item)
                self.tre_b_letters.sortItems(0, Qt.SortOrder.AscendingOrder)
            elif number < 31:
                self.tre_i_letters.addTopLevelItem(item)
                self.tre_i_letters.sortItems(0, Qt.SortOrder.AscendingOrder)
            elif number < 46:
                self.tre_n_letters.addTopLevelItem(item)
                self.tre_n_letters.sortItems(0, Qt.SortOrder.AscendingOrder)
            elif number < 61:
                self.tre_g_letters.addTopLevelItem(item)
                self.tre_g_letters.sortItems(0, Qt.SortOrder.AscendingOrder)
            else:
                self.tre_o_letters.addTopLevelItem(item)
                self.tre_o_letters.sortItems(0, Qt.SortOrder.AscendingOrder)

        except UserWarning:
            self.lbl_number.setText("Game is Over")


    def on_reset_game(self):
        """Resets the game and clears all the number columns."""
        self.bingo_machine.reset_game()
        self.lbl_number.setText("")
        self.tre_b_letters.clear()
        self.tre_i_letters.clear()
        self.tre_n_letters.clear()
        self.tre_g_letters.clear()
        self.tre_o_letters.clear()
        self.btn_next_number.setText("Start Game")
        self.new_game = True
