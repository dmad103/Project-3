import matplotlib.pyplot as plt
import numpy as np
 
# Importing the 10 poorest towns in NJ and storing it in the variable "Town"
Town = ['Camden City','Atlantic City','Newark City','Passaic','Paterson','Trenton',
'Bridgeton','Orange','Asbury Park','Irvington Township']

# Importing the percentages below poverty of those towns
Percentage = [38.4,36.6,29.1,31.9,29.1,27.6,30.4,25.1,30.6,23.4]

# Naming figure 1
plt.figure('Bar Chart')

# The bar graph is shown 
plt.bar(Town, Percentage)

# The title, x label, and y label are displayed for the bar chart
plt.title('The Percentage Below Poverty of the Poorest Towns in NJ')
plt.xlabel('Town')
plt.ylabel('Percentage')

# The label size had to be adjusted that way each label is seen without overlap
plt.tick_params(axis='x', which='major', labelsize=3)

# Naming figure 2
plt.figure("Pie Chart")

# The title is displayed for the pie chart
plt.title('Population of the 10 Poorest Towns in NJ')

# The values (in thousands) are hardcoded and it links directly to the correct town
y = np.array([73, 38, 282, 69, 144, 82, 23, 34, 15, 61,])
towns2 = ['Camden City','Atlantic City','Newark City','Passaic','Paterson','Trenton',
'Bridgeton','Orange','Asbury Park','Irvington Township']

# The pie chart is shown
plt.pie(y, labels = towns2)

# Both charts are able to be displayed
plt.show()



