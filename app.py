import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("성취에 대한 만족도 시각화")

# 한글 CSV 읽기 - 인코딩 문제 해결
try:
    df = pd.read_csv("성취에_대한_만족도__19세_이상_인구__20250605123253.csv", encoding='utf-8-sig')
except UnicodeDecodeError:
    df = pd.read_csv("성취에_대한_만족도__19세_이상_인구__20250605123253.csv", encoding='cp949')

# 데이터 미리보기
st.subheader("데이터 미리보기")
st.write(df.head())

# 시각화 기준 선택
option = st.selectbox("분석 기준을 선택하세요", ["성별", "연령대"])

# 컬럼 존재 여부 확인 후 시각화
if option in df.columns:
    st.subheader(f"{option}별 성취 만족도 평균")
    fig, ax = plt.subplots()
    sns.barplot(data=df, x=option, y="성취에 대한 만족도", ax=ax)
    st.pyplot(fig)
else:
    st.warning(f"'{option}' 컬럼이 데이터에 없습니다.")
