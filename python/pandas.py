import pandas as pd

# Create a dictionary
data = {
    'Age': [23, 45, 34, 29, 50, 31, 22, 40, 36, 28],
    'Height': [165, 180, 175, 160, 170, 185, 158, 172, 178, 169],
    'Weight': [60, 80, 75, 55, 85, 70, 50, 90, 78, 65],
    'Gender': ['Female', 'Male', 'Male', 'Female', 'Male', 'Female', 'Female', 'Male', 'Male', 'Female'],
    'Country': ['USA', 'Canada', 'UK', 'USA', 'Australia', 'Canada', 'UK', 'Australia', 'USA', 'Canada']
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

# View the first few rows
print("First few rows of the DataFrame:")
print(df.head())

# Function to check if a string is a palindrome
def is_palindrome(s):
    s = s.lower()  # Convert to lowercase
    return s == s[::-1]  # Check if the string is the same forwards and backwards

# Check for palindromic values in the 'Country' column
palindromic_countries = [country for country in df['Country'] if is_palindrome(country)]

print("\nPalindromic countries:")
print(palindromic_countries)