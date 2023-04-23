# Author: Andreia Santos
# Scope : week 8 - task  08
# Aim :  Get familiar with matplotlib and numpy. Create data and ploting it on image. Edit the plot  (adding extra info) 



import matplotlib.pyplot as plt
import numpy as np



#-----------------------------------------------histogram

x = np.random.normal(5, 2, 1000) #create a random distribution with 1000 values with a mean of 5 and standart deviation of 2 
plt.hist(x,color="blue", bins=20, edgecolor="black") #  the previous created x random values plotted into a histogram
plt.title("Normal Distribution, AVG=5, stdev=2")
plt.xlabel("Values")
plt.ylabel("Frequency")

#-----------------------------------------------function

xpoints  = np.linspace(0, 10, 100) #create a evenly distributed array  with its starting point at 0 and finishing point at 10. The total no. of points will be 100
ypoints=xpoints*xpoints*xpoints # create the y values (respect the function y=x^3 )
plt.plot(xpoints, ypoints, color="red", label="y = x^3") # plot the function
plt.legend(['y = x^3', 'Normal Distribution, AVG=5, stdev=2'],loc=2)

#-----------------------------------------------graph
plt.grid()
plt.show() # show both plot on the same image once this is the first time using this command

