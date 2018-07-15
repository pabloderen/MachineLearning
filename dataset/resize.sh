count=0
for pic in *.jpg
do
 convert $pic -resize 800x600! resize$count.jpg
 ((++count))
done
