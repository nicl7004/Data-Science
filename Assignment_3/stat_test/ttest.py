from math import sqrt

from scipy.stats import t
from numpy import mean

def degrees_of_freedom(s1, s2, n1, n2):

# for sa, sb in s1, s2
    num = (((s1**2)/n1)+((s2**2)/n2))**2
    denomA = (1/(n1-1))*(((s1**2)/n1)**2)
    denomB = (1/(n2-1))*(((s2**2)/n2)**2)

    return(num/(denomA+denomB))


def unbiased_sample_variance(observations, mean):
    """
    Compute the unbiased sample variance

    @param observations Iterable set of observations
    @param mean The estimated mean
    """
    total = 0
    for each in observations:
        x = (mean - each)**2
        total +=x



    return (total/(len(observations) -1))

def t_statistic(mean1, mean2, n1, n2, svar1, svar2):
    """
    Compute the t-statistic for the given estimates
    """

    mean =mean1 - mean2
    denom = sqrt((svar1/n1)+(svar2/n2))

    return  (mean/denom)



def t_test(sample1, sample2):

    mean1 = sum(sample1)/ len(sample1)
    mean2 = sum(sample2)/ len(sample2)
    n1 = len(sample1)
    n2 = len(sample2)

    s1, s2 = unbiased_sample_variance(sample1, mean1), unbiased_sample_variance(sample2, mean2)

    tStat = t_statistic(mean1, mean2, n1, n2, s1, s2)

    return (1-t.cdf(tStat, degrees_of_freedom(s1, s2, n1, n2)))*2


if __name__ == "__main__":
    v1 = [5, 7, 5, 3, 5, 3, 3, 9]
    v2 = [8, 1, 4, 6, 6, 4, 1, 2]

    print("p-value is %f" % t_test(v1, v2))
