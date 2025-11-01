import pandas as pd

# Student data
data = {
    "Name": ["Ali", "Sara", "Ahmed", "Zara", "Hassan"],
    "Class": ["8th", "8th", "8th", "8th", "8th"],
    "Math": [85, 92, 78, 90, 88],
    "Science": [80, 95, 75, 85, 90],
    "English": [78, 88, 82, 91, 85]
}

# Create DataFrame
df = pd.DataFrame(data)

# Print the DataFrame to see the table
print(df)

df.to_csv("student_results.csv", index=False)

