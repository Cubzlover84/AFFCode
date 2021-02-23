import csv
import os
import pandas as pd
import numpy as np
import json
import codecs
from helpers import *
import time

export = open('edited.json')
data = json.load(codecs.open('edited.json', 'r+', 'utf-8-sig'))
multioffers = pd.read_csv('voting.csv')
wave = 3

current_season=get_current_year(data)
phase=get_phase(data)


sign_multioffers(data, multioffers, current_season, phase)


with open('FAWave'+str(wave)+'.json', 'w') as outfile:
    json.dump(data, outfile)


print('\n Created updated export.')
