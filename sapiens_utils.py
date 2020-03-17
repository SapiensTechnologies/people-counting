
import numpy as np
from datetime import datetime

class Sapiens:
	det_record = []
	time_record = []
  
	def __init__(self):
		pass


	def people_on_output_tensor(self,scores, classes, num_detections,threshold):

		classes = np.squeeze(classes).astype(np.int32)
		scores = np.squeeze(scores)

		scores_of_people = list(filter(lambda x: x >= threshold, scores))

		classes = classes[:len(scores_of_people)]
		
		try:
			classes = np.delete(classes, np.where(classes != 1))
			
		except:
			pass


		num_of_people = len(classes)
		print(classes)
		self.det_record.append(num_of_people)
		now = datetime.now()
		current_time = now.strftime("%H:%M:%S")
		self.time_record.append(current_time)

		return print(num_of_people)




