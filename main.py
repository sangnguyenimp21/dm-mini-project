import streamlit as st
import numpy as np
from utils import helper
from utils import apu

st.title('Bank Telemarketing Prediction')

st.markdown(
    """
    Simple application of bank telemarketing for classification customer
    """
)

st.sidebar.header("User Input Features")

with st.sidebar:
    user_input_data = apu.generate_sidebar()

input_data = apu.apply_data_input(user_input_data)

model = apu.load_model()

predicted_output = model.predict(input_data)
prediction_proba = model.predict_proba(input_data)

st.subheader('Prediction')
if predicted_output[0]:
    st.write("Yes")
else:
    st.write("No")

st.subheader('Prediction Probability')
st.write(prediction_proba)
