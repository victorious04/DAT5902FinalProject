###importing possibly necessary python libraries###
#because there is now a separate file which contains all functions, by importing everything in there
#there is no need for libraries such as numpy and matplotlib as this 'main; file isn't doing anything that woul
#need those libraries, it's all being done in the functions file.
from DAT5902Functions import *

#importing of necessary data
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

##dataset contains data from various years so have to filter out 
# using the year 2016 seemed like a good year to use since the datasets start 
# from different years depending on country so 2016 is recent enough to have full data
life_V_gdpDF = yearSelection(life_V_gdpDF,2016)

#creation of scatter plot
createScatterPlot(life_V_gdpDF,'GDP per capita', 'Life Expectancy','GDP vs Life Expectancy',
                  'GDP per Capita', 'Life Expectancy')

regressionAnalysis(life_V_gdpDF, 'GDP per capita', 'Life Expectancy')

correlationTest(life_V_gdpDF, 'GDP per capita', 'Life Expectancy')