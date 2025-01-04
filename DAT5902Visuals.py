###importing possibly necessary python libraries###
import pandas as pd
import matplotlib as plt
import numpy as np
from DAT5902Functions import *


lifeDf = importDF('life-expectancy.csv')
gdpDF = importDF('gdp-per-capita-worldbank.csv')

#check that file has imported properly and see the layout
print(dfHead(lifeDf))
print(dfHead(gdpDF))

#merging the 2 data sets together
life_V_gdpDF = mergeData(lifeDf,gdpDF,['Entity','Year'],'inner')
#check to see that the datasets have merged successfully
print(dfHead(life_V_gdpDF))

#some columns are unneeded so they can be dropped
life_V_gdpDF = dropColumns(life_V_gdpDF,['Code_x','Code_y'])
print(dfHead(life_V_gdpDF))

#now to create the