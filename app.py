import streamlit as st
import pandas as pd
import os
import webbrowser

st.set_page_config(
    page_title="gpt_trainer",
    page_icon="./data/ai.png"
)

# 제목 및 서브헤딩 설정
st.title("스물 두 고개 v1.0.1")
st.subheader("-Hx. taking with AI patient-")

# 사용자 ID 및 비밀번호 입력창 설정
id = st.text_input("사용자 ID")
password = st.text_input("비밀번호", type="password")

# 로그인 버튼 추가
login_button = st.button('로그인')

# 로그인 버튼이 클릭되었을 때만 처리
if login_button:
    # ID 및 비밀번호 확인
    is_login = id == "ulsanmed1989" and password == "dnftksdmleo89"

    if is_login:
        # 로그인 성공 시 처리
        # 탭 생성
        tab1, tab2, tab3 = st.tabs(["소화기", "Next", "Next"])

        with tab1:
            st.subheader("소화기 환자")
            
            # 데이터 생성
            data = {
                "name": ["22_Questions_01_M50", "22_Questions_02_M69", "22_Questions_03_M68", "22_Questions_04_F55", "22_Questions_05_F48", "22_Questions_06_F26", "22_Questions_07_F35", "22_Questions_08_F52", "22_Questions_09_F58"],
                "url": ["https://ulsanmed-22questions01.streamlit.app/", "https://ulsanmed-22questions02.streamlit.app/", "https://ulsanmed-22questions03.streamlit.app/", "https://ulsanmed-22questions04.streamlit.app/", "https://ulsanmed-22questions05.streamlit.app/", "https://ulsanmed-22questions06.streamlit.app/", "https://ulsanmed-22questions07.streamlit.app/", "https://ulsanmed-22questions08.streamlit.app/", "https://ulsanmed-22questions09.streamlit.app/"],
                "excel_file": ["./data/22_Questions_01.xlsx", "./data/22_Questions_02.xlsx", "./data/22_Questions_03.xlsx", "./data/22_Questions_04.xlsx", "./data/22_Questions_05.xlsx", "./data/22_Questions_06.xlsx", "./data/22_Questions_07.xlsx", "./data/22_Questions_08.xlsx", "./data/22_Questions_09.xlsx"]  # Excel 파일 경로 추가
            }

            # 데이터프레임 생성
            df = pd.DataFrame(data)

            # 설명 텍스트
            with st.expander("**이 프로그램 사용 방법**"):
                st.divider()
                st.write("* 아래 왼쪽 버튼을 누르면, 해당 증례의 탭이 새로 생성됩니다.")
                st.write("* 생성된 탭의 화면 맨 아래 입력창에서 지시한대로 문진을 진행합니다.")
                st.write("* 질문을 입력하고 엔터 키를 칩니다.")
                st.write("* 엔터키를 치고나면 대답이 나올 때 까지 수 초정도 대기해야 합니다.")
                st.write("* 질문은 chief complaint과 관련된 것이어야 하고, 문맥에 맞게 해야됩니다.")
                st.write("* 질문이 모두 끝났으면 반드시 환자에게 궁금한 점이 있는 지 물어봅니다.")
                st.write("* 환자의 두 개의 질문에 대답하고 나면, AI가 질문이 안된 항목을 출력해 줍니다.")
                st.write("* 마지막 과정은 길게는 40초 까지도 걸립니다. 기다려 주세요.")
                st.write("* 뭔가 문제가 생기면 탭을 닫고 링크를 눌러 다시 시작하세요.")
           
            # 링크와 Excel 파일 내용 표시 버튼 생성
            for index, row in df.iterrows():
                col1, col2, col3, col4 = st.columns([1, 1, 1, 1])  # 컬럼을 1:1:1:1 비율로 나눕니다.

                with col1:
                    # 새 탭에서 URL 열기
                    st.markdown(f"<a href='{row['url']}' target='_blank'>{row['name']}</a>", unsafe_allow_html=True)

                with col2:
                    # 파일 경로를 행의 excel_file 컬럼에서 가져옵니다.
                    file_path = row['excel_file']
                    # 파일을 열어 바이트로 읽기
                    with open(file_path, "rb") as file:
                        file_data = file.read()
                    btn = st.download_button(
                        label="해설 자료 다운로드",
                        data=file_data,
                        file_name=os.path.basename(file_path),
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )
            
            with st.expander("제작자 및 copyright 고지"):
                st.divider()          
                st.write("이 프로그램은 울산의대 서울아산병원 소화기내과 이 진혁에 의해 제작되었습니다.")
                st.write("MIT: 자유롭게 이용하실 수 있으나, 제 소속과 이름을 명시해 주시기 바랍니다.")
                        
        with tab2:
            st.title("개발 예정")

            st.text("앞으로 개발 예정입니다.")  

        with tab3:
            st.title("개발 예정")

            st.text("앞으로 개발 예정입니다.")

    else:
        st.write("로그인 실패!")
        st.write("ID 또는 비밀번호가 올바르지 않습니다.")