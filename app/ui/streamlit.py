import streamlit as st
import requests
import json
import re

st.set_page_config(page_title="Resume Screening", page_icon="📄", layout="centered")

st.markdown("## 📄 Resume Screening")
st.markdown("<p style='color:gray; margin-top:-10px;'>AI-powered candidate analysis</p>", unsafe_allow_html=True)
st.markdown("---")

uploaded_file = st.file_uploader("Upload a Resume (PDF)", type="pdf", label_visibility="collapsed")

if uploaded_file is not None:
    st.success(f"✅ {uploaded_file.name}")

    if st.button("Analyze Resume →"):
        with st.spinner("Analyzing..."):
            response = requests.post(
                "http://localhost:8000/screening/",
                files={"resume": uploaded_file}
            )

        if response.status_code == 200:
            data = response.json()

            if isinstance(data, str):
                try:
                    json_match = re.search(r'\{.*\}', data, re.DOTALL)
                    if json_match:
                        data = json.loads(json_match.group())
                except:
                    st.write(data)
                    st.stop()

            st.markdown("---")

            col1, col2 = st.columns([1, 3])
            with col1:
                initials = "".join([n[0] for n in data.get("name", "?").split()][:2])
                st.markdown(f"<div style='width:56px;height:56px;border-radius:50%;background:#f0f0f0;display:flex;align-items:center;justify-content:center;font-size:18px;font-weight:500'>{initials}</div>", unsafe_allow_html=True)
            with col2:
                st.markdown(f"### {data.get('name', 'N/A')}")
                st.markdown(f"<p style='color:gray; margin-top:-10px'>{data.get('education', 'N/A')}</p>", unsafe_allow_html=True)

            st.markdown("")
            c1, c2, c3 = st.columns(3)
            c1.markdown(f"**✉ Email**\n\n{data.get('email', 'N/A')}")
            c2.markdown(f"**📞 Phone**\n\n{data.get('phone', 'N/A')}")
            c3.markdown(f"**💼 Experience**\n\n{data.get('work_experience', 0)} years")

            st.markdown("---")
            st.markdown("**🛠 Skills**")
            skills = data.get("skills", [])
            skill_pills = " ".join([f"`{s}`" for s in skills])
            st.markdown(skill_pills)

            st.markdown("---")
            st.markdown("**🏆 Certifications**")
            certs = data.get("certifications", [])
            if certs:
                for cert in certs:
                    st.markdown(f"— {cert}")
            else:
                st.markdown("_No certifications listed_")
        else:
            st.error("❌ Something went wrong. Please try again.")