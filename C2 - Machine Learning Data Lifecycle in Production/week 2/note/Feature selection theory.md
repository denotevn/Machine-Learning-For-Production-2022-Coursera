## Feature Selection
  + Identify features that best represent the relationship
  + Remove features that don’t inﬂuence the outcome
  + Reduce the size of the feature space
  + Reduce the resource requirements and model complexity
> Why is feature selection needed?
  + Reduce storage and I/O requirements
  + Minimize training and inference costs
## **Feature selection method:**
  + Unsupervised: 
      + Features-target variable relationship not considered
      + Removes redundant features (correlation)
  + Supervised
      + Uses features-target variable relationship
      + Selects those contributing the most
### 1. Supervised methods
  + Filter method:
     + Correlation: Correlated features are usually redundant
        + More information about Correlation here: **[LINK](https://towardsdatascience.com/why-feature-correlation-matters-a-lot-847e8ba439c4)**
        + Pearson Correlation: Between features, and between the features and the label
        + Univariate feature Selection
     + Set of all feature -> selecting the best subset -> ML model -> Performance
     + Univariate feature selection in SKLearn:
        + SelectKBest
        + SelectPercentile
        + GenericUnivariateSelect   
  + Wrapper method
  + Embedded method
  + Feature selection techniques on Breast Cancer Dataset (Diagnostic). Predicting whether tumour is benign or malignant.
> **More information in lecture of week 2**