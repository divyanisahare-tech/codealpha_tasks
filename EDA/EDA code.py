import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------
# 1. Read CSV
# ----------------------------
df = pd.read_csv('books.csv')

# ----------------------------
# 2. Display first rows
# ----------------------------
print("First 5 rows:")
print(df.head())

# ----------------------------
# 3. Basic dataset info
# ----------------------------
print("\nShape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nMissing values:\n", df.isnull().sum())
print("\nData Types:\n", df.dtypes)

# ----------------------------
# 4. Clean Price column
# ----------------------------
df['Price_clean'] = df['Price'].str.replace('[^0-9.]', '', regex=True).astype(float)

# ----------------------------
# 5. Descriptive statistics
# ----------------------------
print("\nCleaned Data Preview:")
print(df.head())

print("\nPrice Statistics:")
print(df['Price_clean'].describe())

# ----------------------------
# 6. Sort books by highest price
# ----------------------------
df_sorted = df.sort_values(by='Price_clean', ascending=False)
print("\nTop 5 Most Expensive Books:")
print(df_sorted[['Book Name', 'Price_clean']].head())

# ----------------------------
# 7. BAR CHART (Top 10 Books Price)
# ----------------------------
plt.figure(figsize=(10,5))
plt.bar(df['Book Name'].head(10), df['Price_clean'].head(10))
plt.xticks(rotation=45, ha='right')
plt.title('Top 10 Books Price')
plt.ylabel('Price')
plt.xlabel('Book Name')
plt.tight_layout()
plt.show()

# ----------------------------
# 8. HISTOGRAM (Price Distribution)
# ----------------------------
plt.figure(figsize=(6,4))
plt.hist(df['Price_clean'], bins=10)
plt.title('Price Distribution')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# ----------------------------
# 9. BOX PLOT (Detect Outliers)
# ----------------------------
plt.figure(figsize=(6,4))
plt.boxplot(df['Price_clean'])
plt.title("Price Boxplot (Outlier Detection)")
plt.ylabel("Price")
plt.tight_layout()
plt.show()

# ----------------------------
# 10. LINE CHART (Price Trend)
# ----------------------------
plt.figure(figsize=(10,4))
plt.plot(df['Price_clean'])
plt.title("Price Trend Across Books")
plt.xlabel("Book Index")
plt.ylabel("Price")
plt.tight_layout()
plt.show()

# ----------------------------
# 11. CORRELATION ANALYSIS
# ----------------------------
print("\nCorrelation Matrix (Numeric Columns):")
print(df.corr(numeric_only=True))
