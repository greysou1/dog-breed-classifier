# Dog Breed Classifier
This model uses ResNet50 as a pretrained model to classify dog images into their breeds.

Currently this model only classifies the dog images into the following 10 breeds. 

 - Beagle
 - Chihuahua
 - Doberman
 - French_Bulldog
 - Golden_Retriever
 - Malamute
 - Pug
 - Saint Bernard
 - Scottish Deerhound
 - Tibetan Mastiff

The model currently has a train accuracy of 98%


## Dataset

The dataset can be found [here](https://www.kaggle.com/c/dog-breed-identification/data).

## API

Send a post request to 143.110.177.46:8000 (domain: dbc.my.to, port: 8000)
`curl -r POST -d '{"image":<base64 encoded image>}' http://dbc.my.to:8000`

or look at [test.py](test.py) for python example.