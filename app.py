import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# CSV 불러오기 (인코딩 대응)
try:
    df = pd.read_csv("성취에_대한_만족도__19세_이상_인구__20250605123253.csv", encoding="utf-8-sig")
except UnicodeDecodeError:
    df = pd.read_csv("성취에_대한_만족도__19세_이상_인구__20250605123253.csv", encoding="cp949")

st.title("성취에 대한 만족도 시각화")

# 유효한 기준 목록 추출 (예: 성별, 연령별, 교육정도별 등)
criteria_options = df["특성별(1)"].unique().tolist()
selected_criteria = st.selectbox("기준을 선택하세요", criteria_options)

# 선택된 기준에 해당하는 데이터 필터링
filtered_df = df[df["특성별(1)"] == selected_criteria]

# 만족도 항목 열 (2024.1 ~ 2024.5)
satisfaction_cols = ["2024.1", "2024.2", "2024.3", "2024.4", "2024.5"]
satisfaction_labels = ["매우 만족", "약간 만족", "보통", "약간 불만족", "매우 불만족"]

# 시각화
st.subheader(f"{selected_criteria}별 성취에 대한 만족도")
for index, row in filtered_df.iterrows():
    st.markdown(f"### {row['특성별(2)']}")
    values = [row[col] for col in satisfaction_cols]
    
    fig, ax = plt.subplots()
    ax.bar(satisfaction_labels, values, color="skyblue")
    ax.set_ylim(0, 100)
    ax.set_ylabel("비율 (%)")
    st.pyplot(fig)
