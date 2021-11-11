import statistics
import plotly.figure_factory as ff
import csv
import random
import pandas as pd
import plotly.graph_objects as go

rd = pd.read_csv('medium_data.csv')

data = rd['reading_time'].tolist()
populationMean = statistics.mean(data)


print('The population mean is : ',str(populationMean))

# Find the sample
def randomSetOFMean(counter):
    dataset = []
    for i in range(0,counter):
        randomIndex = random.randint(0,len(data))
        value = data[randomIndex]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

# Repeat the process 100 times

meanList = []
 
for i in range(0, 100):
    setOfMeans = randomSetOFMean(30)
    meanList.append(setOfMeans)

mean = statistics.mean(meanList)
std = statistics.stdev(meanList)

# Figure
df = meanList
fig = ff.create_distplot([df],['Reading time'],show_hist = False)
fig.show()

# Standard Deviation
OnesdStart,OnesdEnd = mean - std, mean + std
TwosdStart,TwosdEnd = mean - (2*std), mean + (2*std)
ThreesdStart,ThreesdEnd = mean - (3*std), mean + (3*std)

# Print it!
print('First standard deviation start and end  : ', OnesdStart, ',', OnesdEnd)
print('Second standard deviation start and end  : ', TwosdStart , ',', TwosdEnd)
print('Third standard deviation start and end  : ', ThreesdStart , ',', ThreesdEnd)


# Plot it and trace it!
fig.add_trace(go.Scatter(x=[mean,mean], y=[0, 0.17],mode='lines',name='Mean'))
fig.add_trace(go.Scatter(x=[std,std], y=[0, 0.17],mode='markers',name='Standard deviation'))

fig.add_trace(go.Scatter(x=[OnesdStart,OnesdStart], y=[0, 0.17],mode='lines+markers',name='One standard deviation start'))
fig.add_trace(go.Scatter(x=[OnesdEnd,OnesdEnd], y=[0, 0.17],mode='lines+markers',name='One standard deviation end'))

fig.add_trace(go.Scatter(x=[TwosdStart,TwosdStart], y=[0, 0.17],mode='lines+markers',name='Two standard deviation start'))
fig.add_trace(go.Scatter(x=[TwosdEnd,TwosdEnd], y=[0, 0.17],mode='lines+markers',name='Two standard deviation end'))

fig.add_trace(go.Scatter(x=[ThreesdStart,ThreesdStart], y=[0, 0.17],mode='lines+markers',name='Three standard deviation start'))
fig.add_trace(go.Scatter(x=[ThreesdEnd,ThreesdEnd], y=[0, 0.17],mode='lines+markers',name='Three standard deviation end'))

fig.show()