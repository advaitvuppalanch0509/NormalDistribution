import pandas as pd
import csv
import plotly.figure_factory as ff
import statistics
count=[]

pf=pd.read_csv("data.csv")
fig=ff.create_distplot([pf["AvgRating"].tolist()],['AvgRating'],show_hist=False)
mean=statistics.mean(pf["AvgRating"])
fig.show()

print(mean)