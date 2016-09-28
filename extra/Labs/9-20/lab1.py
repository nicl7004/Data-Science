# scipy numpy and pandas, and sklearn, and nltk
import numpy, pandas, scipy, random
from scipy.stats import norm
from scipy.stats import expon
import matplotlib.pyplot as plt
# 10 parts true false
# 340 students

# use normal distro
# or binom distro

# x =(numpy.random.binomial(10, .5, 340))
# plt.hist(x)
# plt.xlabel("Value")
# plt.ylabel("Occurances")
# plt.show()

# POISSON DISTRO

# x = numpy.random.poisson(6,1000000)
#
# plt.hist(x)
# plt.show()
#
# print(x)
# look up kahn on poisson distribution



# REJECTION STUFF USING NORM CDF **************************************
# left =1-(norm.cdf(1.003,1,0.002))
# right = norm.cdf(0.997,1,0.002)
# print(left,right)
# total = left+right
# plt.hist(left)
# plt.show()
#
# print (total*100)
# ****************************************************
y = expon.cdf(4,scale = 2)
over4 = 1 -y
over8 = 1 - (expon.cdf(8,scale = 2))
print(over8, "over8", over4, "over4")
