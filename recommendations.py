# A dictionary of movie critics and their ratings of a small
# set of movies

critics = {
	'Lisa Rose': {
		'Lady in the Water': 2.5,
		'Snakes on a Plane': 3.5,
		'Just My Luck': 3.0,
		'Superman Returns': 3.5,
		'You, Me and Dupree': 2.5,
		'The Night Listener': 3.0
	},
	'Gene Seymour': {
		'Lady in the Water': 3.0,
		'Snakes on a Plane': 3.5,
		'Just My Luck': 1.5,
		'Superman Returns': 5.0,
		'The Night Listener': 3.0,
		'You, Me and Dupree': 3.5
	},
	'Michael Philips': {
		'Lady in the Water': 2.5,
		'Snakes on a Plain': 3.0,
		'Superman Returns': 3.5,
		'The Night Listener': 4.0
	},
	'Claudia Puig': {
		'Snakes on a Plane': 3.5,
		'Just My Luck': 3.0,
		'The Night Listener': 4.5,
		'Superman Returns': 4.0,
		'You, Me and Dupree': 2.0
	},
	'Mick LaSalle': {
		'Lady in the Water': 3.0,
		'Snakes on a Plane': 4.0,
		'Just My Luck': 2.0,
		'Superman Returns': 3.0,
		'The Night Listener': 3.0,
		'You, Me and Dupree': 2.0
	},
	'Jack Matthews': {
		'Lady in the Water': 3.0,
		'Snakes on a Plane': 4.0,
		'The Night Listener': 3.0,
		'Superman Returns': 5.0,
		'You, Me and Dupree': 3.5
	},
	'Toby': {
		'Snakes on a Plane': 4.5,
		'You, Me and Dupree': 1.0,
		'Superman Returns': 4.0
	}
}

from math import sqrt

# Returns a distance-based similarity score for person1 and person2
# Note that this similarity score does not account for consistent grande inflation
# If one person tends to give higher grades than the other, even though both people
# might have similar tastes, their distance will be higher. Still, depending on the
# application, this might be what is expected
def sim_distance(prefs,person1,person2):
	# Get the list of shared_items
	si = {}
	for item in prefs[person1]:
		if item in prefs[person2]:
			si[item]=1

	# if they have no ratins in common, return 0
	if len(si)==0: return 0

	# Add up the squares of all the differences
	sum_of_squares=sum([pow(prefs[person1][item]-prefs[person2][item],2) for item in si])

	return 1/(1+sqrt(sum_of_squares))

def sim_pearson(prefs,p1,p2):
	# Get the list of mutually rated shared_items
	si={}
	for item in prefs[p1]:
		if item in prefs[p2]: si[item]=1

	# Find the number of elements
	n=len(si)

	# if they have no ratings in common, return 0
	if n==0: return 0

	# Add up all the preferences
	sum1=sum([prefs[p1][it] for it in si])
	sum2=sum([prefs[p2][it] for it in si])

	# Sum up the squares
	sum1Sq=sum([pow(prefs[p1][it],2) for it in si])
	sum2Sq=sum([pow(prefs[p2][it],2) for it in si])

	# Sum up the products
	pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])

	# Calculate Pearson score
	num=pSum-(sum1*sum2/n)
	den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
	if den==0: return 0

	r=num/den

	return r
