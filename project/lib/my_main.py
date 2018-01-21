#from lib import read_file
import read_file

harry_potter = read_file.ReadFile('Harry Potter')

avatar = read_file.ReadFile('Avatar')

hunger_games = read_file.ReadFile('Hunger Games')

a_monster_call = read_file.ReadFile('./movie_quotes')

movies = [harry_potter, avatar, hunger_games, a_monster_call]

a_monster_call.get_data()

