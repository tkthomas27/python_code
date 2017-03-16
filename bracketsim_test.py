
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
import random
import math
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

def win(matchup):

    # reset index to 0,1
    matchup = matchup.reset_index(drop=True)
    # compute margin of victory to get probability of win
    margin = ((matchup.adjem[0]-matchup.adjem[1])*(matchup.adjt[0] + matchup.adjt[1]))/200
    # original probability
    probo = 1-(0.5 * (1 + math.erf((0-margin)/(11*math.sqrt(2)))))
    
    # initialize count
    count = 0
    # simulation
    for rep in range(10000):
        
        # random number
        x=random.uniform(0,1)
        # original probability
        prob = 1-(0.5 * (1 + math.erf((0-margin)/(11*math.sqrt(2)))))
        
        # luck
        if x>.5:
            prob = prob + (matchup.luck[0]*1)
        elif x>.3:
            prob = prob + (matchup.luck[0]*1)            

        if x>.5:
            if matchup.adjo[0]>matchup.adjo[1]:
                prob = prob + .05
            else:
                prob = prob - .05
        else:
            if matchup.adjd[0]<matchup.adjd[1]:
                prob = prob + .05
            else:
                prob = prob - .05
        
        # compare new probability to x, if 
        if prob>x:
            count += 1
    
    winners.append(matchup.seed[0]) if count>9000 else None
    winners.append(matchup.seed[1]) if count<1000 else None
    winners.append(matchup.seed[0]) if count<9000 and count>1000 and x>.5 else None
    winners.append(matchup.seed[1]) if count<9000 and count>1000 and x<.5 else None

def split_list(a_list):
    half = int(len(a_list)/2)
    dat1 = a_list[:half]
    dat2 = a_list[half:]
    dat1 = dat1.reset_index(drop=True)
    dat2 = dat2.reset_index(drop=True)
    return dat1, dat2

def rounds(teams):
    
    if len(teams) == 2:
        win(teams)
        
    if len(teams) < 2:
        return 0
        
    t1, t2 = split_list(teams)
    
    rounds(t1)
    rounds(t2)
    
    return winners


# east
winners = []
round1_seeds = rounds(east)
rnd = east[east['seed'].isin(round1_seeds)].team.tolist()
results['east']['round1'] = rnd
round1 = east[east.seed.isin(round1_seeds)]

winners = []
round2_seeds = rounds(round1)
rnd = east[east['seed'].isin(round2_seeds)].team.tolist()
results['east']['round2'] = rnd
round2 = east[east.seed.isin(round2_seeds)]

winners = []
round3_seeds = rounds(round2)
rnd = east[east['seed'].isin(round3_seeds)].team.tolist()
results['east']['round3'] = rnd
round3 = east[east.seed.isin(round3_seeds)]

winners = []
round4_seeds = rounds(round3)
rnd = east[east['seed'].isin(round4_seeds)].team.tolist()
results['east']['round4'] = rnd
round4 = east[east.seed.isin(round4_seeds)]

# south
winners = []
round1_seeds = rounds(south)
rnd = south[south['seed'].isin(round1_seeds)].team.tolist()
results['south']['round1'] = rnd
round1 = south[south.seed.isin(round1_seeds)]

winners = []
round2_seeds = rounds(round1)
rnd = south[south['seed'].isin(round2_seeds)].team.tolist()
results['south']['round2'] = rnd
round2 = south[south.seed.isin(round2_seeds)]

winners = []
round3_seeds = rounds(round2)
rnd = south[south['seed'].isin(round3_seeds)].team.tolist()
results['south']['round3'] = rnd
round3 = south[south.seed.isin(round3_seeds)]

winners = []
round4_seeds = rounds(round3)
rnd = south[south['seed'].isin(round4_seeds)].team.tolist()
results['south']['round4'] = rnd
round4 = south[south.seed.isin(round4_seeds)]

# west
winners = []
round1_seeds = rounds(west)
rnd = west[west['seed'].isin(round1_seeds)].team.tolist()
results['west']['round1'] = rnd
round1 = west[west.seed.isin(round1_seeds)]

winners = []
round2_seeds = rounds(round1)
rnd = west[west['seed'].isin(round2_seeds)].team.tolist()
results['west']['round2'] = rnd
round2 = west[west.seed.isin(round2_seeds)]

winners = []
round3_seeds = rounds(round2)
rnd = west[west['seed'].isin(round3_seeds)].team.tolist()
results['west']['round3'] = rnd
round3 = west[west.seed.isin(round3_seeds)]

winners = []
round4_seeds = rounds(round3)
rnd = west[west['seed'].isin(round4_seeds)].team.tolist()
results['west']['round4'] = rnd
round4 = west[west.seed.isin(round4_seeds)]

# midwest
winners = []
round1_seeds = rounds(midwest)
rnd = midwest[midwest['seed'].isin(round1_seeds)].team.tolist()
results['midwest']['round1'] = rnd
round1 = midwest[midwest.seed.isin(round1_seeds)]

winners = []
round2_seeds = rounds(round1)
rnd = midwest[midwest['seed'].isin(round2_seeds)].team.tolist()
results['midwest']['round2'] = rnd
round2 = midwest[midwest.seed.isin(round2_seeds)]

winners = []
round3_seeds = rounds(round2)
rnd = midwest[midwest['seed'].isin(round3_seeds)].team.tolist()
results['midwest']['round3'] = rnd
round3 = midwest[midwest.seed.isin(round3_seeds)]

winners = []
round4_seeds = rounds(round3)
rnd = midwest[midwest['seed'].isin(round4_seeds)].team.tolist()
results['midwest']['round4'] = rnd
round4 = midwest[midwest.seed.isin(round4_seeds)]


final_four1 = pd.DataFrame()
final_four2 = pd.DataFrame()
final_four1 = final_four1.append(west[west.team == ''.join(results['west']['round4'])])
final_four1 = final_four1.append(east[east.team == ''.join(results['east']['round4'])])
final_four2 = final_four2.append(south[south.team == ''.join(results['south']['round4'])])
final_four2 = final_four2.append(midwest[midwest.team == ''.join(results['midwest']['round4'])])

final_four1 = final_four1.reset_index(drop=True)
final_four2 = final_four2.reset_index(drop=True)

final_four1.seed = [0,1]
final_four2.seed = [0,1]

# rounds function works here but we need to see the names; originally just had one final_four group; but split into two

monday = pd.DataFrame()

winners = []
win(final_four1)
monday = monday.append(final_four1[final_four1.seed == winners])

winners = []
win(final_four2)
monday = monday.append(final_four2[final_four2.seed == winners])

monday.seed = [0,1]

winners = []
win(monday)










        
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
tset = midwest.iloc[4:6]
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
    
    if prob>.5:
        count += 1
    
print("win") if count>7000 else print("null")
print("lose") if count<3000 else print("null")
print("win") if count<7000 and count>3000 and x>.5 else print("null")
print("lose") if count<7000 and count>3000 and x<.5 else print("null")


def win(matchup):

    # reset index to 0,1
    matchup = matchup.reset_index(drop=True)
    # compute margin of victory to get probability of win
    margin = ((matchup.adjem[0]-matchup.adjem[1])*(matchup.adjt[0] + matchup.adjt[1]))/200
    # original probability
    probo = 1-(0.5 * (1 + math.erf((0-margin)/(11*math.sqrt(2)))))
    
    # initialize count
    count = 0
    # simulation
    for rep in range(10000):
        
        # random number
        x=random.uniform(0,1)
        # original probability
        prob = 1-(0.5 * (1 + math.erf((0-margin)/(11*math.sqrt(2)))))
        
        # luck
        if x>.9:
            prob = prob + (matchup.luck[0]*10)
        elif x>.7:
            prob = prob + (matchup.luck[0]*5)            

        if x>.5:
            if matchup.adjo[0]>matchup.adjo[1]:
                prob = prob + .15
            else:
                prob = prob - .15
        else:
            if matchup.adjd[0]<matchup.adjd[1]:
                prob = prob + .15
            else:
                prob = prob - .15
        
        # compare new probability to x, if 
        if prob>x:
            count += 1
    
    winners.append(matchup.seed[0]) if count>7500 else None
    winners.append(matchup.seed[1]) if count<2500 else None
    winners.append(matchup.seed[0]) if count<7500 and count>2500 and x>.5 else None
    winners.append(matchup.seed[1]) if count<7500 and count>2500 and x<.5 else None
    
 

winners = []
tset = midwest.iloc[4:6]
win(tset)

      
print("win") if count>7000 else None
print("lose") if count<3000 else print("null")
print("win") if count<7000 and count>3000 and x>.5 else print("null")
print("lose") if count<7000 and count>3000 and x<.5 else print("null")

        # if x is greater than .5, offense wins
        prob = prob + .15 if matchup.adjo[0]>matchup.adjo[1] and x>.5 else prob
        prob = prob - .15 if matchup.adjo[0]<matchup.adjo[1] and x>.5 else prob
        
        # if x is less than .5, defense wins
        prob = prob + .15 if matchup.adjd[0]<matchup.adjd[1] and x<.5 else prob
        prob = prob - .15 if matchup.adjd[0]>matchup.adjd[1] and x<.5 else prob
        




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



