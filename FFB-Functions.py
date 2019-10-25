






#Get Individual Player Stats 


def get_ind_stats(league_id, season, swid='', espn=''):
    
    '''
    function designed to
    '''
    
    for week in range(1, 17):
        print(week, end=' ')

        r = requests.get(url,
                         params={'scoringPeriodId': week},
                         cookies={"swid": swid,
                              "espn_s2": espn }
                        )
        d = r.json()
        
        for tm in d['teams']:
            tmid = tm['id']
            for p in tm['roster']['entries']:
                name = p['playerPoolEntry']['player']['fullName']
                slot = p['lineupSlotId']
                pos  = slotcodes[slot]

                # injured status (need try/exc bc of D/ST)
                inj = 'NA'
                try:
                    inj = p['playerPoolEntry']['player']['injuryStatus']
                except:
                    pass

                # projected/actual points
                proj, act = None, None
                for stat in p['playerPoolEntry']['player']['stats']:
                    if stat['scoringPeriodId'] != week:
                        continue
                    if stat['statSourceId'] == 0:
                        act = stat['appliedTotal']
                    elif stat['statSourceId'] == 1:
                        proj = stat['appliedTotal']

                data.append([
                    week, tmid, name, slot, pos, inj, proj, act
                ])
                
        return data


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''



