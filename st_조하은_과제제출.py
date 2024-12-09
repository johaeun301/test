import streamlit as st
import datetime

import numpy as np      #넘파이 행렬 데이터 처리
import altair as alt    #데이터 시각화
import pandas as pd     #데이터 처리

from datetime import time, datetime

st.title('과제')

st.header("메뉴판")

with st.form('my_form') :
    # 입력 위젯
    chicken_val = st.selectbox('치킨', ['후라이드', '양념(+1,000원)', '간장 (+1,000원)', '후라반 양념반(+1,000원)'])
    chicken_type_val = st.selectbox('종류', ['뼈', '순살(+1,000원)'])
    pickup_val = st.selectbox('수령 방법', ['배달', '포장방문'])
    drink_val = st.selectbox('주류 선택', ['X', '콜라 1.25L', '사이다 1.25L', '생맥주 1500cc'])
    review_val = st.checkbox('후기 약속 (콜라 1.25L)')
    submitted = st.form_submit_button('제출')   #모든 양식은 제출 버튼을 가져야 함

if submitted :
    st.markdown(f'''
                🍗주문 내용: 
                - 치킨: "{chicken_val}"
                - 뼈/순살: "{chicken_type_val}"
                - 수령 방법: "{pickup_val}"
                - 주류 선택: "{ drink_val}"
                - 후기 약속: "{submitted}"
                ''')
else :
    st.write('주문하세요!')