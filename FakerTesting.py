from faker import Faker
import pandas as pd
import random

# Initialize Faker
fake = Faker()

# Set number of rows
num_rows = 1000

# Generate data
data = []
for i in range(1, num_rows + 1):
    row = {
        "id": fake.unique.random_number(digits=5),
        "name": fake.unique.name(),
        "age": random.randint(20, 60),
        "salary": round(random.uniform(2500, 6000), 2),
        "department_id": random.randint(1, 5),
        "address": fake.unique.address()    }
    data.append(row)

# Create a DataFrame
df = pd.DataFrame(data)

# Display the table
print(df)

df.to_csv('employees1.csv', index=False)