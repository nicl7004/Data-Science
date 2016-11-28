# Nicholas Clement
I updated the LogReg class constructor to accept an additional parameter learning_rate, instead of presetting it to 0.5.

Learning rate is vital to the efficiency and accuracy of our logistic regression. If too small a learning rate is chosen then code will take thousands of iterations to execute.  If our step size is too large we will yield inaccurate results.  To test step sizes I updated the unit tests to run with different step sizes and timed the execution.
