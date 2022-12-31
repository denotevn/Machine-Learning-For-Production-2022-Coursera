1. Which of these is a more accurate description of a data-centric approach to ML development?
+ Holding the neural network architecture fixed, work to improve the data to do well on the problem.
> That's right! Data-centric means you focus your efforts on improving the data to raise the system's performance, while keeping the code fixed. 
2. Say you have an algorithm that diagnoses illnesses from medical X-rays, and achieves high average test set accuracy. What can you now say with high confidence about this algorithm? Check all that apply.
+ None of the above.
> That's right! High average test set accuracy is a great achievement, but there is more work to be done to ensure the algorithm works well on real-world data, is fair, and performs well on rare classes of diseases.
3. Which of these statements about establishing a baseline are accurate? Check all that apply.
+ It can be established based on an older ML system
> That’s right! You can establish a baseline using an older system or via a literature or open source search.
+ For unstructured data problems, using human-level performance as the baseline can give an estimate of the irreducible error/Bayes error and what performance is reasonable to achieve.
> That’s right! For most unstructured data problems, human-level performance is a great estimate of Bayes error - an upper limit to your system's potential. 
+ Human level performance (HLP) is generally more effective for establishing a baseline on unstructured data problems (such as images and audio) than structured data problems
> You're right! Humans perform well on unstructured data, like making sense of an image or a sound, but we aren't great at making sense of large amounts of structured data.
4. On a speech recognition problem, say you run the sanity-check test of trying to overfit a single training example. You pick a clearly articulated clip of someone saying “Today’s weather”, and the algorithm fails to fit even this single audio clip, and outputs “______”. What should you do?
+ Debug the code/algorithm/hyperparameters to make it pass this sanity-check test first, before moving to larger datasets.
> That's right! Something is clearly wrong with the implementation if the algorithm is unable to overfit to a single training example! Find the root cause, fix the problem, and then move onto larger datasets. 