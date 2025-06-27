import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'greenhouse-gas-emissions-industry-and-household-year-ended-2023-NZSIOC.csv'
df = pd.read_csv(file_path)

# 1. Total Greenhouse Gas Emissions by Year
total_ghg = df[df['variable'] == 'Carbon dioxide equivalents']
yearly_emissions = total_ghg.groupby('year')['data_value'].sum()

plt.figure(figsize=(10, 6))
plt.plot(yearly_emissions.index, yearly_emissions.values, marker='o')
plt.title('Total Greenhouse Gas Emissions by Year (CO₂ equivalents)')
plt.xlabel('Year')
plt.ylabel('Emissions (Kilotonnes CO₂ eq.)')
plt.grid(True)
plt.tight_layout()
plt.show()

# 2. Top 10 Emitting Industries in Latest Year (2023)
latest_year = df['year'].max()
latest_emissions = df[(df['year'] == latest_year) & (df['variable'] == 'Carbon dioxide equivalents')]
industry_emissions = latest_emissions.groupby('nzsioc_descriptor')['data_value'].sum().sort_values(ascending=False)
top_10_industries = industry_emissions.head(10)

plt.figure(figsize=(12, 6))
top_10_industries.plot(kind='bar', color='skyblue')
plt.title(f'Top 10 Emitting Industries in {latest_year} (CO₂ equivalents)')
plt.ylabel('Emissions (Kilotonnes CO₂ eq.)')
plt.xlabel('Industry')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# 3. Emission Trends by Gas Type (CO2, Methane, Nitrous Oxide)
ghg_types = ['Carbon dioxide', 'Methane', 'Nitrous oxide']
ghg_trends = df[df['variable'].isin(ghg_types)]
ghg_pivot = ghg_trends.pivot_table(values='data_value', index='year', columns='variable', aggfunc='sum')

plt.figure(figsize=(10, 6))
ghg_pivot.plot(marker='o')
plt.title('GHG Emission Trends by Gas Type (2007–2023)')
plt.ylabel('Emissions (Kilotonnes CO₂ eq.)')
plt.xlabel('Year')
plt.grid(True)
plt.legend(title='Gas Type')
plt.tight_layout()
plt.show()