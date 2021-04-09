# Dog Breed Classifier
This model uses ResNet50 as a pretrained model to classify dog images into their breeds.

The model can now classify dog images for 120 different breeds.

## Dataset

The dataset can be found [here](https://www.kaggle.com/c/dog-breed-identification/data).

## API

Send a post request to 143.110.177.46:8000 (domain: dbc.my.to, port: 8000).

`curl -r POST -d '{"image":path_to_the_image_file}' http://dbc.my.to:8000/api`

or look at [test.py](test.py) for python example.
