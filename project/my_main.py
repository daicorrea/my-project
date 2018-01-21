from lib import read_file

def main():
    file = read_file.ReadFile('../docs/database.csv')
    database = file.get_data()
    print(database)

main()

