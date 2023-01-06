## Problems
   + Inconsistencies in feature engineering
   + Preprocessing granularity
   + Pre-processing training dataset
   + Optimizing instance-level transformations
   + Summarizing the challenges
> **Real-world models: terabytes of data  -> Large-scale data processing frameworks -> Consistent transforms between training & serving**
### Inconsistencies in feature engineering
  + Training & serving code paths are different
  + Diverse deployments scenarios(Kịch bản triển khai đa dạng):
    + Mobile (TensorFlow Lite)
    + Server (TensorFlow Serving)
    + Web (TensorFlow JS)
  + Risks of introducing training-serving skews
  + Skews will lower the performance of your serving model
### Preprocessing granularity
  + Transformation within model:
    + Pros: 
       + Easy iterations
       + Transformation guarantees
    + Cons:
       + Expensive transform
       + Long model latency (do tre)
       + Transformation per batch : skew
    + Why transorm per batch: 
      + For example, normalizing features by their average
      + Access to a single batch of data, not the full dataset
      + Ways to normalize per batch
        + Normalize by average within a batch
        + Precompute average and reuse it during normalization
## **Tensorflow transform**
   + See in lecture 
   + Beneﬁts of using tf.Transform
      + Emitted tf.Graph holds all necessary constants and transformations
      + Focus on data preprocessing only at training time
      + Works in-line during both training and serving
      + No need for preprocessing code at serving time
      + Consistently applied transformations irrespective of deployment platform
   + ![Examples](https://github.com/denotevn/Machine-Learning-For-Production-2022/blob/main/C2%20-%20Machine%20Learning%20Data%20Lifecycle%20in%20Production/week%202/images/tensorflow_for%20ML%20production.png) 

