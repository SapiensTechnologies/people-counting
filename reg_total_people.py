import matplotlib.pyplot as plt
import csv
from sapiens_utils import Sapiens

def plot_results(video_source):

	# mylist = func.sapiens_utils()
	#mylist1 = [12, 10, 11, 11] # prueba
	#mylist2 = ["a", "b", "c", "j"]
	mylist = zip(Sapiens.det_record, Sapiens.time_record)

	with open("register.csv", 'w', newline='') as myfile:
		wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
		wr.writerows(mylist)

	#plt.locator_params(axis='x', nbins=10)
	ax = plt.axes()
	ax.xaxis.set_major_locator(plt.MaxNLocator(8))
	plt.plot(Sapiens.time_record, Sapiens.det_record, marker='o')

	plt.title('Data from the CSV File: People and Time')

	plt.xlabel('Time')
	plt.ylabel('Number of People')

	try:
		if video_source.endswith('.mp4'):
			video_source = video_source[:-4]
		else:
			video_source = "people"
	except:
		video_source = "people"

	plt.savefig(video_source + ".png")

	return print("plot done")