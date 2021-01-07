from random import *


class CellBoard:
    m_rows = 0
    n_columns = 0
    alive = []
    dead = []
    board = []

    def __init__(self, m_rows=None, n_columns=None, filename=None):
        """
        A constructor that keeps input from user, such as size of board or filename, and populates the board of cells.
        :param m_rows (int): the number of rows in board
        :param n_columns (int): the number of columns in board
        :param filename (str): the filename with size of the board and board itself
        """
        if m_rows is not None and n_columns is not None:
            self.m_rows = m_rows
            self.n_columns = n_columns
            self.board = self.create_board()
        if filename is not None:
            self.board = self.read_file(filename)
        self.print_board()

    def read_file(self, filename):
        """
        A method that reads the file and prints the board.
        """
        board = list()
        with open(filename, 'r') as f:
            m, n = f.readline().split()
            self.m_rows, self.n_columns = int(m), int(n)
            for line in f.readlines():
                int_line = [int(x) for x in line.split()]
                board.append(int_line)

        return board

    def create_board(self):
        """
        A method that sets the random state of all cells.
        """
        board = [[2 for _ in range(self.n_columns)] for _ in range(self.m_rows)]
        for i in range(self.m_rows):
            for k in range(self.n_columns):
                state = randint(0, 1)
                board[i][k] = state

        return board

    def print_board(self):
        """
        A method that draws the actual board.
        """
        print('\n')
        for row in self.board:
            for column in row:
                print(column, end=' ')
            print()

    def calculate_next_cells_state(self):
        """
        A method that checks the board of cells.
        :return:
        """
        for i in range(self.m_rows):
            for j, value in enumerate(self.board[i]):
                coords = (i, j)
                self.check_cell_state(coords)

    def check_cell_state(self, coords):
        """
        A method that checks current state of specific cell and save its coordinates in list of dead or alive cells.
        :param coords: a tuple of ints which are the coordinates of current cell
        """
        count_alive_neighbors = 0
        x, y = coords
        for i in range(max(x - 1, 0), min(self.m_rows, x + 2)):
            for j in range(max(y - 1, 0), min(self.n_columns, y + 2)):
                if i == x and j == y:
                    continue
                if self.board[i][j] == 1:
                    count_alive_neighbors += 1

        if self.board[x][y] == 1:
            if 2 > count_alive_neighbors or count_alive_neighbors > 3:
                self.dead.append(coords)
        else:
            if count_alive_neighbors == 3:
                self.alive.append(coords)

    def update_board(self):
        """
        A method which populates the board of cells from list of dead and alive cells, and draws the actual board.
        """
        self.alive = []
        self.dead = []
        self.calculate_next_cells_state()
        for coords in self.alive:
            x, y = coords
            self.board[x][y] = 1
        for coords in self.dead:
            x, y = coords
            self.board[x][y] = 0
        self.print_board()

    def is_same_board(self):
        """
        :return: True for success if same condition of the board remains the same, False otherwise.
        """
        return len(self.alive) == 0 and len(self.dead) == 0
