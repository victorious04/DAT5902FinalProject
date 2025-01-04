###importing possibly necessary python libraries###
import pandas as pd
import matplotlib as plt
import numpy as np

###Functions that may be used often/speed up process

#function to import data into program
def importDF(filePath):
    df = pd.read_csv(filePath)
    return df

#merges 2 datasets together 
def mergeData(dataSet1, dataSet2,mergeCols,type):
    merged = dataSet1.merge(dataSet2, on=mergeCols, how=type)
    return merged

#creation of a scatter plot
def createScatterPlot(dataSet,xdata,ydata,title,xlabel,ylabel):
    plt.scatter(dataSet[xdata], dataSet[ydata])
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()
    return

#saves visuals to be later used
def saveVisual(outputpath):
    plt.savefig(outputpath)
    return
##END OF FUNCTIONS


#MAIN PROGRAM
lifeDf = importDF('life-expectancy.csv')
gdpDF = importDF('gdp-per-capita-worldbank.csv')

#check that file has imported properly and see the layout
print(lifeDf.head())
print(gdpDF.head())


