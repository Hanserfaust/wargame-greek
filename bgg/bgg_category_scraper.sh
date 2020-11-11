START=$1
END=$2

echo "Fetching IDs from wargame, category, pages from ${START} to ${END}"

for PAGE in $(seq $START $END); 
	do echo ${PAGE};
	wget -O - "https://boardgamegeek.com/wargames/browse/boardgame/page/${PAGE}?sort=rank&sortdir=asc&limit=20"|grep results_objectname -A 2|grep boardgame|grep -o '/[0-9]\+/'|sed 's/\///g' >> wargame_ids_in_order.txt
	sleep 2
done

