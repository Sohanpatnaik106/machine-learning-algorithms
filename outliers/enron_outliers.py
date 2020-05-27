#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data_dict.pop("TOTAL")
data = featureFormat(data_dict, features)


### your code below

for point in data:
	max_bonus = point[1]
	break

for point in data:
	if point[1] > max_bonus:
		max_bonus = point[1]

print max_bonus

for point in data:
	print point[1]

sorted_data = sorted(data, key = lambda x: x[1])

for point in sorted_data:
	print point[1]

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

