from cell_board import CellBoard
import schedule
import time


def run_scheduler(cell_board: CellBoard, timeout: int):
    job = schedule.every().seconds.do(cell_board.update_board)
    job.run()

    while True:
        schedule.run_pending()
        time.sleep(timeout)
        if cell_board.is_same_board():
            cell_board.print_board()
            break
