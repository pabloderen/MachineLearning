# MachineLearning
Machine Learning notes


#Prepare the dataset
##	Get images from google search
	google-search.py
##	Remove duplicate
	duplicated.py
##	Resize images
Create bash script with:
'''
count=0
for pic in *.jpg
do
 convert $pic -resize 800x600! resize$count.jpg
 ((++count))
done
'''
##	Label images
	https://github.com/tzutalin/labelImg
