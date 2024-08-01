#Steps to Perform the T-Test:
#Categorize Your Data: Divide countries into two groups based on their Micropollution level (e.g., above and below the mean another logical threshold).

#Perform T-Test: Compare the mean micropollution levels between the two groups


#Null Hypothesis (H0) : There is no significant difference in microplastic pollution levels between the two groups.
#Alternative Hypothesis (H1): There is a significant difference in microplastic pollution levels between the two groups



import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import scipy.stats as stats

df = pd.read_csv('final merge.csv')
# Perform a t-test to compare microplastic levels
mean_mpl = df['Share of global plastics emitted to ocean'].mean()

print("Mean value of the column 2 is:", mean_mpl)

# Split this data into high and low Microplastic  groups based on their mean
high_mpl = df[df['Share of global plastics emitted to ocean'] > mean_mpl]
low_mpl = df[df['Share of global plastics emitted to ocean'] <= mean_mpl]

#Perfrom  a t-test to compare means of high and low MPL Groups
t_stat2, p_value2 = stats.ttest_ind(high_mpl['Share of global plastics emitted to ocean'], low_mpl['Share of global plastics emitted to ocean'])

print('T-static for micropollution:',t_stat2)
print('P-value for micropollution:',p_value2)

# The output will be :
#Mean value of the column: 9.789786259541984
#T-statistic: 10.358635324582876
#P-value: 1.1423617464722175e-18
#Conclusion: Since, our p-value is greater than 0.05. So, we can conclude that there is a significant difference in micropollution levels between this groups which means that there will be different micropollution levels for each country.
