1. Transformation operations can happen at the instance level or be applied to the entire dataset. Which one is an instance-level transformation?
   + Feature Cross
2. In a pre-processing training dataset, all transformations that are carried out in the training set must also be done in the serving set:
   + True
   > Also, this is considered a con, as it can produce slower iterations being less efficient than in the training.
3. What statement is true about TensorFlow Transfor
   + TF Transform eliminates the risk of introducing training-serving skew
   > TF Transform uses the same code path for both training and serving.