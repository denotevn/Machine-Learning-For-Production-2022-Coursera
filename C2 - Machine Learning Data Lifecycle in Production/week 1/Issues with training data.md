1. What formula represents a dataset shift?
  + P_train(y,x) != P_serve(y,x)
  >  The most generic case of distribution skews is when the joint distribution of inputs and outputs differs between training and serving.
2. What measure is typically used to determine the degree of data drift?
  + Chebyshev distance (L-infinity)
  > Chebyshev distance is defined as max|x_i - y_i|
3. Distribution skew occurs when the distribution of the training dataset is significantly different from the distribution of the serving dataset, and is typically caused by: (check all that apply). 
  + Trend, seasonality, changes in data over time.
  > Keep it up! Data distributions between training and serving often change and so this is another case of distribution skew.
  + Different data sources for training and serving data.
  > Way to go! Data sources between training and serving often change and so this is another case of distribution skew.
  + Faulty sampling method that selects a sample for training which is not representative of serving data distribution.
  > A faulty sampling mechanism that chooses a non-representative subsample is an example of distribution skew.
4. TensorFlow Data Validation (TFDV) helps TFX users maintain the health of their ML pipelines. TFDV can analyze training and serves data to:
  + Infer a schema.
  > In short, schemas describe the expectations for "correct" data and can thus be used to detect errors in the data.
  + Detect data anomalies.
  > TFDV can check your data for error in the aggregate across an entire dataset or by checking for errors on a per-example basis.
  + Compute descriptive statistics.
  > TFDV goes beyond computing relevant statistics, it also has nice browser-based visualization tools.