# -*- coding: utf-8 -*-

# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('airbnb - Copy.csv')
df.head()

# Create a copy of the dataframe and fill missing values with 'test' (for demonstration)
df_copy = df.copy()
df_fillna = df_copy.fillna('test')
df_fillna.head()

# Distribution of Prices
plt.figure(figsize=(10, 6))
sns.histplot(df['price'], bins=50, kde=True, color='blue')
plt.title('Price Distribution')
plt.xlabel('Price')
plt.ylabel('Count')
plt.show()

# Distribution of Room Types
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='room_type', palette='viridis')
plt.title('Room Type Distribution')
plt.xlabel('Room Type')
plt.ylabel('Count')
plt.show()

# Geographical Distribution of Listings
plt.figure(figsize=(10, 8))
sns.scatterplot(data=df, x='longitude', y='latitude', hue='neighbourhood_group', palette='bright', alpha=0.6)
plt.title('Geographical Distribution of Listings')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend(title='Neighbourhood Group')
plt.show()

# Relationship Between Price and Number of Reviews
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='price', y='number_of_reviews', alpha=0.5, color='green')
plt.title('Relationship Between Price and Number of Reviews')
plt.xlabel('Price')
plt.ylabel('Number of Reviews')
plt.show()

# Top Hosts with Most Listings
top_hosts = df['host_id'].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_hosts.index, y=top_hosts.values, palette='magma')
plt.title('Top Hosts with Most Listings')
plt.xlabel('Host ID')
plt.ylabel('Number of Listings')
plt.show()

# Distribution of Availability (365 Days)
plt.figure(figsize=(10, 6))
sns.histplot(df['availability_365'], bins=50, kde=True, color='purple')
plt.title('Availability Distribution Over 365 Days')
plt.xlabel('Number of Available Days')
plt.ylabel('Count')
plt.show()

# Relationship Between Minimum Nights and Price
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='minimum_nights', y='price', alpha=0.5, color='orange')
plt.title('Relationship Between Minimum Nights and Price')
plt.xlabel('Minimum Nights')
plt.ylabel('Price')
plt.show()

# Convert 'last_review' column to datetime
df['last_review'] = pd.to_datetime(df['last_review'])

# Number of Reviews Over Time
df.set_index('last_review', inplace=True)
monthly_reviews = df['number_of_reviews'].resample('M').sum()

plt.figure(figsize=(12, 6))
monthly_reviews.plot(color='red')
plt.title('Number of Reviews Over Time')
plt.xlabel('Time')
plt.ylabel('Number of Reviews')
plt.show()

# Correlation Matrix
corr_matrix = df[['price', 'minimum_nights', 'number_of_reviews', 'reviews_per_month', 'availability_365']].corr()

plt.figure(figsize=(10, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
plt.show()

# Average Price by Neighbourhood Group
avg_price_by_neighbourhood = df.groupby('neighbourhood_group')['price'].mean().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x=avg_price_by_neighbourhood.index, y=avg_price_by_neighbourhood.values, palette='rocket')
plt.title('Average Price by Neighbourhood Group')
plt.xlabel('Neighbourhood Group')
plt.ylabel('Average Price')
plt.show()

# Check for Missing Values
print("Missing values in 'price':", df['price'].isna().sum())
print("Missing values in 'number_of_reviews':", df['number_of_reviews'].isna().sum())

# Drop rows with missing values in 'price' and 'number_of_reviews'
df_cleaned = df.dropna(subset=['price', 'number_of_reviews'])

# Check Data Types
print("Data type of 'price':", df_cleaned['price'].dtype)
print("Data type of 'number_of_reviews':", df_cleaned['number_of_reviews'].dtype)

# Convert columns to numeric (if not already)
df_cleaned.loc[:, 'price'] = pd.to_numeric(df_cleaned['price'], errors='coerce')
df_cleaned.loc[:, 'number_of_reviews'] = pd.to_numeric(df_cleaned['number_of_reviews'], errors='coerce')

# Drop rows with missing values after conversion
df_cleaned = df_cleaned.dropna(subset=['price', 'number_of_reviews'])

# Check Variance of X
if np.var(df_cleaned['number_of_reviews']) == 0:
    print("Error: Variance of X is zero. All values of X are the same.")
else:
    print("Variance of X is valid.")

# Prepare data for linear regression
X = df_cleaned['number_of_reviews'].values  # Independent variable (number of reviews)
Y = df_cleaned['price'].values              # Dependent variable (price)

# Calculate mean of X and Y
mean_X = np.mean(X)
mean_Y = np.mean(Y)

# Calculate slope (beta_1) and intercept (beta_0)
numerator = np.sum((X - mean_X) * (Y - mean_Y))
denominator = np.sum((X - mean_X) ** 2)
beta_1 = numerator / denominator
beta_0 = mean_Y - beta_1 * mean_X

# Predict price
Y_pred = beta_0 + beta_1 * X

# Calculate Mean Squared Error (MSE)
mse = np.mean((Y - Y_pred) ** 2)

# Display results
print(f"Regression Coefficients: Intercept (beta_0) = {beta_0:.2f}, Slope (beta_1) = {beta_1:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")

# Plot the regression line
plt.figure(figsize=(10, 6))
plt.scatter(X, Y, color='blue', label='Actual Data', alpha=0.5)
plt.plot(X, Y_pred, color='red', label='Regression Line')
plt.title('Linear Regression: Price vs Number of Reviews')
plt.xlabel('Number of Reviews')
plt.ylabel('Price')
plt.legend()
plt.show()