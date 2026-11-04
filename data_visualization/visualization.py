import pandas as pd
import matplotlib.pyplot as plt

# Load portfolio data (replace with your own CSV if desired)
# The CSV should contain columns: Product,Revenue,Cost,Sector,Sales
csv_path = 'data_visualization/portfolio_data.csv'

data = pd.read_csv(csv_path)

# -------------------------------------------------
# Chart 1 – Profit Analysis (Week 4 – Program 1)
# -------------------------------------------------
# Calculate profit = Revenue - Cost
data['Profit'] = data['Revenue'] - data['Cost']

plt.figure(figsize=(8,5))
plt.plot(data['Product'], data['Profit'], label='Profit', color='green', marker='o')
plt.title('Profit Analysis')
plt.xlabel('Products')
plt.ylabel('Profit (₹)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('profit_analysis.png')  # save as image for reference
plt.show()

# -------------------------------------------------
# Chart 2 – Profit & Revenue Dual Line (Week 4 – Program 2)
# -------------------------------------------------
plt.figure(figsize=(8,5))
plt.plot(data['Product'], data['Profit'], label='Profit', color='green')
plt.plot(data['Product'], data['Revenue'], label='Revenue', color='#2e5fa3')
plt.title('Profit and Revenue Analysis')
plt.xlabel('Products')
plt.ylabel('Amount (₹)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('profit_revenue.png')
plt.show()

# -------------------------------------------------
# Chart 3 – Investment by Sector – Pivot Table (Week 5)
# -------------------------------------------------
# Pivot: sum of Sales (or Investment) per Sector
pivot = data.pivot_table(values='Sales', index='Sector', aggfunc='sum')

pivot.plot(kind='bar', figsize=(8,5), color=['#1a3a6b','#2e5fa3','#4a85d4','#6ba3e8','#9bbff0'])
plt.title('Total Investment by Sector')
plt.xlabel('Sector')
plt.ylabel('Total Investment (₹)')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.savefig('sector_investment.png')
plt.show()
