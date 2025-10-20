import streamlit as st
import os

st.set_page_config(page_title="Hazem Soussi - SaaS Solutions", page_icon="🚀", layout="wide")

# Hero Section
st.markdown("""
<style>
.hero {
    text-align: center;
    padding: 50px 0;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border-radius: 10px;
    margin-bottom: 50px;
}
.hero h1 {
    font-size: 3em;
    margin-bottom: 10px;
}
.hero p {
    font-size: 1.2em;
    margin-bottom: 30px;
}
.cta-button {
    background-color: #ff6b6b;
    color: white;
    padding: 15px 30px;
    text-decoration: none;
    border-radius: 5px;
    font-weight: bold;
}
</style>
<div class="hero">
    <h1>Hazem Soussi</h1>
    <p>Expert in Cloud Computing & DevOps Solutions</p>
    <p>Transform your infrastructure with cutting-edge SaaS technologies</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])
with col1:
    st.image("https://avatars.githubusercontent.com/u/64667872?v=4", width=200)
with col2:
    st.markdown("### About Me")
    st.write("Hi, I'm Hazem Soussi, a specialist in Cloud computing architecture. I help businesses scale with modern DevOps practices and full-stack development.")
    st.write("**Contact:** +216 98 454 001 | hazem.soussi@gmail.com")

# Features Section
st.header("🚀 Services & Skills")
col1, col2 = st.columns(2)
with col1:
    st.subheader("DevOps & Cloud Engineering")
    st.write("- Kubernetes orchestration")
    st.write("- Docker containerization")
    st.write("- AWS/Azure/GCP cloud platforms")
    st.write("- CI/CD pipelines (Jenkins, GitLab CI)")
    st.progress(90, text="Expertise Level")
with col2:
    st.subheader("Full-Stack Development")
    st.write("- Frontend: React, Angular")
    st.write("- Backend: Node.js, Python, Java")
    st.write("- Databases: MongoDB, PostgreSQL")
    st.write("- Version Control: Git")
    st.progress(85, text="Expertise Level")

# Projects Section
st.header("💼 Featured Projects")
st.markdown("Discover innovative solutions I've built:")
with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("MERN Stack Tutorial")
        st.write("Complete MERN stack implementation for modern web apps.")
        st.link_button("View on GitHub", "https://github.com/hazem-soussi-HA/MERN-Stack-Tutorial")
    with col2:
        st.subheader("Kali Linux on Proxmox")
        st.write("Secure containerized penetration testing environment.")
        st.link_button("View on GitHub", "https://github.com/hazem-soussi-HA/Kali-Linux-Container-on-Proxmox")
    with col3:
        st.subheader("Ollama AI Models")
        st.write("Easy deployment of large language models like Llama 3.3.")
        st.link_button("View on GitHub", "https://github.com/hazem-soussi-HA/ollama")

# Certifications Section
st.header("🏆 Certifications")
st.write("- AWS Certified Solutions Architect")
st.write("- Certified Kubernetes Administrator (CKA)")
st.write("- Docker Certified Associate")
st.write("- Scrum Master Certification")

# Experience Section
st.header("💼 Professional Experience")
st.markdown("""
**DevOps Engineer** - Company XYZ (2022-Present)  
Led migration to microservices using Kubernetes, implemented CI/CD pipelines.

**Full-Stack Developer** - Startup ABC (2020-2022)  
Built web apps with React and Node.js, integrated cloud services.
""")

# Contact Section
st.header("📞 Get In Touch")
col1, col2 = st.columns(2)
with col1:
    st.write("**Email:** hazem.soussi@gmail.com")
    st.write("**Phone:** +216 98 454 001")
    st.write("**LinkedIn:** [linkedin.com/in/hazem-soussi](https://www.linkedin.com/in/hazem-soussi)")
    st.write("**GitHub:** [github.com/hazem-soussi-HA](https://github.com/hazem-soussi-HA)")
    # Download CV
    cv_path = "Hazem Soussi.docx"
    if os.path.exists(cv_path):
        with open(cv_path, "rb") as file:
            st.download_button("📄 Download CV", file, file_name="Hazem_Soussi_CV.docx")
with col2:
    with st.form("contact_form"):
        st.subheader("Send a Message")
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Send Message")
        if submitted:
            st.success("Thank you! Your message has been sent.")  # Placeholder