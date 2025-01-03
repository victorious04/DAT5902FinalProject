#importing python libraries needed
import unittest
import pandas as pd

'''
for this visualisation, the following functions for continuos testing 
seem to be the best to use. being:
1. merge check - to see that the merge can successfully be performed
2. column check - to make sure all the necessary columns are present
3. performance - makes sure the whole file runs without errors
4. visuals - check that visuals are saved correctly that every component
             is present. this may need to be 2 separate functions
In total, there should be about 5 test functions overall. 
'''