# Task3--EDA-on-Retail-Spark-Foundation

#Import Libraries:

importing necessary libraries, including pandas for data manipulation, numpy for numerical operations, seaborn for data visualization, and matplotlib.pyplot for creating plots.

#Load the Data:

The dataset from a local file (C:/Users/HP/Downloads/SampleSuperstore.csv) using pd.read_csv. It then displays the first few rows of the data using data.head() to get an initial overview of the dataset.

#Data Dimension:

data.shape gives the dimensions of the dataset (number of rows and columns).

#Statistics About the Dataset:

data.describe() provides summary statistics for the dataset, such as mean, standard deviation, and quartiles for numeric columns.

#Checking Null Values:

data.isnull().sum() is used to check for null values in the dataset. This is important for data quality assessment.

#Profit by Category:

A bar plot that shows the profit by category, using sns.barplot() to visualize the relationship between categories and profits. Categories are labeled on the x-axis, and profits are on the y-axis.

#Profit by Subcategory:

Similarly, create a bar plot to show the profit by subcategory, using sns.barplot() with subcategories on the x-axis and profits on the y-axis.

#Profit by Region:

Create another bar plot to show the profit by region, using sns.barplot() with regions on the x-axis and profits on the y-axis.

#Profit by Ship Mode:

This code creates a bar plot for profit by ship mode, using sns.barplot() with ship modes on the x-axis and profits on the y-axis.

#Profit by Segment:

Create a bar plot for profit by segment, using sns.barplot() with segments on the x-axis and profits on the y-axis.

#Profit vs. Discount:

A line plot is used to show how profit changes with different levels of discounts.

#Sales vs. Profit:

A scatter plot is created to visualize the relationship between sales and profits. Sales are on the x-axis, and profits are on the y-axis.

#Correlation:

A heatmap is used to visualize the correlation between different numeric attributes in the dataset.

#Checking Minimum and Maximum Profit:

The code calculates the average profit at different discount levels and identifies the discount levels that lead to the maximum and minimum average profits.
