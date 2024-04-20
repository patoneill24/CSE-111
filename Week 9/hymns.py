import csv

FILE = 'Week 9/hymns.csv'

HYMN_NAME     = 0
HYMN_AUTHOR   = 1
HYMN_COMPOSER = 2


def main():
    with open(FILE, "r") as hymns:
        reader = csv.reader(hymns)
        header = next(reader)
        row = next(reader)
        while row != None:
            print(f'NAME: {row[HYMN_NAME]}     AUTHOR:{row[HYMN_AUTHOR]},      COMPOSER:{row[HYMN_COMPOSER]}')
            row = next(reader, None)

if __name__ == "__main__":
    main()