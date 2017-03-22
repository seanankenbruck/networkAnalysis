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
#print test.head()


# Create a pivot table from the dataframe with profile names as indexes
subset = test.pivot_table(values="review_overall", index="review_profilename", columns="beer_style")
subset = subset.fillna(0)

# Due to memory constraints, we have to work in increments (parallel processing would remedy this)
subset = subset[:100]

# Output review_profilename values to csv in order to use them in the reviewers variable below
#subset.to_csv('C:\Users\Sean Ankenbruck\Desktop\socialmediadata-beeradvocate\code\subset100.csv')

# Create the lists of unique reviewer(subset) and beer names(all unique)

#List unique values in the data['review_profilename'] column -> must obtain these values in the subset.to_csv line above
reviewers = ["100floods",	"3Vandoo",	"ADR",	"ADZA",	"AKBelgianBeast",	"AMo",	"AaronRed",	"Ackman",	"AdamGarcia",	"Aenema",	"Agold",	"AltBock",	"Anthony1",	"Atron67",	"Augustiner719",	"Axic10",	"AylwinForbes",	"BBP",	"BDJake",	"BDTyre",	"BEERchitect",	"Backer2004",	"BardofBeer",	"BeardedBoffin",	"BeerAngel",	"BeerFMAndy",	"BeerForMuscle",	"BeerLover48Fan",	"BeerLover729",	"BeerLover99",	"BeerMansGirl",	"BeerResearcher",	"BeerSox",	"BeerTaster",	"Bierman9",	"BigPlay1824",	"Bighuge",	"BitteBier",	"BlackHaddock",	"Blakaeris",	"BoitSansSoif",	"Bonis",	"Brad007",	"BradLikesBrew",	"Brent",	"BrewMaster",	"BrewnZ",	"Brewnami",	"Brian700",	"BuckSpin",	"BuckeyeNation",	"Buebie",	"Bung",	"CaptDavyJones",	"ChainGangGuy",	"Chaney",	"CharlesRiver",	"Chaz",	"ClassyLadyJen",	"Clembo1957",	"ColdPoncho",	"CrashWorship",	"Crosling",	"DNA",	"Dave128",	"DaveHS",	"DeaconBluez",	"Dentist666",	"Derek",	"Dertbert",	"DesMoinesMike",	"Deuane",	"DijonKetchup",	"DirtyPenny",	"Dogbrick",	"DoktaHops",	"DovaliHops",	"DrDemento456",	"DrJay",	"Draughted",	"Drew966",	"DrewV",	"Drinkerofales",	"DrunkMcDermott",	"Dubbercody",	"Duff27",	"Dukeofearl",	"ElGrecoVerde",	"ElGuapo",	"FickleBeast",	"Flightoficarus",	"FosterJM",	"FreshHawk",	"Fuzzy1",	"GCBrewingCo",	"GabrielM",	"Gaisgeil",	"GallowsThief",	"GarrettB",	"Gavage"]
print len(reviewers)

#List unique values in the data['beer_name'] column -> all unique beers regardless of subset
beers = test.beer_style.unique()
print len(beers)


# Create the adjacency matrix (beers x beers) -> beers are the nodes

positive_reviews = pd.DataFrame(index = beers, columns = beers)
positive_reviews = positive_reviews.fillna(0)
# print positive_reviews.head()


# Calculate all reviews for each beer
for x in reviewers:
	for i in beers:
		for j in beers:
			if subset.get_value(x,i) and subset.get_value(x,j):
				positive_reviews.loc[i,j] += 1


# Output results in increments (4 in total)
positive_reviews.to_csv('C:\Users\Sean Ankenbruck\Desktop\socialmediadata-beeradvocate\code\_adjacency_100style.csv')

# Next -> get data ready for network analysis