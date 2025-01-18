1.  a. ❌

We want to minimize bias and variance, so when we have a lot of samples we can use a flexible model to lower the bias. Overfitting is less of a concern with a lot of samples.

b. I feel like the answer is less flexible because we don't have many samples so we run the risk of overfitting. We would have high variance because if we fit closely to the limited amount of samples and we get a new set the estimate $\hat{f}$

_Also the high number of predictors could lead to overfitting._

c. More flexible because the relationship is more complex and if we used inflexible we'd get a lot of bias

d. If the variance of the error is very high maybe it's a trick question and it doesn't matter because it will dwarf the bias and variance.

_I give myself a check for that as another answer states that the answer is "unknown" because our model cannot reduce the irreducible error._

2.  a.

We want regression because salary is not categorical. We are interested in inference here. n=500, p={profit, # employees, ceo salary and industry}

_Mostly correct, but p=3, the number of predictors!!_

b. classification, prediction, n=20, p=13

c. regression, predicton, n=52, p=3

3. a. As flexibility increases:

- 1. bias goes high to low
- 2. variance goes low to high
- 3. training error goes high to low
- 4. test error is u-shaped
- 5. irreducible error is flat??

b.

- 1. we are reducing the amount of over-simplification as we increase flexibility
- 2. when we fit closely to to the training data with a highly flexibile model different training data would produce very different fhats.
- 3. we are fitting closer and closer to the training data
- 4. the test error needs to hit the sweet spot between bias and variance
- 5. irreducible error is not dependent on the flexibility of the model. See the formula for the expected test error!

4. a.

- 1. over/under game totals. Response total goals being over or under the posted total. Some possible predictors include XG, corsi, fenwick, goalie quality measured by GSAX, rest, etc. This is prediction but also inference because we might want to know which features have the strongest effect
- 2. what religion someone identifies as. Response is the religion. Age, race, country living in, country of origin, gender. Prediction.
- 3. cancer detection. Response is benign or malignant tumor. Mass size, age, smoking status, drinking status, weight, gender, race, socioeconomic status. Prediction

b.

- 1. total goals scored in the game. Response is # of goals scored. Similar predictors as part a. Prediction and inference as well
- 2. How tall someone will be when they grow up. Response is height at age 21. Socioeconomic status, mother's height, father's height, height at age 2,5,10,15 etc. weight at same ages, sex, ethnicity. Prediction
- 3. What causes a student's SAT score. Response is the SAT score. IQ, hours spent studying, extracurricular activities, courseload, socioeconomic status, race... inference.

c.

- 1. geographic clustering of homes. Note that if the features are lat and long only then you get a geographic representation for the clusters, but you can have many features and cluster on whatever
- 2. consumer profiling. What archetype does a shopper fit into.
- 3. bettor profiling, are they sharp or recreational

5.

more flexible:

- possible overfitting
- high variance
- low bias
- possibly higher test error

Use if we think the relationship is very complex. We can safely use more flexibility when we have more observations.

less flexible:

- high bias
- low variance
- high training error
- underfitting
- not capturing the complexity of the relationships between the predictors and the response

Use when we think the relationship is not complex, e.g. linear. When we have fewer observations. _Also when interpretability is important_.

6. Parametric means we are estimating parameters in order to fit the model to the training data and estimate $f$. _We need to make an assumption about the functional form as a first step as well_. Non-parametric we make no assumptions about the shape of the function and we arrive at some function through fitting the model. Parametric you need way less data, Non-parametric you don't run the risk of making the wrong assumption about the functional form.

7. a.

| point | distance    |
| ----- | ----------- |
| 1     | 3           |
| 2     | 2           |
| 3     | $\sqrt{10}$ |
| 4     | $\sqrt{5}$  |
| 5     | $\sqrt{2}$  |
| 6     | $\sqrt{3}$  |

b. when K=1 5 is closest so you'd predict red.

c. when K=3 we choose 5,6 and 2 as the closest so we predict red.

d. We'd want small K because that way the boundary can be more nonlinear. If we choose high K then the boundary would be more linear because each point would be affected by averaging too many other points.
