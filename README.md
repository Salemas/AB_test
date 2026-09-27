# Marketing Campaign A/B Test Analysis

This repository contains two A/B test analysis notebooks:

1. Cookie Cats A/B Test
2. Fast Food Marketing Campaign Test
3. Looker Studio report https://lookerstudio.google.com/s/nfeQe2zb-J8

## Project Overview
This project analyzes two A/B tests:

1. Cookie Cats A/B Test
2. Fast Food Marketing Campaign Test

## Setup and Installation

### Prerequisites
- Python 3.x
- Required Python packages:
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - statsmodels
  - scipy

### Installation
1. Install the required packages using pip:
```bash
pip install pandas numpy matplotlib seaborn statsmodels scipy
```

2. Ensure you have the dataset file `cookie_cats.csv` and `fast_food_marketing.csv` in the same directory as the notebook.

## Project Goals

### Fast Food Marketing Campaign Test
The main goal of this analysis is to evaluate three marketing campaigns for a new fast food item. Specifically:

1. Compare weekly sales performance across three different promotions
2. Analyze the impact of market size and store age on sales
3. Conduct statistical tests to determine which promotion strategy is most effective
4. Examine correlations between market characteristics and sales performance
5. Provide actionable recommendations for the most effective marketing strategy

### Cookie Cats A/B Test
1. Compare 1-day and 7-day retention rates between the two groups
2. Analyze the distribution of game rounds played
3. Conduct statistical tests to determine if differences in retention are statistically significant
4. Identify and handle outliers in game rounds data
5. Compare player engagement metrics between control and test groups

## Data Description

### Fast Food Marketing Campaign Data
The dataset includes information from multiple market locations and stores. Key variables include:

- `MarketID`: Unique identifier for market
- `MarketSize`: Size of market area by sales
- `LocationID`: Unique identifier for store location
- `AgeOfStore`: Age of store in years
- `Promotion`: One of three promotions that were tested (1, 2, or 3)
- `week`: One of four weeks when the promotions were run
- `SalesInThousands`: Sales amount for a specific LocationID, Promotion, and week

### Cookie Cats A/B Test Data
- `userid`: Unique player identifier
- `version`: Group assignment (gate_30 or gate_40)
- `sum_gamerounds`: Number of game rounds played in the first 14 days
- `retention_1`: Whether the player returned 1 day after install
- `retention_7`: Whether the player returned 7 days after install

## Analysis Approach

### Fast Food Marketing Campaign Analysis
The analysis follows these steps:

1. Data Loading and Initial Inspection
   - Load and inspect the dataset
   - Check for missing values and data quality
   - Verify data types
   - Data cleaning and outlier detection

2. Exploratory Data Analysis
   - Compare sales distribution between different promotions
   - Analyze sales trends over the four weeks
   - Examine the relationship between market characteristics and sales
   - Visualize sales patterns across different market sizes

3. Statistical Testing
   - Perform ANOVA to compare sales across different promotions
   - Conduct Tukey's HSD for post-hoc analysis
   - Analyze correlations between market characteristics and sales
   - Test assumptions of normality and equal variances

4. Data Visualization
   - Create visualizations to compare sales distribution between different promotions
   - Visualize sales trends over the four weeks
   - Visualize the relationship between market characteristics and sales
   - Visualize sales patterns across different market sizes

5. Conclusions
   - Provide insights into the impact of different promotions on sales performance
   - Provide recommendations for marketing strategy based on findings
   - Provide recommendations for handling outliers in the data

### Cookie Cats Analysis
The analysis follows these steps:

1. Data Loading and Initial Inspection
   - Load and inspect the dataset
   - Check for missing values and data quality
   - Verify data types
   - Data cleaning and outlier detection

2. Exploratory Data Analysis
   - Compare game rounds distribution between groups
   - Calculate player counts in each group
   - Analyze 1-day and 7-day retention rates
   - Examine outlier distribution between groups

3. Statistical Testing
   - Perform hypothesis testing using Z-test and Chi-square test
   - Compare retention rates between control and test groups
   - Analyze statistical significance of differences

4. Data Visualization
   - Create visualizations to compare retention rates between groups
   - Visualize game rounds distribution between groups
   - Visualize 1-day and 7-day retention rates
   - Visualize outlier distribution between groups

5. Conclusions
   - Provide insights into the impact of different promotions on sales performance
   - Provide insights into the impact of gate placement on player retention
   - Provide recommendations for game design based on findings
   - Provide recommendations for handling outliers in the data

## Key Findings

### Fast Food Marketing Campaign Results

#### Data Quality
- Dataset contains records from multiple market locations
- No missing values in any columns
- Categorical variables properly encoded
- Sales data recorded in thousands of dollars

#### Market Characteristics
- Markets categorized by size
- Stores of varying ages included
- Data collected over 4 weeks
- Three different promotions tested

#### Statistical Analysis
- Tests include:
  - ANOVA for comparing means
  - Tukey's HSD for post-hoc comparisons
  - Correlation analysis
  - Assumption testing (normality, equal variances)

### Cookie Cats Results

### Data Quality
- The dataset contains 90,189 player records
- No missing values in any columns
- Outlier analysis using IQR (Interquartile Range) with coefficient 1.5
- Approximately 11.28% of total data identified as outliers
- Similar outlier distribution between both groups (11.32% for gate_30, 11.24% for gate_40)

### Player Engagement
- Median game rounds played: 16
- 75th percentile of players played 51 game rounds
- Maximum game rounds played: 49,854 (outlier)

### Statistical Analysis
- Statistical tests include:
  - Z-test for proportions
  - Chi-square test for independence
- Analysis of both 1-day and 7-day retention rates

## Conclusions

### Fast Food Marketing Campaign Conclusions
The analysis aims to provide insights into: 
- The impact of different promotions on sales performance
- Correlation between market size and sales performance
- Statistical significance of observed differences
- Recommendations for marketing strategy based on findings


### Cookie Cats Conclusions
The analysis aims to provide insights into:
- The impact of gate placement on player retention
- Differences in player engagement between the two groups
- Statistical significance of observed differences
- Recommendations for game design based on findings
- The effect of outliers on overall analysis results

## Notebooks
- `cookie_cats.ipynb`: Contains the complete analysis code and visualizations for the Cookie Cats A/B Test
- `fast_food_marketing.ipynb`: Contains the complete analysis code and visualizations for the Fast Food Marketing Campaign Test

