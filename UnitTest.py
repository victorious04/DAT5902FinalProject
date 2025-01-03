##importing python libraries needed##
import unittest
import pandas as pd

'''
for this visualisation, the following functions for continuos testing 
seem to be the best to use. being:
1. column check - to make sure all the necessary columns are present
2. merge check - to see that the merge can successfully be performed
3. visuals - check that visuals are saved correctly that every component
             is present. this may need to be 2 separate functions
In total, there should be about 4 test functions overall. 
'''

##the data files will be called in quite offten so saves time making
#them global variables
gdpDf = pd.read_csv('gdp-per-capita-worldbank.csv')
lifeDf = pd.read_csv('life-expectancy.csv')

class DataAnalysisTestFunctions(unittest.TestCase):
    ##1. Column Check
    def columnPresenceCheck(self):
        #list of columns that need to bein each file in order to continue
        requiredDGPColumns = ['Entity','Year','GDP per capita']
        requiredLifeColumns = ['Entity','Year','Life Expectancy']

        #checks that every column in the required array is present
        #if not, a message is returned
        for column in requiredDGPColumns:
            assert column in gdpDf.columns, f"Missing column for GDP: {column}"
        for column in requiredLifeColumns:
            assert column in lifeDf.columns, f"Missing column for Life Expectancy: {column}"


