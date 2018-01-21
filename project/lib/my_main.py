#from lib import read_file
import read_file

a_monster_call = read_file.ReadFile('./database.csv')

content = a_monster_call.get_data()
print(content)

