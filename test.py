
from PIL import Image
import numpy as np 
import streamlit as st
import tensorflow as tf

# Function to Read and Manupilate Images

# number = st.number_input('Insert a number')
# st.write('starting to perform classification on',number,'classes')

# string_value=st.text_input('enter name to download dataset','')
# from bing_image_downloader import downloader
# downloader.download(string_value, limit=10,  output_dir='testing', adult_filter_off=True, force_replace=False, timeout=60, verbose=True)

# import time

# my_bar = st.progress(0)

# for percent_complete in range(len('/content/testing/bike')):
#     my_bar.progress(percent_complete + 1)



# Uploading the File to the Page
uploadFile = st.file_uploader(label="Upload image", type=['jpg', 'png'])

# Checking the Format of the page
if uploadFile is not None:
    # Perform your Manupilations (In my Case applying Filters)
    im = Image.open(uploadFile)
    new_im=im.resize((224,224))
    image = np.array(new_im)
    st.image(image)
    resize = tf.image.resize(image, (224,224))
    mymodel = tf.keras.models.load_model('model.h5')
    yhat = mymodel.predict(np.expand_dims(resize/255, 0))
    if yhat > 0.5: 
        st.write(f'Predicted class is dog')
    else:
        st.write(f'Predicted class is cat')
    # st.write("Image Uploaded Successfully")
else:
    st.write("Make sure you image is in JPG/PNG Format.")