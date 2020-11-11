import operator

from wgg.bgg.xml_processor import game_data_generator

GLOBAL_FILTER_MIN_USERSRATED = 50
EXCLUDE_EXPANSIONS = True

# Add any global kind of filters here, applied in all functions
def std_game_filter(game_data):
    if int(game_data['ratings_usersrated']) < GLOBAL_FILTER_MIN_USERSRATED:
        return False

    if EXCLUDE_EXPANSIONS and "Expansion for Base-game" in game_data['categories']:
        return False

    for designer in game_data['designers']:
        if designer[0] == '(':
            return False

    return True

def print_ranked(s_list, limit=30):
    rank = 0
    lv = 999999999
    extra_rank = 0
    for d in s_list[0:limit]:
        if d[1] < lv:
            rank +=1
            rank += extra_rank
            extra_rank = 0
            print("%s \t %s (%s)" % (rank, d[0], d[1]))
        else:
            extra_rank +=1
            print(" \t %s (%s)" % (d[0], d[1]))
        lv = d[1]

def print_top_publishers(list_of_games, lowest_rating=0.0, limit=30):
    publisher_data = dict()

    print("GAME PUBLISHERS filtered on rating > %s" % lowest_rating)

    for game_data in list_of_games:

        # Basic filter to accept game for stats
        if not std_game_filter(game_data):
            continue

        if float(game_data['ratings_average']) < lowest_rating:
            continue

        for publisher in game_data['publishers']:
            if publisher[0] == '(':
                continue

            pd = publisher_data.get(publisher, 0)
            pd += 1
            publisher_data[publisher] = pd

    # Sort by n games
    spd = sorted(publisher_data.items(), key=operator.itemgetter(1), reverse=True)

    print_ranked(spd, limit)

def print_top_designers(list_of_games, lowest_rating=0.0, limit=30):
    designer_data = dict()

    print("GAME DESIGNERS filtered on rating > %s" % lowest_rating)

    for game_data in list_of_games:

        # Basic filter to accept game for stats
        if not std_game_filter(game_data):
            continue

        if float(game_data['ratings_average']) < lowest_rating:
            continue

        for designer in game_data['designers']:
            if designer[0] == '(':
                continue
            pd = designer_data.get(designer, 0)
            pd += 1
            designer_data[designer] = pd

    # Sort by number of games
    spd = sorted(designer_data.items(), key=operator.itemgetter(1), reverse=True)

    print_ranked(spd, limit)

def print_top_years(list_of_games, lowest_rating=0.0, limit=30):
    year_data = dict()


    for game_data in list_of_games:

        # Basic filter to accept game for stats
        if not std_game_filter(game_data):
            continue

        if float(game_data['ratings_average']) < lowest_rating:
            continue

        year = game_data['yearpublished']
        pd = year_data.get(year, 0)
        pd += 1
        year_data[year] = pd

    # Sort by number of games
    print("GAME RELEASE YEAR filtered on rating > %s, ordered by # games" % lowest_rating)
    spd = sorted(year_data.items(), key=operator.itemgetter(1), reverse=True)
    print_ranked(spd, limit)

    # Sort by year
    print("GAME RELEASE YEAR filtered on rating > %s, ordered by year" % lowest_rating)
    spd = sorted(year_data.items(), key=operator.itemgetter(0), reverse=False)

    # Just print all rows in year order
    for d in spd:
        print(" \t %s, %s" % (d[0], d[1]))

#
# Create bulk list since we need to re-use the data list.
#
list_of_games = list(game_data_generator())

print_top_publishers(list_of_games, 0, 30)
print_top_publishers(list_of_games, 6.0, 30)
print_top_publishers(list_of_games, 7.5, 30)
print_top_publishers(list_of_games, 8.0, 30)

print_top_designers(list_of_games, 0, 30)
print_top_designers(list_of_games, 6.0, 30)
print_top_designers(list_of_games, 7.5, 30)
print_top_designers(list_of_games, 8.0, 30)

print_top_years(list_of_games, 0, 30)
print_top_years(list_of_games, 6.0, 30)
print_top_years(list_of_games, 7.5, 30)
print_top_years(list_of_games, 8.0, 30)
