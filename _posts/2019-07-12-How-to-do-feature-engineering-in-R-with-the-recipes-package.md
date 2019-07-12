---
layout: post
title: "How to do feature engineering in R with the recipes package"
date:  2019-07-12 09:00:00
categories: R
image: /assets/images/salt-fat-acid-heat.jpg
---

I was excited to start using Max Khun (creator of [Caret](https://topepo.github.io/caret/)'s) new set of '[tidymodels](https://github.com/tidymodels)' packages - rsample, recipe, yardstick, parsnip and dials. These are still under development but seem promising. The one I have so far found most useful is [recipe](https://tidymodels.github.io/recipes/). Here I'll give a quick overview of how you use it to do some simple data preparation for machine learning.

R's approach to machine learning has always been a bit haphazard and fragmented. There has never been an equivalent to python's [scikit-learn](https://scikit-learn.org). I have never really got along with caret (the main contender) or [mlr](https://mlr.mlr-org.com/). I found the API difficult to learn and I've never liked the amount of control you give up as a result of using them. I like the fact that these new set of packages are modular and so can be used without fully giving up on other approaches.

### Recipe

{: .center}
![image from the excellent book salt fat acid heat](/assets/images/salt-fat-acid-heat.jpg){: width="80%" }

Basically, recipe provides a bunch of tools for preparing data and creating design matrices. This is a form of feature engineering. These matrices can then be used as training data for ML models. This is done in four steps:

1. Create a recipe made up of steps (eg. missing data imputation and skew correction - many are provided in the package)
2. Prep that recipe using the training data (eg. use the training data to learn imputation values)
3. Create a model matrix by applying the prepped recipe to the training data
4. (Optional) Create another model matrix using the same steps but applied to a new dataset (a test or production dataset say).

Here is a quick example the does median imputation, centres and scales the airquality dataset to give an idea for how it would work.

{% highlight R %}
library(recipes)
aq_train = airquality[1:100, ]
aq_test = airquality[-(1:100), ]

#make recipe
recipe_1 = recipe(formula = Ozone ~ Solar.R + Wind + Temp + Month + Day,
                  data = aq_train) %>%
  #add steps
  step_medianimpute(all_numeric()) %>%
  step_center(all_numeric())  %>%
  step_scale( all_numeric())  %>%
  #prep recipe
  prep(training = aq_train, retain = TRUE,  verbose = TRUE)

#make model matrices
mm_train = bake(recipe_1, new_data = aq_train, composition = 'matrix')
mm_test = bake(recipe_1, new_data = aq_test, composition = 'matrix')
{% endhighlight %}

After doing this you can go off and do what you want with the model matrix. Changing the composition argument allows you to get a ""tibble", "matrix", "data.frame", or "dgCMatrix".

This approach is flexible and allows a prepped recipe to be applied to a new dataset avoiding [data leakage](https://medium.com/@ODSC/how-to-fix-data-leakage-your-models-greatest-enemy-e34fa26abac5) problems. A list of available functions is [here](https://tidymodels.github.io/recipes/reference/index.html#section-basic-functions). User defined functions can also be made.

The recipe package is really useful and i've been using it a lot lately - it has streamlined a bit of my workflow that I'd been struggling with. It still has a few rough edges but is really worth trying out.
