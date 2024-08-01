#Null Hypothesis (H0) : There is no significant difference in microplastic pollution levels between the two groups.
#Alternative Hypothesis (H1): There is a significant difference in microplastic pollution levels between the two groups.

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
