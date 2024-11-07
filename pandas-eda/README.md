make sure to pip install matplotlib

import matplotlib.plyplot as plt  
import pandas as pd  
import altair as alt  
Load dataframe with:  
df = pd.read_csv("https://raw.githubusercontent.com/melaniewalsh/responsible-datasets-in-context/main/datasets/top-500-novels/library_top_500.csv", sep=',', header=0, low_memory=False)  

Organized the data in some ways that convey its point of gender trends in top novels in an easier to read / absorb way. 