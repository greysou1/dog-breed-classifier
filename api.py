# import the necessary packages
import keras
from keras.applications import ResNet50
from keras.preprocessing.image import img_to_array
from keras.applications import imagenet_utils
from keras.models import load_model
from PIL import Image
import numpy as np
import flask
import io

# initialize our Flask application and the Keras model
app = flask.Flask(__name__)
model = None
image_resize = 224

def load_model():
    # load the pre-trained Keras model (here we are using a model
    # pre-trained on ImageNet and provided by Keras, but you can
    # substitute in your own networks just as easily)	
    global model
    print('Importing Model')
    model = keras.models.load_model('dog_breed_classifier_resnet_model.h5')
    if model != None: print('Model successfully imported')

def prepare_image(image, target=image_resize):
    # if the image mode is not RGB, convert it
    if image.mode != "RGB":
        image = image.convert("RGB")

    # resize the input image and preprocess it
    image = image.resize(target)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = imagenet_utils.preprocess_input(image)

    # return the processed image
    return image

@app.route("/", methods=["POST"])
def predict():
    # initialize the data dictionary that will be returned from the
    # view
    # data = {"success": False}

    # ensure an image was properly uploaded to our endpoint
    if flask.request.method == "POST":
        if flask.request.files.get("image"):
            # read the image in PIL format
            image = flask.request.files["image"].read()
            image = Image.open(io.BytesIO(image))

            # preprocess the image and prepare it for classification
            image = prepare_image(image, target=(224, 224))
            
            # Labels list to classify the images into
            labels = ['beagle', 'chihuahua', 'doberman', 'french_bulldog', 'golden_retriever', 'malamute', 'pug', 'saint_bernard', 'scottish_deerhound', 'tibetan_mastiff']
            
            # classify the input image and then initialize the list
            # of predictions to return to the client
            preds = model.predict(image) 
            prob = np.max(preds)
            label = labels[np.argmax(preds)]

            # add label and it's probablity to return dic
            output = {"breed": str(label), "score": str(prob)}

            # indicate that the request was a success
            # data["success"] = True

    # return the data dictionary as a JSON response
    return flask.jsonify(output)

    # if this is the main thread of execution first load the model and
# then start the server


if __name__ == "__main__":
    load_model()
    app.run(host="0.0.0.0", port=8000, debug=False)