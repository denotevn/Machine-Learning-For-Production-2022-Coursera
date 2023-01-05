1. In the mapping of categorical values, can models directly multiply strings by the learned weights?
  + No
  > Correct! Feature engineering must be  applied in advance  to convert strings into numerical values.
2. You are working on a taxi tip prediction model and your raw dataset has columns for the latitude and longitude of both pickup and dropoff locations. These do not assume a Gaussian distribution. Among the choices below, which two approaches are more likely to make your model learn better from these features? Assume that you are just starting the feature engineering process. (Select two answers)
  + Bucketize the locations into discrete bins.
  > Bucketizing the coordinates will group close proximities together. With this technique, the model can learn which areas are likely to give a bigger tip.
  + Bucketize the locations into discrete bins then do a feature cross of the latitude and longitude.
  > Bucketizing then crossing the features can possibly enhance the predictive quality of the data. For example, a latitude x longitude cross of the pickup locations can let the model learn which combination of these features yield to a bigger tip.
3. Which of the following should you implement when serving your model to ensure its performance?
  + Make sure all data transformations are the same in any scenario
  > The same transformations you did during feature engineering should be applied to the user input when serving your model. This is to avoid training-serving skews. For example, if a feature is normalized during training, then the serving input should also be normalized. Else, the model might behave unexpectedly