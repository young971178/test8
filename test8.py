import streamlit as st
import random

st.set_page_config(layout="wide")

users = ["박지성", "이영표", "류현진", "손흥민", "박찬호"]
modules = [
    "기술통계", "추론통계", "실험계획법", "통계적공정관리", "구조적문제해결방법론", 
    "미니탭리터러시", "파이썬리터러시", "바이브코딩", "머신러닝 이론", "탐색적데이터분석", 
    "머신러닝 모델링", "AI Automation", "시각화"
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

badge_icons = {
    "노랑": "🟡", "녹색": "🟢", "검정": "⚫", 
    "실버크라운": "🥈", "골드크라운": "👑", "없음": "🤍"
}

if 'user' not in st.session_state:
    st.session_state.user = random.choice(users)
if 'page' not in st.session_state:
    st.session_state.page = 'main'
if 'module' not in st.session_state:
    st.session_state.module = None
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'course_type' not in st.session_state:
    st.session_state.course_type = None
if 'selection' not in st.session_state:
    st.session_state.selection = None

user_idx = users.index(st.session_state.user)

def go_main():
    st.session_state.page = 'main'
    st.session_state.module = None
    st.session_state.step = 0
    st.session_state.course_type = None
    st.session_state.selection = None

def next_step():
    st.session_state.step += 1

def select_module(m):
    st.session_state.module = m
    st.session_state.page = 'course'
    st.session_state.step = 0

def course_process(mod):
    st.markdown(f"<h2 style='text-align: center; color: #4B8BBE;'>{mod} 수강신청</h2>", unsafe_allow_html=True)
    st.write("---")
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.session_state.step == 0:
            prereq = {
                "추론통계": "'기술통계'",
                "실험계획법": "'기술통계', '추론통계'",
                "통계적공정관리": "'기술통계', '추론통계'",
                "구조적문제해결방법론": "오프라인 전용",
                "미니탭리터러시": "'기술통계', '추론통계', '통계적공정관리', '실험계획법'",
                "파이썬리터러시": "'기술통계', '추론통계'",
                "바이브코딩": "'파이썬리터러시'",
                "머신러닝 이론": "'기술통계', '추론통계', '파이썬리터러시'",
                "탐색적데이터분석": "'기술통계', '추론통계', '파이썬리터러시', '바이브코딩'",
                "머신러닝 모델링": "'기술통계', '추론통계', '파이썬리터러시', '바이브코딩', '머신러닝 이론', '탐색적데이터분석'",
                "AI Automation": "'바이브코딩'",
                "시각화": "'기술통계', '바이브코딩'"
            }
            
            if mod == "기술통계":
                st.session_state.step = 1
                st.rerun()
            elif mod == "구조적문제해결방법론":
                st.info("본 과정은 오프라인 교육만 제공되고 있습니다. 수강신청 하시겠습니까?")
                c1, c2 = st.columns(2)
                if c1.button("예", use_container_width=True):
                    st.session_state.course_type = "오프라인"
                    st.session_state.step = 2
                    st.rerun()
                if c2.button("아니오", use_container_width=True): go_main()
            else:
                st.info(f"선행학습으로 {prereq[mod]} 과정이 요구됩니다. 수강신청 하시겠습니까?")
                c1, c2 = st.columns(2)
                if c1.button("예", use_container_width=True): next_step(); st.rerun()
                if c2.button("아니오", use_container_width=True): go_main()
                
        elif st.session_state.step == 1:
            st.write("교육 방식을 선택해 주세요.")
            c1, c2 = st.columns(2)
            if c1.button("온라인", use_container_width=True):
                st.session_state.course_type = "온라인"
                next_step(); st.rerun()
            if c2.button("오프라인", use_container_width=True):
                if mod == "실험계획법":
                    st.warning("실험계획법 오프라인 과정은 현재 개발중에 있습니다. 온라인 과정을 이용해 주세요.")
                    if st.button("이전 화면으로 돌아가기"): go_main()
                else:
                    st.session_state.course_type = "오프라인"
                    next_step(); st.rerun()
                    
        elif st.session_state.step == 2:
            ctype = st.session_state.course_type
            if ctype == "온라인":
                on_msgs = {
                    "기술통계": "휴넷에서 제공되는 통계학 개론 과정의 Chapter 1,2,3 에 해당합니다.",
                    "추론통계": "휴넷에서 제공되는 통계학 개론 과정의 Chapter 4,5,6 에 해당합니다.",
                    "실험계획법": "휴넷에서 제공되는 실험계획법 과정의 Chapter 1~4 에 해당합니다.",
                    "통계적공정관리": "휴넷에서 제공되는 SPC 개론 과정의 Chapter 1,2,3 에 해당합니다.",
                    "미니탭리터러시": "휴넷에서 제공되는 미니탭 개론 과정의 Chapter 1~5 에 해당합니다.",
                    "파이썬리터러시": "휴넷에서 제공되는 빅데이터분석기사 과정의 Chapter 1~3 에 해당합니다.",
                    "바이브코딩": "휴넷에서 제공되는 바이브코딩 마스터 과정에 해당합니다.",
                    "머신러닝 이론": "휴넷에서 제공되는 빅데이터분석기사 과정의 Chapter 1,2,3에 해당합니다.",
                    "탐색적데이터분석": "휴넷에서 제공되는 빅데이터분석기사 과정의 Chapter 4,5,6에 해당합니다.",
                    "머신러닝 모델링": "휴넷에서 제공되는 빅데이터분석기사 과정의 Chapter 7,8,9에 해당합니다.",
                    "AI Automation": "휴넷에서 제공되는 Stramlit 마스터 과정에 해당합니다.",
                    "시각화": "휴넷에서 제공되는 Tableau 마스터 과정에 해당합니다."
                }
                st.info(f"{mod} 온라인 과정은 {on_msgs[mod]} 수강신청 하시겠습니까?")
                c1, c2 = st.columns(2)
                if c1.button("예", use_container_width=True): next_step(); st.rerun()
                if c2.button("아니오", use_container_width=True): go_main()
                
            elif ctype == "오프라인":
                ext_courses = ["파이썬리터러시", "바이브코딩", "머신러닝 이론", "탐색적데이터분석", "머신러닝 모델링"]
                if mod in ext_courses:
                    st.info(f"{mod} 오프라인 과정은 외부교육기관(베가스)의 집체교육입니다. 신청하고자 하는 날짜를 선택하세요.")
                    dates = ["2026년 8월 10일", "2026년 9월 14일", "2026년 10월 12일"]
                    for d in dates:
                        if st.button(d, use_container_width=True):
                            st.session_state.selection = d
                            st.session_state.step = 3
                            st.rerun()
                    if st.button("취소", use_container_width=True): go_main()
                else:
                    st.write("사내강사를 선택해 주세요.")
                    instructors = ["김영태", "지덱수", "기냥"] if mod == "구조적문제해결방법론" else ["지덱수", "빤히", "기냥"]
                    for ins in instructors:
                        if st.button(ins, use_container_width=True):
                            st.session_state.selection = ins
                            st.session_state.step = 3
                            st.rerun()
                    if st.button("취소", use_container_width=True): go_main()
                    
        elif st.session_state.step == 3:
            ctype = st.session_state.course_type
            if ctype == "온라인":
                st.success("수강신청이 완료되었습니다. 온라인 교육은 강의 종료일로부터 한 달 이내에 두 번의 응시 기회가 부여됩니다.")
            elif ctype == "오프라인":
                ext_courses = ["파이썬리터러시", "바이브코딩", "머신러닝 이론", "탐색적데이터분석", "머신러닝 모델링"]
                if mod in ext_courses:
                    st.success(f"({st.session_state.selection}) 수강신청이 완료되었습니다. 오프라인 교육은 강사의 안내에 따라 과제를 제출하여 평가에 응하시기 바랍니다.")
                else:
                    st.write(f"선택 강사: {st.session_state.selection}")
                    st.info("수강신청하시겠습니까?")
                    c1, c2 = st.columns(2)
                    if c1.button("예", use_container_width=True):
                        st.session_state.step = 4; st.rerun()
                    if c2.button("아니오", use_container_width=True): go_main()
            if st.button("처음으로 돌아가기"): go_main()
            
        elif st.session_state.step == 4:
            st.success("수강신청이 완료되었습니다. 오프라인 교육은 강사의 안내에 따라 과제를 제출하여 평가에 응하시기 바랍니다.")
            if st.button("처음으로 돌아가기"): go_main()

if st.session_state.page == 'main':
    st.markdown(f"### 👤 접속 사용자: **{st.session_state.user}**님 환영합니다.")
    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
    
    st.markdown("#### 🏆 모듈 별 배지 획득 현황")
    st.markdown("<div style='background-color: #f0f2f6; padding: 20px; border-radius: 10px;'>", unsafe_allow_html=True)
    
    cols = st.columns(3)
    for i, mod in enumerate(modules):
        col_idx = i % 3
        badge_status = badge_data[mod][user_idx]
        icon = badge_icons[badge_status]
        with cols[col_idx]:
            st.markdown(f"**{mod}** &nbsp; {icon}")
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)
    
    st.markdown("#### 📚 교육 과정 신청 (모듈 선택)")
    btn_cols = st.columns(4)
    for i, mod in enumerate(modules):
        with btn_cols[i % 4]:
            st.markdown(f"""
            <style>
            div.stButton > button:first-child {{
                background-color: #ffffff;
                color: #333333;
                border: 2px solid #4B8BBE;
                border-radius: 8px;
                height: 60px;
                font-weight: bold;
                margin-bottom: 10px;
            }}
            div.stButton > button:first-child:hover {{
                background-color: #4B8BBE;
                color: white;
            }}
            </style>
            """, unsafe_allow_html=True)
            if st.button(mod, key=f"btn_{mod}", use_container_width=True):
                select_module(mod)
                st.rerun()

elif st.session_state.page == 'course':
    course_process(st.session_state.module)
