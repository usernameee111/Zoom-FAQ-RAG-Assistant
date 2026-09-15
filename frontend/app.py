import streamlit as st
from api_client import query_backend

# إعدادات الصفحة
st.set_page_config(page_title="Zoom FAQ Assistant", page_icon="💬")
st.title("💬 Zoom Support Assistant")
st.write("Ask me anything about Zoom (Accounts, Webinars, Meetings, etc.)!")

# حفظ تاريخ المحادثة عشان الشات يفضل موجود
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض الرسايل القديمة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "sources" in message and message["sources"]:
            st.caption(f"**Sources:** {', '.join(message['sources'])}")

# مربع إدخال السؤال (Chat Input)
if prompt := st.chat_input("E.g., How many panelists are allowed in a webinar?"):
    
    # 1. عرض سؤال المستخدم
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. عرض حالة التحميل (Loading State) واستدعاء السيرفر
    with st.chat_message("assistant"):
        with st.spinner("Searching documents & thinking... 🔍"):
            result = query_backend(prompt)
            
        # 3. عرض الإجابة أو رسالة الخطأ
        if "error" in result:
            st.error("Oops! Something went wrong.")
            st.error(result["error"])
        else:
            answer = result.get("answer", "")
            sources = result.get("sources", [])
            
            st.markdown(answer)
            if sources:
                st.info(f"**Sources used:** {', '.join(sources)}")
                
            # حفظ الإجابة في تاريخ المحادثة
            st.session_state.messages.append({
                "role": "assistant", 
                "content": answer,
                "sources": sources
            })