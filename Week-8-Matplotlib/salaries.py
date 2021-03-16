import numpy as np 

minSalary = 20000
maxSalary = 80000
numberEntries = 3

salaries = np.random.randint(minSalary, maxSalary, numberEntries)
salariesPlus = salaries + 5000
salariesMult = salaries + 1.05
#np.random.seed(salaries)
print(salaries)
print(salariesPlus)
print(salariesMult)