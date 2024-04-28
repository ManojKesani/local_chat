**Time Series Forecasting (Stationary Data)**
==============================================

**Lecture Outline**
-------------------

* Predicting Models for Stationary Data
	+ Moving Average
	+ Weighted Moving Average
	+ Exponential Smoothing
	+ A model for stationary data with additive seasonal effects
	+ A model for stationary data with multiplicative seasonal effects

**Introduction**
---------------

* Time series analysis: analyzing past behavior of data to predict its future behavior (extrapolation)
* Examples:
	+ Dow Jones Industrial Averages
	+ Historical data on sales, inventory, customer counts, interest rates, and costs
	+ Inflation, unemployment, and growth rates between 1970 to 2020
* Time-series data: a set of observations on a quantitative variable collected over time

**Some Time Series Terms**
---------------------------

* Stationary Data: no significant trend, non-explosive, non-wandering
* Nonstationary Data: significant upward/downward trend, wandering up and down over time
* Seasonal Data: repeating patterns at regular intervals over time
	+ Additive effects
	+ Multiplicative effects

**Extrapolation Model**
---------------------

* General form of an extrapolation model: 
	+ 
* Goal of an extrapolation model: identifying the function f(⋅) that produces the most accurate forecast of future values of Y
* Many different time series techniques; impossible to know which technique will be best for a particular data set
* Need a way to compare different time series techniques for a given data set

**Measuring Accuracy**
--------------------

* Informal Approach: constructing line graphs that show the actual value versus the predicted values for various modeling techniques
* Formal Techniques:
	+ Minimizing Mean Absolute Deviation (MAD):
		- MAD = (1/n) \* Σ|Y - Ŷ|
	+ Minimizing Mean Absolute Percent Error (MAPE):
		- MAPE = (1/n) \* Σ|(Y - Ŷ)/Y|
	+ Minimizing Mean Square Error (MSE):
		- MSE = (1/n) \* Σ(Y - Ŷ)^2
	+ Minimizing Root Mean Square Error (RMSE):
		- RMSE = √MSE

**Stationary Models: An Example**
-----------------------------

* The manager wants to estimate the number of DVRs the store will sell in the next four months
* He has collected sales data for the past 24 months
* Electra-City is a retail store that sells audio and video equipment for homes and cars
* Each month, the manager of the store must order merchandise from a distant warehouse

**Moving Average (MA) Technique**
---------------------------------

* The MA technique is the simplest forecasting method
* MA over the past k periods:
	+ Ŷt+1 = (Yt + Yt-1 + … + Yt-k+1)/k
* Note: no general rule for determining the best k exists; must try out several k values to see what works best

**Weighted Moving Average (WMA) Technique**
-----------------------------------------

* The WMA technique allows different weights to be assigned to past values
* WMA:
	+ Ŷt+1 = w0Yt + w1Yt-1 + … + wkYt-k
	+ 0 ≤ wi ≤ 1 and ∑wi = 1
* Forecasting with WMA (assuming k=2):
	+ Ŷ25 = 0.291(36) + 0.709(35) = 35.29
* Assuming data is stationary and exhibits no trends:
	+ Ŷ26 = Ŷ27 = Ŷ28 = 35.29

**Exponential Smoothing Technique**
-----------------------------------

* Exponential smoothing is another averaging technique for stationary data
* Ŷt+1 = αYt + (1-α)Ŷt
	+ 0 ≤ α ≤ 1
* Iterating the above equation:
	+ Ŷt+1 = αYt + α(1-α)Yt-1 + α(1-α)^2Yt-2 + …
* As we see, the exponential smoothing technique is a special case of the WMA technique
	+ The weights become smaller and smaller as we move farther away from the current period

**Exponential Smoothing: Optimal α**
-------------------------------------

* Minimizing MSE:
	+ MSE = (1/n) \* Σ(Yt - Ŷt)^2
	+ ST: 0 ≤ α ≤ 1
* Note: for the very first period, we assume that Ŷ = Y
* Forecasted values:
	+ Ŷ25 = Ŷ24 + α(Y24 - Ŷ24)
	+ Since the data is assumed to be stationary:
	+ Ŷ26 = Ŷ27 = Ŷ28 = Ŷ25

**Seasonality**
-------------

* Seasonality: a regular and repeating pattern in time series data
* Examples:
	+ Fuel oil price jumps up during the winter
	+ Price of suntan lotion and ice cream increases during the summer
* Two types of seasonal effects:
	+ Additive effects
	+ Multiplicative effects

**Seasonal Effects: An Example**
-----------------------------

* Sales of heat pumps tend to be:
	+ higher than average in the winter and summer quarters
	+ lower than average in the spring and fall quarters
* Savannah Climate Control (SCC) sells residential heat pumps
* SCC collected quarterly sales data for the past 6 years
* Using past data, SCC wants to predict the sales in next year’s quarters

**Stationary Data with Additive Seasonal Effects**
-------------------------------------------------

* Let p = The number of seasonal periods (p=4 in quarterly data)
* The expected level at period t is the weighted average of the de-seasonalized value at t and the expected level at t-1:
	+ Et = αYt - St-p+1 - (1-α)Et-1
	+ 0 ≤ α ≤ 1
* The seasonal factor at period t is the weighted average of the expected seasonal effect at period t and the seasonal factor at period t-p:
	+ St = βYt - Et + (1-β)St-p
	+ 0 ≤ β ≤ 1
* The predicted value at period t+n (for n=1,2,…,p) is:
	+ Ŷt+n = Et + St+n-p

**Forecasting Stationary Data with Additive Seasonal Effects**
---------------------------------------------------------

* Forecasts for time periods 25 to 28 at period 24:
	+ Ŷ25 = Et + St+1-p = 234.55 + 8.45 = 363.00
	+ Ŷ26 = Et + St+2-p = 234.55 - 17.82 = 336.73
	+ Ŷ27 = Et + St+3-p = 234.55 + 46.58 = 401.13
	+ Ŷ28 = Et + St+4-p = 234.55 - 31.73 = 322.81

**Stationary Data with Multiplicative Seasonal Effects**
-----------------------------------------------------

* Let p = The number of seasonal periods (p=4 in quarterly data)
* The expected level at period t is the weighted average of the de-seasonalized value at t and the expected level at t-1:
	+ Et = αYt/St-p+1 - (1-α)Et-1
	+ 0 ≤ α ≤ 1
* The seasonal factor at period t is the weighted average of the expected seasonal effect at period t and the seasonal factor at period t-p:
	+ St = βYt/Et + (1-β)St-p
	+ 0 ≤ β ≤ 1
* The predicted value at period t+n (for n=1,2,…,p) is:
	+ Ŷt+n = Et \* St+n-p

**Forecasting Stationary Data with Multiplicative Seasonal Effects**
---------------------------------------------------------

* Forecasts for time periods 25 to 28 at period 24:
	+ Ŷ25 = Et \* St+1-p = 353.95 \* 1.015 = 359.13
	+ Ŷ26 = Et \* St+2-p = 353.95 \* 0.946 = 334.94
	+ Ŷ27 = Et \* St+3-p = 353.95 \* 1.133 = 400.99
	+ Ŷ28 = Et \* St+4-p = 353.95 \* 0.912 = 322.95