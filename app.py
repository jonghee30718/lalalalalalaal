import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("성취에 대한 만족도 시각화")

# CSV 파일 읽기 (파일명 정확히 맞춰야 함)
df = pd.read_csv("성취에_대한_만족도__19세_이상_인구__20250605123253.csv")

# 컬럼명 확인 (간단히 상위 5행만 보기)
st.subheader("데이터 미리보기")
st.write(df.head())

# 시각화
option = st.selectbox("분석 기준을 선택하세요", ["성별", "연령대"])

if option in df.columns:
    st.subheader(f"{option}별 성취 만족도 평균")
    fig, ax = plt.subplots()
    sns.barplot(data=df, x=option, y="성취에 대한 만족도", ax=ax)
    st.pyplot(fig)
else:
    st.warning(f"'{option}' 컬럼이 데이터에 없습니다.")
