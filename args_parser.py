import argparse


def parse_args():
    text = 'You can read a file with an argument -f or 2 numbers with arguments -m and -n'
    parser = argparse.ArgumentParser(description=text)
    parser.add_argument("-f", "--file", help="file with the cell board")
    parser.add_argument("-m", "--rows", help="number of rows", type=int)
    parser.add_argument("-n", "--columns", help="number of columns", type=int)
    args = parser.parse_args()
    if args.file:
        print("This is the file you are using %s" % args.file)
    if args.rows:
        print("This is the number of rows %s" % args.rows)
    if args.columns:
        print("This is the number of columns %s" % args.columns)
    return args
