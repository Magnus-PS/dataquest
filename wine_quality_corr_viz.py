
# specify color-mapping based on +ve vs. -ve correlation 
## +ve: blue, -ve: orange
positive_white = white_corr >= 0
positive_red = red_corr >= 0

color_map_white = positive_white.map({True:'#33A1C9', False:'#ffae42'})
color_map_red = positive_red.map({True:'#33A1C9', False:'#ffae42'})

# specify plot style and figure size
style.use('fivethirtyeight')
fig, ax = plt.subplots(figsize=(9, 5))

# plot white and red wine correlations
## shift left, adjust height, and map color
ax.barh(white_corr.index, white_corr, left=2, height=0.5,
        color=color_map_white)
ax.barh(red_corr.index, red_corr, height=0.5, left=-0.1, color=color_map_red)

# remove grid and tick labels
ax.grid(b=False)
ax.set_yticklabels([])
ax.set_xticklabels([])

# manually specify coordinates and add x tick labels
x_coords = {'Alcohol': 0.82, 'Sulphates': 0.77, 'pH': 0.91,
            'Density': 0.80, 'Total Sulfur Dioxide': 0.59,
            'Free Sulfur Dioxide': 0.6, 'Chlorides': 0.77,
            'Residual Sugar': 0.67, 'Citric Acid': 0.76,
            'Volatile Acidity': 0.67, 'Fixed Acidity': 0.71}
y_coord = 9.8

for y_label, x_coord in x_coords.items():
    ax.text(x_coord, y_coord, y_label)
    y_coord -= 1

# add grey lines to left and right of x tick labels    
ax.axvline(0.5, c='grey', alpha=0.1, linewidth=1,
           ymin=0.1, ymax=0.9)
ax.axvline(1.45, c='grey', alpha=0.1, linewidth=1,
           ymin=0.1, ymax=0.9)

# add grey lines and y labels
ax.axhline(-1, color='grey', linewidth=1, alpha=0.5,
          xmin=0.01, xmax=0.32)
ax.text(-0.7, -1.7, '-0.5'+ ' '*31 + '+0.5',
        color='grey', alpha=0.5)
ax.axhline(-1, color='grey', linewidth=1, alpha=0.5,
           xmin=0.67, xmax=0.98)
ax.text(1.43, -1.7, '-0.5'+ ' '*31 + '+0.5',
        color='grey', alpha=0.5)

# add grey lines and subplot titles
ax.axhline(11, color='grey', linewidth=1, alpha=0.5,
          xmin=0.01, xmax=0.32)
ax.text(-0.33, 11.2, 'RED WINE', weight='bold')
ax.axhline(11, color='grey', linewidth=1, alpha=0.5,
          xmin=0.67, xmax=0.98)
ax.text(1.75, 11.2, 'WHITE WINE', weight='bold')

# add dataquest/source footer
ax.text(-0.7, -2.9, '©DATAQUEST' + ' '*92 + 'Source: P. Cortez et al.',
        color = '#f0f0f0', backgroundcolor = '#4d4d4d',
       size=12)

# add title and subtitle
ax.text(-0.7, 13.5,
        'Wine Quality Most Strongly Correlated With Alcohol Level',
        size=17, weight='bold')
ax.text(-0.7, 12.7,
        'Correlation values between wine quality and wine properties (alcohol, pH, etc.)')

plt.show()
