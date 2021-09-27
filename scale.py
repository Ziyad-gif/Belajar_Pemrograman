from numpy import random
import matplotlib.pyplot as pit
import seaborn as sns
sns.displot(random.exponential(size=10000))
pit.show()