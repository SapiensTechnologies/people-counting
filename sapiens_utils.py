
import numpy as np

class Sapiens:
  def __init__(self):
    pass


  def people_on_output_tensor(self,scores, classes, num_detections,threshold):

  	classes = np.squeeze(classes).astype(np.int32)
  	scores = np.squeeze(scores)

  	scores_of_people = list(filter(lambda x: x >= threshold, scores))

  	classes = classes[:len(scores_of_people)]

  	for i in np.nditer(classes):
  		if i != 1:
  			np.delete(classes,i)


  	num_of_people = len(classes)


  	return print(num_of_people)




