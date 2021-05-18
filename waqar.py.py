import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image


st.title("Hunza North Pakistan")
st.text("let me introduce Hunza ,culture,language and food  ")
st.header("Hunza is a mountainous valley in Gilgit")



st.info("moutains")

st.subheader("Blue sky")

st.title("hello waqar")
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
 'first column': [1, 2, 3, 4],
 'second column': [10, 20, 30, 40]
}))
df = pd.DataFrame({
 'first column': [1, 2, 3, 4],
 'second column': [10, 20, 30, 40]
})
st.info("moutains")

st.subheader("Blue sky")

df
chart_data = pd.DataFrame(
 np.random.randn(20, 3),
 columns=['a', 'b', 'c'])
video_file = open('video.mp4', 'rb')
video_bytes = video_file.read()
st.line_chart(chart_data)
map_data = pd.DataFrame(
 np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
 columns=['lat', 'lon'])
st.map(map_data)
dqn = Image.open('image.jpg')
st.image(dqn, caption='Using a Deep Q Network can approximate Q(s,a)', use_column_width=True)
st.text("this is a python video")
video_file = open('video.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)
