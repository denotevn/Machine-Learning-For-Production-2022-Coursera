### Overwiew
  + The important of data: Data is gardest path and the most important piece to get right... broken data is the most common cause of problems in production ML systems
  + Production ML = ML development + sofware development
  + Data -> Training -> Evaluation -> Data .....
  + Managing the entire life cycle of data: 
    + Labeling
    + Feature space coverage
    + Minimal dimensionality
    + Maximum predictive data
    + Fairness 
    + Rare conditions
  + Modern software development:
    + Scalability: khả năng mở rộng
    + Extensibility: khả năng mở rộng
    + Configuration: Cấu hình 
    + Consistency and reproducibility: Tính nhất quán và khả năng tái sản xuất
    + Safety & security
    + Modularity
    + Testability
    + Monitoring 
    + Best practices
  + Product Machine Learning system:
    + Scoping: Define the project
    + Data: Defining the features, label and organize data
    + Modeling: Select and train model, perform error analysis
    + Deployment: Deploy in production, Monitor and maintain system
    + And go back iteratively 
  + Challenges in production grade ML:
    + Build integrated ML system
    + Continously operate it in production
    + Handle continously changing data
    + Optimize compute resource costs

## **ALL knowdlege in lectures** 

### Important of data
  + Important of data quality
  + Data pipeline: data collection, ingestion and preparagation
  + Data collection and monitoring
### Key considerations
  + Data availability and collection
  + What kind of/how much data is available?
  + How often does the new data come in?
  + Is it annotated?
    + If not, how hard/expensive is it to get it labeled?
+ Translate user needs into data needs
  + Data needed
  + Features needed
  + Labels needed
+ Get to know your data
  + Identify data sources
  + Check if they are refreshed
  + Consistency for values, units, & data types
  + Monitor outliers and errors
### Dataset issues
  + Inconsistent formatting
    + Is zero “0”, “0.0”, or an indicator of a missing measurement
  + Compounding errors from other ML Models
  + Monitor data sources for system issues and outages
### Measure data effectiveness
  + Intuition about data value can be misleading
    + Which features have predictive value and which ones do not?
  + Feature engineering helps to maximize the predictive signals
  + Feature selection helps to measure the predictive signals
### Meaningful data: 
  + maximaize predictive content
  + remove non-informative data
  + features space coverage
### Data security and privacy
  + Data collection and management isn’t just about your model
    + Give user control of what data can be collected
    + Is there a risk of inadvertently revealing user data?
  + Compliance with regulations and policies (e.g. GDPR)
### Users privacy
  + Protect personal identiﬁable information
    + Aggregation - replace unique values with summary value
    + Redaction - remove some data to create less complete picture
  + How ML systems can fail users
    + Representational harm
    + Opportunity denial
    + Disproportionate product failure
    + Harm by disadvantage
### Commit to fairness
  + Make sure your models are fair
    + Group fairness, equal accuracy
    + Bias in human labeled and/or collected data
    + ML Models can amplify biases
### Types of human raters
  + Generalists: crowdsourcing tools
  + Subject matter experts: Specialized tools, e.g. medical Image labelling
  + Our Users: Derived labels, e.g. tagging photos
### **Why is labeling important in production ML?**
  + Using business/organisation available data
  + Frequent model retraining
  + Labeling ongoing and critical process
  + Creating a training datasets requires labels
> **Direct labeling: continuous creation of training dataset**
  + Features from inference requests - >Labels from monitoring predictions -> Join results with inference requests -> Similar to reinforcement learning rewards -> Features from inference requests
### **Process feedback - Cloud log analytics**
  + Google Cloud Logging: 
    + Data and events from Google Cloud and AWS
    + BindPlane. Logging: application components, on-premise and hybrid cloud systems
    + Sends it to your favorite "stash"
  + AWS ElasticSearch
  + Azure Monitor
### Human labeling
  + People (“raters”) to examine data and assign labels manually
    + Unlabeled data is collected
    + Instructions to guide raters are created
    + Data is divided and assigned to raters
    + Labels are collected and conﬂicts resolved
  + Human labeling - advantages
    + More labels
    + Pure supervised learning
  + Human labeling - Disadvantages
    + Quality consistency: Many datasets difﬁcult for human labeling
    + Slow
    + Expensive
    + Small datasets curation