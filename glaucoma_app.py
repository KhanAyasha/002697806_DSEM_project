import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np

# Set the theme configuration
st.markdown(
    """
    <style>
    .stApp {
        background-color: black;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.set_option('deprecation.showfileUploaderEncoding', False)

# Function to import and predict
def import_and_predict(image_data, model):
    image = ImageOps.fit(image_data, (100,100),Image.ANTIALIAS)
    image = image.convert('RGB')
    image = np.asarray(image)
    st.image(image, channels='RGB')
    image = (image.astype(np.float32) / 255.0)
    img_reshape = image[np.newaxis,...]
    prediction = model.predict(img_reshape)
    return prediction

model = tf.keras.models.load_model('my_model2.h5')

#     st.title("/")
html_temp = """
<div style="background-color:#DFFF00;padding:10px">
<h2 style="color:black;text-align:center;">Glaucoma Detector ML App</h2>
</div>
<br> <!-- Adding a line break here -->
<br> <!-- Adding a line break here -->
"""
st.markdown(html_temp, unsafe_allow_html=True)
st.write("This is a simple image classification web app to predict glaucoma through fundus image of the eye")

st.markdown('<span style="color: #FFFF00;">Please upload an image(jpg) file</span>', unsafe_allow_html=True)
file = st.file_uploader(" ", type=["jpg"])

if file is None:
    st.text("You haven't uploaded a jpg image file")
else:
    imageI = Image.open(file)
    prediction = import_and_predict(imageI, model)
    pred = prediction[0][0]
    if(pred > 0.5):
        st.write("""
                # <span style="color: #39FF14;">**Prediction:** ***Great News!!*** <br/>**Your eye is Healthy.**</span>
                """, unsafe_allow_html=True
                 )
        st.balloons()
    else:
        st.write("""
                # <span style="color: red;"> **Prediction:** ***Caution!!*** <br/>**You are affected by Glaucoma. <br/>Please consult an ophthalmologist as soon as possible.**</span>
                """, unsafe_allow_html=True
                 )
        
st.markdown("<br/><br/><br/>", unsafe_allow_html=True)


# Uncommented and corrected indentation
# st.success('The output is {}'.format(result))
st.markdown('<span style="color: #FFFF00;">Check my Python Notebook: <a href="">link</a></span>', unsafe_allow_html=True)
st.markdown('<span style="color: #FFFF00;">Check my GitHub repository: <a href="https://github.com/KhanAyasha/002697806_DSEM_assignments-.git">link</a></span>', unsafe_allow_html=True)
