# # 파일 업로드 버튼 (업로드 기능)
# file = st.file_uploader("파일 선택(csv or excel)", type=['csv', 'xls', 'xlsx'])

# Excel or CSV 확장자를 구분하여 출력하는 경우
# if file is not None:
#     ext = file.name.split('.')[-1]
#     if ext == 'csv':
#         # 파일 읽기
#         df = pd.read_csv(file)
#         # 출력
#         st.dataframe(df)
#     elif 'xls' in ext:
#         # 엑셀 로드
#         df = pd.read_excel(file, engine='openpyxl', encoding='cp949')
#         # 출력
#         st.dataframe(df)

import streamlit as st
import pandas as pd
import time
import chardet

uploaded_file = st.file_uploader("파일 선택(csv or excel)", type=["csv", "xlsx"])

# 파일이 업로드 된 경우
if uploaded_file is not None:
    # If the file is an Excel file
    if uploaded_file.name.endswith('.xlsx'):
        df = pd.read_excel(uploaded_file, engine='openpyxl')
        st.dataframe(df)
    else:
        # Detect the encoding if it's a CSV file
        result = chardet.detect(uploaded_file.read(10000))  # Read the first 10000 bytes for encoding detection
        encoding = result['encoding']
        
        # Seek back to the start of the file since read() moves the cursor
        uploaded_file.seek(0)
        
        df = pd.read_csv(uploaded_file, encoding=encoding)
        st.dataframe(df)

    time.sleep(3)

# #파일이 정상 업로드 된 경우
# if uploaded_file is not None:
#     # 파일 읽기
#     df = pd.read_csv(uploaded_file)
#     # 출력
#     st.dataframe(df)

# time.sleep(3)

# if uploaded_file is not None:
#     with open(uploaded_file, 'rb') as f:
#         result = chardet.detect(f.read())
#         encoding = result['encoding']

#     if uploaded_file.name.endswith('.csv'):
#         df = pd.read_csv(uploaded_file, encoding=encoding)
#     elif uploaded_file.name.endswith('.xlsx'):
#         df = pd.read_excel(uploaded_file, engine='openpyxl', encoding=encoding)

#     st.dataframe(df)