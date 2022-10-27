# Hierarchy_Analysis_Method
Or
# Analytic hierarchy process

In the theory of decision making, is a structured technique for organizing and analyzing complex decisions, based on mathematics and psychology. It was developed by Thomas L. Saaty in the 1970s; 
Saaty partnered with Ernest Forman to develop Expert Choice software in 1983, and AHP has been extensively studied and refined since then. It represents an accurate approach to quantifying the weights of decision criteria. Individual experts’ experiences are utilized to estimate the relative magnitudes of factors through pair-wise comparisons. Each of the respondents compares the relative importance each pair of items using a specially designed questionnaire.

# Overal description of the method

The methode has a scheme, that consists of 4 levels:
1. The first level is the goal (key question) of the decision 
2. The second level is criteria of the decision. What parameters are important while making the decision?
3. If some or all the critera of the previous level are complicated, a third level is introduced. It consists of the criteria for the criteria of the previous level. – at the time the program does not  support multilevel hierarchies
4. The last level describes the alternatives, that we are facing when deciding

# Algorithm
1. Formulate goal of the decision
2. Build a hierarchical decision tree for the problem
3. Evaluate the relative 'importance' of each criteria for the goal above
4. Calculate the priority vector
5. Make sure, that the evaluation of the criteria is well consistent. To do this one needs to calculate the consistensy relation and index
6. If the consistensy index is not satisfying, then reevaluate the criteria of the decision task
7. steps 3-6 are repeated for each level of the decision task
8. The one should syntesise the levels of the decision

# Let's look at the algorythm and solve a sample task:
