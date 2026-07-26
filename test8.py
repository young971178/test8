import streamlit as st
import random

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

# ----------------- 데이터 정의 -----------------
users = ['박지성', '이영표', '류현진', '손흥민', '박찬호']

badge_levels = {'없음': 0, '노랑': 1, '녹색': 2, '검정': 3, '실버크라운': 4, '골드크라운': 5}
badge_colors = ['#E0E0E0', '#FFD700', '#32CD32', '#000000', '#C0C0C0', '#FFDF00']
badge_names = ['없음', '노랑', '녹색', '검정', '실버크라운', '골드크라운']

data = {
    '기술통계': ['녹색', '검정', '녹색', '검정', '골드크라운'],
    '추론통계': ['녹색', '녹색', '검정', '노랑', '실버크라운'],
    '실험계획법': ['녹색', '검정', '녹색', '노랑', '노랑'],
    '통계적공정관리': ['없음', '없음', '검정', '실버크라운', '골드크라운'],
    '구조적문제해결방법론': ['없음', '검정', '녹색', '검정', '검정'],
    '미니탭리터러시': ['검정', '노랑', '노랑', '노랑', '녹색'],
    '파이썬리터러시': ['골드크라운', '검정', '실버크라운', '녹색', '노랑'],
    '바이브코딩': ['노랑', '골드크라운', '실버크라운', '녹색', '노랑'],
    '머신러닝 이론': ['없음', '없음', '노랑', '노랑', '노랑'],
    '탐색적데이터분석': ['없음', '없음', '노랑', '녹색', '녹색'],
    '머신러닝 모델링': ['없음', '노랑', '노랑', '없음', '녹색'],
    'AI Automation': ['녹색', '검정', '녹색', '노랑', '없음'],
    '시각화': ['없음', '노랑', '검정', '골드크라운', '없음']
}

modules_info = {
    '기술통계': {
        'prereq': None,
        'has_online': True, 'has_offline': True,
        'online_msg': "기술통계 온라인 과정은 휴넷에서 제공되는 통계학 개론 과정의 Chapter 1,2,3 에 해당합니다.",
        'offline_type': 'instructor', 'offline_options': ['지덱수', '빤히', '기냥']
    },
    '추론통계': {
        'prereq': "선행학습으로 '기술통계' 과정이 요구됩니다.",
        'has_online': True, 'has_offline': True,
        'online_msg': "추론통계 온라인 과정은 휴넷에서 제공되는 통계학 개론 과정의 Chapter 4,5,6 에 해당합니다.",
        'offline_type': 'instructor', 'offline_options': ['지덱수', '빤히', '기냥']
    },
    '실험계획법': {
        'prereq': "선행학습으로 '기술통계' , '추론통계' 과정이 요구됩니다.",
        'has_online': True, 'has_offline': True,
        'online_msg': "실험계획법 온라인 과정은 휴넷에서 제공되는 실험계획법 과정의 Chapter 1~4 에 해당합니다.",
        'offline_type': 'developing'
    },
    '통계적공정관리': {
        'prereq': "선행학습으로 '기술통계' , '추론통계' 과정이 요구됩니다.",
        'has_online': True, 'has_offline': True,
        'online_msg': "통계적공정관리 온라인 과정은 휴넷에서 제공되는 SPC 개론 과정의 Chapter 1,2,3 에 해당합니다.",
        'offline_type': 'instructor', 'offline_options': ['지덱수', '빤히', '기냥']
    },
    '구조적문제해결방법론': {
        'prereq': "본 과정은 오프라인 교육만 제공되고 있습니다.",
        'has_online': False, 'has_offline': True,
        'offline_type': 'instructor', 'offline_options': ['김영태', '지덱수', '기냥']
    },
    '미니탭리터러시': {
        'prereq': "선행학습으로 '기술통계' , '추론통계' , '통계적공정관리', '실험계획법' 과정이 요구됩니다.",
        'has_online': True, 'has_offline': True,
        'online_msg': "미니탭리터러시 온라인 과정은 휴넷에서 제공되는 미니탭 개론 과정의 Chapter 1~5 에 해당합니다.",
        'offline_type': 'instructor', 'offline_options': ['지덱수', '빤히', '기냥']
    },
    '파이썬리터러시': {
        'prereq': "선행학습으로 '기술통계' , '추론통계' 과정이 요구됩니다.",
        'has_online': True, 'has_offline': True,
        'online_msg': "파이썬리터러시 온라인 과정은 휴넷에서 제공되는 빅데이터분석기사 과정의 Chapter 1~3 에 해당합니다.",
        'offline_type': 'date', 'offline_msg': "파이썬리터러시 오프라인 과정은 외부교육기관(베가스)의 집체교육입니다. 신청하고자 하는 날짜를 선택하세요.",
        'offline_options': ['2026-08-10', '2026-09-14', '2026-10-12']
    },
    '바이브코딩': {
        'prereq': "선행학습으로 '파이썬리터러시' 과정이 요구됩니다.",
        'has_online': True, 'has_offline': True,
        'online_msg': "바이브코딩 온라인 과정은 휴넷에서 제공되는 바이브코딩 마스터 과정에 해당합니다.",
        'offline_type': 'date', 'offline_msg': "바이브코딩 오프라인 과정은 외부교육기관(베가스)의 집체교육입니다. 신청하고자 하는 날짜를 선택하세요.",
        'offline_options': ['2026-08-17', '2026-09-21', '2026-10-19']
    },
    '머신러닝 이론': {
        'prereq': "선행학습으로 '기술통계', '추론통계', '파이썬리터러시' 과정이 요구됩니다.",
        'has_online': True, 'has_offline': True,
        'online_msg': "머신러닝 온라인 과정은 휴넷에서 제공되는 빅데이터분석기사 과정의 Chapter 1,2,3에 해당합니다.",
        'offline_type': 'date', 'offline_msg': "머신러닝 오프라인 과정은 외부교육기관(베가스)의 집체교육입니다. 신청하고자 하는 날짜를 선택하세요.",
        'offline_options': ['2026-08-24', '2026-09-28', '2026-10-26']
    },
    '탐색적데이터분석': {
        'prereq': "선행학습으로 '기술통계', '추론통계', '파이썬리터러시', '바이브코딩' 과정이 요구됩니다.",
        'has_online': True, 'has_offline': True,
        'online_msg': "탐색적데이터분석 온라인 과정은 휴넷에서 제공되는 빅데이터분석기사 과정의 Chapter 4,5,6에 해당합니다.",
        'offline_type': 'date', 'offline_msg': "탐색적데이터분석 오프라인 과정은 외부교육기관(베가스)의 집체교육입니다. 신청하고자 하는 날짜를 선택하세요.",
        'offline_options': ['2026-08-31', '2026-10-05', '2026-11-02']
    },
    '머신러닝 모델링': {
        'prereq': "선행학습으로 '기술통계', '추론통계', '파이썬리터러시', '바이브코딩', '머신러닝 이론', '탐색적데이터분석' 과정이 요구됩니다.",
        'has_online': True, 'has_offline': True,
        'online_msg': "머신러닝모델링 온라인 과정은 휴넷에서 제공되는 빅데이터분석기사 과정의 Chapter 7,8,9에 해당합니다.",
        'offline_type': 'date', 'offline_msg': "머신러닝 모델링 오프라인 과정은 외부교육기관(베가스)의 집체교육입니다. 신청하고자 하는 날짜를 선택하세요.",
        'offline_options': ['2026-09-07', '2026-10-12', '2026-11-09']
    },
    'AI Automation': {
        'prereq': "선행학습으로 '바이브코딩' 과정이 요구됩니다.",
        'has_online': True, 'has_offline': True,
        'online_msg': "AI Automation 온라인 과정은 휴넷에서 제공되는 Stramlit 마스터 과정에 해당합니다.",
        'offline_type': 'instructor', 'offline_options': ['지덱수', '빤히', '기냥']
    },
    '시각화': {
        'prereq': "선행학습으로 '기술통계', '바이브코딩' 과정이 요구됩니다.",
        'has_online': True, 'has_offline': True,
        'online_msg': "시각화 온라인 과정은 휴넷에서 제공되는 Tableau 마스터 과정에 해당합니다.",
        'offline_type': 'instructor', 'offline_options': ['지덱수', '빤히', '기냥']
    }
}

# ----------------- 세션 상태 초기화 -----------------
if 'current_user' not in st.session_state:
    st.session_state.current_user = random.choice(users)
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'selected_module' not in st.session_state:
    st.session_state.selected_module = None
if 'step' not in st.session_state:
    st.session_state.step = 'prereq'
if 'selected_option' not in st.session_state:
    st.session_state.selected_option = None
if 'edu_type' not in st.session_state:
    st.session_state.edu_type = None

# ----------------- CSS 스타일링 -----------------
st.markdown("""
    <style>
    .block-container { padding-top: 1rem; padding-bottom: 0rem; max-width: 1400px; }
    .badge-container { display: flex; gap: 5px; justify-content: center; align-items: center; }
    .badge-circle { width: 15px; height: 15px; border-radius: 50%; border: 1px solid #999; }
    .module-box {
        background-color: #f0f2f6; border-radius: 10px; padding: 15px; margin-bottom: 10px;
        text-align: center; font-weight: bold; cursor: pointer; transition: 0.3s;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1); height: 80px; display: flex;
        align-items: center; justify-content: center;
    }
    .module-box:hover { background-color: #e0e2e6; transform: scale(1.02); }
    .center-content { text-align: center; margin-top: 10vh; }
    .big-text { font-size: 24px; font-weight: bold; margin-bottom: 30px; }
    div.stButton > button:first-child { width: 100%; height: 60px; font-size: 18px; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# ----------------- 화면 라우팅 -----------------
def go_home():
    st.session_state.page = 'home'
    st.session_state.selected_module = None
    st.session_state.step = 'prereq'

def set_step(step):
    st.session_state.step = step

if st.session_state.page == 'home':
    st.markdown(f"### 👤 접속자: **{st.session_state.current_user}** 님 환영합니다.")
    
    # --- 상단: 배지 현황 (화면 30%) ---
    st.markdown("#### 🏆 모듈별 배지 획득 현황")
    user_idx = users.index(st.session_state.current_user)
    
    cols = st.columns(4)
    for i, (mod, badges) in enumerate(data.items()):
        user_badge_str = badges[user_idx]
        level = badge_levels[user_badge_str]
        
        with cols[i % 4]:
            circles_html = ""
            for j in range(1, 6):
                color = badge_colors[j] if j <= level else badge_colors[0]
                circles_html += f'<div class="badge-circle" style="background-color: {color};"></div>'
            st.markdown(f"""
                <div style="border: 1px solid #ddd; padding: 10px; border-radius: 8px; margin-bottom: 10px; text-align: center; font-size: 14px;">
                    <div style="margin-bottom: 5px; font-weight: bold;">{mod}</div>
                    <div class="badge-container">{circles_html}</div>
                </div>
            """, unsafe_allow_html=True)
            
    st.markdown("---")
    
    # --- 하단: 모듈 선택 ---
    st.markdown("#### 📚 교육 과정 수강신청")
    mod_cols = st.columns(5)
    for i, mod in enumerate(data.keys()):
        with mod_cols[i % 5]:
            if st.button(mod, key=f"btn_{mod}"):
                st.session_state.selected_module = mod
                st.session_state.page = 'module'
                st.session_state.step = 'prereq'
                st.rerun()

elif st.session_state.page == 'module':
    mod = st.session_state.selected_module
    info = modules_info[mod]
    
    st.markdown(f"<div class='center-content'>", unsafe_allow_html=True)
    st.markdown(f"## [{mod}] 수강신청", unsafe_allow_html=True)
    
    # 1. 선수학습 확인 단계
    if st.session_state.step == 'prereq':
        if info['prereq']:
            st.markdown(f"<div class='big-text'>{info['prereq']}<br><br>수강신청 하시겠습니까?</div>", unsafe_allow_html=True)
            c1, c2, c3, c4 = st.columns([1, 1, 1, 1])
            with c2:
                if st.button("예", key="prereq_yes"):
                    if not info['has_online']:
                        st.session_state.step = 'offline_select'
                        st.session_state.edu_type = '오프라인'
                    else:
                        st.session_state.step = 'select_type'
                    st.rerun()
            with c3:
                if st.button("아니오", key="prereq_no"):
                    go_home()
                    st.rerun()
        else:
            st.session_state.step = 'select_type'
            st.rerun()
            
    # 2. 온/오프라인 선택 단계
    elif st.session_state.step == 'select_type':
        st.markdown(f"<div class='big-text'>교육 방식을 선택해 주세요.</div>", unsafe_allow_html=True)
        c1, c2, c3, c4 = st.columns([1, 1, 1, 1])
        with c2:
            if st.button("온라인"):
                st.session_state.edu_type = '온라인'
                st.session_state.step = 'online_confirm'
                st.rerun()
        with c3:
            if st.button("오프라인"):
                st.session_state.edu_type = '오프라인'
                if info['offline_type'] == 'developing':
                    st.session_state.step = 'offline_developing'
                else:
                    st.session_state.step = 'offline_select'
                st.rerun()
                
    # 3. 오프라인 개발중 안내
    elif st.session_state.step == 'offline_developing':
        st.markdown(f"<div class='big-text'>{mod} 오프라인 과정은 현재 개발중에 있습니다. 온라인 과정을 이용해 주세요.</div>", unsafe_allow_html=True)
        c1, c2, c3 = st.columns([1, 1, 1])
        with c2:
            if st.button("이전화면으로 돌아가기"):
                st.session_state.step = 'select_type'
                st.rerun()
                
    # 4. 오프라인 강사/일자 선택 단계
    elif st.session_state.step == 'offline_select':
        if info.get('offline_msg'):
            st.markdown(f"<div class='big-text'>{info['offline_msg']}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='big-text'>담당 강사를 선택해 주세요.</div>", unsafe_allow_html=True)
            
        opts = info['offline_options']
        cols = st.columns(len(opts) + 2)
        for i, opt in enumerate(opts):
            with cols[i+1]:
                if st.button(opt):
                    st.session_state.selected_option = opt
                    st.session_state.step = 'offline_confirm'
                    st.rerun()
        
        st.markdown("<br>", unsafe_allow_html=True)
        c1, c2, c3 = st.columns([1, 1, 1])
        with c2:
             if st.button("돌아가기"):
                 st.session_state.step = 'select_type' if info['has_online'] else 'prereq'
                 st.rerun()
                 
    # 5. 오프라인 최종 확인 단계
    elif st.session_state.step == 'offline_confirm':
        st.markdown(f"<div class='big-text'>선택: {st.session_state.selected_option}<br><br>수강신청 하시겠습니까?</div>", unsafe_allow_html=True)
        c1, c2, c3, c4 = st.columns([1, 1, 1, 1])
        with c2:
            if st.button("예", key="off_yes"):
                st.session_state.step = 'offline_done'
                st.rerun()
        with c3:
            if st.button("아니오", key="off_no"):
                st.session_state.step = 'offline_select'
                st.rerun()
                
    # 6. 오프라인 완료 단계
    elif st.session_state.step == 'offline_done':
        prefix = f"({st.session_state.selected_option}) " if info['offline_type'] == 'date' else ""
        st.success(f"{prefix}수강신청이 완료되었습니다. 오프라인 교육은 강사의 안내에 따라 과제를 제출하여 평가에 응하시기 바랍니다.")
        c1, c2, c3 = st.columns([1, 1, 1])
        with c2:
            if st.button("홈으로 이동"):
                go_home()
                st.rerun()

    # 7. 온라인 최종 확인 단계
    elif st.session_state.step == 'online_confirm':
        st.markdown(f"<div class='big-text'>{info['online_msg']}<br><br>수강신청 하시겠습니까?</div>", unsafe_allow_html=True)
        c1, c2, c3, c4 = st.columns([1, 1, 1, 1])
        with c2:
            if st.button("예", key="on_yes"):
                st.session_state.step = 'online_done'
                st.rerun()
        with c3:
            if st.button("아니오", key="on_no"):
                st.session_state.step = 'select_type'
                st.rerun()

    # 8. 온라인 완료 단계
    elif st.session_state.step == 'online_done':
        st.success("수강신청이 완료되었습니다. 온라인 교육은 강의 종료일로부터 한 달 이내에 두 번의 응시 기회가 부여됩니다.")
        c1, c2, c3 = st.columns([1, 1, 1])
        with c2:
            if st.button("홈으로 이동"):
                go_home()
                st.rerun()
                
    st.markdown("</div>", unsafe_allow_html=True)
