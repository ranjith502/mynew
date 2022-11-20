import streamlit as st
import os
from bing_image_downloader import downloader
import time

path=os.path.join(os.getcwd(),'dataset')

text_input=st.text_input('enter the dataset name to download eg cats,dogs','')
number = int(st.number_input('Insert a number'))
st.write('The current number is ', number)

downloader.download(text_input,limit=number,  output_dir='dataset', adult_filter_off=True, force_replace=False, timeout=60, verbose=True)


if len(os.path.join(os.getcwd(),'dataset',text_input)) >= 5:
    st.write('Download')
    


# st.text('data is loading ......')
# my_bar = st.progress(0)

# for percent_complete in range(100):
#     my_bar.progress(percent_complete + 1)
    

    
# if len(os.path.join(os.getcwd(),'dataset',text_input)) > 5:
#     st.write('apple')




# for file in os.listdir(path):
#       # print(file)
#   # print(os.path.join(path,file))
#   remove_path=os.path.join(path,file)
#   if os.path.isfile(remove_path)==True:
#     os.remove(remove_path)
#     print(remove_path)




