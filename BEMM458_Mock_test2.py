#######################################################################################################################################################
# 
# Name:
# SID:
# Exam Date:
# Module:
# Github link for this assignment:  
#
#######################################################################################################################################################
# Instruction 1. Read each question carefully and complete the scripts as instructed.

# Instruction 2. Only ethical and minimal use of AI is allowed. You may use AI to get advice on tool usage or language syntax, 
#                but not to generate code. Clearly indicate how and where you used AI.

# Instruction 3. Include comments explaining the logic of your code and the output as a comment below the code.

# Instruction 4. Commit to Git and upload to ELE once you finish.

#######################################################################################################################################################

# Question 1 - Loops and Lists
# You are given a list of numbers representing weekly sales in units.
weekly_sales = [120, 85, 100, 90, 110, 95, 130]
avg=sum(weekly_sales)/len(weekly_sales)
for x in weekly_sales:
    if x>=avg:
        print('Above avg')
    else:
        print('Below avg')
print(avg)

# Write a for loop that iterates through the list and prints whether each week's sales were above or below the average sales for the period.
# Calculate and print the average sales.

#######################################################################################################################################################

# Question 2 - String Manipulation
# A customer feedback string is provided:
customer_feedback = """The product was good but could be improved. I especially appreciated the customer support and fast response times."""
key=['good','improved']
value=[]
for x in key :
    start=customer_feedback.find(x)
    end=start+len(x)-1
    value.append((start,end))
print(value)

# Find the first and last occurrence of the words 'good' and 'improved' in the feedback using string methods.
# Store each position in a list as a tuple (start, end) for both words and print the list.

#######################################################################################################################################################

# Question 3 - Functions for Business Metrics
# Define functions to calculate the following metrics, and call each function with sample values (use your student ID digits for customization).

# 1. Net Profit Margin: Calculate as (Net Profit / Revenue) * 100.
# 2. Customer Acquisition Cost (CAC): Calculate as (Total Marketing Cost / New Customers Acquired).
# 3. Net Promoter Score (NPS): Calculate as (Promoters - Detractors) / Total Respondents * 100.
# 4. Return on Investment (ROI): Calculate as (Net Gain from Investment / Investment Cost) * 100.
def npm(np,re):
    return (np/re)*100
def cac(tmc,nca):
    return (tmc/nca)
def nps(pr,de,TR):
    return (pr-de)/TR*100
def ROI(ng,ic):
    return(ng/ic)*100
print(npm(73,43))
print(cac(73,43))
print(nps(73,43,23))
print(ROI(73,43))
#######################################################################################################################################################

# Question 4 - Data Analysis with Pandas
# Using a dictionary sales_data, create a DataFrame from this dictionary, and display the DataFrame.
# Write code to calculate and print the cumulative monthly sales up to each month.
import pandas as pd

sales_data = {'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'], 'Sales': [200, 220, 210, 240, 250]}
data=pd.DataFrame(sales_data)
data
data['cum_sales']=data['Sales'].cumsum()
data


#######################################################################################################################################################

# Question 5 - Linear Regression for Forecasting
# Using the dataset below, create a linear regression model to predict the demand for given prices.
# Predict the demand if the company sets the price at £26. Show a scatter plot of the data points and plot the regression line.

# Price (£): 15, 18, 20, 22, 25, 27, 30
# Demand (Units): 200, 180, 170, 160, 150, 140, 130
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
price=np.array([15, 18, 20, 22, 25, 27, 30]).reshape(-1,1)
demand=np.array([200, 180, 170, 160, 150, 140, 130])
model=LinearRegression()
model.fit(price,demand)
pred_dem=model.predict([[26]])
plt.scatter(price,demand,color='b')
plt.plot(price,model.predict(price),'r')
plt.scatter(26,pred_dem,color='g')
plt.xlabel=('price')
plt.ylabel=('demand')
plt.title=('Price VS Demand')
plt.show()
print('The Demand is:', pred_dem)

#######################################################################################################################################################

# Question 6 - Error Handling
# You are given a dictionary of prices for different products.

def total_prices(prices):
    t_price=0
    for key,value in prices.items():
        try:
            if isinstance(value,(int,float)):
               t_price+=value
            else:
               raise ValueError('Non Numeric Value')
        except ValueError as a:
            print(a)
    return(t_price)
prices = {'A': 50, 'B': 75, 'C': 'unknown', 'D': 30}
print(total_prices(prices))

# Write a function to calculate the total price of all items, handling any non-numeric values by skipping them.
# Include error handling in your function and explain where and why it’s needed.

#######################################################################################################################################################

# Question 7 - Plotting and Visualization
# Generate 50 random numbers between 1 and 500, then:
# Plot a histogram to visualize the distribution of these numbers.
# Add appropriate labels for the x-axis and y-axis, and include a title for the histogram.

import matplotlib.pyplot as plt
import random
numbers=[random.randint(1,500) for _ in range(50)]
plt.title('Random Numbers')
plt.xlabel('number')
plt.ylabel('frequency')
plt.hist(numbers,color='r')
plt.show()

#######################################################################################################################################################

# Question 8 - List Comprehensions
# Given a list of integers representing order quantities.
quantities = [5, 12, 9, 15, 7, 10]
new_quantity=[quantity*2 if quantity>=10 else quantity for quantity in quantities]
print(quantities)
print(new_quantity)

# Use a list comprehension to create a new list that doubles each quantity that is 10 or more.
# Print the original and the new lists.

#######################################################################################################################################################

# Question 9 - Dictionary Manipulation
# Using the dictionary below, filter out the products with a rating of less than 4 and create a new dictionary with the remaining products.
ratings = {'product_A': 4, 'product_B': 5, 'product_C': 3, 'product_D': 2, 'product_E': 5}
new_rating={}
for keys,values in ratings.items():
    if values<=4:
        pass
    else:
        new_rating[keys]=values
print(new_rating)
#######################################################################################################################################################

# Question 10 - Debugging and Correcting Code
# The following code intends to calculate the average of a list of numbers, but it contains errors:
values = [10, 20, 30, 40, 50]
total = 0
for i in values:
    total = total + i
average = sum(values) / len(values)
print("The average is" , average)

# Identify and correct the errors in the code.
# Comment on each error and explain your fixes.

#######################################################################################################################################################
