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

## Least Squares regression
model  <- lm(y~x, data=data)

## Weighted ls

## Bayes classifier
model <- naiveBayes(y~xmin + ymax, data=data)

#Robust regression

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

## Tree
library(rpart)
rpart(y ~ x + <i + j + k + ... + l>, data=data)

## Model Analysis
predict(model)
confint(model)
anova(model)
