
# https://www.reddit.com/r/CollegeBasketball/comments/5xir8t/calculating_win_probability_and_margin_of_victory/

import pandas as pd
tourney = pd.read_csv("/Users/kthomas1/github/python_code/bracketsim_kenpom.csv")

east = tourney.loc[tourney.region == "east",['seed','team','adjem','adjt']]
east.name = "east"
west = tourney.loc[tourney.region == "west",['seed','team','adjem','adjt']]
west.name = "west"
south = tourney.loc[tourney.region == "south",['seed','team','adjem','adjt']]
south.name = "south"
midwest = tourney.loc[tourney.region == "midwest",['seed','team','adjem','adjt']]
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

