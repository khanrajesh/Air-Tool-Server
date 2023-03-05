from flask import Flask,request, jsonify,render_template
import base64
from PIL import Image
from io import BytesIO
import sys
# import code.v5.odec as dec
  
# Insert the path of modules folder 


from  odecv5 import Odec
odec = Odec()

app = Flask(__name__)



@app.route('/')
def hello_world():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>
    <video id="video" width="640" height="480" autoplay></video>
    <button id="snap">Snap Photo</button>
    <canvas id="canvas" width="640" height="480"></canvas>
    </body>
    <script>

    var video = document.getElementById('video');
    if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({ video: true }).then(function(stream) {
            //video.src = window.URL.createObjectURL(stream);
            video.srcObject = stream;
            video.play();
        });
    }

    var canvas = document.getElementById('canvas');
    var context = canvas.getContext('2d');
    var video = document.getElementById('video');

    // Trigger photo take
    document.getElementById("snap").addEventListener("click", function() {
        context.drawImage(video, 0, 0, 640, 480);
    var request = new XMLHttpRequest();
    request.open('POST', '/submit?image=' + video.toString('base64'), true);
    request.send();
    });



</script>
</html>
    """

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
    f = request.files['url']
    f.save('./static/detect/uploaded.jpeg')
    missing = odec.detect_by_image('static/detect/uploaded.jpeg')
    return missing

if __name__=='__main__':
    app.run(debug=True,port=8080, )
    