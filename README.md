# SBSPS-Challenge-5297-Fashion-Redefined-with-Virtual-Grooming-Shopping-Assistant

# Fashion Redefined with Virtual Grooming and  Shopping Assistant

![image](https://user-images.githubusercontent.com/58814795/131345636-2e42344f-c94d-47a2-94e9-05d556966e43.png)

## Contents
  * [Introduction](README.md#Intoduction)
  * [IBM Chatbot (Watson Assistant)](README.md#ibm-chatbot-watson-assiatant)
  * [CNN Classfication Model](README.md#cnn-classfication-model)
  * [Virtual Try-on](README.md#virtual-try-on)
  * [Flask App for Suggesting Fashion Trends](README.md#flask-app-for-suggesting-fashion-trends)
  * [Flask App for Virtual Try-on](README.md#flask-app-for-virtual-try-on)
  * [Overall Application](README.md#overall-application)

## Introduction
Fashion trends are considered to be one of the most important aspect of everyone's life today. Many people finds it hard to get appropriate costumes as per their own interest that also suits their look. Our solution is to provide fashion suggestions for users based on their look and appearance and they can select from the list of suggestions provided. We are using CNN classification model that analyze the user's image and provide a set of suggestions based on the class that the model detected. We have also used IBM's chatbot service (Watson Assistant) which helps in providing suggestions by gathering basic inputs as parameters. We have also incorporated a special model that gets user image as input along with the cloth image of user's own interest and provide a combined virtual try-on image and this process is named as virtual try-on. Our solution will enable user's to gather various fashion trends as suggestion from different e-Commerce and onlinne shopping websites/applications and importantly that suits them and  of their own interest.

## IBM Chatbot (Watson Assistant)
Chatbots are applications that maintains a stable communication with users through which it obtains certains inputs and get the work done by using them. Chatbot helps in reducing the time involved in a process but get the work done. It follows a workflow rather than maintaining a linear sequence to complete a work. IBM provides a chatbot service named "Watson Assiatant" through which we can create chatbots for our business of our own interest. The dialogues provided by the user are called "Intents" and the keywords through which the chatbot detects the intents are called "Entities". The conversation that happens between user and the chatbot is consider to be "Dialogues". We need to create those dialogue nodes that respond for each user intents by detecting entities. We have configured the chatbot to gather various parameters as inputs and based on that certains fashion suggestions along with it's navigation link to appropriate e-Commerce website. The following block diagram depicts the working flow of IBM Watson Assistant:

![Chabot_Flow](https://user-images.githubusercontent.com/58814795/131342586-eb486379-6325-410b-b40d-3f79a692387f.JPG)

## CNN Classfication Model
The Convolutional Neural Network model is used to detect the class of the image that user sends in as input. We have created a custom dataset by collecting various images of different classes so that it can be trained to detect the appropriate class. The custom dataset is classified and it is seperated accordingly based on the class name that we have made. The dataset is the splitted ino "train" and "test" datasets and is made to train. The trained model is of about 80% accuracy and is made to test with the set of images so that the model prediction rate can be checked. We have configured a function to provide a set of fashion suggestions from a specific folder that contains various images for the purpose of displaying it to the user and providing more insights on fashion products which are related to predicted fashion class. Finally, the set of fashion suggestions are displayed to the user as per the image which he uploaded for classification. We have also used to the chatbot so that the predicted class is given as intent to the chatbot and the set of responses will be displayed in the website section. The following block diagram depicts the workflow of CNN classification model:

![CNN Model Image](https://user-images.githubusercontent.com/58814795/131344201-29bd1c82-6d71-4391-9b8b-196fcabe14b2.JPG)

## Virtual Try-on
The Virtual try-on model provides an realistic virtual try-on experience for users. This model is created by geometric measurement model gmm and try on module. The Virtual Try on Dataset consists of train and test folders with cloth images, warped images , mask images in both train and test folders with train and test pairs of images. The model is trained on gmm and tom and final checkpoints are downloaded for testing the model’s prediction. In order to test this in website, the system builds an flask application to implement this virtual try-on feature. Create an html template for displaying cloth images and to upload user image and cloth image. Create css and js scripts to get the output from python script and display them in website. Put html file in templates folder and js, css files in static folder. Create Checkpoints folder and store the pretrained checkpoints. Install the dependency packages required to run this flask application. Create python script app.py to load the checkpints and to perform virtual try-on network on user image and cloth image and to produce the realistic virtual try-on image. Deploy the flask application on localhost using anaconda prompt. This virtual try-on feature provides insights to users’ whether to select particular product or not. They can also upload their individual cloth image and can find out whether the product matches them or not. When the flask application is deployed, the user visits fashion website and when they select virtual try-on, they are navigated to virtual try-on page. They upload their image and either can choose cloth image from cloth list or they can upload personal cloth image to check the virtual try-on result.


![VTON_FLOW](https://user-images.githubusercontent.com/60148115/131562485-2a0b0e62-c910-45de-95f3-c1df665f99e6.JPG)



## Flask App for Suggesting Fashion Trends
Flask is an python package that is used to create web applications of our own wish with the help of HTML, CSS, and JS. We have used Flask package to create a website that provides fashion suggestion to the user by obtaining user image as input. The user image is provided to the CNN classfication model and it gives the class name as the output. With the help of the class name that is obtained, we planned to provide a set of fashion suggestions from the images that we possess. Here, the class name is also provided as input (intents) to the chatbot and the set of response is displayed in a presentable way to the user in the same website. We also created a home page using HTML, CSS, JS, Bootstrap to help the user to navigate and to provide tips for them. We also added the Chatbot that we created to the Home page of the website. The folowing block diagram depicts the workflow of Flask App for suggesting fashion trends:

![Flask_APP_FLOW](https://user-images.githubusercontent.com/58814795/131345489-a3c91732-ec77-44ae-97b6-90a59dcb995e.JPG)

## Deploying the CNN Model on IBM Cloud 
After building the CNN Model, the model has to be deployed in an deployment space. To deploy the model, the proposed system uses IBM Cloud service and IBM Machine learning service. After saving the model, the machine learning service credentials are obtained by creating a new api key. Then launch watson studio and navigate to deployments and create a new space. Once new space is created, navigate to notebook and initialize the tar file to be downloaded with the model. After initializing, get space id and model id of the user space. Download the model with tensorflow version-1.5.0py3.6. Get the model id. Save the model to the newly created space. Once saved, the model appears in the assests tab of that space. Open localhost and type jupyter notebook, initialize the same machine learning credentials and get the user space id and initialize the tar file to be downloaded with tensorflow version 1.15py3.6. Get the model_id and download the tar file. Extract the model to downloads and then the model can be used in local system.


![Deploy Model on IBM Cloud Flow](https://user-images.githubusercontent.com/60148115/131564619-5ea60bc3-f04c-4b3e-8ce7-8af111a8b57e.JPG)


## Overall Application
The overall application acts as an complete package that provides various fashion suggestions from different platforms and e-Commerce applications. The main point is, it matches the user's interest and will best suit them and allows them to try out the costumes that they like before purchasing.  The folowing block diagram depicts the workflow of the entire application:

![Block_DIag_flow](https://user-images.githubusercontent.com/58814795/131356728-a48103be-1b26-4193-8fe0-c1fc1e3e3ca3.JPG)


**Requirements for this project:**

->Anaconda prompt

->tensorflow==1.13.1

->torch==1.2.0

->torchvision==0.2.0

->Google colab

->Checkpoints folder

->keras==2.2.4

->Jupyter Notebook


In the Notebooks folder, there are 5 notebook files 

**Fashion_Redefined_CNN_Model_Train_Notebook (1).ipynb**  - is used for building CNN Model

**Testing CNN Model Notebook.ipynb**  - is used for tesing the cnn model

**Deploying CNN Model to IBM CLOUD NOTEBOOK.ipynb**  -  is used for deploying cnn model to ibm cloud

**IBM NOTEBOOK.ipynb** - is used for downloading the deployed model

**Virtual Try-On Notebook.ipynb** - is used for performing virtual try on using flask 


**UI Screenshots** 

![Fashion Redefined Home Page](https://user-images.githubusercontent.com/60148115/131563584-74ef3dcc-ba27-4ebe-a6bc-fbcb95b3a951.JPG)


![Recommendation Links](https://user-images.githubusercontent.com/60148115/131563612-e536479e-ec99-435b-b46c-b144f0dc87fc.JPG)



![Try-on Result](https://user-images.githubusercontent.com/60148115/131563640-470a6dde-9191-48b5-8725-9538ab299532.JPG)


**ADVANTAGES AND DISADVANTAGES:**

 It enables users to find costume based on their interest that also best suits their looks. 

 It allows users to check how the costumes of their wish which fits them by using Virtual Try-on feature. 

 It provides various set of matching fashion suggestions from different e-Commerce websites / applications along with their shopping links to purchase them. 

 Chatbot’s suggestions also contain shopping links that will be useful for users to purchase their fashion products. 

 It provides a complete fashion based try-on fetaures for individuals who aren’t aware of fashion trends and also for fashion geeks. 


**Disadvantages:** 

 The model’s prediction rate is an critical factor 

 Need large dataset for training the model





**GOOGLE DRIVE LINK FOR CHECKPOINTS :** https://drive.google.com/drive/folders/1f4pkV9mRzmUL9g3iSRFl9foQQhMAPOSj?usp=sharing

**YOUTUBE DEMO LINK :** https://youtu.be/y0-iC4UvjZs
