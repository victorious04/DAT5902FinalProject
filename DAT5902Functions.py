###importing possibly necessary python libraries###
from sklearn.linear_model import LinearRegression
from scipy.stats import pearsonr
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

###Functions that may be used often/speed up process

##1. function to import data into program
def importDF(filePath):
    df = pd.read_csv(filePath)
    return df


##2. printing first 5 values of dataset
def dfHead(dataSet):
    return dataSet.head()


##3. merges 2 datasets together 
def mergeData(dataSet1, dataSet2,mergeCols,type):
    merged = dataSet1.merge(dataSet2, on=mergeCols, how=type)
    return merged


##4. creation of a scatter plot
def createScatterPlot(dataSet,xdata,ydata,title,xlabel,ylabel):
    plt.figure(figsize=(10,6))
    plt.scatter(dataSet[xdata], dataSet[ydata], alpha=0.6, edgecolor='black')
    #labelling of scatter
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    plt.show()
    return


##5. calculation of regression analytics factors
def regressionAnalysis(dataSet, xdata, ydata):
    X = dataSet[xdata].values.reshape(-1,1)
    Y = dataSet[ydata].values
    model = LinearRegression()
    model.fit(X, Y)
    slope = model.coef_[0]
    intercept = model.intercept_
    rSquared = model.score(X, Y)
    #printing of regression analytics values
    print(f"Regression Coefficient (Slope): {slope}")
    print(f"Intercept: {intercept}")
    print(f"R^2 Value: {rSquared}")
    return 


##6. calculation of correlation analytics factors
def correlationTest(dataSet, xdata, ydata):
    corr, pValue = pearsonr(dataSet[xdata], dataSet[ydata])
    #printing of correlation and p value
    print(f"Pearson Correlation: {corr}")
    print(f"P-Value: {pValue}")
    #calculation to see significance of correlation
    if pValue<0.05:
        print("Correlation is statistically significant.")
    else:
        print("Correlation is not statiscally significant.")
    return


##7. dropping of unneeded columns in df
def dropColumns(dataSet, dropCols):
    dataSet = dataSet.drop(columns=dropCols)
    return dataSet


##8. selection of a specific year to focus on
def yearSelection(dataSet, year):
    dataSet = dataSet[dataSet['Year'] == year]
    return dataSet


##9. creation of bar chart
def createBarChart(dataSet, xdata, ydata, title, xlabel, ylabel):
    plt.bar(dataSet[xdata], dataSet[ydata], color='pink')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45, ha='right')
    plt.grid(True)
    plt.show()
    return