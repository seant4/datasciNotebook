# Residuals vs Fitted:
	• Purpose: This plot shows the residuals (errors) on the y-axis and the fitted values (predicted values) on the x-axis.
	• Interpretation: It is used to check the linearity and homoscedasticity (constant variance) of the residuals. Ideally, the residuals should be randomly scattered around the horizontal axis (zero line) without any apparent pattern. If you see patterns (e.g., a funnel shape), it may indicate issues such as non-linearity or heteroscedasticity.

# Q-Q Plot:
	• Purpose: The Quantile-Quantile (Q-Q) plot compares the quantiles of the residuals to the quantiles of a normal distribution.
	•Interpretation: This plot is used to assess whether the residuals follow a normal distribution. If the residuals are normally distributed, the points should fall approximately along the reference line (a 45-degree line). Deviations from this line indicate departures from normality, such as skewness or heavy tails.

# Scale location plot:
	• Purpose: This plot shows the square root of the standardized residuals on the y-axis versus the fitted values on the x-axis.
	• Interpretation: It is used to check the homoscedasticity (constant variance) of the residuals. The plot should display a horizontal line with equally spread points. If there is a pattern (e.g., a fan shape), it indicates heteroscedasticity, meaning that the variance of the residuals is not constant.

# Cooks distance
	• Purpose: Cook's distance measures the influence of each data point on the regression coefficients.
	• Interpretation: This plot helps identify influential observations that have a disproportionate effect on the model's parameters. Points with a high Cook's distance are potential outliers or influential points. Typically, Cook's distance values greater than 1 (or more conservatively, greater than 4/n where n is the number of observations) are considered influential.
