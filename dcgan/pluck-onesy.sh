f=/home/max/apps/matchbox-twelvy/twelvys/twelvy.png
o=/home/max/apps/matchbox-twelvy/twelvys/onesy_
s="*"
n=".png"
rm $o$s
for i in {0..7}
do
	x=$((i*130))
	for j in {0..7}
	do
		y=$((j*130))
		a="+$x"
		b="+$y"
		z="$o$i$j$n"
		convert $f -crop "128x128$a$b" +repage $z
		convert $z -resize 256x256 $z
		echo $z
	done
done