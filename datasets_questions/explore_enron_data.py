#!/usr/bin/python

"""
    starter code for exploring the Enron dataset (emails + finances)
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "People count:", len(enron_data)

feature_count = 0
for k in enron_data:
    if feature_count <= len(enron_data[k]):
        feature_count = len(enron_data[k])
print "Feature count:", feature_count

poi_records = 0
for k in enron_data:
    if enron_data[k].get('poi'):
        poi_records += 1
print "POI record:", poi_records

print "Total stock:", enron_data['PRENTICE JAMES']['total_stock_value']

print "Email messages to poi:", enron_data['COLWELL WESLEY']['from_this_person_to_poi']

print "Stock options", enron_data['SKILLING JEFFREY K']['exercised_stock_options']

print "Lay Total Payment", enron_data['LAY KENNETH L']['total_payments']

print "Skilling Total Payment", enron_data['SKILLING JEFFREY K']['total_payments']

print "Fastow Total Payment", enron_data['FASTOW ANDREW S']['total_payments']

salary_count = 0
email_count = 0
email_non_salary = 0
non_email_non_salary =0
for k in enron_data:
    if enron_data[k].get('salary') != 'NaN':
        salary_count += 1

    if enron_data[k].get('email_address') != 'NaN':
        email_count += 1

print "Salary count", salary_count
print "Email count", email_count

total_payment_count = 0
for k in enron_data:
    if enron_data[k].get('total_payments') == 'NaN':
        total_payment_count += 1
print "Total Payment Count", total_payment_count
print "Total Payment Person Percentage:", total_payment_count * 1.0 / len(enron_data) * 100

total_payment_poi_count = 0
for k in enron_data:
    if enron_data[k].get('poi') and enron_data[k].get('total_payments') == 'NaN':
        total_payment_poi_count += 1

print "Total Payment POI Count", total_payment_poi_count
print "Total Payment POI Percentage:", total_payment_poi_count * 1.0 / poi_records * 100

