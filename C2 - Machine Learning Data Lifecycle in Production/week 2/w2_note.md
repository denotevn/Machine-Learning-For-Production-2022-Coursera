## **Feature engineering**
### Introduction to preprocessing
  + Coming up with features is difﬁcult, time-consuming, and requires expert knowledge. Applied machine learning often requires careful engineering of the features and dataset.
  + Outline;
    + Squeezing the most out of data: Khai thác tối đa dữ liệu
    + The art of feature engineering: Nghệ thuật kỹ thuật tính năng
    + Feature engineering process: Quy trình kỹ thuật tính năng
    + How feature engineering is done in a typical ML pipeline: Cách kỹ thuật tính năng được thực hiện trong quy trình ML điển hình
  + Squeezing the most out of data
    + Making data useful before training a model
    + Representing data in forms that help models learn
    + Increasing predictive quality
    + Reducing dimensionality with feature engineering
  + it does this by transforming and projecting, eliminating and or combining the features in your raw data to form a new version of your data set.
  + Add new features thai is avalable
  + You need to do the same feature engineering for data both training data and serving data also with valuation data
### Preprocessing Operations
   + Main preprocessing operations
   + Mapping raw data into features
   + Mapping numeric values
   + Mapping categorical values
   + Empirical knowledge of data
   + Make new features by using several different techniques
   + Empirical knowledge of data:
     + Text - stemming, lemmatization, TF-IDF, n-grams, embedding lookup
     + Images - clipping, resizing, cropping, blur, Canny ﬁlters, Sobel ﬁlters, photometric distortions
### Feature Engineering Techniques
  + Feature Scaling: 
     + Feature scaling is a method used to normalize the range of independent variables or features of data
     + In data processing, it is also known as data normalization and is generally performed during the data preprocessing step
     + Methods for Scaling: 
        + Normalization: x' = (x-x_min)/(max(x) - min(x))
        + max(x) and min(x) are the maximum and the minimum values of the feature respectively
        + Standardization: x' = (x-x_tb)/σ 
        + σ is the standard deviation of the feature vector, and x̄ is the average of the feature vector.
  + Normalization and Standardization:
     + Normalization is good to use when the distribution of data does not follow a Gaussian distribution. It can be useful in algorithms that do not assume any distribution of the data like K-Nearest Neighbors.
     + In Neural Networks algorithm that require data on a 0–1 scale, normalization is an essential pre-processing step
     + Standardization can be helpful in cases where the data follows a Gaussian distribution.
     + Compare between them: 
        + Standardization may be used when data represent Gaussian Distribution, while Normalization is great with Non-Gaussian Distribution
        + Impact of Outliers is very high in Normalization
  + Bucketizing / Binning:
        + If you choose to bucketize your numerical features, be clear about how you are setting the boundaries and which type of bucketing you’re applying:
        + Buckets with equally spaced boundaries: the boundaries are fixed and encompass the same range (for example, 0-4 degrees, 5-9 degrees, and 10-14 degrees, or $5,000-$9,999, $10,000-$14,999, and $15,000-$19,999). Some buckets could contain many points, while others could have few or none.
        + Buckets with quantile boundaries: each bucket has the same number of points. The boundaries are not fixed and could encompass a narrow or wide span of values.
        + Roughly dividing the data into equally spaced subgroups
  + Other techniques:
     + PCA - Principal component analysis
     + t-Distrubuted stochatic neghibor embedding(t-SNE)
     + Uniform manifold approximation and projection (UMAP)
  + Tensorflow projector
    + Intuitive exploration of high-dimensional data
    + Visualize & analyze
    + Techniques
        + PCA
        + t-SNE
        + UMAP
        + Custom linear projections
    + Ready to play
### **PCA - Principal component analysis**
    + Visualize multidimensional data. Data visualizations are a great tool for communicating multidimensional data as 2- or 3-dimensional plots.
    + Compress information. Principal Component Analysis is used to compress information to store and transmit data more efficiently. For example, it can be used to compress images without losing too much quality, or in signal processing. The technique has successfully been applied across a wide range of compression problems in pattern recognition (specifically face recognition), image recognition, and more.
    + Simplify complex business decisions.PCA has been employed to simplify traditionally complex business decisions. For example, traders use over 300 financial instruments to manage portfolios.The algorithm has proven successful in the risk management of interest rate derivative portfolios,owering the number of financial instruments from more than 300 to just 3-4 principal components.
    + Clarify convoluted scientific processes. he algorithm has been applied extensively  in the understanding of convoluted and multidirectional factors, which increase the probability of neural ensembles to trigger action potentials.
    > When PCA is used as part of preprocessing, the algorithm is applied to:
      + Reduce the number of dimensions in the training dataset.
      + De-noise the data. Because PCA is computed by finding the components which explain the greatest amount of variance, it captures the signal in the data and omits the noise.
      + More information about PCA here: **[PCA](https://www.keboola.com/blog/pca-machine-learning)**
### **t-SNE - t-Distributed Stochastic Neighbor Embedding**
  + is an unsupervised, non-linear technique primarily used for data exploration and visualizing high-dimensional data.
  + The t-SNE algorithm calculates a similarity measure between pairs of instances in the high dimensional space and in the low dimensional space.  It then tries to optimize these two similarity measures using a cost function. Let’s break that down into 3 basic steps.
  + More information here **[t-SNE](https://towardsdatascience.com/an-introduction-to-t-sne-with-python-example-5a3a293108d1)**
### Feature Crosses
  + Combines multiple features together into a new feature
  + Encodes nonlinearity in the feature space, or encodes the same information in fewer features
  + [A X B]: multiplying the values of two features
  + [A x B x C x D x E]: multiplying the values of 5 features
  + [Day of week, Hour] => [Hour of week]