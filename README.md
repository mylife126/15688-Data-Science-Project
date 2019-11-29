# Multi-Feature Energy Consumption Prediction 
This is the group project conducted by **Xin Shen, Ruiji Sun, Zhonglin Cao**. The goal for this project is designed to discern the correlations among possible features that could affect the energy consumption with the CMU buildings. The project would conduct topics:
- Feature Visualization and Feature Engineering 
- Feature correlation study
- Liner Regression on time series
- Multi-feature prediction with Boosting Algorithm

## November 29th Update
- Cleaned up the raw data
- Created a model selection script to perform:
	- data fine- processing by Pandas and timeseries manipulation (ordinal transformation)
	- grid search operated on Ridge Regression for the optimal lambda
	- Performed lightGBM for the best performance of regression
	- visualized the predictions performance via both Distribution plot and the Bivariate Correlation Plot (KDE)