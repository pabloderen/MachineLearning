from imagesoup import ImageSoup

soup = ImageSoup()
images = soup.search('"mechanical room"', n_images=100)
count=0
for i in images:
    try:
        
        i.to_file("%s.jpg" % count)
        count +=1
    except:
        pass