###importing possibly necessary python libraries###
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

###Functions that may be used often/speed up process

#function to import data into program
def importDF(filePath):
    df = pd.read_csv(filePath)
    return df

def dfHead(dataSet):
    return dataSet.head()

#merges 2 datasets together 
def mergeData(dataSet1, dataSet2,mergeCols,type):
    merged = dataSet1.merge(dataSet2, on=mergeCols, how=type)
    return merged

#creation of a scatter plot
def createScatterPlot(dataSet,xdata,ydata,title,xlabel,ylabel):
    plt.figure(figsize=(10,6))
    plt.scatter(dataSet[xdata], dataSet[ydata], alpha=0.6, edgecolor='black')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    plt.show()
    return

#saves visuals to be later used
def saveVisual(outputpath):
    plt.savefig(outputpath)
    return

#dropping of unneeded columns in df
def dropColumns(dataSet, dropCols):
    dataSet = dataSet.drop(columns=dropCols)
    return dataSet

#selection of a specific year to focus on
def yearSelection(dataSet, year):
    dataSet = dataSet[dataSet['Year'] == year]
    return dataSet