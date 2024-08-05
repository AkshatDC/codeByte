#Null Hypothesis (H0 ): There is no significant difference in microplastic pollution levels between countries with high MPA percentages and those with low MPA percentages.
#Alternative Hypothesis (H1): Countries with high MPA percentages have significantly lower microplastic pollution levels than those with low MPA percentages.

#Steps to Perform the T-Test:
#Categorize Your Data: Divide countries into two groups based on their MPA percentage (e.g., above and below the median or another logical threshold).

#Perform T-Test: Compare the mean pollution levels between the two groups

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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

# Initialize the plot
plt.figure(figsize=(10, 6))

# Create a boxplot
sns.boxplot(x='MPA_Group', y='Microplastic Pollution', data=df)

# Calculate means
high_mpa_mean = df[df['MPA_Group'] == 'High MPA']['Microplastic Pollution'].mean()
low_mpa_mean = df[df['MPA_Group'] == 'Low MPA']['Microplastic Pollution'].mean()

# Add mean lines
plt.axhline(y=high_mpa_mean, color='blue', linestyle='--', linewidth=1, label=f'High MPA Mean: {high_mpa_mean:.2f}')
plt.axhline(y=low_mpa_mean, color='orange', linestyle='--', linewidth=1, label=f'Low MPA Mean: {low_mpa_mean:.2f}')

# Add titles and labels
plt.title('Microplastic Pollution Levels by MPA Group')
plt.xlabel('MPA Group')
plt.ylabel('Microplastic Pollution Level')
plt.legend()

# Show the plot
plt.show()
