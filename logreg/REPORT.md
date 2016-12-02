# Nicholas Clement
## 1. Learning Rate
Learning rate is vital to the efficiency and accuracy of our logistic regression. If too small a learning rate is chosen then code will take thousands of iterations to execute.
![?](min.png =250x100)

If our step size is too large we will end up oscillating and never finding a good solution.

![?](max.png =250x)

## 2. Number of Iterations

![?](log.png =250x)

It can be seen that it took 1061 steps for us to reach a HA (Heldout accuracy) of about 95% and a TA (Train Accuracy) of about 97.5%. This counts as a single pass of our data, which is all we need for it to converge.

## 3. Good Predictors

![?](histo.png =250x)

This is a histogram of our final beta (weight) vector.  It can be seen that the majority of weights fell between the -0.2 and +0.2 barriers.  For this reason we can assume that any weight that falls beyond -0.2 or +0.2 would be a "good" indicator of the document. The absolute best indicators are going to lie near the -0.6 or +0.6 marks, because their weights are very strong and suggestive of the document they correlate to.

It is good to keep in mind that a positive probability is tied to baseball, while a negative probability correlates to hockey.

### Best Predictors:

The best predictors for this dataset were "runs" and "hockey". In order to find these I used `numpy.argmin()` and `numpy.argmax()`.  These functions returned the max/min indexes of the beta vector. With these indexes I used the vocabulary to find the best words to determine if the document was correlated to baseball or hockey.

![?](max-min.png =250x)
