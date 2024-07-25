import pandas as pd
import matplotlib.pyplot as plt

# Define the file paths
data_dir = 'C:\\Users\\PC\\Desktop\\code\\data_files'
file1 = 'fantasypros_tenzonewr_2023.csv'
file2 = 'fantasypros_widereceivers_2023.csv'

# Load the data from the CSV files
ten_zone_data = pd.read_csv(f'{data_dir}\\{file1}')
wr_data = pd.read_csv(f'{data_dir}\\{file2}')

# Merge the two data sets on the 'Player' column
merged_data = pd.merge(ten_zone_data, wr_data, on='Player')

# Calculate the Pearson's correlation between Ten Zone Targets and Total TDs
correlation = merged_data['TGT_x'].corr(merged_data['TD_y'])

print(f'Pearson\'s correlation: {correlation:.2f}')

# Create the scatter plot
plt.figure(figsize=(10, 8))
plt.scatter(merged_data['TD_y'], merged_data['TGT_x'], c='blue')
plt.xlabel('Total Touchdowns (TD)')
plt.ylabel('Ten Zone Targets (TGT)')
plt.title('Scatter Plot of TD vs TGT')
plt.show()