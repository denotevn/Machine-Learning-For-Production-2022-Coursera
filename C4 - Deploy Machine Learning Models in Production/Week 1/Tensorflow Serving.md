1. What is the most straightforward way of installing TensorFlow Serving?
  + Using Docker Images
  > This route is the most recommended unless there are specific needs not addressed by running in a container.
2. What is the advantage of using the TensorFlow-model-server-universal binary to install TensorFlow Serving over the TensorFlow-model-server binary?
  + The universal binary works on most of the machines.
  > TensorFlow-model-server-universal should work on most if not all machines out there since it doesn't include any platform-specific instruction sets.