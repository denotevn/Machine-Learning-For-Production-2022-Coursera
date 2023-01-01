## **Data defination and Baseline**
> Learning Objectives:
        > List the questions you need to answer in the process of data definition.
        > Compare and contrast the types of data problems you need to solve for structured vs. unstructured and big vs. small data.
        > Explain why label consistency is important and how you can improve it
        > Explain why beating human level performance is not always indicative of success of an ML model.
        > Make a case for improving human level performance rather than beating it.
        > Identify how much training data you should gather given time and resource constraints.
        > Describe the key steps in a data pipeline.
        > Compare and contrast the proof of concept vs. production phases on an ML project.
        > Explain the importance of keeping track of data provenance and lineage.

### Why data is defination hard?
 + Data definition:
   + What is input x? Lighting? Contract? Resolution?
   + for examples you want to detect defects on phone. You need to answer the folowing question:
        + Is the camera resolution good enough?
        + For the picture you take, Is the lighting good enough?
        + If the photo is so dark that people can't distinguish the defects of the phone. You should ask for other photos with better brightness.
### Major types of data problems of machine learning projects:
  + Human are great at processing unstructured data like images or text and not at good at processing structured data like database records.
  + The size of datasets: You have small datasets or large datasets?
  + Unstrutured data vs. strutured data:
    + Unstrutured data: 
        + May or not have huge collection of unlabeled examples x: just colect and don't labeling for data.
        + Humans can lable more data
        + Data augmentation more likely to be helpful
    + Strutured data:
        + Maybe more dificult to obtain more data
        + Human labeling may not be possible (with some exceptions)
  + Small data (<10000 examples) avs. Big data(>10000 examples): 
    + Small data: 
        + Clean labels are crucial
        + Can manually look through datasets and fix label
        + Can get all the labelers to talk to each other
    + Big data: 
        + Emphasis data process
### Small data and label consistently:
  + Why label consistency is important
  + If you have a small datasets, clean (consistent) labels is very crucial
  + Even you have a big dataset , the label consistency is very important for you model.
### Improving label consistentcy
  + Have multiple label consistency
  + When there is dissagrement, have MLE, subject matter expert. MLE - là phương pháp dự đoán tham số của một mô hình thống kê dựa trên những “quan sát” có sẵn, bằng cách tìm bộ tham số sao cho có thể tối đa hoá khả năng mà mô hình với bộ tham số đó sinh ra các “quan sát” có sẵn.
  + If labelers believe that x doesn't contain enough information, consider changing x.
  + Iterate until it is hard to significantly increase agreement 
  + Small data:
    + Usually small number of labelers 
    + Can ask labelers to dicuss specific labels
  + Big data: 
    + get to consistent definition with a small group
    + then send labeling instruction to labelers
    + Can consider having multiple labelers label every example and using voting or consensus labels to increase accurancy
### Human level performance (HLP):
  + Why measure HLP: Estimate bayes error/ irreducible error to help with error analysis and prioritization. Esspesially on unstrutured data tasks in oder to help with their analysis and prioritization and jus establish what might be possible. 
