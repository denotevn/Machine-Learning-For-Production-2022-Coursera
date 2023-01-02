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
  + Other use of HLP:
    + In academica, establish and beat a respectable benchmark to support publication
    + Bussiness or product owner asks for 99% accurancy. HPL helps establish a more resonable target. 
    + Prove the ML system is superior to humans doing the job and thus the business or product owner should adopt it with crusial. 
    + In fact, HLP usually use for establish baseline, analysis error and prioritization. But using it to benchmark machines  and human sometimes runs into problematic case. 
### Raise Human Level Performance (HLP):
  + We raise HLP by improving label consistency and that ultimately results in better learning outcomes performance as well.
  + When the ground truth is defined by a human, maybe even a doctor labeled an X-ray image, then HLP is just measuring how well can one doctor predict another doctor's label versus how well can one learning algorithm predict another doctor's label. That too is useful, but it's different than if you're measuring how well you versus a doctor are predicting some ground truth outcome from a medical biopsy

### Label and Organize Data
  + Level consistent label of data help improve HLP
  + POC :
    + Goal is decide if the application is workable and worth deploying 
    + Focus on getting the prototype to work
    + It's ok if data pre-processing is manual. But take extensive notes/comments
  + Production phases:
    + After project utility is established , use more sophisticated tools to make sure the data pipeline is replicable 
    + Eg. Tensorflow Transform, Apache Beam, Airflow, ..
### Metadata:
  + For some applications, having and tracking metadata, data provenance, and data lineage can be a big help
  + For example, in manufacturing visual inspection, the data would be the pictures of phones and the labels but if you have metadata that tells you what time was this picture of a phone taken, what factory was this picture from, what's the line number, what were the camera settings such as camera exposure time and camera aperture, what's the number of the phone you're inspecting, what's the ID of the inspector that provided this label. These are examples of data about your dataset X and Y.
  + To summarize, metadata can be very useful for error analysis and spotting unexpected effects or tags or categories of data that have some unusually poor performance or something else, to suggest how to improve your system.
### Scoping data:
  + Scoping examples. Ecommerce retailer looking to increase sales:
    + Better recommender system
    + Better search
    + Improve catalog data
    + Invetory managment
    + Proce optimazation
  + Scoping process:
    + share with you a process for scoping projects, that hope will be valuable for how you decide what to work on
    + scoping process: 
      + Brainstorm business problems (not AI problems)
      + Brainstorm AI solutions
      + Assess the feasibility and value of potential solution
      + Determin milestones
      + Budget for resource
  + **To be more information, see lecture of week 3**
### Diligence on feasibility and value:
  + How do you know if this thing can even be built? 
    + Use external benchmark(literature, other company, competitor)