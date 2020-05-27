#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))
#enron_data = pickle.load(open("../final_project/poi_names.txt", "rb"))

print len(enron_data)
for key, value in enron_data.items():
	print len(value)
	break;

no_of_poi = 0
for personNames, features in enron_data.items():
	for key in features:
		if key == "poi": 
			if features[key] == 1:
				no_of_poi = no_of_poi + 1

			
print no_of_poi


for personNames, features in  enron_data.items():
	if personNames == "PRENTICE JAMES":
		for key in features:
			if key == "total_stock_value":
				print features[key]
				break

for personNames, features in  enron_data.items():
	if personNames == "COLWELL WESLEY":
		for key in features:
			if key == "from_this_person_to_poi":
				print features[key]
				break

for personNames, features in  enron_data.items():
	if personNames == "SKILLING JEFFREY K":
		for key in features:
			if key == "exercised_stock_options":
				print features[key]
				break

for personNames, features in enron_data.items():
	if personNames == "SKILLING JEFFREY K":
		for key in features:
			if key == "total_payments":
				print "Skilling : ", features[key]

for personNames, features in enron_data.items():
	if personNames == "LAY KENNETH L":
		for key in features:
			if key == "total_payments":
				print "lay : ", features[key]

for personNames, features in enron_data.items():
	if personNames == "FASTOW ANDREW S":
		for key in features:
			if key == "total_payments":
				print "fastow : ", features[key]


no_of_quantified_salary = 0 
no_of_email = 0

for personNames, features in enron_data.items():
	for key in features:
		if key == "salary":
			if features[key] != "NaN":
				no_of_quantified_salary = no_of_quantified_salary + 1
		if key == "email_address":
			if features[key] != "NaN":
				no_of_email = no_of_email + 1

print "salary : ", no_of_quantified_salary
print "email : ", no_of_email

no_of_nan_salary = 0

for personNames, features in enron_data.items():
	for key in features:
		if key == "total_payments":
			if features[key] == "NaN":
				no_of_nan_salary = no_of_nan_salary + 1

print no_of_nan_salary

no_of_poi = 0

for personNames, features in enron_data.items():
	for key in features:
		if key == "poi":
			if features[key] == 1:
				for key1 in features:
					if key1 == "total_payments":
						if features[key1] == "NaN":
							no_of_poi = no_of_poi + 1 


print no_of_poi