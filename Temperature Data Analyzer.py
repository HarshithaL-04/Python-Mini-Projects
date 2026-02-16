#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Temperature Data Analyzer
# Mini data-based Python project

# Function to analyze temperature data
def analyze_temperature(temperatures):

    total_days = len(temperatures)      # Number of days entered
    average_temp = sum(temperatures) / total_days   # Calculate average temperature
    highest_temp = max(temperatures)    # Find highest temperature
    lowest_temp = min(temperatures)     # Find lowest temperature

    # Count number of hot days (temperature > 35)
    hot_days = 0
    for temp in temperatures:
        if temp > 35:
            hot_days += 1

    print("\n--- Temperature Analysis Report ---")
    print("Total Days:", total_days)
    print("Average Temperature:", average_temp)
    print("Highest Temperature:", highest_temp)
    print("Lowest Temperature:", lowest_temp)
    print("Number of Hot Days (>35°C):", hot_days)


# List to store temperature values
temperatures = []

# Taking input for 7 days
for i in range(7):
    temp = float(input(f"Enter temperature for day {i+1}: "))
    temperatures.append(temp)

# Call the analysis function
analyze_temperature(temperatures)


# In[ ]:




