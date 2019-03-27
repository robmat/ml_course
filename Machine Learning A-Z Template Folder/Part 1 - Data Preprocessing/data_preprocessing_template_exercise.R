dataset = read.csv('Data.csv')

dataset$Age = ifelse(test = is.na(dataset$Age),
                     yes = ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)), 
                     no = dataset$Age)

dataset$Salary = ifelse(test = is.na(dataset$Salary),
                        yes = ave(dataset$Salary, FUN = function(x) mean(x, na.rm = TRUE)), 
                        no = dataset$Salary)

dataset$Country = factor(x = dataset$Country,
                         levels = c('France', 'Spain', 'Germany'),
                         labels = c(1, 2, 3))
dataset$Purchased = factor(x = dataset$Purchased,
                           levels = c('No', 'Yes'),
                           labels = c(0, 1))

# install.packages('caTools')
# library(caTools)
set.seed(seed = 123)
split = sample.split(Y = dataset$Purchased,
                     SplitRatio = 0.8)

trianing_set = subset(x = dataset,
                      subset = split == TRUE)
test_set = subset(x = dataset,
                      subset = split == FALSE)