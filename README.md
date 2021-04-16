# Dog Breed Classifier
This model uses ResNet50 as a pretrained model to classify dog images into their breeds.

The model can now classify dog images for 120 different breeds.

## Dataset

The dataset can be found [here](https://www.kaggle.com/c/dog-breed-identification/data).

## API

Send a post request to 143.110.177.46:8000 (domain: dbc.my.to, port: 8000). <br>
`curl -i -X POST -H "Content-Type: multipart/form-data" -F "image=@path_to_the_image_file" http://dbc.my.to:8000/api`

or look at [test.py](test.py) for python example.

API hosted at
<a href="https://www.digitalocean.com" target="_blank"> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/DigitalOcean_logo.svg/1024px-DigitalOcean_logo.svg.png" alt="DigitalOcean" width="40" height="40"/> </a> </p>

## Website

Website can be found at [classifythatdog.netlify.app](https://classifythatdog.netlify.app)

Developed my @bhanuprakashj [dog-breed-classifier-UI](https://github.com/bhanuprakashj/dog-breed-classifier-UI)



