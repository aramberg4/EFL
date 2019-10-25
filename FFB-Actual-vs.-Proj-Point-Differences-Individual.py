import requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import seaborn as sns
import pandas as pd

from FFB_Functions import get_ind_stats, subset_df_by_pos, get_stdev_ind_players



swid      = '{8ECCF67B-4709-4DD0-8916-0CEDAC593A06}'
espn_s2   = 'AEAPGlQDfrLoF9MvmatEvE0ucZSJaVpzkpwEvJcHDBc%2BeyamLCon554%2Bgu3H5HiBfHiLPrjZfEgecZl1C%2Bt%2FqIMeSyBiD8lV1q9ohY1i5Z1Y57pV8bJiIaBN8GbsUBYyWSCqc9cFR5sDNGwE4aYxuvAnNb7QTGNAynCjEjoWiEPcugY6oRvMErJcvkQSg6FgpePfh2dLDk7zZlejK2ACcn%2F8quDlH9dTKSzvDRr7jyxgnxbSQZZqgLWRhearYQQBlpQ4i%2FvPJo2XZ5AM6ZFeF2t8'
league_id = 26867
season    = 2019
week      = 1

'''

slotcodes = {
    0 : 'QB', 2 : 'RB', 4 : 'WR',
    6 : 'TE', 10 : 'DE', : 16: 'Def', 17: 'K',
    20: 'Bench', 21: 'IR', 23: 'Flex'
}
'''
slotcodes = {0: 'QB', 1: '2', 2: 'RB', 3: '3', 4: 'WR', 5: '5', 6: 'TE', 7: '7', 8: 'DT',
             9: 'DE', 10: 'LB', 11: '11', 12: 'CB', 13: 'S', 14: '14', 15: 'DP',
         16: 'D/ST', 17: 'K', 18:'P', 19: 'HC', 20: 'BE', 21: 'IR', 22: '22', 23: 'FLEX'}

url = 'https://fantasy.espn.com/apis/v3/games/ffl/seasons/' + \
      str(season) + '/segments/0/leagues/' + str(league_id) + \
      '?view=mMatchup&view=mMatchupScore'

data = []
pos = ['QB', 'RB', 'WR', 'TE', 'K']



df = get_ind_stats(league_id, season, swid, espn_s2)

ind_player = "Christian McCaffrey"
print( df[df['Player'] == ind_player])




#topQB = subset_df_by_pos(df, 'QB')


k_only = subset_df_by_pos(df, 'K')
rb_only = subset_df_by_pos(df, 'RB') 
ind_player_stdev = get_stdev_ind_players(rb_only)
print('\n\n')
print(ind_player_stdev)


print('\nComplete.')





