# This code is to be complemented by the "top20_deathtoll.csv" (from DataQuest)
# It generates a nice, clean horizontal bar plot per Tukey's principles of maximizing the data-ink ratio

import pandas as pd
import matplotlib.pyplot as plt

# Read in the data
top20_deathtoll = pd.read_csv('top20_deathtoll.csv')

# Generate figure, axis and specify figure size
fig, ax = plt.subplots(figsize=(4.5, 6))

# Generate horizontal bar plot with specified height and color (red)
ax.barh(top20_deathtoll['Country_Other'],
        top20_deathtoll['Total_Deaths'],
        height=0.45, color='#af0b1e')

# Remove axes / spines
for location in ['left', 'right', 'top', 'bottom']:
    ax.spines[location].set_visible(False)

# Set x ticks, labels, and color    
ax.set_xticks([0, 150000, 300000])
ax.set_xticklabels(['0', '150,000', '300,000'])
ax.xaxis.tick_top() # Move x ticks to top
ax.tick_params(top=False, left=False) # Remove x ticks
ax.tick_params(axis='x', colors='grey') # Color grey

# Left align y tick labels 
ax.set_yticklabels([]) # an empty list removes the labels
country_names = top20_deathtoll['Country_Other']
for i, country in zip(range(20), country_names):
    ax.text(x=-80000, y=i-0.15, s=country)

# Add 150k line for readability
ax.axvline(x=150000, ymin=0.045, c='grey', alpha=0.5)
    
# Add title and subtitle text
ax.text(x=-80000, y=23.5,
        s='The Death Toll Worldwide Is 1.5M+',
        weight='bold', size=17)
ax.text(x=-80000, y=22.5,
        s='Top 20 countries by death toll (December 2020)',
        size=12)

plt.show()
