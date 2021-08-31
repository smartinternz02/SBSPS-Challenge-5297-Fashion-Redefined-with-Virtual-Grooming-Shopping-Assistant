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
from flask_ngrok import run_with_ngrok
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

app = Flask(__name__)
run_with_ngrok(app)


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

def readb64(base64_string):
    sbuf = BytesIO()
    sbuf.write(base64.b64decode(base64_string))
    res = Image.open(sbuf)
    return np.array(res)


def writeb64(img):
    img_str = cv2.imencode('.bmp', img)[1]
    imagebase64 = base64.b64encode(img_str)
    imagebase64 = bytes.decode(imagebase64)
    return imagebase64

os.environ["CUDA_VISIBLE_DEVICES"] = "0"

# init for all global variables

modelnew = Model("checkpoints/jpp.pb",
              "checkpoints/gmm.pth",
              "checkpoints/tom.pth",
              use_cuda=True)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# cloth list for web server
cloth_list_raw = os.listdir(os.path.join(BASE_DIR, "static", "img"))
cloth_list = []
counter = 0
for cloth in cloth_list_raw:
    if 'jpg' in cloth:
        cloth_list.append([os.path.join("static", "img1", cloth), counter])
        counter += 1


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
    class_name = str(index1[preds[0]])
    if(class_name == "Female Kurti"):
        li = ['Female Kurti', 'Female Legin', 'Female Sleeve Top', 'Earrings', 'Female Flat Sandal']
        img = []
        for folder in li:
            path = "static/Display_Images/"  + folder
            for i in range(0,2):
                random_filename = random.choice([x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))])
                img.append(folder + "/" + random_filename)
            print(img)
    if(class_name == "Female Legin"):
        li = ['Female Legin', 'Female Sleeve Top', 'Female Kurti', 'Female Salvar', 'Female Gladiator Sandal']
        img = []
        for folder in li:
            path = "static/Display_Images"  + folder
            for i in range(0,2):
                random_filename = random.choice([x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))])
                img.append(folder + "/" + random_filename)
            print(img)
    if(class_name == "Female Patiala Pant"):
        li = ['Female Patiala Pant', 'Female Sleeve Top', 'Female Kurti', 'Female Salvar', 'Female Flat Sandal']
        img = []
        for folder in li:
            path = "static/Display_Images"  + folder
            for i in range(0,2):
                random_filename = random.choice([x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))])
                img.append(folder + "/" + random_filename)
            print(img)
    if(class_name == "Female Salvar"):
        li = ['Female Salvar', 'Female Patiala Pant', 'Female Sleeve Top', 'Earrings', 'Female Gladiator Sandal']
        img = []
        for folder in li:
            path = "static/Display_Images"  + folder
            for i in range(0,2):
                random_filename = random.choice([x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))])
                img.append(folder + "/" + random_filename)
            print(img)
    if(class_name == "Male Casual Pant"):
        li = ['Male Casual Pant', 'Male Formals Shirt', 'Male Striped Casual Shirt', 'Male Striped Formal Shirt', 'Casual Shoes']
        img = []
        for folder in li:
            path = "static/Display_Images"  + folder
            for i in range(0,2):
                random_filename = random.choice([x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))])
                img.append(folder + "/" + random_filename)
            print(img)
    if(class_name == "Male Checked Casual Shirt"):
        li = ['Male Checked Casual Shirt', 'Male Casual Pant', 'Male Jean Pant', 'Watch', 'Casual Shoes']
        img = []
        for folder in li:
            path = "static/Display_Images"  + folder
            for i in range(0,2):
                random_filename = random.choice([x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))])
                img.append(folder + "/" + random_filename)
            print(img)
    if(class_name == "Male Checked Formal Shirt"):
        li = ['Male Checked Formal Shirt', 'Male Formal Pant', 'Tie', 'Belt', 'Formal Shoes']
        img = []
        for folder in li:
            path = "static/Display_Images"  + folder
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
            path = "static/Display_Images"  + folder
            for i in range(0,2):
                random_filename = random.choice([x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))])
                img.append(folder + "/" + random_filename)
            print(img)
    if(class_name == "Male Plain Casual Shirt"):
        li = ['Male Plain Casual Shirt', 'Male Casual Pant', 'Male Jean Pant', 'Watch', 'Casual Shoes']
        img = []
        for folder in li:
            path = "static/Display_Images"  + folder
            for i in range(0,2):
                random_filename = random.choice([x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))])
                img.append(folder + "/" + random_filename)
            print(img)
    if(class_name == "Male Plain T-Shirt"):
        li = ['Male Plain T-Shirt', 'Male Jean Pant', 'Cooling Glass', 'Male Belt Sandal', 'Casual Shoes']
        img = []
        for folder in li:
            path = "static/Display_Images"  + folder
            for i in range(0,2):
                random_filename = random.choice([x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))])
                img.append(folder + "/" + random_filename)
            print(img)
    if(class_name == "Male Striped Casual Shirt"):
        li = ['Male Striped Casual Shirt', 'Male Casual Pant', 'Male Jean Pant', 'Watch', 'Casual Shoes']
        img = []
        for folder in li:
            path = "static/Display_Images"  + folder
            for i in range(0,2):
                random_filename = random.choice([x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))])
                img.append(folder + "/" + random_filename)
            print(img)
    if(class_name == "Male Striped Formal Shirt"):
        li = ['Male Striped Formal Shirt', 'Male Formal Pant', 'Tie', 'Belt', 'Formal Shoes']
        img = []
        for folder in li:
            path = "static/Display_Images"  + folder
            for i in range(0,2):
                random_filename = random.choice([x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))])
                img.append(folder + "/" + random_filename)
            print(img)
    if(class_name == "Male Striped T-Shirt"):
        li = ['Male Striped T-Shirt', 'Male Jean Pant', 'Cooling Glass', 'Male Belt Sandal', 'Casual Shoes']
        img = []
        for folder in li:
            path = "static/Display_Images"  + folder
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

@app.route('/web')
def hello_world():
    return render_template('login.html', img_list=cloth_list)


@app.route('/upload', methods=['GET', 'POST'])
def upload_image():
    print(request.form)
    print(request.files)
    if (not len(request.files) == 2 or (len(request.form) == 1 and len(request.files) == 1)):
        return render_template('login.html', info="selection error", img_list=cloth_list)
    else:
        index = 0  # init
        cloth_image = None
        if len(request.form) == 1:
            index = int(request.form['optionsRadios'][6:])
        person_image = request.files['person_image']
        if len(request.files) == 2:
            cloth_image = request.files['cloth_image']

        start_time = time.time()
        o_name, h_name = run_model_web(
            person_image, cloth_list[index][0].split("\\")[-1], cloth_image)
        end_time = time.time()
        if o_name is None: # bad cloth image
            return 'I told you only clothes image with shape 256*192*3'
        else:
            return render_template('login.html', img_list=cloth_list, result1=h_name, result2=o_name, info="time: %.3f" % (end_time-start_time))


def run_model_web(f, cloth_name, cloth_f=None):
    '''
    为web服务进行预测。cloth_name和cloth_f中必有一个有内容，优先选择cloth_f，即用户上传的衣服图片
    prediction service. cloth_name and cloth_f cannot be both None. cloth_f is prior, which is from user upload.
    '''
    if cloth_f is None:
        print(f, cloth_name)
        c_img = np.array(Image.open(cloth_name))
    else:
        print(f, cloth_f)
        try:
            c_img = np.array(Image.open(cloth_f))
        except:
            c_img = np.array(Image.open(cloth_name))

    # 固化到本地的缓存文件夹，访问的时候作为静态资源被调用
    # local resource temp file would be used as static resource.
    temp_o_name = os.path.join("static", "result", "%d_%s" % (
        int(time.time()), cloth_name.split("/")[-1]))
    temp_h_name = os.path.join("static", "human", "%d_%s" % (
        int(time.time()), cloth_name.split("/")[-1]))

    if c_img.shape[0] != 256 or c_img.shape[1] != 192 or c_img.shape[2] != 3:
        return None, None

    img = Image.open(f)
    human_img = np.array(img)

    out, v = modelnew.predict(human_img, c_img, need_bright=False, keep_back=True)
    print("v:"+str(v))
    out = np.array(out, dtype='uint8')

    img.save(temp_h_name)
    Image.fromarray(out).save(temp_o_name, quality=95)  # 注意这个95
    return temp_o_name, temp_h_name


def getimg():
    data_str = request.data
    data_str = bytes.decode(data_str)
    data_str = data_str.replace('\n', '')
    data_json = json.loads(data_str)
    base64img_p = data_json['image_person']
    img_person = readb64(base64img_p)
    img_person = cv2.rotate(img_person, 2)
    img_person = cv2.flip(img_person, 1)
    base64img_c = data_json['image_cloth']
    img_cloth = readb64(base64img_c)
    return [img_person, img_cloth]


'''
json format example:
client:
    {
        'image_person':'...',
        'image_cloth':'...'
    }

server:
    {
        'status':'ok',
        'output_image':'...'
    }
'''
@app.route('/cloth', methods=['GET', 'POST'])
def Hello_cloth():
    '''
    响应客户端请求
    reponse requests from clients
    '''
    output_str = ""
    output_json = {}
    status = 'ok'
    if request.method == 'POST':
        # temp file would be writed to root dir
        input_person, input_cloth = getimg()
        cv2.imwrite('in.jpg', input_person)
        input_person = input_person[60:580, 45:435]
        cv2.imwrite('in_2.jpg', input_person)
        output_img, v = modelnew.predict(input_person, input_cloth, need_bright=True, keep_back=True, need_dilate=True)
        output_img = cv2.cvtColor(output_img, cv2.COLOR_RGB2BGR)
        cv2.imwrite('out.jpg', output_img)
        print("v:"+str(v))
        output_base64 = writeb64(output_img)
        if v < 0.1: # confidence is too weak to show
            status = 'failure'
        else:
            status = 'ok'
        output_json["status"] = status
        output_json["output_image"] = output_base64
        output_str = json.dumps(output_json)
        return output_str
    return "please use http client to request!"

if __name__ == "__main__":
    app.run()
