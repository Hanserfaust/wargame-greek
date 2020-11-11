FILENAME=$1

echo "Fetching game data using IDs from file ${FILENAME}"

while read id; do

    if [ ! -f ./xml/${id}.xml ]; then
        echo ${id};
        wget "https://api.geekdo.com/xmlapi2/thing?id=${id}&stats=1" -O - | xmllint --format - > ./xml/${id}.xml
        sleep 2
    else
        echo "File ${id}.xml exists... skipping."
    fi

done <${FILENAME}