import streamlit as st

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib import rc

# 포수 / 내야수 / 외야수
df = pd.read_csv('62540_KBO_prediction_data/Regular_Season_Batter.csv')

positions = ['내야수','외야수','포수']
selected_positions = st.selectbox('포지션을 선택하세요', positions)
options = st.multiselect(
    '팀을 선택하세요.',
    df['team'].unique(),
    df['team'].unique())

rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

select_team_df = df[df['team'].isin(options)]

try:
    if selected_positions=='내야수':
        # Streamlit 앱 생성
        st.title('팀별 내야수 Box Plot')
        st.write('여기에 박스 플롯이 나타납니다.')

        in_df = select_team_df[select_team_df['position'].str.contains('내야수')==True] # 내야수

        # 박스 플롯 그리기
        fig1, ax1 = plt.subplots()
        in_df.boxplot(column='OPS', by='team', ax=ax1)
        st.pyplot(fig1)

    elif selected_positions=='외야수':
        st.title('팀별 외야수 Box Plot')
        st.write('여기에 박스 플롯이 나타납니다.')

        out_df = select_team_df[select_team_df['position'].str.contains('외야수')==True] # 외야수

        # 박스 플롯 그리기
        fig2, ax2 = plt.subplots()
        out_df.boxplot(column='OPS', by='team', ax=ax2)
        st.pyplot(fig2)

    elif selected_positions=='포수':
        st.title('팀별 포수 Box Plot')
        st.write('여기에 박스 플롯이 나타납니다.')

        home_df = select_team_df[select_team_df['position'].str.contains('포수')==True] # 포수

        # 박스 플롯 그리기
        fig3, ax3 = plt.subplots()
        home_df.boxplot(column='OPS', by='team', ax=ax3)
        st.pyplot(fig3)

except:
    fig4, ax4 = plt.subplots()
    st.pyplot(fig4)