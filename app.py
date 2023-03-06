from flask import Flask,request, jsonify,render_template
import base64
from PIL import Image
from io import BytesIO
import sys
import  numpy as np
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
from  odecv5 import Odec
odec = Odec()

app = Flask(__name__, static_url_path='/static')
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
    logger.warning('reuest  : '+str(request))
    
    # request.date
    data = request.get_json()
    logger.warning('data: '+data)
    # f = data['image']
    # logger.warning('fff: '+f)

    f = request.files['image']
    # logger.warning('fff: '+f)

    f.save('./static/detect/uploaded.jpeg')
    missing = odec.detect_by_image('static/detect/uploaded.jpeg')
    return "missing tool count: " + str(missing) + " missing" 
    # print('request: '+str(request))
    #  # Get the JSON data from the request
    # json_data = request.get_json()
    # print('json_data: '+ str(json_data))
    # # Get the image data from the JSON data
    # image_data = json_data['image']
    # print('image_data: '+ str(image_data))

   
    # logger.warning('request image : '+str(image_data))

    
    # # Decode the Base64 encoded image data
    # image_bytes = base64.b64decode(image_data.split(',')[1])
    # return ""
    # # Save the image data to a file
    # with open('image.jpg', 'wb') as f:
    #     f.write(image_bytes)
        
    # # Process the image and return the result
    # missing = odec.detect_by_image('image.jpg')
    # return "missing tool count: " + str(missing) + " missing"

if __name__=='__main__':
    app.run(debug=True,port=8080, )
    

def base64_to_img(base64_image):    
    encoded_data = base64_image.split(",")[1]    
    base64_decoded = base64.b64decode(encoded_data)    
    image = Image.open(BytesIO(base64_decoded))    
    return np.array(image)


#export FLASK_ENV=development
# set FLASK_ENV=development
