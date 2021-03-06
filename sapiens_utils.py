
import numpy as np
import time
from math import ceil

VIDEO_FPS = 25

class Sapiens:
	det_record = []
	time_record = []

	def __init__(self):
		pass


	def people_on_output_tensor(self, scores, classes, num_detections,
								threshold, frames_processed):

		classes = np.squeeze(classes).astype(np.int32)
		scores = np.squeeze(scores)

		scores_of_people = list(filter(lambda x: x >= threshold, scores))

		classes = classes[:len(scores_of_people)]

		try:
			classes = np.delete(classes, np.where(classes != 1))

		except:
			pass


		num_of_people = len(classes)
		self.det_record.append(num_of_people)
		video_second = ceil(frames_processed / VIDEO_FPS)
		self.time_record.append(video_second)

		return print(num_of_people)
