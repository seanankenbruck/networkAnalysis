###############################   Network Analysis of BeerAdvocate Reviews ###################################

# Load packages
import pandas as pd
import numpy as np 
import csv
 
# Load the csv
# We need the following columns: review_overall [3], review_profilename [6], beer_style [7], beer_name [10], beer_beerid  [12]
data = pd.read_csv("C:/Users/Sean Ankenbruck/Desktop/socialmediadata-beeradvocate/beer_sample.csv", header=0,usecols=[3,6,7,10,12])

# First 5 rows
# print data.head()

test = data[data["review_overall"] >= 3.5]
print test.head()

# Create the lists of unique reviewer and beer names

#List unique values in the data['review_profilename'] column
reviewers = test.review_profilename.unique()

#List unique values in the data['beer_name'] column
beers = test.beer_name.unique()

subset = test.pivot_table(values="review_overall", index="review_profilename", columns="beer_name")

print subset

# Create the loops to create intermediary dataframe containing positive reviews
#positive_reviews = pd.DataFrame(index=reviewers, columns=beers)
#positive_reviews = positive_reviews.fillna(0)
#print positive_reviews


# positive_reviews = pd.DataFrame(positive_reviews)

# for i in beers:
# 	for j in beers:
# 		for x in reviewers:
# 			if rating_overall[i] > 3.5 & rating_overall[j] > 3.5:
# 				matrix[i,j] += 1

# count = 0
# for index, row in test.iterrows():
#     for x in reviewers:
#     	for i in beers:
#     		for j in beers:
#     			if row["review_profilename"] ==x and row["beer_name"] == i and row["review_overall"] >= 3.5:
#     				print row
    			
	# 		for j in beers:
	# 			if rating_overall[j] > 3.5:
	# 				matrix[i,j] += 1


# iterate through all combinations of beers
## check if a person has reviewed both and the reviews are > 3.5
### count the number for each