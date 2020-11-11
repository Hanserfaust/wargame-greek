
import os
from collections import OrderedDict
import xmltodict

'''
    This module contains a couple of functions that will parse XML files (assuming to be located in ./xml/ and return (yield)
    useful data objects that can be processed / analysed or stored to a database etc.
    
    The data below for game Twilight Struggle is an example of what each data object contains, formatted as JSON:

{
    "name": "Twilight Struggle",
    "yearpublished": "2005",
    "description": "&quot;Now the trumpet summons us again, not as a call to bear arms, though arms we need; not as a call to battle, though embattled we are &ndash; but a call to bear the burden of a long twilight struggle\t&quot;&#10;&ndash; John F. Kennedy&#10;&#10;In 1945, unlikely allies toppled Hitler's war machine, while humanity's most devastating weapons forced the Japanese Empire to its knees in a storm of fire. Where once there stood many great powers, there then stood only two. The world had scant months to sigh its collective relief before a new conflict threatened. Unlike the titanic struggles of the preceding decades, this conflict would be waged not primarily by soldiers and tanks, but by spies and politicians, scientists and intellectuals, artists and traitors. Twilight Struggle is a two-player game simulating the forty-five year  dance of intrigue, prestige, and occasional flares of warfare between the Soviet Union and the United States. The entire world is the stage on which these two titans fight to make the world safe for their own ideologies and ways of life. The game begins amidst the ruins of Europe as the two new &quot;superpowers&quot; scramble over the wreckage of the Second World War, and ends in 1989, when only the United States remained standing.&#10;&#10;Twilight Struggle inherits its fundamental systems from the card-driven classics We the People and Hannibal: Rome vs. Carthage. It is a quick-playing, low-complexity game in that tradition. The game map is a world map of the period, whereon players move units and exert influence in attempts to gain allies and control for their superpower. As with GMT's other card-driven games, decision-making is a challenge; how to best use one's cards and units given consistently limited resources?&#10;&#10;Twilight Struggle's Event cards add detail and flavor to the game. They cover a vast array of historical happenings, from the Arab-Israeli conflicts of 1948 and 1967, to Vietnam and the U.S. peace movement, to the Cuban Missile Crisis and other such incidents that brought the world to the brink of nuclear annihilation. Subsystems capture the prestige-laden Space Race as well as nuclear tensions, with the possibility of game-ending nuclear war.&#10;&#10;Components (original edition):&#10;&#10;&#10;     228 full colour counters &#10;     22&quot;x34&quot; full colour map &#10;     103 event cards &#10;     2 six-sided dice&#10;     1 24-page rulebook&#10;     2 full colour player aid cards&#10;&#10;&#10;Components (2009 Deluxe edition and after)&#10;&#10;     260 full colour counters &#10;     22&quot;x34&quot; mounted map with revised graphics&#10;     110 event cards&#10;     2 six-sided dice&#10;     1 24-page rulebook&#10;     2 full colour player aid cards&#10;&#10;&#10;&#10;&#10;TIME SCALE:     approx. 3-5 years per turn&#10;MAP SCALE:     Point-to-point system&#10;UNIT SCALE:     Influence markers&#10;NUMBER OF PLAYERS:     2&#10;&#10;DESIGNER: Ananda Gupta &amp; Jason Matthews&#10;MAP, CARD, &amp; COUNTER ART: Mark Simonitch&#10;&#10;&#10;A deluxe edition, published in 2009 includes the following changes from the basic game:&#10;&#10;     Mounted map with revised graphics&#10;     Two double-thick counter sheets with 260 counters&#10;     Deck of 110 event cards (increased from 103)&#10;     Revised rules and player aid cards&#10;     Revised at start setup and text change for card #98 Aldrich Ames&#10;&#10;&#10;&#10;&#10;Upgrade kit for the owners of the previous version includes the following:&#10;&#10;     Mounted Map with revised graphics&#10;     New card decks&#10;     Updated Rules &amp; Charts&#10;&#10;&#10;&#10;&#10;",
    "image": "https://cf.geekdo-images.com/original/img/ZPnnm7v2RTJ6fAZeeseA5WbC9DU=/0x0/pic361592.jpg",
    "thumbnail": "https://cf.geekdo-images.com/thumb/img/mEmeJrI3AbGTpWyeFOZnR0s_LcY=/fit-in/200x150/pic361592.jpg",
    "minplayers": "2",
    "maxplayers": "2",
    "minage": "13",
    "integration": [],
    "mechanics": [
        "Area Control / Area Influence",
        "Campaign / Battle Card Driven",
        "Dice Rolling",
        "Hand Management",
        "Simulation",
        "Simultaneous Action Selection"
    ],
    "publishers": [
        "GMT Games",
        "(Self-Published)",
        "Asterion Press",
        "Bard Centrum Gier",
        "Chrononauts Games",
        "Devir",
        "DiceTree Games",
        "GaGa Games",
        "MINDOK",
        "PHALANX",
        "Udo Grebe Gamedesign",
        "Wargames Club Publishing"
    ],
    "implementations": [],
    "artists": [
        "Viktor Csete",
        "Rodger B. MacGowan",
        "Chechu Nieto",
        "Guillaume Ries",
        "Mark Simonitch"
    ],
    "families": [
        "Cold War",
        "Country: Soviet Union",
        "Country: USA",
        "Historical Figures:  Fidel Castro",
        "Twilight Struggle"
    ],
    "categories": [
        "Modern Warfare",
        "Political",
        "Wargame"
    ],
    "expansions": [
        "Twilight Struggle: \"Anni di Piombo\" Promo Card",
        "Twilight Struggle: \"Gladio\" Promo Card",
        "Twilight Struggle: \"Pakt Bagdadzki\" and \"Stan Wojenny\" Promo Cards",
        "Twilight Struggle: \"Referendum NATO\" Promo Card",
        "Twilight Struggle: \"\u0424\u0438\u043d\u043b\u044f\u043d\u0434\u0438\u0437\u0430\u0446\u0438\u044f\" Promo Card",
        "Twilight Struggle: Promo Deck",
        "Twilight Struggle: Regime of the Colonels Promo Card",
        "Twilight Struggle: Turn Zero",
        "Twilight Struggle: Turn Zero and Promo Packs"
    ],
    "designers": [
        "Ananda Gupta",
        "Jason Matthews"
    ],
    "ratings_usersrated": "35254",
    "ratings_average": "8.32142",
    "ratings_bayesaverage": "8.17032",
    "ratings_stddev": "1.58176",
    "ratings_median": "0",
    "ratings_owned": "48489",
    "ratings_trading": "800",
    "ratings_wanting": "1344",
    "ratings_wishing": "9027",
    "ratings_numcomments": "7863",
    "ratings_numweights": "3277",
    "ratings_averageweight": "3.5685"
}
'''

def get_from_node(node_obj, name='@value', first_if_list=False):
    try:
        if isinstance(node_obj, str):
            return node_obj
        elif isinstance(node_obj, list):
            if first_if_list:
                return node_obj[0][name]
            else:
                return node_obj

        elif isinstance(node_obj, OrderedDict):
            return node_obj[name]
        else:
            return node_obj
    except Exception as e:
        return None

def get_from_misc(misc, name):
    result = list()
    for obj in misc:
        if obj['@type'] == name:
            result.append(obj['@value'])
    return result

def extract_game_data(data_dict):
    gd = dict()

    # All data lies, here, just shorten
    game_item = data_dict['items']['item']

    #
    # BASIC DATA
    #
    gd['name'] = get_from_node(game_item['name'], first_if_list=True)
    gd['yearpublished'] = get_from_node(game_item['yearpublished'])
    gd['description'] = get_from_node(game_item['description'])
    gd['image'] = get_from_node(game_item.get('image', None))   # Seem to be missing sometimes
    gd['thumbnail'] = get_from_node(game_item.get('thumbnail', None))

    gd['playingtime'] = get_from_node(game_item['playingtime'])
    gd['minplaytime'] = get_from_node(game_item['minplaytime'])
    gd['maxplaytime'] = get_from_node(game_item['maxplaytime'])

    gd['minplayers'] = get_from_node(game_item['minplayers'])
    gd['maxplayers'] = get_from_node(game_item['maxplayers'])
    gd['minage'] = get_from_node(game_item['minage'])

    #
    # DETAILED DATA
    #
    # The node "link" contains more useful data that can be extracted further:

    # misc_types is any of =
    #  {
    #   'boardgameintegration',
    #   'boardgamemechanic',
    #   'boardgamecompilation',
    #   'boardgamepublisher',
    #   'boardgameimplementation',
    #   'boardgameartist',
    #   'boardgamefamily',
    #   'boardgamecategory',
    #   'boardgameexpansion',
    #   'boardgamedesigner'
    # }
    #
    misc = get_from_node(game_item['link'])
    gd['integration'] = get_from_misc(misc, 'boardgameintegration')
    gd['mechanics'] = get_from_misc(misc, 'boardgamemechanic')
    gd['publishers'] = get_from_misc(misc, 'boardgamepublisher')
    gd['implementations'] = get_from_misc(misc, 'boardgameimplementation')
    gd['artists'] = get_from_misc(misc, 'boardgameartist')
    gd['families'] = get_from_misc(misc, 'boardgamefamily')
    gd['categories'] = get_from_misc(misc, 'boardgamecategory')
    gd['expansions'] = get_from_misc(misc, 'boardgameexpansion')
    gd['designers'] = get_from_misc(misc, 'boardgamedesigner')

    #
    # RATING DATA
    # ratings contains: ['usersrated', 'average', 'bayesaverage', 'ranks', 'stddev', 'median', 'owned', 'trading', 'wanting', 'wishing', 'numcomments', 'numweights', 'averageweight']
    #  (all but "ranks" can be obtained through @value
    gd['ratings_usersrated'] = game_item['statistics']['ratings']['usersrated']['@value']
    gd['ratings_average'] = game_item['statistics']['ratings']['average']['@value']
    gd['ratings_bayesaverage'] = game_item['statistics']['ratings']['bayesaverage']['@value']
    gd['ratings_rank_boardgame'] = game_item['statistics']['ratings']['ranks']['rank'][0]['@value']
    gd['ratings_rank_wargame'] = game_item['statistics']['ratings']['ranks']['rank'][1]['@value']
    gd['ratings_stddev'] = game_item['statistics']['ratings']['stddev']['@value']
    gd['ratings_median'] = game_item['statistics']['ratings']['median']['@value']
    gd['ratings_owned'] = game_item['statistics']['ratings']['owned']['@value']
    gd['ratings_trading'] = game_item['statistics']['ratings']['trading']['@value']
    gd['ratings_wanting'] = game_item['statistics']['ratings']['wanting']['@value']
    gd['ratings_wishing'] = game_item['statistics']['ratings']['wishing']['@value']
    gd['ratings_numcomments'] = game_item['statistics']['ratings']['numcomments']['@value']
    gd['ratings_numweights'] = game_item['statistics']['ratings']['numweights']['@value']
    gd['ratings_averageweight'] = game_item['statistics']['ratings']['averageweight']['@value']

    return gd

#
# This generator yields a nice dict that can be processed further
# or transformed to JSON, CSV etc. or stored to a database
#
def game_data_generator(directory='./xml'):

    for filename in os.listdir(directory):

        if not filename.endswith('.xml'):
            continue

        with open(directory + '/' + filename) as file:

            data_dict = xmltodict.parse(file.read())
            game_data = extract_game_data(data_dict)
            game_data['bgg_id'] = filename.replace('.xml', '')
            yield game_data

# Example how to use the generator
def print_all_titles():
    for game_data in game_data_generator():
        print(game_data['name'])


# print_all_titles()