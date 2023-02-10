1. What determines the maturity of the MLOps process?
  + The level of automation of ML pipelines.
  > Fundamentally, the level of automation of the Data Collection, Modeling, Deployment, and Maintenance systems determines the maturity of the MLOps process.
2. True Or False: At the basic level of maturity, or level 0, tracking or logging are required to detect model performance degradation and other model behavioral drifts
  + Level 0 is concerned only with deploying the trained model as a prediction service (for example, a microservice with a REST API). This manual, data-scientist-driven process doesn’t track predictions and might be sufficient when models are rarely changed or retrained.
3. What steps do you need to introduce into the ML pipeline to move towards MLOps maturity level one? (Select all that apply)
  + Automated Model Validation
  > Model Validation makes sure that the new model performs better than the current one before promoting it to production. Also, Model Validation ensures that model performance is consistent on various segments of the data.
  + Automated Data Validation
  > Automated data validation is necessary to decide whether your model should be retrained or the execution of the pipeline must stop. This decision is automatically made only if the data is deemed valid.
4. In case of an interruption, what key component of the pipeline allows you to resume execution seamlessly?
    + The Model Registry component is a centralized model store, set of APIs, and UI, to collaboratively manage the MLOps lifecycle. It provides model lineage, model versioning, stage transitions, and annotations, but it won't resume execution if interrupted.
    +  A feature store lets you discover and reuse available feature sets. You can also serve up-to-date feature values from the feature store and avoid training-serving skew. However, it's not designed for contingencies.
    + Trigger: In MLOps, it's common to retrain your model when new data is available. Once programmatically scheduled, the trigger runs the pipeline when more data is added, but it won't resume execution if the process is interrupted.
    + Metadata Store: The metadata store tracks each pipeline execution, so you can rely on pointers to the artifacts produced at each step, like the location of prepared data, validation anomalies, or computed statistics, to resume execution in case of an interruption.
    > Answer Metadata store