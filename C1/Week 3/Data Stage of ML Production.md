1. Which of these statements do you agree with regarding structured vs. unstructured data problems?
    + It is generally easier for humans to label data and to apply data augmentation on unstructured data than structured data.
    > That's right! Humans are better able to label unstructured data such as images and audio clips than complex, high-dimensional structured data. As well, it's not always possible to apply data augmentation to structured data.
2. Take speech recognition. Some labelers transcribe with “...” (as in, “Um… today’s weather”) whereas others do so with commas “,”. Human-level performance (HLP) is measured according to how well one transcriber agrees with another. You work with the team and get everyone to consistently use commas “,”. What effect will this have on HLP?
    + HLP will increase.
    > That's right! Since the labels will be more consistent, the labelers will agree with each other more often, raising HLP.
3. Take a phone visual inspection problem. Suppose even a human inspector looking at an image cannot tell if there is a scratch. If however the same inspector were to look at the phone directly (rather than an image of the phone) then they can clearly tell if there is a scratch. Your goal is to build a system that gives accurate inspection decisions for the factory (not publish a paper). What would you do?
    + Try to improve their imaging (camera/lighting) system to improve the quality or clarity of the input images, x.  
    > That's right! If even a human looking at the image cannot identify the presence of a scratch, you'll need to improve the optical quality of your camera to improve your system's performance. 
4. You are building a system to detect cats. You ask labelers to please “use bounding boxes to indicate the position of cats.” Different labelers label as follows:
    + Ambiguous labeling instructions.
    > That's right! Your hardworking labelers may interpret the ambiguous instructions differently and label the images differently. Improve your instructions, and your labelled data will improve!
5. You are building a visual inspection system. HLP is measured according to how well one inspector agrees with another. Error analysis finds:
You decide that it might be worth checking for label consistency on both scratch and discoloration defects. If you had to pick one to start with, which would you pick?
   + It is more promising to check (and potentially improve) label consistency on discoloration defects than scratch defects. Since HLP is lower on discoloration, it's possible that there might be ambiguous labelling instructions that is affecting HLP.
   > Correct. That's right! HLP is lower for discoloration defects so there is an opportunity to improve this metric by improving label consistency. 
6. To implement the data iteration loop effectively, the key is to take all the time that’s needed to construct the right dataset first, so that all development can be done on that dataset without needing to spend time to update the data.
    + False
    > Right on! Collecting and labelling data is an iterative process, get into the data iteration loop as quickly as possible.
7. ou have a data pipeline for product recommendations that (i) cleans data by removing duplicate entries and spam, (ii) makes predictions. An engineering team improves the system used for step (i). If the trained model for step (ii) remains the same, what can we confidently conclude about the performance of the overall system?
    + It's not possible to say - it may perform better or worse.
    > It's really hard to tell, as it depends on how the data was changed, and how your model behaves.
8. What is the primary goal of building a PoC (proof of concept) system?
    + To check feasibility and help decide if an application is workable and worth deploying.
    > That's right! A proof of concept system is a simple way to determine whether its worth the time and effort to develop the product.
9. MLOps tools can store meta-data to keep track of data provenance and lineage. What do the terms data provenance and lineage mean?
    + Data provenance refers to where the data comes from, and data lineage the sequence of processing steps applied to it.
10. You are working on phone visual inspection, where the task is to use an input image, x, to classify defects, y. You have stored meta-data for your entire ML system, such as which factory each image came from. Which of the following are reasonable uses of meta-data?
    + To suggest tags or to generate insights during error analysis.
    + Keeping track of data provenance and lineage.
    > That's right! Meta-data will contain information about where the data come from and what processing steps were applied to it. This can be helpful when performing error analysis.