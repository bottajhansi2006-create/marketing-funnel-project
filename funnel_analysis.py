import pandas as pd
import matplotlib.pyplot as plt

# STEP 1: LOAD DATA
print("\n===== STARTING PROGRAM =====")

try:
    df = pd.read_csv("marketing_funnel_data.csv")
    print("Data loaded successfully!")
except FileNotFoundError:
    print("Error: marketing_funnel_data.csv not found.")
    exit()

# STEP 2: BEFORE DATA (RAW DATA)
print("\n===== BEFORE DATA =====")
print(df)

# STEP 3: CALCULATE CONVERSION RATES

df["Lead_Conversion_%"] = (
    df["Leads"] / df["Visitors"]
) * 100

df["Qualified_Lead_Conversion_%"] = (
    df["Qualified_Leads"] / df["Leads"]
) * 100

df["Opportunity_Conversion_%"] = (
    df["Opportunities"] / df["Qualified_Leads"]
) * 100

df["Customer_Conversion_%"] = (
    df["Customers"] / df["Opportunities"]
) * 100

# STEP 4: AFTER DATA (PROCESSED DATA)
print("\n===== AFTER DATA =====")
print(df)

# STEP 5: OVERALL FUNNEL PERFORMANCE

total_visitors = df["Visitors"].sum()
total_leads = df["Leads"].sum()
total_customers = df["Customers"].sum()

overall_conversion = (
    total_customers / total_visitors
) * 100

print("\n===== OVERALL PERFORMANCE =====")
print("Total Visitors :", total_visitors)
print("Total Leads    :", total_leads)
print("Total Customers:", total_customers)
print(f"Overall Conversion Rate: {overall_conversion:.2f}%")

# STEP 6: CHANNEL PERFORMANCE

print("\n===== CHANNEL PERFORMANCE =====")

channel_performance = df[
    ["Channel", "Customer_Conversion_%"]
]

print(channel_performance)

best_channel = df.loc[
    df["Customer_Conversion_%"].idxmax(),
    "Channel"
]

print("\nBest Performing Channel:", best_channel)

# STEP 7: DROPOFF ANALYSIS

df["Dropoff_%"] = (
    (df["Visitors"] - df["Customers"])
    / df["Visitors"]
) * 100

print("\n===== DROPOFF ANALYSIS =====")
print(df[["Channel", "Dropoff_%"]])

# STEP 8: VISUALIZATION

# Funnel Stage Totals
stages = [
    total_visitors,
    df["Leads"].sum(),
    df["Qualified_Leads"].sum(),
    df["Opportunities"].sum(),
    total_customers
]

stage_names = [
    "Visitors",
    "Leads",
    "Qualified Leads",
    "Opportunities",
    "Customers"
]

plt.figure(figsize=(8,5))
plt.bar(stage_names, stages)
plt.title("Marketing Funnel")
plt.xlabel("Stages")
plt.ylabel("Users")
plt.show()

# Channel Performance Chart
plt.figure(figsize=(8,5))
plt.bar(
    df["Channel"],
    df["Customer_Conversion_%"]
)
plt.title("Channel Conversion Performance")
plt.xlabel("Channel")
plt.ylabel("Customer Conversion %")
plt.xticks(rotation=45)
plt.show()

# STEP 9: INSIGHTS

print("\n===== INSIGHTS =====")
print("1. Identify channels with highest conversion rates.")
print("2. Find stages where most users drop off.")
print("3. Improve landing pages and lead nurturing.")
print("4. Invest more budget in top-performing channels.")
print("5. Optimize conversion from Leads to Customers.")
