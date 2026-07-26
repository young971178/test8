import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="GDX 교육 수강 신청", layout="wide")

if 'current_user' not in st.session_state:
    st.session_state.current_user = random.choice(["박지성", "이영표", "류현진", "손흥민", "박찬호"])
if 'page' not in st.session_state:
    st.session_state.page = 'home'

def go_home():
    st.session_state.page = 'home'
    st.rerun()

users = ["박지성", "이영표", "류현진", "손흥민", "박찬호"]
modules = [
    "기술통계", "추론통계", "실험계획법", "통계적공정관리", "구조적문제해결방법론",
    "미니탭리터러시", "파이썬리터러시", "바이브코딩", "머신러닝 이론",
    "탐색적데이터분석", "머신러닝 모델링", "AI Automation", "시각화"
]

badge_data = {
    "기술통계": ["녹색", "검정", "녹색", "검정", "골드크라운"],
    "추론통계": ["녹색", "녹색", "검정", "노랑", "실버크라운"],
    "실험계획법": ["녹색", "검정", "녹색", "노랑", "노랑"],
    "통계적공정관리": ["없음", "없음", "검정", "실버크라운", "골드크라운"],
    "구조적문제해결방법론": ["없음", "검정", "녹색", "검정", "검정"],
    "미니탭리터러시": ["검정", "노랑", "노랑", "노랑", "녹색"],
    "파이썬리터러시": ["골드크라운", "검정", "실버크라운", "녹색", "노랑"],
    "바이브코딩": ["노랑", "골드크라운", "실버크라운", "녹색", "노랑"],
    "머신러닝 이론": ["없음", "없음", "노랑", "노랑", "노랑"],
    "탐색적데이터분석": ["없음", "없음", "노랑", "녹색", "녹색"],
    "머신러닝 모델링": ["없음", "노랑", "노랑", "없음", "녹색"],
    "AI Automation": ["녹색", "검정", "녹색", "노랑", "없음"],
    "시각화": ["없음", "노랑", "검정", "골드크라운", "없음"]
}

if st.session_state.page == 'home':
    st.title("GDX 교육 수강 신청")
    st.subheader(f"현재 접속자: {st.session_state.current_user}")
    
    df = pd.DataFrame(badge_data, index=users).T
    df.columns.name = "사용자"
    st.write("### 각 모듈 별 배지 현황")
    st.dataframe(df[[st.session_state.current_user]], use_container_width=True)

    st.write("### 교육 과정 선택")
    cols = st.columns(4)
    for i, mod in enumerate(modules):
        if cols[i % 4].button(mod, use_container_width=True):
            st.session_state.page = mod
            st.rerun()

else:
    mod = st.session_state.page
    st.title(f"{mod} 과정 신청")
    
    msg_off = "수강신청이 완료되었습니다. 오프라인 교육은 강사의 안내에 따라 과제를 제출하여 평가에 응하시기 바랍니다."
    msg_on = "수강신청이 완료되었습니다. 온라인 교육은 강의 종료일로부터 한 달 이내에 두 번의 응시 기회가 부여됩니다."
    
    def check_prereq(msg):
        ans = st.radio(f"{msg} 수강신청 하시겠습니까?", ["선택", "예", "아니오"], key=f"prereq_{mod}")
        if ans == "아니오":
            go_home()
        return ans == "예"
    
    def render_online(desc):
        st.write(f"{desc} 수강신청 하시겠습니까?")
        c1, c2 = st.columns(2)
        if c1.button("예"): st.success(msg_on)
        if c2.button("아니오"): go_home()

    def render_offline_int(instructors):
        inst = st.radio("사내강사를 선택하세요.", ["선택"] + instructors)
        if inst != "선택":
            st.write("수강신청하시겠습니까?")
            c1, c2 = st.columns(2)
            if c1.button("예"): st.success(msg_off)
            if c2.button("아니오"): go_home()

    def render_offline_ext(mod_name):
        mod_label = "머신러닝" if mod_name == "머신러닝 이론" else mod_name
        date = st.radio(f"{mod_label} 오프라인 과정은 외부교육기관(베가스)의 집체교육입니다. 신청하고자 하는 날짜를 선택하세요.", 
                        ["선택", "2026-08-03", "2026-08-10", "2026-08-17"])
        if date != "선택":
            st.write("수강신청하시겠습니까?")
            c1, c2 = st.columns(2)
            if c1.button("예"): st.success(f"({date}) {msg_off}")
            if c2.button("아니오"): go_home()

    passed = True
    
    if mod == "기술통계":
        pass
    elif mod == "추론통계": passed = check_prereq("선행학습으로 '기술통계' 과정이 요구됩니다.")
    elif mod == "실험계획법": passed = check_prereq("선행학습으로 '기술통계' , '추론통계' 과정이 요구됩니다.")
    elif mod == "통계적공정관리": passed = check_prereq("선행학습으로 '기술통계' , '추론통계' 과정이 요구됩니다.")
    elif mod == "구조적문제해결방법론":
        ans = st.radio("본 과정은 오프라인 교육만 제공되고 있습니다. 수강신청 하시겠습니까?", ["선택", "예", "아니오"])
        if ans == "아니오": go_home()
        elif ans == "예": render_offline_int(["김영태", "지덱수", "기냥"])
        passed = False
    elif mod == "미니탭리터러시": passed = check_prereq("선행학습으로 '기술통계' , '추론통계' , '통계적공정관리', '실험계획법' 과정이 요구됩니다.")
    elif mod == "파이썬리터러시": passed = check_prereq("선행학습으로 '기술통계' , '추론통계' 과정이 요구됩니다.")
    elif mod == "바이브코딩": passed = check_prereq("선행학습으로 '파이썬리터러시' 과정이 요구됩니다.")
    elif mod == "머신러닝 이론": passed = check_prereq("선행학습으로 '기술통계', '추론통계', '파이썬리터러시' 과정이 요구됩니다.")
    elif mod == "탐색적데이터분석": passed = check_prereq("선행학습으로 '기술통계', '추론통계', '파이썬리터러시', '바이브코딩' 과정이 요구됩니다.")
    elif mod == "머신러닝 모델링": passed = check_prereq("선행학습으로 '기술통계', '추론통계', '파이썬리터러시', '바이브코딩', '머신러닝 이론', '탐색적데이터분석' 과정이 요구됩니다.")
    elif mod == "AI Automation": passed = check_prereq("선행학습으로 '바이브코딩' 과정이 요구됩니다.")
    elif mod == "시각화": passed = check_prereq("선행학습으로 '기술통계', '바이브코딩' 과정이 요구됩니다.")

    if passed:
        mode = st.radio("방식을 선택하세요.", ["선택", "온라인", "오프라인"])
        if mode == "온라인":
            if mod == "기술통계": render_online("기술통계 온라인 과정은 휴넷에서 제공되는 통계학 개론 과정의 Chapter 1,2,3 에 해당합니다.")
            elif mod == "추론통계": render_online("추론통계 온라인 과정은 휴넷에서 제공되는 통계학 개론 과정의 Chapter 4,5,6 에 해당합니다.")
            elif mod == "실험계획법": render_online("실험계획법 온라인 과정은 휴넷에서 제공되는 실험계획법 과정의 Chapter 1~4 에 해당합니다.")
            elif mod == "통계적공정관리": render_online("통계적공정관리 온라인 과정은 휴넷에서 제공되는 SPC 개론 과정의 Chapter 1,2,3 에 해당합니다.")
            elif mod == "미니탭리터러시": render_online("미니탭리터러시 온라인 과정은 휴넷에서 제공되는 미니탭 개론 과정의 Chapter 1~5 에 해당합니다.")
            elif mod == "파이썬리터러시": render_online("파이썬리터러시 온라인 과정은 휴넷에서 제공되는 빅데이터분석기사 과정의 Chapter 1~3 에 해당합니다.")
            elif mod == "바이브코딩": render_online("바이브코딩 온라인 과정은 휴넷에서 제공되는 바이브코딩 마스터 과정에 해당합니다.")
            elif mod == "머신러닝 이론": render_online("머신러닝 온라인 과정은 휴넷에서 제공되는 빅데이터분석기사 과정의 Chapter 1,2,3에 해당합니다.")
            elif mod == "탐색적데이터분석": render_online("탐색적데이터분석 온라인 과정은 휴넷에서 제공되는 빅데이터분석기사 과정의 Chapter 4,5,6에 해당합니다.")
            elif mod == "머신러닝 모델링": render_online("머신러닝모델링 온라인 과정은 휴넷에서 제공되는 빅데이터분석기사 과정의 Chapter 7,8,9에 해당합니다.")
            elif mod == "AI Automation": render_online("AI Automation 온라인 과정은 휴넷에서 제공되는 Stramlit 마스터 과정에 해당합니다.")
            elif mod == "시각화": render_online("시각화 온라인 과정은 휴넷에서 제공되는 Tableau 마스터 과정에 해당합니다.")
        elif mode == "오프라인":
            if mod in ["기술통계", "추론통계", "통계적공정관리", "미니탭리터러시", "AI Automation", "시각화"]:
                render_offline_int(["지덱수", "빤히", "기냥"])
            elif mod == "실험계획법":
                st.write("실험계획법 오프라인 과정은 현재 개발중에 있습니다. 온라인 과정을 이용해 주세요.")
                if st.button("이전화면으로 돌아가기"): go_home()
            elif mod in ["파이썬리터러시", "바이브코딩", "머신러닝 이론", "탐색적데이터분석", "머신러닝 모델링"]:
                render_offline_ext(mod)