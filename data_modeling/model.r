## kNN
index = sample(1:nrow[data], round(nrow(dataset)*.7)) ## Get sample of 70% of data
training_df <- dataset[index,]
testing_df <- dataset[-index,]
train_features <- training_df[,x:y] ##X and Y refer to the bottom and top bounds of the features of the dataset (depending which ones you want to use)
test_features <- testing_df[,x:y]
train_classes <- training_df$y ##Y refers to the value we are hoping to predict
test_classes <- testing_df$y
knn_classes <- knn(train=train_features, test=test_features, cl=train_classes, k=n) ## n refers to something idk 
confusionMatrix(data=knn_classes, reference=as.factor(test_classes))

## Regression
# Assumptions
# 1. Linearity
# 2. Independence of errors
# 3. Homoscedasticity
# 4. Normality of errors
# 5. No perfect multicollinearity
# 6. No outliers
# 7. No influential points
## Linear Regression
model  <- lm(y~x, data=data)

## Cubic regression
lims <- range(data)
grid <- seq(from=lims[1], to=lims[2])
fit.cbsp <- lm(y~bs(x), data=data)

## Multiple linreg
mlm <- lm(y~x + < i + j + k + ... + l>, data=data)


## Logistic regression:
model <- glm(y~x, family=binomial, data=data)

## Stepwise regression:
library(MASS)
step.model <- stepAIC(lm_model, direction= "", trace=)

## Weighted ls

#Robust regression

## Bayes classifier
# Assumptions
# 1. Feature Independence
# 2. Class-conditional independence
# 3. Data Adequacy
# 4. Well-seperated classes
# 5. Numeric features assumption
# 6. Distributional assumption
model <- naiveBayes(y~xmin + ymax, data=data)

## Tree
library(rpart)
rpart(y ~ x + <i + j + k + ... + l>, data=data)

## Model Analysis
predict(model)
confint(model)
anova(model)
