import jetson.inference
import jetson.utils
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage

camera = jetson.utils.videoSource("/dev/video0")      # '/dev/video0' for V4L2
display = jetson.utils.videoOutput("display://0") # 'my_video.mp4' for file

def get_img():
	"""Returns an numpy array of the pixels"""
	img = camera.Capture()
	array = jetson.utils.cudaToNumpy(img)

	return(array)

def process_img(img):
	#Applying Sobel edge detection
	filter_h = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
	filter_v = np.flip(filter.T,axis=0)

	img = ndimage.sobel(img)
	plt.imshow(img)
	plt.show()

	#img = sobel_edge_detection(img, filter, verbose=True)



process_img(get_img())	

	#display.Render(img)
	#display.SetStatus("Marker Detection")
