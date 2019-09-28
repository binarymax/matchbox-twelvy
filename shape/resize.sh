#!/bin/bash
i=0
for f in /home/max/apps/matchbox-twelvy/raw-images/jpg/*.jpg
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
		o="../jpg-images/128/$o.jpg"
		
		convert $f -resize 128 -quality 100 $o
		convert $o -gravity center -background white -extent 128x128 -quality 100 $o
		echo $o
		((i++))

		p=$i
		if [ $i -lt 1000 ]; then
			p="0$p"
		fi

		if [ $i -lt 100 ]; then
			p="0$p"
		fi

		if [ $i -lt 10 ]; then
			p="0$p"
		fi
		p="../jpg-images/128/$p.jpg"
		
		convert $o -flop -quality 100 $p
		echo $p
		((i++))
	fi
done;