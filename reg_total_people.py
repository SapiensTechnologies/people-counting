import csv
from datetime import datetime
# import sapiens_utils

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

# mylist = func.sapiens_utils()
mylist1 = [12, 10, 11, 11] # prueba
mylist2 = ["a", "b", "c", "j"]
mylist = zip(mylist1, mylist2)

with open("register.csv", 'w', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     wr.writerows(mylist)