##THIS MAY NEED TO BE CHANGED

##importing python libraries needed##
import unittest
import pandas as pd
import matplotlib as plt
import os
from DAT5902Functions import (
    importDF,
    dfHead,
    mergeData,
    createScatterPlot,
    regressionAnalysis,
    correlationTest,
    dropColumns,
    yearSelection,
    createBarChart
)

'''
for this visualisation, the following functions for continuos testing 
seem to be the best to use. being:
1. column check - to make sure all the necessary columns are present
2. merge check - to see that the merge can successfully be performed
3. visuals - check that visuals are saved correctly that every component
             is present. this may need to be 2 separate functions
In total, there should be about 4 test functions overall. 
'''

##using mock data as it helps to speed up testing 
#and is also independent of external data
#global as they are used often so easier to call
gdpDf = pd.DataFrame({
    'Entity':['UK','France','Spain'],
    'Code':['UK','FRA','SPA'],
    'Year':[2016,2016,2016],
    'GDP per capita':[6000,4000,2000]
})

lifeDf = pd.DataFrame({
    'Entity':['UK','France','Spain'],
    'Code':['UK','FRA','SPA'],
    'Year':[2016,2016,2016],
    'Life Expectancy':[75,72,70]
})

class DataAnalysisTestFunctions(unittest.TestCase):

    ##1. Column Check - check that all necessary columns are present
    def columnPresenceCheck(self):
        #list of columns that need to bein each file in order to continue
        requiredDGPColumns = ['Entity','Year','GDP per capita']
        requiredLifeColumns = ['Entity','Year','Life Expectancy']

        #checks that every column in the required array is present
        #if not, a message is returned to say which is missing
        for column in requiredDGPColumns:
            assert column in gdpDf.columns, f"Missing column for GDP: {column}"
        for column in requiredLifeColumns:
            assert column in lifeDf.columns, f"Missing column for Life Expectancy: {column}"

    ##2. Merge check - see that the merge can be successfully performed
    def test_MergeCheck(self):
        #inner merge of the 2 datasets
        mergedData = gdpDf.merge(lifeDf, on=['Country','Year'], how='inner')

        #check that there is data after the merge, if not, error returns
        self.assertFalse(mergedData.empty, "The merge was unsuccessful: Empty")
        #checks that the number of columns are equal in column number, if not, error returns
        self.assertEqual(len(mergedData.columns), len(gdpDf.columns) + 1, "Not all columns included in merge")

    ##3a. checks that a visual can be saved successfully
    def visualSavingCheck(self):
        #creation of tester - in this case a bar chart
        plt.bar(gdpDf['Entity'], gdpDf['GDP per capita'], color='blue')
        plt.xlabel('Country')
        plt.ylabel('GDP per Capita')
        plt.title('GDP per Capita by Country')
        plt.savefig('testerBarChart.png')
        plt.close()

        #tests that the file of that name exists, if not, erorr message returns
        self.assertTrue(os.path.exists('testerBarChart.png'), 'File was not saved correctly')
        #removes the file after test is completed
        os.remove('testerBarChart.png')