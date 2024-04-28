**Time Series Forecasting (Stationary Data) Quiz**

**Introduction**

1. What is time series analysis?
a) Analyzing past behavior of data to predict its future behavior
b) Analyzing future behavior of data to predict its past behavior
c) Analyzing present behavior of data to predict its past behavior
d) Analyzing past behavior of data to predict its present behavior

Answer: a) Analyzing past behavior of data to predict its future behavior

2. What is an example of time series data?
a) Dow Jones Industrial Averages
b) Historical data on sales
c) Customer counts
d) All of the above

Answer: d) All of the above

**Stationary Data**

3. What is stationary data?
a) Data with a significant trend
b) Data with no significant trend, non-explosive, non-wandering
c) Data with a significant upward trend
d) Data with a significant downward trend

Answer: b) Data with no significant trend, non-explosive, non-wandering

**Nonstationary Data**

4. What is nonstationary data?
a) Data with no significant trend
b) Data with a significant upward/downward trend, wandering up and down over time
c) Data with a significant seasonal effect
d) Data with no significant seasonal effect

Answer: b) Data with a significant upward/downward trend, wandering up and down over time

**Seasonal Data**

5. What is seasonal data?
a) Data with a repeating pattern at regular intervals over time
b) Data with no repeating pattern at regular intervals over time
c) Data with a significant trend
d) Data with no significant trend

Answer: a) Data with a repeating pattern at regular intervals over time

**Extrapolation Model**

6. What is the general form of an extrapolation model?
a) 𝑌𝑡+1 = 𝑓(𝑌𝑡, 𝑌𝑡−1, 𝑌𝑡−2, …)
b) 𝑌𝑡+1 = 𝑓(𝑌𝑡, 𝑌𝑡−1)
c) 𝑌𝑡+1 = 𝑓(𝑌𝑡)
d) 𝑌𝑡+1 = 𝑓(𝑌𝑡−1)

Answer: a) 𝑌𝑡+1 = 𝑓(𝑌𝑡, 𝑌𝑡−1, 𝑌𝑡−2, …)

**Measuring Accuracy**

7. What is one way to measure the accuracy of a forecasting model?
a) Minimizing Mean Absolute Deviation (MAD)
b) Minimizing Mean Absolute Percent Error (MAPE)
c) Minimizing Mean Square Error (MSE)
d) All of the above

Answer: d) All of the above

**Stationary Models: An Example**

8. What is the goal of the manager of Electra-City?
a) To estimate the number of DVRs the store will sell in the next four months
b) To estimate the number of DVRs the store will sell in the next year
c) To estimate the number of DVRs the store will sell in the next quarter
d) To estimate the number of DVRs the store will sell in the next week

Answer: a) To estimate the number of DVRs the store will sell in the next four months

**Moving Average (MA) Technique**

9. What is the MA technique?
a) The simplest forecasting method
b) A complex forecasting method
c) A method that uses exponential smoothing
d) A method that uses weighted moving averages

Answer: a) The simplest forecasting method

**Weighted Moving Average (WMA) Technique**

10. What is the WMA technique?
a) A technique that assigns equal weights to past values
b) A technique that assigns different weights to past values
c) A technique that uses exponential smoothing
d) A technique that uses moving averages

Answer: b) A technique that assigns different weights to past values

**Exponential Smoothing Technique**

11. What is the exponential smoothing technique?
a) A technique that uses moving averages
b) A technique that uses weighted moving averages
c) A technique that uses exponential smoothing
d) A technique that uses seasonal decomposition

Answer: c) A technique that uses exponential smoothing

**Seasonality**

12. What is seasonality?
a) A regular and repeating pattern in time series data
b) A irregular and non-repeating pattern in time series data
c) A trend in time series data
d) A random fluctuation in time series data

Answer: a) A regular and repeating pattern in time series data

**Forecasting Stationary Data with Additive Seasonal Effects**

13. What is the formula for forecasting stationary data with additive seasonal effects?
a) 𝑌𝑡+𝑛 = 𝐸𝑡 + 𝑆𝑡+𝑛−𝑝
b) 𝑌𝑡+𝑛 = 𝐸𝑡 × 𝑆𝑡+𝑛−𝑝
c) 𝑌𝑡+𝑛 = 𝐸𝑡 - 𝑆𝑡+𝑛−𝑝
d) 𝑌𝑡+𝑛 = 𝐸𝑡 / 𝑆𝑡+𝑛−𝑝

Answer: a) 𝑌𝑡+𝑛 = 𝐸𝑡 + 𝑆𝑡+𝑛−𝑝

**Forecasting Stationary Data with Multiplicative Seasonal Effects**

14. What is the formula for forecasting stationary data with multiplicative seasonal effects?
a) 𝑌𝑡+𝑛 = 𝐸𝑡 × 𝑆𝑡+𝑛−𝑝
b) 𝑌𝑡+𝑛 = 𝐸𝑡 + 𝑆𝑡+𝑛−𝑝
c) 𝑌𝑡+𝑛 = 𝐸𝑡 - 𝑆𝑡+𝑛−𝑝
d) 𝑌𝑡+𝑛 = 𝐸𝑡 / 𝑆𝑡+𝑛−𝑝

Answer: a) 𝑌𝑡+𝑛 = 𝐸𝑡 × 𝑆𝑡+𝑛−𝑝