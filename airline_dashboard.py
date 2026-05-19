import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load dataset
df = pd.read_csv("airline_project_data.csv")

# -----------------------------
# BASIC CHECK
# -----------------------------
print(df.head())
print(df.info())
print(df.isnull().sum())

# -----------------------------
# 1. Flights by Time of Day
# -----------------------------
time_counts = df["Departure_Time"].value_counts()

plt.figure()
time_counts.plot(kind="bar")
plt.title("Flights by Departure Time")
plt.xlabel("Time")
plt.ylabel("Number of Flights")
plt.show()

# -----------------------------
# 2. Flights by Airline
# -----------------------------
airline_counts = df["Airline"].value_counts()

plt.figure()
airline_counts.plot(kind="bar")
plt.title("Flights by Airline")
plt.show()

# -----------------------------
# 3. Average Price by Airline
# -----------------------------
avg_price = df.groupby("Airline")["Price"].mean()

plt.figure()
avg_price.plot(kind="bar")
plt.title("Average Price by Airline")
plt.ylabel("Price")
plt.show()

# -----------------------------
# 4. Price by Class
# -----------------------------
sns.boxplot(x="Class", y="Price", data=df)
plt.title("Price Distribution by Class")
plt.show()

# -----------------------------
# 5. Price vs Days Left
# -----------------------------
sns.scatterplot(x="Days_Left", y="Price", data=df)
plt.title("Price vs Days Left")
plt.show()

# -----------------------------
# 6. Price by Time of Day
# -----------------------------
sns.boxplot(x="Departure_Time", y="Price", data=df)
plt.title("Price by Time of Day")
plt.show()