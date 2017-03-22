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

test = data[data["review_overall"] < 3.5]
#print test.head()


# Create a pivot table from the dataframe with profile names as indexes
subset = test.pivot_table(values="review_overall", index="review_profilename", columns="beer_name")
subset = subset.fillna(0)

# Due to memory constraints, we have to work in increments (parallel processing would remedy this)
subset = subset[500:]

# Output review_profilename values to csv in order to use them in the reviewers variable below
#subset.to_csv('C:\...\subset500_end.csv')

# Create the lists of unique reviewer(subset) and beer names(all unique)

#List unique values in the data['review_profilename'] column -> must obtain these values in the subset.to_csv line above
reviewers = ["jtierney89",	"juju7",	"jujubeast6000",	"julian",	"jwinship83",	"kajerm",	"katan",	"kazmanbrew",	"kbub6f",	"kdoc8",	"kegger22",	"kgotcher",	"kimcgolf",	"kingcrowing",	"kmpitz2",	"lackenhauser",	"lacqueredmouse",	"leaddog",	"lovindahops",	"luxbwin",	"malty",	"marlinsfan4",	"marty21",	"matjack85",	"mattcrill",	"maxpower",	"mcann2pu",	"mccordbmw",	"mcmidc",	"mduncan",	"meathookjones",	"meatyard",	"mentor",	"merlin48",	"metter98",	"mhewes",	"mikesgroove",	"mithrascruor",	"mjaskula",	"mjhorn",	"mjl21",	"mjuthewise",	"mntlover",	"mobyfann",	"mooseisloose",	"morimech",	"mothman",	"moulefrite",	"moz9",	"mrandypandy",	"mrfrancis",	"mudbug",	"mulder1010",	"nekronos",	"nflmvp",	"ngandhi",	"ngeunit1",	"nickd717",	"nickfl",	"nickthegun12",	"nickynick",	"nokes",	"northaustin",	"northyorksammy",	"nortmand",	"notchucknorris",	"nppeders",	"nrmiller",	"nsmartell",	"number1bum",	"oberon",	"objectivemonkey",	"oggg",	"olmatty",	"onix1agr",	"output01x",	"paterlodie",	"patvibrato",	"paulieatworld",	"pburland23",	"peabody",	"pecokid",	"pgenius",	"philbertk",	"plaid75",	"pmatz2",	"portia99",	"ppoitras",	"prototypic",	"psbmumbles",	"psuKinger",	"pwoods",	"pzrhsau",	"quaybr",	"rajendra82",	"rand",	"raoulduke37",	"rastaman",	"rfgetz",	"rhoadsrage",	"riored4v",	"ritzkiss",	"robkeely",	"roblowther",	"rockstarnati",	"rodenbach99",	"russpowell",	"ryanocerus",	"rye726",	"saintwarrick",	"sbe1",	"schmitter",	"schoolteacher",	"scooter231",	"scootny",	"scottyf1",	"seand",	"seaoflament",	"sethmeister",	"sfprint",	"shaunb81",	"shbobdb",	"sholland119",	"silentjay",	"sinstaineddemon",	"siradmiralnelson",	"sixerofelixir",	"slitherySOB",	"snowench",	"sockeye101",	"sommersb",	"soper2000",	"spointon",	"squilky",	"srandycarter",	"starrdogg",	"stcules",	"stegmakk",	"steinlifter",	"stephendr",	"strangemusic",	"stulowitz",	"suedehead",	"sulldaddy",	"superdedooperboy",	"sweetkness",	"swid",	"t420o",	"taez555",	"tapman",	"tastybeer",	"tchenery",	"tedpeer",	"tempest",	"tgbljb",	"thagr81us",	"the42ndtourist",	"thekevlarkid",	"therica",	"tigg924",	"timtim",	"tjkinate",	"tkepx182",	"tmoneyba",	"tpd975",	"treque",	"trevorjn06",	"trumick",	"twbrewer",	"twi1609372",	"twiggamortis420",	"twilight",	"tzieser",	"ujsplace",	"ultralarry2006",	"vickersspitfire",	"walteez",	"warnerry",	"warrenc",	"wavz",	"wcudwight",	"weasbri",	"weeare138",	"whitemomba",	"whynot44",	"wnh",	"woemad",	"womencantsail",	"woodychandler",	"woosterbill",	"wspscott",	"yakko",	"yemenmocha",	"younger35",	"zander4dawin",	"zeff80",	"zymurgy4all"]
print len(reviewers)

#List unique values in the data['beer_name'] column -> all unique beers regardless of subset
beers = test.beer_name.unique()
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
positive_reviews.to_csv('C:\...\_adjacency500_ALL.csv')

# Next -> get data ready for network analysis