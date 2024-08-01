#Steps to Perform the T-Test:
#Categorize Your Data: Divide countries into two groups based on their Fishery Consumption  level ( e.g., above and below the mean another logical threshold).

#Perform T-Test: Compare the mean Fishery Consumption levels between the two groups


#Null Hypothesis (H0) : There is no significant difference in Fishery Consumption levels between the two groups.
#Alternative Hypothesis (H1): There is a significant difference in Fishery Consumption  levels between the two groups



import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import scipy.stats as stats

df = pd.read_csv('final merge.csv')
# Perform a t-test to compare fishconsumption levels
mean_fcl = df['FisheryConsumption'].mean()

print("Mean value of the column 2 is:", mean_fcl)

# Split this data into high and low Fish Consumption  groups based on their mean
high_fcl = df[df['FisheryConsumption'] > mean_fcl]
low_fcl = df[df['FisheryConsumption'] <= mean_fcl]

#Perform  a t-test to compare means of high and low FCL Groups
t_stat2, p_value2 = stats.ttest_ind(high_fcl['FisheryConsumption'], low_fcl['FisheryConsumption'])

print('T-static for FisheryConsumption:',t_stat2)
print('P-value for FisheryConsumption:',p_value2)

# The output will be :
#Mean value of the column 2 is: 1537842.340534351
#T-static for FisheryConsumption: 5.756763923641438
#P-value for FisheryConsumption: 5.936887606711161e-08

#Conclusion: Since, our p-value is greater than 0.05. So, we can conclude that there is a significant difference in Fishery Consumption  levels between the two groups which means different countries across the globes have different fish consumption levels.
