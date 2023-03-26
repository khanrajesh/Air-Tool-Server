from flask import Flask,request, jsonify,render_template
from flask_cors import CORS, cross_origin
import base64
from PIL import Image
from io import BytesIO
import sys
import  numpy as np
import cv2
from  odecv5 import Odec
# import code.v5.odec as dec

###########################logging part#################################
import logging

# Create a logger object
logger = logging.getLogger('my_app')

# Set the logging level
logger.setLevel(logging.INFO)

# Create a file handler and set the logging level
file_handler = logging.FileHandler('my_app.log')
file_handler.setLevel(logging.INFO)

# Create a formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)
###########################logging part#################################

  
# Insert the path of modules folder 

odec = Odec()
app = Flask(__name__, static_url_path='/static')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
# app = Flask(__name__)


@app.route('/')
def index():
    return render_template('tool.html')

# HtmlVideoElement
@app.route('/test',methods=['GET'])
def test():
    return "hello world!"

@app.route('/submit',methods=['POST'])
def submit():
    image = request.args.get('image')
    print(type(image))
    return ""

@app.route('/detectv5',methods=['POST'])
def detectv5():
    # logger.warning('reuest  : '+str(request))
    
    # # request.date
    data = request.get_json()       
   
    f = data['image'] 
    
    # logger.warning(f)
    encoded_data = f.split(",")[1]    
    base64_decoded = base64.b64decode(encoded_data)    
    image = Image.open(BytesIO(base64_decoded))    
    image =  np.array(image)

    # logger.warning('fff: '+f)

    # f = request.files['image']
    # # logger.warning('fff: '+f)

    # f.save('./static/detect/uploaded.jpeg')
    # missing = odec.detect_by_image(image)
    m_image, m_count = odec.detectByUploadImage(image)

    # Convert the ndarray to bytes
    image_bytes = cv2.imencode('.jpg', m_image)[1].tobytes()

# Convert binary image data to base64-encoded string
    base64_image = base64.b64encode(image_bytes).decode('utf-8')
    # logger.warning("data:image/jpeg;base64,"+base64_image)

    data = {
        'image': "data:image/jpeg;base64,"+base64_image,
        'count': m_count,
    }

    return data

if __name__=='__main__':
    app.run(debug=True,port=8080, )
    

def base64_to_img(base64_image):    
    encoded_data = base64_image.split(",")[1]    
    base64_decoded = base64.b64decode(encoded_data)    
    image = Image.open(BytesIO(base64_decoded))    
    return np.array(image)


#export FLASK_ENV=development
# set FLASK_ENV=development

# export FLASK_APP=app.py
# flask run --host=0.0.0.0
