1. What is the core idea of the TensorFlow Serving Architecture?
   + The servable
   > he servable is the central abstraction in TF-Serving. Clients use these underlying objects to perform computation.
2. True or False: Triton Inference Server simplifies deployment since it is compatible with trained AI models from any framework.
   + True
   > Triton Inference Server allows deployment of models from any framework, from local storage, Google Cloud Platform, or AWS S3.
3. In the TorchServe architecture, where does the actual inference take place?
   + Model Workers at the backend
   > Model Workers are running instances of the model responsible for performing the actual inference. Thus, multiple workers can run simultaneously on Torch Serve.