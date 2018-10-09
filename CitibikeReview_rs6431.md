This Rewiew is written by rs6431.

### a. verify the Null and alternative hypotheses: 
The Null and Alternative hypothesis meet the idea and are also testable. Specifically, the hypothesis contains three key parts. First is "statistics", which refers to "the trip duration". Second is "sample", which refers to "riders born before or in year 1960/riders born after 1960". Third is "quantities that can be measured", which refers to "longer/same/shorter" of the duration. 

In terms of the formulation, the author wirte correct equation, highlight the meaning of characters, and also point out the significance level.

Suggestions: If use the $t_0$ instead of t0 when writing the hypothesis, the formulation will be more readable and beautiful. In addtion, be careful of the spelling, such as "beofre".

Overall, this is good hypothesis and also formulated correctly.


### b. verify that the data supports the project: i.e. if the a data has the appropriate features (variables) to answer the question, and if the data was properly pre-processed to extract the needed values:
In order to test the hypothesis, the author picks out two variables: trip deuration and birth year, which is appropriate and correct to answer the question.

Suggestions: To better extract needed values, the data can be further processed into two groups "rider born before and in 1960" and "rider born after 1960" with correponding duration, which refers to two samples that will be tested. Then, in the next step visualozation (plotting), the x axis can be these two groups rather than seperate years, which seems more fit the hypothesis. In addtion, if highlight the scare of y-axis ("seconds" in this case) when plotting, it will be more readable. 


### c. chose an appropriate test to test H0 given the type of data, and the question asked:
In this case, the data is numerical data (as "trip duration" is measured by numberical type data "seconds"), and it is two groups comparison rather than multiple group comparison (as two groups are "rider born before and in 1960" and "rider born after 1960"). In addition, the hypothesis wants to test two samples rather than samples versus population. Therefore, the t-test is suitable for testing the $H_0$.

As for the one-tail and two-tail, a one-tailed test calculates the possibility of deviation from the null hypothesis in a specific direction, whereas a two-tailed test calculates the possibility of deviation from the null hypothesis in either direction. In this case, since the hypothesis measures more/less for one group than for the other, one tail test should be used. 