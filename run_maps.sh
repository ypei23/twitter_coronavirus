#!/bin/sh
for file in '/data/Twitter dataset/'geoTwitter20-*.zip; do
    $(./src/map.py --input_path="$file") &
    #echo "$file"
done
