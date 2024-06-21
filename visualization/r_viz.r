
# Basic plot
plot(data$col1, data$col2)

# Histogram
dist(data$col)

# Boxplot
boxplot(data$col1 ~ data$col2)

## GGplot
ggplot(data, aes(x=col1, y=col2)) + geom_point()

