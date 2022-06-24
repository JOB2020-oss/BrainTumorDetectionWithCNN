import streamlit as st
from PIL import Image
import tensorflow
import base64
import numpy as np
import streamlit.components.v1 as cmp
from streamlit_option_menu import option_menu
import tensorflow.keras as keras

h1 = """
<div style='background-color:#F2F3F5;padding:10px;border-radius:5px;'>
<h1 style='text-align: center; color: Black;'>Brain Tumor Detection System</h1>
</div>
"""
h2 = """
<div style='background-color:#F2F3F5;padding:10px;border-radius:5px;'>
<h2 style='text-align: center; color: Black;'>NO TUMOR DETECTED</h2>
</div>
"""
h3 = """
<div style='background-color:#F2F3F5;padding:10px;border-radius:5px;'>
<h2 style='text-align: center; color: Red;'>PITUITARY TUMOR DETECTED</h2>
</div>
"""
h4 = """
<div style='background-color:#F2F3F5;padding:10px;border-radius:5px;'>
<h2 style='text-align: center; color: Red;'>MENINGIOMA TUMOR DETECTED</h2>
</div>
"""
    
def brain_work():
    model = keras.models.load_model("model/model.h5")
    file = st.file_uploader("File")
    if file:
        image = Image.open(file)
        st.image(image,use_column_width=False,width=200,caption=None)
        image = keras.preprocessing.image.img_to_array(image)
        image = tensorflow.image.resize(image,(30,30))
        image = image/255
        image = tensorflow.expand_dims(image,0)
        if st.button("Predict"):
            pred = model.predict(image)
            pred = np.argmax(pred)
            if pred == 0:
                   cmp.html(h2)#NO
            elif pred == 1:
                   cmp.html(h3)
            elif pred == 2:
                   cmp.html(h4)
                      
    
def back_ground(main_bg):
    main_bg_ext = "png"
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
back_ground("back/back.jpg")
