i=/home/max/apps/matchbox-twelvy/output/fake_samples_epoch_*.png
o=/home/max/apps/matchbox-twelvy/frames/epoch_
s="*"
n=".png"
x=0
rm $o$s
for f in $i
do
	y="$x"
	if [ $x -lt 10 ]
	then
		y="0$y"
	fi
	if [ $x -lt 100 ]
	then
		y="0$y"
	fi
	if [ $x -lt 1000 ]
	then
		y="0$y"
	fi
	z="$o$y$n"
	convert $f -crop "128x128+390+130" +repage $z
	convert $z -resize 256x256 $z
	echo $z
	x=$((x+1))
done