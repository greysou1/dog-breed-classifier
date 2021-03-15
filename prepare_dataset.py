# This script sorts the images (test/train) into corresponding labeled folders
import pandas as pd
import os, shutil

df = pd.read_csv (r'labels.csv')
ids = df['id']
breeds = df['breed']
labels_dic = {}

# create a labels dictionary
for i, id in enumerate(ids):
    labels_dic[id] = breeds[i]

# create folders with label names
labels = ['beagle', 'chihuahua', 'doberman', 'french_bulldog', 'golden_retriever', 'malamute', 'pug', 'saint_bernard', 'scottish_deerhound', 'tibetan_mastiff'] #set(labels_dic.values()) 


for label in labels:
    try:
        os.mkdir('train/train/'+label)
        os.mkdir('test/test/'+label)
    except OSError as error:  
        print(error) 

# for f in os.listdir('train'):
#         id, ext = os.path.splitext(f)
#         if ext == '.jpg':
#             path = '/Users/prudvikamtam/Projects/dog-breed-identification/dog-breed-identification/train/'
#             train_source = path+id+'.jpg'
#             train_destination = path+'train/'+labels_dic[id]+'/'+id+ '.jpg'
#             try:
#                 shutil.move(train_source, train_destination)
#             except:
#                 continue

for id in labels_dic.keys():
    if labels_dic[id] in labels:
        path = '/Users/prudvikamtam/Projects/dog-breed-identification/dog-breed-identification/train/'
        train_source = path+id+'.jpg'
        train_destination = path+'train/'+labels_dic[id]+'/'+id+ '.jpg'
        try:
            shutil.move(train_source, train_destination)
        except:
            continue

# for f in os.listdir('test'):
#         id, ext = os.path.splitext(f)
#         if ext == '.jpg':
#             path = '/Users/prudvikamtam/Projects/dog-breed-identification/dog-breed-identification/test/'
#             test_source = path+id+'.jpg'
#             test_destination = path+labels_dic[id]+'/'+id+ '.jpg'
#             try:
#                 shutil.move(train_source, train_destination)
#             except:
#                 continue
