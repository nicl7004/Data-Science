# scipy numpy and pandas, and sklearn, and nltk
import numpy, pandas, scipy
import matplotlib.pyplot as plt
# 10 parts true false
# 340 students

# use normal distro
# or binom distro

x =(numpy.random.binomial(10, .5, 340))
plt.hist(x)
plt.xlabel("Value")
plt.ylabel("Occurances")
plt.show()
