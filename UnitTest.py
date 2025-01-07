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

update: since i have all my functions in a separate file, I'm going to test all the functions that are in there 
to make sure that they all work.
meaning? major overhaul of all existing functions (yay!)
'''


##using mock data as it helps to speed up testing 
#and is also independent of external data
#global as they are used often so easier to call
gdpDf = pd.DataFrame({
    'Entity':['UK','France','Spain','Portugal'],
    'Code':['UK','FRA','SPA','POR'],
    'Year':[2016,2016,2016,2001],
    'GDP per capita':[6000,4000,2000,3000]
})

lifeDf = pd.DataFrame({
    'Entity':['UK','France','Spain','Portugal'],
    'Code':['UK','FRA','SPA','POR'],
    'Year':[2016,2016,2016,2001],
    'Life Expectancy':[75,72,70,73]
})

class DataAnalysisTestFunctions(unittest.TestCase):

    ##1. testing importing of dataframe
    def test_importDF(self):
        test_data = gdpDf
        test_data.to_csv('testFile.csv', index=False)

        df = importDF('testFile.csv')
        self.assertEqual(len(df), 4, 'DF should have 4 rows.')
        self.assertIn('Entity', df.columns, "'Entity' ahould be in DF")
        os.remove('testFile.csv')

    ##2. testing the printing of the first 5 rows
    def test_dfHead(self):
        result = dfHead(gdpDf)
        self.assertEqual(len(result), 4, 'DF head should return 4 rows')

    ##3. testing the merging function
    def test_mergeData(self):
        merged = mergeData(gdpDf,lifeDf, ['Entity', 'Year'], 'inner')
        self.assertEqual(len(merged), 4, 'merged DF should have 4 rows')
        self.assertIn('Life Expectancy', merged.columns, 'Life Expectancy should be in merged DF')

    ##4. testing column drop
    def test_dropColumns(self):
        result = dropColumns(gdpDf, 'Code')
        self.assertNotIn('Code', result.columns, 'Code should be dropped')
    
    ##5. testing year selection
    def test_yearSelection(self):
        result = yearSelection(gdpDf, 2016)
        self.assertEqual(len(result), 3, 'Year selection should return 3 rows')
        self.assertTrue( (result['Year']==2016).all(), 'all rows should be for the year 2016')
    
    ##6. testing regression analysis
    def test_regressionAnalysis(self):
        from io import StringIO
        import sys

        capturedOutput = StringIO()
        sys.stdout = capturedOutput

        testData = pd.DataFrame({'X': [1, 2, 3, 4], 'Y': [2, 4, 6, 8]})
        regressionAnalysis(testData, 'X', 'Y')

        sys.stdout = sys.__stdout__

        output = capturedOutput.getvalue()
        self.assertIn("Regression Coefficient", output, "output should contain 'regression coefficient'.")

    ##7. testing correlation
    def test_correlationTest(self):
        from io import StringIO
        import sys

        capturedOutput = StringIO()
        sys.stdout = capturedOutput

        testData = pd.DataFrame({'X': [1, 2, 3, 4], 'Y': [2, 4, 6, 8]})
        correlationTest(testData, 'X', 'Y')

        sys.stdout = sys.__stdout__
        output = capturedOutput.getvalue()
        self.assertIn("Pearson Correlation", output, "Output should contain 'Pearson Correlation'")

    ##8. testing scatter plot creation
    def test_createScatterPlot(self):
        testData = pd.DataFrame({'X': [1, 2, 3], 'Y': [4, 5, 6]})

        createScatterPlot(testData, 'X', 'Y', 'Test Scatter Plot', 
                          'X-Axis', 'Y-Axis')
        
    ##9. testing box plot creation
    def test_createBarChart(self):
        testData = pd.DataFrame({'X': [1, 2, 3], 'Y': [4, 5, 6]})

        createBarChart(testData, 'X', 'Y', 'Test Bar Chart', 
                          'X-Axis', 'Y-Axis')
        
if __name__ == '__main__':
    unittest.main()