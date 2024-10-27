import streamlit as st
from datetime import time, datetime
import pandas as pd
import numpy as np

# -------------------------------day8-------------------------------

st.header('st.slider')

# 年齢：st.slider('見出しテキスト',最小値,最大値,デフォルト値)
st.subheader('Slider')
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

# 幅：st.salider('見出しテキスト',最小値,最大値,(下限のデフォルト値,上限のデフォルト値))
st.subheader('Range slider')
values = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

# 時刻 ：st.salider('見出しテキスト',value=(time(下限のデフォルト値),time(上限のデフォルト値)))
st.subheader('Range time slider')
appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

# 日時 ： st.salider('見出しテキスト',value=(datetime(デフォルト値),format="形式")
st.subheader('Datetime slider')
start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)


# -------------------------------day9-------------------------------

st.header('Line chart')

# ランダムな数値データを作成 → 折れ線グラフ表示
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
st.line_chart(chart_data)


# -------------------------------day10-------------------------------

st.header('st.selectbox')

# 好きな色の選択 ： st.selectbox('見出しテキスト',('選択肢1','選択肢2',・・・)) 
option = st.selectbox(
     'What is your favorite color?',
     ('Blue', 'Red', 'Green'))
st.write('Your favorite color is ', option)