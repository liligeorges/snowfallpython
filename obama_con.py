from PIL import Image
im = Image.open("hihihi.")
picture = list(im.getdata())
#print(picture)
#im.show()
DARKBLUE = (0, 51, 76)
RED = (217,26, 33)
LIGHTBLUE = (112, 150, 158)
YELLOW = (252, 227, 166)
newCOLOR = [] 


# Process every pixel
for i in picture: 
	intensity = i[0] + i[1] + i[2]
	if intensity <= 182:
		newCOLOR.append(DARKBLUE)
	elif intensity >= 183 and intensity <= 364:
		newCOLOR.append(RED)
	elif intensity >= 365 and intensity <=546:
		newCOLOR.append(LIGHTBLUE)
	elif intensity >= 547:
		newCOLOR.append(YELLOW)
im.putdata(newCOLOR)
im.show()

