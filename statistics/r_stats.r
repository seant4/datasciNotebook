## Correlation alaysis
cor(data)
cor.test(data$col1, data$col2)

## Anova - Analysis of Variance
fit  <- anova(dependent_variable ~ independed_variable, data=data)
summary(fit)

## Chi-Squared Test
chisq.test(table(data$col1, data$col2))

## T-Test
t.test(data$data$col, mu=value)

## Z-Score
mutate(zscore=(data-mean(data))/sd(data))

# Descriptive statistics
mean()
median()
mode()
var()
range()
quantile()
