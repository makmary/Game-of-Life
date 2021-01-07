from scheduler import run_scheduler
from args_parser import parse_args
from cell_board import CellBoard


def main():
    timeout = 1
    args = parse_args()
    if args.file:
        life_cycle = CellBoard(filename=args.file)
    else:
        life_cycle = CellBoard(m_rows=args.rows, n_columns=args.columns)
    run_scheduler(life_cycle, timeout)


if __name__ == "__main__":
    main()
