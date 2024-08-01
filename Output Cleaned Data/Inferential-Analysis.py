#Null Hypothesis (H0 ): There is no significant difference in microplastic pollution levels between countries with high MPA percentages and those with low MPA percentages.
#Alternative Hypothesis (H1): Countries with high MPA percentages have significantly lower microplastic pollution levels than those with low MPA percentages.

#Steps to Perform the T-Test:
#Categorize Your Data: Divide countries into two groups based on their MPA percentage (e.g., above and below the median or another logical threshold).

#Perform T-Test: Compare the mean pollution levels between the two groups

import pandas as pd
import scipy.stats as stats

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('final merge.csv')

# Calculate the mean of the MPA column
mean_mpa = df['MPA'].mean() 

print("Mean value of the column:", mean_mpa)

# Split data into high and low MPA groups
high_mpa = df[df['MPA'] > mean_mpa]
low_mpa = df[df['MPA'] <= mean_mpa]

# Perform a t-test to compare means of high and low MPA groups
t_stat, p_value = stats.ttest_ind(high_mpa['MPA'], low_mpa['MPA'])

print('T-statistic:', t_stat)
print('P-value:', p_value)

#P-value < 0.05: Reject the null hypothesis. There is significant evidence to suggest that countries with high MPA percentages have lower microplastic pollution levels.
#P-value ≥ 0.05: Fail to reject the null hypothesis. There is not enough evidence to suggest a significant difference.

# The output will be :
#Mean value of the column: 9.789786259541984
#T-statistic: 10.358635324582876
#P-value: 1.1423617464722175e-18

#Conclusion: Since, our p-value is greater than 0.05. So, we can conclude that countries with high MPA percentages have significantly lower microplastic pollution levels than those with low MPA percentages.
