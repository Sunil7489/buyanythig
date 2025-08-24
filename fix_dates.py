import pandas as pd

# Load the raw CSV file with original dates in dd-MM-yy format
df = pd.read_csv('orders_raw.csv')

# Convert the 'OrderDate' column from dd-MM-yy to yyyy-MM-dd format
df['OrderDate'] = pd.to_datetime(df['OrderDate'], format='%d-%m-%y').dt.strftime('%Y-%m-%d')

# Save the corrected data to a new CSV file
df.to_csv('orders_clean.csv', index=False)
