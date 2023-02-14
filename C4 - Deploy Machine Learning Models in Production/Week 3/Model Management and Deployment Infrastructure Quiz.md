1. When does the minor version number increase in the MAJOR.MINOR.PIPELINE approach of model versioning?
   + When we’ve improved the model's output.
   >  The minor version will increment when we believe that we've improved or enhanced the model's output.
2. Which well known product uses pipeline execution versioning?
   + TensorFlow Extended
   > TFX uses pipeline execution versioning. In this style, a new version is defined with each successfully run training pipeline. Models will be versioned regardless of changes to model architecture, input, or output.
3. What are some non-standard ML Unit Testing Considerations? (Select all that apply)
   + Code Coverage
   > If you've created good mocks and good tests, you should have good code coverage. Using the available code coverage libraries, you can test and track that you're not missing unit tests for any part of the code.
   + Data Coverage
   > Ideally, your mocks should occupy roughly the same region of your feature space as the actual data would, but much more sparsely, of course.
   + Mocking
   >  Designing mocks of datasets is essential for ML unit testing. They should cover your edge and corner cases, requiring you to think about your features and domain.
4.  Which of the following is true about the comparison between canary and blue-green deployment?
   + Canary is cheaper than a blue-green deployment because it does not require two production environments.
   > Canary deployments allow organizations to test in production with real users and cases and compare different service versions side by side.