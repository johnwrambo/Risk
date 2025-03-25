from utils import *
from map_data import *

territory = "iceland"
# Test functions
init_gamedata(game_df)

#should print 1
print(set_occupied(game_df, territory, True))
#should print 2
print(set_occupied(game_df, territory, False))

#should print list
print(territory_connections(game_df, territory))
# should print <class 'list'>
print(type(territory_connections(game_df, territory)))

print(check_is_occupied(game_df, territory))
print(type(game_df))