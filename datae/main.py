import os
import time
import csv

with open('output.csv', 'w', newline='') as csvfile:	
	writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	writer.writerow(['img_url', 'caption'])
	
	for root, dirs, files in os.walk("."):  
		for filename in files:
			with open(filename, 'r') as myfile:
				print(filename)
				data=myfile.read().replace('\n', '')
				count = 0
				for x in range(1,1000):
					number = "<h1 style='color:red'>"+str(x)+"</h1>"
					if(number in data):
						count = count + 1
						image = data.split(number)[0]
						image = image.split("src=\"")[-1]
						image = image.split("\"")[0]
						
						caption = data.split(number)[1]
						caption = caption.split("</div>")[1]
						writer.writerow([image, caption])