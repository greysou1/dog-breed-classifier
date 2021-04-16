# import the necessary packages
from flask.globals import request
import keras
import pandas as pd
from keras.applications import ResNet50
from keras.preprocessing.image import img_to_array
from keras.applications import imagenet_utils
from keras.models import load_model
from PIL import Image
import numpy as np
import flask
from flask import Flask, flash, redirect, render_template, request, session, make_response
from flask_cors import CORS, cross_origin
from OpenSSL import SSL
import io, json

# initialize our Flask application and the Keras model
app = Flask(__name__)
context = SSL.Context(SSL.PROTOCOL_TLSv1_2)
context.use_privatekey_file('/etc/letsencrypt/live/dbc.my.to/privkey.pem')
context.use_certificate_file('/etc/letsencrypt/live/dbc.my.to/fullchain.pem')
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
model = None
image_resize = 224

@app.before_first_request
def load_model():
    ''' 
    load the pre-trained model
    '''
    global model
    print('Importing Model')
    model = keras.models.load_model('dog_breed_classifier_resnet_model120.h5')
    if model != None: print('Model successfully imported')

def prepare_image(image, target=image_resize):
    '''
    prepare the input image to suit the input of the classifier model (RESNET-50)
    '''
    #if the image mode is not RGB, convert it
    if image.mode != "RGB":
        image = image.convert("RGB")

    # resize the input image and preprocess it
    image = image.resize(target)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = imagenet_utils.preprocess_input(image)

    # return the processed image
    return image

'''
@app.route("/", methods=["GET"])
def home():
    return render_template('home.html')

@app.route("/upload", methods=["POST"])
def upload():
    output = predict()
    output = output.json
    breed = output['breed']
    score = output['score']

    return render_template('prediction.html', breed=breed, score=score)
'''

@app.route("/api", methods=["POST"])
@cross_origin()
def predict():
    '''
    takes the input image from the POST request, pre-processes it and passes it to the trained model,
    the output of the model is then returned as a JSON object
    '''
    # ensure an image was properly uploaded to our endpoint
    if flask.request.method == "POST":
        # ensure the user has attached an image file with the POST request
        if flask.request.files.get("image"):
            #read the image in PIL format
            image = flask.request.files["image"].read()
            image = Image.open(io.BytesIO(image))
        else:
            return make_response('File not uploaded!'), 400

        # preprocess the image and prepare it for classification
        image = prepare_image(image, target=(224, 224))
        
        # labels list to classify the images into
        df = pd.read_csv (r'labels.csv')
        breeds = df['breed']
        labels = sorted(breeds.unique())
        
        # classify the input image and find it's label
        preds = model.predict(image) 
        prob = np.max(preds)
        label = labels[np.argmax(preds)]

        # add label and it's probablity to return dic
        output = {"breed": str(label), "score": str(prob)}
        print(output)

    # return the data dictionary as a JSON response
    return flask.jsonify(output)

if __name__ == "__main__":
    load_model()
    app.run(host="0.0.0.0", port=8000, debug=False, ssl_context=context)