# SBSPS-Challenge-5297-Fashion-Redefined-with-Virtual-Grooming-Shopping-Assistant

<h1 align="center">
    Fashion Redefined with Virtual Grooming Shopping Assistant
</h1>

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
Fashion trends are considered to be one of the most important aspect of everyone's life today. Many people finds it hard to get appropriate costumes as per their own interest that also suits their look. Our solution is to provide fashion suggestions for users based on their look and appearance and they can select from the list of suggestions provided. We are using CNN classification model that analyze the user's image and provide a set of suggestions based on the class that the model detected. We have also used IBM's chatbot service (Watson Assistant) which helps in providing suggestions by gathering basic inputs as parameters. We have also incorporated a special model that gets user image as input along with the cloth image of user's own interest and provide a wraped image and this process is named as virtual try-on. Our solution will enable user's to gather various fashion trends as suggestion from different e-Commerce and onlinne shopping websites/applications and importantly that suits them and  of their own interest.

## IBM Chatbot (Watson Assiatant)
Chatbots are applications that maintains a stable communication with users through which it obtains certains inputs and get the work done by using them. Chatbot helps in reducing the time involved in a process but get the work done. It follows a workflow rather than maintaining a linear sequence to complete a work. IBM provides a chatbot service named "Watson Assiatant" through which we can create chatbots for our business of our own interest. The dialogues provided by the user are called "Intents" and the keywords through which the chatbot detects the intents are called "Entities". The conversation that happens between user and the chatbot is consider to be "Dialogues". We need to create those dialogue nodes that respond for each user intents by detecting entities. We have configured the chatbot to gather various parameters as inputs and based on that certains fashion suggestions along with it's navigation link to appropriate e-Commerce website. The following block diagram depicts the working flow of IBM Watson Assistant:

![Chabot_Flow](https://user-images.githubusercontent.com/58814795/131342586-eb486379-6325-410b-b40d-3f79a692387f.JPG)

## CNN Classfication Model
The Convolutional Neural Network model is used to detect the class of the image that user sends in as input. We have created a custom dataset by collecting various images of different classes so that it can be trained to detect the appropriate class. The custom dataset is classified and it is seperated accordingly based on the class name that we have made. The dataset is the splitted ino "train" and "test" datasets and is made to train. The trained model is of about 88.9% accuracy and is made to test with the set of images so that the model prediction rate can be checked. We have configured a function to provide a set of fashion suggestions from a specific folder that contains various images for the pupose of displaying it to the user. Finally, the set of fashion suggestion is displayed to the user as per the image which he uploaded for classification. We have also used to the chatbot so that the predicted class is given as intent to the chatbot and the set of responses will be displayed in the website section. The folowing block diagram depicts the workflow of CNN classification model:

![CNN Model Image](https://user-images.githubusercontent.com/58814795/131344201-29bd1c82-6d71-4391-9b8b-196fcabe14b2.JPG)

## Virtual Try-on
The Virtual Try-on


## Flask App for Suggesting Fashion Trends
Flask is an python package that is used to create web applications of our own wish with the help of HTML, CSS, and JS. We have used Flask package to create a website that provides fashion suggestion to the user by obtaining user image as input. The user image is provided to the CNN classfication model and it gives the class name as the output. With the help of the class name that is obtained, we planned to provide a set of fashion suggestions from the images that we possess. Here, the class name is also provided as input (intents) to the chatbot and the set of response is displayed in a presentable way to the user in the same website. We also created a home page using HTML, CSS, JS, Bootstrap to help the user to navigate and to provide tips for them. We also added the Chatbot that we created to the Home page of the website. The folowing block diagram depicts the workflow of Flask App for suggesting fashion trends:

![Flask_APP_FLOW](https://user-images.githubusercontent.com/58814795/131345489-a3c91732-ec77-44ae-97b6-90a59dcb995e.JPG)

## Flask App for Virtual Try-on
Flask App for Virtual Try-on


## Overall Application
The overall application acts as an complete package that provides various fashion suggestions from different platforms and e-Commerce applications. The main point is, it matches the user's interest and will best suit them and allows them to try out the costumes that they like before purchasing.  The folowing block diagram depicts the workflow of the entire application:

![Block_DIag_flow](https://user-images.githubusercontent.com/58814795/131356728-a48103be-1b26-4193-8fe0-c1fc1e3e3ca3.JPG)
