#!/bin/bash
i=0
for f in /home/max/apps/matchbox-twelvy/raw-images/full/*.jpg
do
	w=`convert $f -format "%w" info:`
	h=`convert $f -format "%h" info:`

	if [ $w -gt 128 ] && [ $w -gt $h ]; then
		
		o=$i
		if [ $i -lt 1000 ]; then
			o="0$o"
		fi

		if [ $i -lt 100 ]; then
			o="0$o"
		fi

		if [ $i -lt 10 ]; then
			o="0$o"
		fi
		o="../images/$o.jpg"
		
		convert $f -resize 128 $o
		convert $o -gravity center -background white -extent 128x128 $o
		echo $o
		((i++))
	fi
done;