# -*- coding: utf-8 -*-
"""
Created on Tue May 14 22:27:57 2024

@author: Arijit Bhattacharya
Designation: 
    Ph.D. Scholar, 
    Mind-Brain-Body-Society Lab, Dept. of Psychology, Ashoka University and Cognitive Neurology Lab, Dept. of Neurology, National Institute of Mental Health and Neuroscinces
Cite: Bhattacharya Arijit (2024), Ph.D. Scholar, Ashoka University
"""
#Task: Tukey Fence method for outliers Ditection

#%%

#Import Libraries
import numpy as np
import matplotlib.pyplot as plt

#Write Datasets
data1 = np.array([]) #Write First datasets inside the ([])
data2 = np.array([]) #Write Second datasets inside the ([])

#%%
#Calculate the outliers Ditection following the Tukey Fence method
#Step1: Calculate the Q1: data at 25% is considred as first quatrile
#Step2: Calculate the Q3: data at 75% is considred as Third quatrile
#Step3: Calculate the iqr: Q3 - Q1
#Step4: #Calculate the Lower Fence and Upper Fence
#Score lower than the Lower fence and higher than the upper fence will be considered as outliers
#%%

#For Data1
data1_q1 = np.percentile(data1, 25) 
data1_q3 = np.percentile(data1, 75)
iqr = data1_q3 - data1_q1
lower_fence = data1_q1 - 1.5 * iqr
upper_fence = data1_q3 + 1.5 * iqr
outliers = np.where((data1 < lower_fence) | (data1 > upper_fence))

print("Outliers of array for data1 ",data1,"is : \n", data1[outliers])
#%%

#For Data2  (Following the similer steps)
data2_q1 = np.percentile(data2, 25)
data2_q3 = np.percentile(data2, 75)
iqr = data2_q3 - data2_q1
lower_fence = data2_q1 - 1.5 * iqr
upper_fence = data2_q3 + 1.5 * iqr
outliers = np.where((data2 < lower_fence) | (data2 > upper_fence))

print("Outliers of array for data2",data2,"is : \n", data2[outliers])

#%%
#create a box plot
#%%

# Creating plot for data1 (With Colour)
fig1, ax = plt.subplots()
ax.boxplot(data1, patch_artist=True, boxprops=dict(facecolor='pink'))
plt.show()

# Creating plot for data2 (With Colour)
fig2, ax = plt.subplots()
ax.boxplot(data2, patch_artist=True, boxprops=dict(facecolor='pink'))
plt.show()

#%% EXTRA (BOX PLOT WITHOUT COLOUR)

# Creating plot for data1
#fig1 = plt.figure(figsize =(10, 7))
#plt.boxplot(data1)

# Creating plot for data2
#fig = plt.figure(figsize =(10, 7))
#plt.boxplot(data2)