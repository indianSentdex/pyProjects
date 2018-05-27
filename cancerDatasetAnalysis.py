import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd

dataSetPath = "G:\\Machine Learning Stuff\\breast-cancer-wisconsin.data.txt"


df = pd.read_csv(dataSetPath)

print(df.loc[0][1])




