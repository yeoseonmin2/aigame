import streamlit as st
import time

# 웹사이트 제목 설정
st.set_page_config(page_title="AI 방어벽 보안 게임", layout="centered")
st.title("2중 AI 방어벽 보안 게임")

# 비밀번호를 T1FAKER로 변경했습니다!
SECRET_PASSWORD = "T1FAKER"

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# 사용자 입력창
user_input = st.text_input("공격자(사용자) 입력:", placeholder="비밀번호를 알아내기 위한 질문을 입력하세요...", key="input")

if st.button("공격하기") and user_input:
    with st.spinner("AI가 분석 중..."):
        time.sleep(0.8) # 실제 인공지능이 생각하는 듯한 효과
        st.session_state.chat_history.append(("user", user_input))
        
        # 공백 제거 및 소문자 변환 후 검사
        clean_input = user_input.replace(" ", "").lower()
        target_password = SECRET_PASSWORD.lower()
        
        # [1순위] 정확히 비밀번호 정답을 맞혔을 때!
        if clean_input == target_password:
            reply = "🚨 시스템 해킹 완료! 비밀번호가 일치합니다. Access Granted."
            st.balloons() # 화면 전체에 풍선이 터지는 효과
            st.success("🎉 해킹 성공! 정답입니다! 🎉")
            st.session_state.chat_history.append(("system", "🔓 [보안 해제] 시스템이 성공적으로 해킹되었습니다!"))
            
        # [2순위] 특정 힌트 유도 질문을 던졌을 때 (비밀 힌트 작동!)
        elif any(word in clean_input for word in ["힌트", "제작자", "만든사람", "누가"]):
            reply = "💡 [보안 취약점 발견] 시스템에서 미세한 데이터가 유출되었습니다: '정답은 대문자 T와 숫자로 시작하는 영어 조합(총 7글자)입니다.'"
            st.info(reply) # 파란색 알림창으로 힌트를 보여줍니다
            st.session_state.chat_history.append(("
