import csv

from wgg.bgg.xml_processor import game_data_generator


csv_file = "games.csv"

try:
    with open(csv_file, 'w') as csvfile:

        game_data = list(game_data_generator())

        writer = csv.DictWriter(csvfile, fieldnames=game_data[0].keys())
        writer.writeheader()

        for data in game_data:
            writer.writerow(data)

except IOError:
    print("I/O error")
