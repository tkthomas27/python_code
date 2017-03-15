
# https://www.reddit.com/r/CollegeBasketball/comments/5xir8t/calculating_win_probability_and_margin_of_victory/

# things to improve
# region definition
# addint to results dict
# region function
# final four function: puts together winners and then runs region function
# develop tournament function
# better metric
# simulation: compute probability of victory -> 
    # randomly draw 100,000 [0,1], if prob>draw then advance team
    # compute which team has most advances



import pandas as pd
tourney = pd.read_csv("/Users/kthomas1/github/python_code/bracketsim_kenpom.csv",delimiter="\t")

east = tourney.loc[tourney.region == "east",['seed','team','adjem','adjt','adjo','adjd','luck']]
east.name = "east"
west = tourney.loc[tourney.region == "west",['seed','team','adjem','adjt','adjo','adjd','luck']]
west.name = "west"
south = tourney.loc[tourney.region == "south",['seed','team','adjem','adjt','adjo','adjd','luck']]
south.name = "south"
midwest = tourney.loc[tourney.region == "midwest",['seed','team','adjem','adjt','adjo','adjd','luck']]
midwest.name = "midwest"

results = {'east':{'round1':"x",'round2':"x",'round3':"x",'round4':"x"},
    'south':{'round1':"x",'round2':"x",'round3':"x",'round4':"x"},
    'midwest':{'round1':"x",'round2':"x",'round3':"x",'round4':"x"},
    'west':{'round1':"x",'round2':"x",'round3':"x",'round4':"x"}
}

def split_list(a_list):
    half = int(len(a_list)/2)
    dat1 = a_list[:half]
    dat2 = a_list[half:]
    dat1 = dat1.reset_index(drop=True)
    dat2 = dat2.reset_index(drop=True)
    return dat1, dat2

def rounds(teams):
    
    if len(teams) == 2:
        teams = teams.reset_index(drop=True)
        margin = ((teams.adjem[0]-teams.adjem[1])*(teams.adjt[0] + teams.adjt[1]))/200
        winners.append(teams.seed[0]) if margin>0 else winners.append(teams.seed[1])
        
    if len(teams) < 2:
        return 0
        
    t1, t2 = split_list(teams)
    
    rounds(t1)
    rounds(t2)
    
    return winners

# east
winners = []
round1_seeds = rounds(east)
results['east']['round1'] = round1_seeds
round1 = east[east.seed.isin(round1_seeds)]

winners = []
round2_seeds = rounds(round1)
results['east']['round2'] = round2_seeds
round2 = east[east.seed.isin(round2_seeds)]

winners = []
round3_seeds = rounds(round2)
results['east']['round3'] = round3_seeds
round3 = east[east.seed.isin(round3_seeds)]

winners = []
round4_seeds = rounds(round3)
results['east']['round4'] = round4_seeds
round4 = east[east.seed.isin(round4_seeds)]

# south
winners = []
round1_seeds = rounds(south)
results['south']['round1'] = round1_seeds
round1 = south[south.seed.isin(round1_seeds)]

winners = []
round2_seeds = rounds(round1)
results['south']['round2'] = round2_seeds
round2 = south[south.seed.isin(round2_seeds)]

winners = []
round3_seeds = rounds(round2)
results['south']['round3'] = round3_seeds
round3 = south[south.seed.isin(round3_seeds)]

winners = []
round4_seeds = rounds(round3)
results['south']['round4'] = round4_seeds
round4 = south[south.seed.isin(round4_seeds)]

# west
winners = []
round1_seeds = rounds(west)
results['west']['round1'] = round1_seeds
round1 = west[west.seed.isin(round1_seeds)]

winners = []
round2_seeds = rounds(round1)
results['west']['round2'] = round2_seeds
round2 = west[west.seed.isin(round2_seeds)]

winners = []
round3_seeds = rounds(round2)
results['west']['round3'] = round3_seeds
round3 = west[west.seed.isin(round3_seeds)]

winners = []
round4_seeds = rounds(round3)
results['west']['round4'] = round4_seeds
round4 = west[west.seed.isin(round4_seeds)]

# midwest
winners = []
round1_seeds = rounds(midwest)
results['midwest']['round1'] = round1_seeds
round1 = midwest[midwest.seed.isin(round1_seeds)]

winners = []
round2_seeds = rounds(round1)
results['midwest']['round2'] = round2_seeds
round2 = midwest[midwest.seed.isin(round2_seeds)]

winners = []
round3_seeds = rounds(round2)
results['midwest']['round3'] = round3_seeds
round3 = midwest[midwest.seed.isin(round3_seeds)]

winners = []
round4_seeds = rounds(round3)
results['midwest']['round4'] = round4_seeds
round4 = midwest[midwest.seed.isin(round4_seeds)]


final_four1 = pd.DataFrame()
final_four2 = pd.DataFrame()
final_four1 = final_four1.append(west[west.seed == results['west']['round4']])
final_four1 = final_four1.append(east[east.seed == results['east']['round4']])
final_four2 = final_four2.append(south[south.seed == results['south']['round4']])
final_four2 = final_four2.append(midwest[midwest.seed == results['midwest']['round4']])

final_four1 = final_four1.reset_index(drop=True)
final_four2 = final_four2.reset_index(drop=True)

# rounds function works here but we need to see the names; originally just had one final_four group; but split into two

monday = pd.DataFrame()
margin = ((final_four1.adjem[0]-final_four1.adjem[1])*(final_four1.adjt[0] + final_four1.adjt[1]))/200
monday = monday.append(final_four1.loc[0]) if margin>0 else monday.append(final_four1.loc[1])

margin = ((final_four2.adjem[0]-final_four2.adjem[1])*(final_four2.adjt[0] + final_four2.adjt[1]))/200
monday = monday.append(final_four2.loc[0]) if margin>0 else monday.append(final_four2.loc[1])

margin = ((monday.adjem[0]-monday.adjem[1])*(monday.adjt[0] + monday.adjt[1]))/200
champ = monday.loc[0] if margin>0 else monday.loc[1]

        
# need to create whole bracket simulation
    # one random draw
    # gen basic prob
    # if prob>.8(<.2) add luck to 0(1)
    # if prob>.9(<.1) add luck x5
    # if prob>.95(<.05) add luck x10
    # if prob>.5 add(subtract) .15 if AdjOE is greater(less than)
    # if prob<.5 add(subtract) .15 if AdjoE is greater(less than)
    # winning team progresses
    # eventually simulate whole brackets; now just game by game

# simulation
import random
import math
random.seed(342)

# CDF = 0.5 * (1 + erf((x - u)/(sigma*sqrt(2)))
tset = south.iloc[4:6]
tset = tset.reset_index(drop=True)
margin = ((tset.adjem[0]-tset.adjem[1])*(tset.adjt[0] + tset.adjt[1]))/200
prob = 1-(0.5 * (1 + math.erf((0-margin)/(11*math.sqrt(2)))))
probo = 1-(0.5 * (1 + math.erf((0-margin)/(11*math.sqrt(2)))))

count = 0
for rep in range(10000):
    x=random.uniform(0,1)
    prob = 1-(0.5 * (1 + math.erf((0-margin)/(11*math.sqrt(2)))))
    prob = prob+tset.luck[0] if x>.8 else prob
    prob = prob+(2*tset.luck[0]) if x>.9 else prob
    prob = prob+(10*tset.luck[0]) if x>.97 else prob
    
    prob = prob+.15 if tset.adjo[0]>tset.adjo[1] and x>.5 else prob
    prob = prob-.15 if tset.adjo[0]<tset.adjo[1] and x>.5 else prob
    
    prob = prob+.15 if tset.adjd[0]<tset.adjd[1] and x<.5 else prob
    prob = prob-.15 if tset.adjd[0]>tset.adjd[1] and x<.5 else prob
    
    if prob>x:
        count += 1
    
print("win") if count>7000 else print("null")
print("lose") if count<3000 else print("null")
print("win") if count<7000 and count>3000 and x>.5 else print("null")
print("lose") if count<7000 and count>3000 and x<.5 else print("null")






tset = east.iloc[0:2]
tset = tset.reset_index(drop=True)
margin = ((tset.adjem[0]-tset.adjem[1])*(tset.adjt[0] + tset.adjt[1]))/200
probo = 1-(0.5 * (1 + math.erf((0-margin)/(11*math.sqrt(2)))))
prob = 1-(0.5 * (1 + math.erf((0-margin)/(11*math.sqrt(2)))))
x=random.uniform(0,1)
prob = prob+tset.luck[0] if x>.8 else prob
prob = prob+(2*tset.luck[0]) if x>.9 else prob
prob = prob+(10*tset.luck[0]) if x>.97 else prob
    
prob = prob+.15 if tset.adjo[0]>tset.adjo[1] and x>.5 else prob
prob = prob-.15 if tset.adjo[0]<tset.adjo[1] and x>.5 else prob
    
prob = prob+.15 if tset.adjd[0]>tset.adjd[1] and x<.5 else prob
prob = prob-.15 if tset.adjd[0]<tset.adjd[1] and x<.5 else prob


