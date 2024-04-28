**Time Series Forecasting (Stationary Data)**
=============================================

### Predicting Models for Stationary Data

* Moving Average (MA)
* Weighted Moving Average (WMA)
* Exponential Smoothing
* Models for stationary data with additive seasonal effects
* Models for stationary data with multiplicative seasonal effects

### Introduction to Time Series Analysis

* Analyzing past behavior of data to predict its future behavior (extrapolation)
* Examples: Dow Jones Industrial Averages, sales data, inventory, customer counts, interest rates, and costs
* Time series data: a set of observations on a quantitative variable collected over time

### Stationary Data

* No significant trend, non-explosive, non-wandering
* Characteristics:
	+ No significant upward or downward trend
	+ No explosive or wandering behavior over time
	+ Repeating patterns at regular intervals (seasonal data)

### Nonstationary Data

* Significant upward or downward trend, wandering up and down over time
* Characteristics:
	+ Significant upward or downward trend
	+ Wandering up and down over time
	+ No repeating patterns at regular intervals

### Seasonal Data

* Repeating patterns at regular intervals over time
* Characteristics:
	+ Additive effects
	+ Multiplicative effects

### Extrapolation Model

* General form: $$\hat{Y}_{t+1} = f(Y_t, Y_{t-1}, Y_{t-2}, ...)$$
* Goal: Identify the function f that produces the most accurate forecast of future values of Y

### Measuring Accuracy

* Informal approach: Constructing line graphs to compare actual and predicted values
* Formal techniques:
	+ Minimizing Mean Absolute Deviation (MAD)
	+ Minimizing Mean Absolute Percent Error (MAPE)
	+ Minimizing Mean Square Error (MSE)
	+ Minimizing Root Mean Square Error (RMSE)

### Moving Average (MA) Technique

* Simplest forecasting method
* Assigns equal weight to past values
* Formula: $$\hat{Y}_{t+1} = \frac{1}{k} \sum_{i=0}^{k-1} Y_{t-i}$$

### Weighted Moving Average (WMA) Technique

* Allows different weights to be assigned to past values
* Formula: $$\hat{Y}_{t+1} = \sum_{i=0}^{k-1} w_i Y_{t-i}$$
* Constraints: $$0 \leq w_i \leq 1, \sum_{i=0}^{k-1} w_i = 1$$

### Exponential Smoothing (ES) Technique

* Another averaging technique for stationary data
* Formula: $$\hat{Y}_{t+1} = \alpha Y_t + (1 - \alpha) \hat{Y}_t$$
* Where: $$0 \leq \alpha \leq 1$$

### Seasonality

* Regular and repeating pattern in time series data
* Examples: Fuel oil price, suntan lotion and ice cream sales
* Two types of seasonal effects:
	+ Additive effects
	+ Multiplicative effects

### Forecasting Stationary Data with Additive Seasonal Effects

* Formula: $$\hat{Y}_{t+n} = E_t + S_{t+n-p}$$
* Where: $$E_t = \alpha Y_t - \alpha E_{t-1}, S_t = \beta (Y_t - E_t) + (1 - \beta) S_{t-p}$$

### Forecasting Stationary Data with Multiplicative Seasonal Effects

* Formula: $$\hat{Y}_{t+n} = E_t \times S_{t+n-p}$$
* Where: $$E_t = \alpha \frac{Y_t}{S_{t-p}} - \alpha E_{t-1}, S_t = \beta \frac{Y_t}{E_t} + (1 - \beta) S_{t-p}$$

This is the complete and structured notes of all the concepts in the provided class notes.