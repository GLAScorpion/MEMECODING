import os
from PIL import Image
def mySort(e):
	#start index 8
	value=0
	for x in range(3):
		if(e[8+x]!='.'):
			value = value*10 + int(e[8+x])
		else:
			break
	return value
	
def make_gif(frame_folder):
	direct = os.listdir(frame_folder)
	for txt in direct:
		if mySort(txt) < 10:
			os.rename(frame_folder + '/' +txt,frame_folder + '/biglinus00'+str(mySort(txt))+'.jpg')
		elif mySort(txt) < 100:
			os.rename(frame_folder + '/' +txt,frame_folder + '/biglinus0'+str(mySort(txt))+'.jpg')
	#direct.sort(key = mySort)
	''''
	frames = []
	for image in direct:
		frames.append(Image.open(frame_folder + '/' + image))
	frame_one = frames[0]
	frame_one.save("autism.gif", format="GIF", append_images=frames,save_all=True, duration=1, loop=0)
    '''
if __name__ == "__main__":
    make_gif("autism")
