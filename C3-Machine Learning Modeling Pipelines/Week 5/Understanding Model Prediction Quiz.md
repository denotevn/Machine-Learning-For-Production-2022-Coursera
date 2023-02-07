1. Model-agnostic methods have access to the model's internals, and they can be applied to any model after being trained.
   + False 
   > You must remember that model-agnostic methods are essentially post-hoc methods. The termIt refers to treating the models as black boxes and not having access to the model's internals. Therefore, the claim is false.
2. PDP (Partial Dependence Plots) is a local method that evaluates a specific relationship between the labels and the results
   + False
   > PDP is a global method. It considers all instances and also the features and the results for evaluating the global relationships.
3. We can measure the importance of a feature with the Permutation Feature Importance technique. What statements are true about an “important” feature?
   + Shuffling its values increases the model error.
   > Correct! This indicates the model relied on the feature for the prediction.
4. A technique for understanding model predictions is the concept of the Shapley Values. It assigns payouts (predictions) to players (features) depending on their contribution. So, The Shapley Values is a method for knowing how much each feature depends on the results.
   + False
   > The features do not depend on the results, but the results do depend on the characteristics. The Shapley Values is a method for determining and understanding the relation between the important factors in the features and the generated model’s result.