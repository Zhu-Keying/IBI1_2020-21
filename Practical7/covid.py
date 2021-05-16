#use os and pandas
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#input the data from file called "full_data.csv"
os.chdir("/Users/zhukeying/IBI1_2020-21/Practical7")
covid_data = pd.read_csv("full_data.csv")
#every second row between 0 and 10
x=covid_data.iloc[0:12:2,:]
print(x)
#use Boolean to show “total cases” related to Afghanistan
covid_data.loc[(covid_data["location"] == 'Afghanistan'), ["total_cases"]]
data1=[]
# To choose data in covid_data with "location" = "Afghanistan" 
for i in range (0,7996):
	if covid_data.iloc[i,1]=="Afghanistan":
		data1.append(True)
	else:
		data1.append(False)
y=covid_data.loc[data1,"total_cases"]
print(y)

#worldwide new cases
data2= []
#choose data in covid_data with "location" = "World"
for i in range (0,7996):
     if covid_data.iloc[i,1]=="World":
             data2.append(True)
     else:
             data2.append(False)
world_new_cases=covid_data.loc[data2,"new_cases"]

#calculate the mean and median 
mean = str(np.mean(world_new_cases))
median = str(np.median(world_new_cases))
print("the mean and median of new cases for the entire world are "+mean+" and "+median)

#create a boxplot 
plt.title('Worldwide new cases')
plt.ylabel('word_new_case_numbers')
plt.xlabel('date')
plt.boxplot(world_new_cases,
            vert=True,
            whis=2,
            patch_artist=True,
            meanline=True,
            showmeans=True,
            showbox=True,
            showcaps=True,
            showfliers=True,
            )
plt.show()


world_new_deaths=covid_data.loc[data2,"new_deaths"]
plt.title('Worldwide new cases and deaths')
plt.xlabel('world_dates')
plt.ylabel('world_new_deaths')
plt.boxplot(world_new_deaths,
             vert = True,
             whis = 2,
             patch_artist = True,
             meanline = True,
             showbox = True,
             showcaps = True,
             showfliers = True,
             )
plt.show()

# my question: How have new cases and total cases developed over time in Germany?
data3 = []
#choose data in covid_data with "location" = "Germany"
for i in range (0,7996):
     if covid_data.iloc[i,1]=="Germany":
             data3.append(True)
     else:
             data3.append(False)
Germany_new_cases=covid_data.loc[data3,"new_cases"]

data4 = []
for i in range (0,7996):
     if covid_data.iloc[i,1]=="Germany":
             data4.append(True)
     else:
             data4.append(False)
Germany_total_cases=covid_data.loc[data3,"total_cases"]

world_dates = []
for i in range (0,7996):
    if covid_data.loc[i, 'location'] == 'World':
        world_dates.append(covid_data.iloc[i, 0])
print(world_dates)

#plot the new cases in Germany
plt.plot(world_dates,Germany_new_cases, 'bo', label = "Germany new cases")
plt.xlabel('world_dates')
plt.ylabel('Germany_new_cases')
plt.title('Germany new cases')
plt.legend()
plt.show()

#plot the total cases in Germany
plt.plot(world_dates,Germany_total_cases, 'bo', label = "Germany total cases")
plt.xlabel('world_dates')
plt.ylabel('Germany_total_cases')
plt.title('Germany total cases')
plt.legend()
plt.show()
