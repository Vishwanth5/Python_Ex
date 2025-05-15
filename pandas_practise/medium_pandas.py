import pandas as pd

data = {
    'region': ['North', 'South', 'East', 'West', 'North', 'South', 'East', 'West'],
    'sales_rep': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah'],
    'sales': [2500, 1800, 2200, 3100, 2700, 1900, 2100, 3300]
}

df = pd.DataFrame(data)
average_sales= df.groupby('region')['sales'].mean()
high_performance =average_sales[average_sales>2500]
print(high_performance)

##2

person_data = {
    'personId': [1, 2],
    'lastName': ['Wang', 'Alice'],
    'firstName': ['Allen', 'Bob']
}
person_df = pd.DataFrame(person_data)

# Create Address DataFrame
address_data = {
    'addressId': [1, 2],
    'personId': [2, 3],
    'city': ['New York City', 'Leetcode'],
    'state': ['New York', 'California']
}
address_df = pd.DataFrame(address_data)
merged_df = pd.merge(person_df, address_df, on='personId', how='left')

result = merged_df[['firstName', 'lastName', 'city', 'state']]
print(result)
 