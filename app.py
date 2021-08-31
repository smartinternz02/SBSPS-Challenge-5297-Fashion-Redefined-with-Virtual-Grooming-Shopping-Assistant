import numpy as np
import os
import random
import json
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory
from tensorflow.keras.preprocessing import image
from PIL import Image
import cv2
import base64
from datetime import datetime
from Model import Model
from io import StringIO, BytesIO
from tensorflow.keras.models import load_model
from flask import Flask , request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import time
#from flask_ngrok import run_with_ngrok

app = Flask(__name__)
#run_with_ngrok(app)


model = load_model("IBM_Fashion_Prediction_Model.h5")

UPLOAD_FOLDER = 'static/uploads/'
global filepath
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

authenticator = IAMAuthenticator('R8mM6G5I5MZFow1V2LOMWcUsE0PsgyQzZhuJqT7fmsZG')
assistant = AssistantV2(
    version='2021-06-14',
    authenticator = authenticator
)

assistant.set_service_url('https://api.eu-gb.assistant.watson.cloud.ibm.com')
response = assistant.create_session(
    assistant_id='f7f44aae-54ba-48c8-b400-58bd612f5f75'
).get_result()
session_id = response
session_id = session_id["session_id"]

time.sleep(2.4)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/fashion_suits_me/")
def fashion_suits_me():
    return render_template('fashion.html')

@app.route('/', methods=['POST'])
def upload_image():
    file = request.files['file']
    basepath = os.path.dirname(__file__)
    print("current path", basepath)
    filepath = os.path.join(basepath,'uploads',file.filename)
    print("upload folder is ", filepath)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    print(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    print(filepath)
    img = image.load_img(filepath,target_size = (64,64))
    x = image.img_to_array(img)
    print(x)
    x = np.expand_dims(x,axis =0)
    print(x)
    preds = model.predict_classes(x)
    print("prediction",preds)
    index1= ['Female Kurti', 'Female Legin', 'Female Patiala Pant', 'Female Salvar',
             'Male Casual Pant', 'Male Checked Casual Shirt',
             'Male Checked Formal Shirt', 'Male Formals Pant',
             'Male Formals Shirt', 'Male Plain Casual Shirt', 'Male Plain T-Shirt',
             'Male Striped Casual Shirt', 'Male Striped Formal Shirt',
             'Male Striped T-Shirt']
    index = ['Bag', 'Bangle', 'Belt', 'Bracelet',
             'Cap', 'Casual Shoes', 'Cooling Glass',
             'Earrings', 'Female Ballerina Flat Sandal',
             'Female Casual Pant', 'Female Checked Casual Shirt',
             'Female Club Wear Top', 'Female Collar T-Shirt',
             'Female Fashion Layered Top', 'Female Flat Sandal',
             'Female Formal Pant', 'Female Formal Shirt',
             'Female Gathering Pant', 'Female Gladiator Sandal',
             'Female Graphic T-Shirt', 'Female Heels', 'Female Jean Pant',
             'Female Jerkin', 'Female Kurti', 'Female Legin',
             'Female Patiala Pant', 'Female Round-Neck T-Shirt',
             'Female Salvar', 'Female Sarees', 'Female Short Sleeve Top',
             'Female Shorts', 'Female Skirts', 'Female Sleeve Top',
             'Female Sleeveless Top', 'Female Sportswear T-shirt',
             'Female Strap Sandal', 'Female Strip Top', 'Female Tank Top',
             'Female Tracksuit Pants', 'Female Tube Top', 'Female V-Neck T-Shirt',
             'Formal Shoes', 'Handbag', 'Male Belt Sandal', 'Male Casual Pant',
             'Male Checked Casual Shirt', 'Male Checked Formal Shirt',
             'Male Collar T-Shirt', 'Male Flat Sandal',
             'Male Formal Pant', 'Male Formals Shirt', 'Male Graphic T-Shirt',
             'Male Jean Pant', 'Male Jerkin', 'Male Kurta',
             'Male Plain Casual Shirt', 'Male Plain T-Shirt',
             'Male Round-Neck T-Shirt', 'Male Shorts',
             'Male Sportswear T-Shirt', 'Male Strap Sandal',
             'Male Striped Casual Shirt', 'Male Striped Formal Shirt',
             'Male Striped T-Shirt', 'Male Tracksuit Pant', 'Male V-Neck T-Shirt',
             'Male West Coat', 'Necklace', 'Purse', 'Ring', 'Socks',
             'Sports Shoes', 'Stole', 'Tie', 'Wallet', 'Watch']
    class_name = str(index1[preds[0]])
    if(class_name == "Female Kurti"):
        li = ['Female Kurti', 'Female Legin', 'Female Sleeve Top', 'Earrings', 'Female Flat Sandal']
        img = []
        for folder in li:
            path = "C:/Users/sushanth/Desktop/New Flask/static/Display_Images/"  + folder
            for i in range(0,2):
                random_filename = random.choice([x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))])
                img.append(folder + "/" + random_filename)
            print(img)
    if(class_name == "Female Legin"):
        li = ['Female Legin', 'Female Sleeve Top', 'Female Kurti', 'Female Salvar', 'Female Gladiator Sandal']
        img = []
        for folder in li:
            path = "C:/Users/sushanth/Desktop/New Flask/static/Display_Images/"  + folder
            for i in range(0,2):
                random_filename = random.choice([x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))])
                img.append(folder + "/" + random_filename)
            print(img)
    if(class_name == "Female Patiala Pant"):
        li = ['Female Patiala Pant', 'Female Sleeve Top', 'Female Kurti', 'Female Salvar', 'Female Flat Sandal']
        img = []
        for folder in li:
            path = "C:/Users/sushanth/Desktop/New Flask/static/Display_Images/"  + folder
            for i in range(0,2):
                random_filename = random.choice([x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))])
                img.append(folder + "/" + random_filename)
            print(img)
    if(class_name == "Female Salvar"):
        li = ['Female Salvar', 'Female Patiala Pant', 'Female Sleeve Top', 'Earrings', 'Female Gladiator Sandal']
        img = []
        for folder in li:
            path = "C:/Users/sushanth/Desktop/New Flask/static/Display_Images/"  + folder
            for i in range(0,2):
                random_filename = random.choice([x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))])
                img.append(folder + "/" + random_filename)
            print(img)
    if(class_name == "Male Casual Pant"):
        li = ['Male Casual Pant', 'Male Formals Shirt', 'Male Striped Casual Shirt', 'Male Striped Formal Shirt', 'Casual Shoes']
        img = []
        for folder in li:
            path = "C:/Users/sushanth/Desktop/New Flask/static/Display_Images/"  + folder
            for i in range(0,2):
                random_filename = random.choice([x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))])
                img.append(folder + "/" + random_filename)
            print(img)
    if(class_name == "Male Checked Casual Shirt"):
        li = ['Male Checked Casual Shirt', 'Male Casual Pant', 'Male Jean Pant', 'Watch', 'Casual Shoes']
        img = []
        for folder in li:
            path = "C:/Users/sushanth/Desktop/New Flask/static/Display_Images/"  + folder
            for i in range(0,2):
                random_filename = random.choice([x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))])
                img.append(folder + "/" + random_filename)
            print(img)
    if(class_name == "Male Checked Formal Shirt"):
        li = ['Male Checked Formal Shirt', 'Male Formal Pant', 'Tie', 'Belt', 'Formal Shoes']
        img = []
        for folder in li:
            path = "C:/Users/sushanth/Desktop/New Flask/static/Display_Images/"  + folder
            for i in range(0,2):
                random_filename = random.choice([x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))])
                img.append(folder + "/" + random_filename)
                print(img)
    if(class_name == "Male Formals Pant"):
        li = ['Male Formal Pant', 'Male Formals Shirt', 'Male Striped Formal Shirt', 'Belt', 'Formal Shoes']
        img = []
        for folder in li:
            path = "C:/Users/sushanth/Desktop/New Flask/static/Display_Images"  + folder
            for i in range(0,2):
                random_filename = random.choice([x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))])
                img.append(folder + "/" + random_filename)
            print(img)
    if(class_name == "Male Formals Shirt"):
        li = ['Male Formals Shirt', 'Male Formal Pant', 'Tie', 'Belt', 'Formal Shoes']
        img = []
        for folder in li:
            path = "C:/Users/sushanth/Desktop/New Flask/static/Display_Images/"  + folder
            for i in range(0,2):
                random_filename = random.choice([x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))])
                img.append(folder + "/" + random_filename)
            print(img)
    if(class_name == "Male Plain Casual Shirt"):
        li = ['Male Plain Casual Shirt', 'Male Casual Pant', 'Male Jean Pant', 'Watch', 'Casual Shoes']
        img = []
        for folder in li:
            path = "C:/Users/sushanth/Desktop/New Flask/static/Display_Images/"  + folder
            for i in range(0,2):
                random_filename = random.choice([x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))])
                img.append(folder + "/" + random_filename)
            print(img)
    if(class_name == "Male Plain T-Shirt"):
        li = ['Male Plain T-Shirt', 'Male Jean Pant', 'Cooling Glass', 'Male Belt Sandal', 'Casual Shoes']
        img = []
        for folder in li:
            path = "C:/Users/sushanth/Desktop/New Flask/static/Display_Images/"  + folder
            for i in range(0,2):
                random_filename = random.choice([x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))])
                img.append(folder + "/" + random_filename)
            print(img)
    if(class_name == "Male Striped Casual Shirt"):
        li = ['Male Striped Casual Shirt', 'Male Casual Pant', 'Male Jean Pant', 'Watch', 'Casual Shoes']
        img = []
        for folder in li:
            path = "C:/Users/sushanth/Desktop/New Flask/static/Display_Images/"  + folder
            for i in range(0,2):
                random_filename = random.choice([x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))])
                img.append(folder + "/" + random_filename)
            print(img)
    if(class_name == "Male Striped Formal Shirt"):
        li = ['Male Striped Formal Shirt', 'Male Formal Pant', 'Tie', 'Belt', 'Formal Shoes']
        img = []
        for folder in li:
            path = "C:/Users/sushanth/Desktop/New Flask/static/Display_Images/"  + folder
            for i in range(0,2):
                random_filename = random.choice([x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))])
                img.append(folder + "/" + random_filename)
            print(img)
    if(class_name == "Male Striped T-Shirt"):
        li = ['Male Striped T-Shirt', 'Male Jean Pant', 'Cooling Glass', 'Male Belt Sandal', 'Casual Shoes']
        img = []
        for folder in li:
            path = "C:/Users/sushanth/Desktop/New Flask/static/Display_Images/"  + folder
            for i in range(0,2):
                random_filename = random.choice([x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))])
                img.append(folder + "/" + random_filename)
            print(img)
    links=[]
    links1=[]
    l=class_name
    #input_text = input(l)
    response = assistant.message(assistant_id='f7f44aae-54ba-48c8-b400-58bd612f5f75',session_id=session_id,input={'message_type' : 'text','text' : class_name}).get_result()
    response_type = response["output"]["generic"][0]['response_type']
    if(response_type == "text" or response_type=="image"):
        links.append("<img src='"+response["output"]["generic"][0]["source"]+"'\>") #+ (response["output"]["generic"][1]["text"]))
        links1.append(response["output"]["generic"][1]["text"])
        links.append("<img src='"+response["output"]["generic"][2]["source"]+"'\>") #+   (response["output"]["generic"][3]["text"]))
        links1.append(response["output"]["generic"][3]["text"])
        #response = assistant.delete_session(assistant_id='f7f44aae-54ba-48c8-b400-58bd612f5f75',session_id=session_id).get_result()
        #return render_template('index.html', linkslist=links)
        print(links)
        print(links1)
    return render_template('fashion.html', filename = file.filename, imagelist = img, linkslist=links, linkslist1=links1)	


if __name__ == "__main__":
    app.run()
