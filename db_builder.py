import django
django.setup()

from wgg.bgg.xml_processor import game_data_generator

from wgg.models import BoardGame


'''
NOTE: Must be run from Django context

$ manage.py shell

from wgg.db_builder import build_sql_db_from_xmls
build_sql_db_from_xmls()

'''
def build_sql_db_from_xmls(directory='./bgg/xml'):
    fail_games = list()
    stored = 0
    for game in game_data_generator(directory=directory):

        # game_as_json = json.dumps(game, indent=4)

        try:
            # Remove noise
            try:
                game['categories'].remove('Wargame')
            except Exception:
                # Or ignore all missing that tag? (ie continue...)
                pass

            board_game = BoardGame(
                bgg_id=int(game['bgg_id']),

                name=game['name'],
                yearpublished=int(game['yearpublished']),
                description=game['description'].replace('&#10;', '\n'),
                image=game['image'],
                thumbnail=game['thumbnail'],

                playingtime=int(game['playingtime']),

                designers=', '.join(game['designers']),
                publishers=', '.join(game['publishers']),

                mechanics=', '.join(game['mechanics']),
                categories=', '.join(game['categories']),

                minplayers=game['minplayers'],
                maxplayers=game['maxplayers'],

                ratings_usersrated=int(game['ratings_usersrated']),
                ratings_average=float(game['ratings_average']),
                ratings_averageweight=float(game['ratings_averageweight']),

                # bgg_json=game_as_json
            )

            board_game.save()
            stored +=1

        except Exception as e:
            print("-> Failed to store %s (%s)" % ( game['name'], e))
            fail_games.append(game['name'])

    print("The following games failed to store:")
    print(fail_games)
    print("Stored %s games successfully" % stored)

if __name__ == "__main__":
    build_sql_db_from_xmls()



'''

Objective: Odessa
{
    "name": "Objective: Odessa",
    "yearpublished": "2011",
    "description": "Campaigns in WW2 #2 Expansion Kit&#10;&#10;As part of Army Group South&rsquo;s effort in Operation Barbarossa, the Romanian 3rd and 4th Armies were tasked with covering the right flank of the offensive, clearing the area between the Dniester and Bug Rivers, and occupying the port city of Odessa. Axis planners hoped the badly outnumbered Soviet garrison in this area would collapse quickly, but the hastily assembled Independent Coastal Army managed to withstand 73 days of siege before being evacuated to the Crimea by the Black Sea Fleet, effectively gutting the cream of the pre-war Romanian Army in the process.&#10;&#10;The Objective: Odessa expansion kit includes a map extension and additional units to cover the added area and forces that participated in this region during the campaign.&#10;&#10;Note, Objective: Odessa is not a &lsquo;stand alone&rsquo; game. You must own a copy of Objective: Kiev to use this expansion kit.&#10;&#10;Game Data:&#10;&#10;Complexity: 3 on a 9 scale&#10;Solitaire Suitability: 7 on a 9 scale&#10;Scale: Each unit is one German corps or Russian army, and each turn is approximately one to two weeks.&#10;&#10;Game Components:&#10;&#10;&bull;    Eight 5/8&quot; square pieces&#10;&bull;    One 8&quot; x 11&quot; map extension&#10;&bull;    One Rules booklet&#10;&#10;",
    "image": "https://cf.geekdo-images.com/original/img/VxTGSZe0E-73RKGdIX9TBk-A5lA=/0x0/pic1444317.jpg",
    "thumbnail": "https://cf.geekdo-images.com/thumb/img/1BHe9XXa5gYKLjuEoW5Sszyk7ck=/fit-in/200x150/pic1444317.jpg",
    "playingtime": "0",
    "minplaytime": "0",
    "maxplaytime": "0",
    "minplayers": "2",
    "maxplayers": "2",
    "minage": "12",
    "integration": [],
    "mechanics": [
        "Hex-and-Counter"
    ],
    "publishers": [
        "Victory Point Games"
    ],
    "implementations": [],
    "artists": [
        "Alan Emrich"
    ],
    "families": [
        "Campaigns in Russia"
    ],
    "categories": [
        "Expansion for Base-game",
        "Wargame",
        "World War II"
    ],
    "expansions": [
        "Objective: Kiev"
    ],
    "designers": [
        "Frank Chadwick"
    ],
    "ratings_usersrated": "5",
    "ratings_average": "7.4",
    "ratings_bayesaverage": "0",
    "ratings_rank_boardgame": "Not Ranked",
    "ratings_rank_wargame": "Not Ranked",
    "ratings_stddev": "1.0198",
    "ratings_median": "0",
    "ratings_owned": "40",
    "ratings_trading": "0",
    "ratings_wanting": "5",
    "ratings_wishing": "8",
    "ratings_numcomments": "6",
    "ratings_numweights": "2",
    "ratings_averageweight": "2",
    "bgg_id": "115825"
}

'''