import numpy as np
from inflammation .models import daily_mean
data = np.loadtxt(fname='inflammation-01.csv', delimiter=',')
print(data.shape)

print(daily_mean(data[0:4]))