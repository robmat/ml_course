dataset = read.csv('Data.csv')
dataset$Age = ifelse(test = is.na(dataset$Age),
                     yes = ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)), 
                     no = dataset$Age)

dataset$Salary = ifelse(test = is.na(dataset$Salary),
                        yes = ave(dataset$Salary, FUN = function(x) mean(x, na.rm = TRUE)), 
                        no = dataset$Salary)