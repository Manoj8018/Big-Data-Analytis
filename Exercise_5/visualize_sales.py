import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# Use a non-interactive backend
matplotlib.use("Agg")

# Read the Hadoop output
df = pd.read_csv(
    "city_sales_results.txt",
    sep="\t",
    header=None,
    names=["City", "TotalSales", "TransactionCount"]
)

print("\n=== Sales by City Summary ===")
print(df)

# Calculate average transaction value
df["AvgTransaction"] = df["TotalSales"] / df["TransactionCount"]

# Plot
plt.figure(figsize=(12,6))
top = df.nlargest(10, "TotalSales")

plt.bar(top["City"], top["TotalSales"] / 1_000_000)

plt.title("Top Cities by Sales")
plt.xlabel("City")
plt.ylabel("Sales (Million ₹)")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("sales_analysis.png")

print("\nChart saved as sales_analysis.png")
