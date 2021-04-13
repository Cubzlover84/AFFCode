
import json
import codecs
from helpers import *

export = open('export.json')
data = json.load(codecs.open('export.json', 'r+', 'utf-8-sig'))
offers= pd.read_csv('offers.csv', names=['time','user','code word','team','player','salary','years','pitch'],header=0)

pd.options.mode.chained_assignment = None

current_season=get_current_year(data)
phase=get_phase(data)
wave = int(input("What FA wave is it? If it's PSFA, type 4"))

tiers, rookiecontracts = get_tier_sheets()

#rookie_resignings(data, rookiecontracts, current_season, phase)


newoffers = validate_playername_offers(data,offers, current_season)
print_multioffers(newoffers,current_season, wave)
sign_singleoffers(data,newoffers,current_season, phase, wave)

with open('edited.json', 'w') as outfile:
    json.dump(data, outfile)


# sign_player(data,'Adam Scales','den',salary=30,years=1, year=current_season, phase=current_phase)


print('\n Created updated export.')
