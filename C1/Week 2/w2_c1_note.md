## **Selecting and Training a Model**
 + Select train model
 + Perform error analysis
 + how to improve your model

### Key challenges
> AI system = Code + data
 + Code: algorithms / model
 + model development is an iterative process
 + ML model: 
    + Algorithms 
    + Hyperpareameters
    + **Data**
 + Model + Hyperparameter + Data -> Training -> Error analysis -> (Model + Hyperparameter+ Data)-> ....
> Challenges in models development: 
 + Doing well on trainning set
 + Doing well on dev/test set
 + Doing well on bussiness metrics/projects goal
 ### Why low average error isn't good enough?
 + See on the leature to receipt more information
 + Skewed (Lech) data distribution: 99% negative 1 positive => Print(0) we have 99% accurany without using algirithms
 + just doing well on the test set is not enough for many priduction applications
 + Pay attention to what the ML system is aiming for in practice
### Establish a baseline
 + usefull - create base line
 + Need to compare accurancy with humman performance, we will evaluate exactly performance of model (Example accurancy - 70%, humman - 70% => error =0, But acc = 92, humman = 99 => error = 7%)
 + Unstructured data: Image , Audio, text
 + Structured Data: For example: data of user in database (name, age, purchase, price, ...)
 + Humman is not are not as looking at data like structured data to make predictions. Humman performance is usually a less usefull baseline for structured data application.
 + Humman level performane (HLP) - particulary for unstructured data problems. 
 + Another way to establish a baseline is to do literature search for state-of-the-art source.
 (tìm kiếm tài liệu cho mã nguồn mở tiên tiến nhất)
 + Quick-and-dirty implementation
 + Performance of older system
 > It's mean create simple model to see in a general way of project machine learning
### Tips for getting started
 + Model, data, hyperparameter -> training -> Error analysis
 + Literature search to see what's possible (courses, blogs, open sources)
 + Find open source implementation if available
 + A resonable algorithm with good data will open outperform a great algorithm with no so good data
 > Deployment constraints when picking a model
 + Yes, if baseline is already established and goal is to build and deploy.
 + No (or not necessary), if purpose is to establish a baseline and determine what is possible an might be worth pursing.
 > Sanity-check for code and algorithm (kiem tra do chinh xac cua ma va thaut toan)
 + Try to overfit a small training datasets before training on a large one.
 + Try to training with a small datasets help us save time for training
## **Error analysis and performance auditing**
### Error analysis example