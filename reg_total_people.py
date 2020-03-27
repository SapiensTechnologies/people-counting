import matplotlib.pyplot as plt
import csv
from sapiens_utils import Sapiens
from sapiens_utils import VIDEO_FPS
from math import ceil

def plot_results(video_source):

	try:
		if video_source.endswith('.mp4'):
			video_source = video_source[:-4]
		else:
			video_source = "people"
	except:
		video_source = "people"

	avg_det_record = []
	for i in range(ceil(len(Sapiens.det_record) / VIDEO_FPS)):
		if ((i+1)*VIDEO_FPS) < len(Sapiens.det_record):
			gen_list = Sapiens.det_record[i*VIDEO_FPS:((i+1)*VIDEO_FPS)-1]
		else:
			gen_list = Sapiens.det_record[i*VIDEO_FPS:]

		avg_det_record.append(round(sum(gen_list) / len(gen_list)))

	avg_time_record = list(set(Sapiens.time_record))
	mylist = zip(avg_det_record, avg_time_record)

	with open(video_source + ".csv", 'w', newline='') as myfile:
		wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
		wr.writerows(mylist)

	#plt.locator_params(axis='x', nbins=10)
	ax = plt.axes()
	ax.xaxis.set_major_locator(plt.MaxNLocator(16))
	plt.plot(avg_time_record, avg_det_record, marker='o')

	plt.title('Data from the CSV File: People and Time')

	plt.xlabel('Time (Sec)')
	plt.ylabel('Number of People')

	plt.savefig(video_source + ".png")

	return print("plot done")
