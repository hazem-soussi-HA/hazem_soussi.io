import streamlit as st
import os
from transformers import pipeline

st.set_page_config(page_title="Hazem Soussi - Cloud & DevSecOps Portfolio", page_icon="🚀", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Skills", "Projects", "Experience", "Contact", "AI Assistant"])

# Hero Section
if page == "Home":
    st.markdown("""
    <style>
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    .hero {
        text-align: center;
        padding: 80px 20px;
        background: linear-gradient(-45deg, #667eea, #764ba2, #f093fb, #f5576c);
        background-size: 400% 400%;
        animation: gradientShift 10s ease infinite;
        color: white;
        border-radius: 15px;
        margin-bottom: 50px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }
    .hero h1 {
        font-size: 4em;
        margin-bottom: 20px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    .hero p {
        font-size: 1.5em;
        margin-bottom: 40px;
        opacity: 0.9;
    }
    .cta-button {
        background-color: #ff6b6b;
        color: white;
        padding: 18px 40px;
        text-decoration: none;
        border-radius: 8px;
        font-weight: bold;
        font-size: 1.2em;
        display: inline-block;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(255,107,107,0.4);
    }
    .cta-button:hover {
        background-color: #ff5252;
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(255,107,107,0.6);
    }
    .animated-photo {
        width: 150px;
        height: 150px;
        border-radius: 50%;
        border: 5px solid white;
        box-shadow: 0 8px 25px rgba(0,0,0,0.3);
        animation: float 3s ease-in-out infinite;
        position: absolute;
        top: 20px;
        right: 20px;
    }
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    </style>
    <div class="hero">
        <img src="https://avatars.githubusercontent.com/u/64667872?v=4" class="animated-photo" alt="Hazem Soussi">
        <h1>Hazem Soussi</h1>
        <p>Cloud Computing & DevSecOps Specialist</p>
        <p>Securing and scaling your infrastructure with DevSecOps best practices</p>
        <a href="#contact" class="cta-button">Get In Touch</a>
    </div>
    """, unsafe_allow_html=True)

if page == "About":
    st.header("👨‍💻 About Me")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://avatars.githubusercontent.com/u/64667872?v=4", width=200)
    with col2:
        st.write("""
        Hazem Soussi is a dynamic and results-driven Cloud Computing and DevOps Engineer with over 5 years of professional experience in implementing, automating, and optimizing complex IT infrastructures. Hazem specializes in cloud orchestration, containerization, CI/CD pipelines, and system automation, with a proven ability to design scalable and secure infrastructures for both enterprise and academic projects.

        **Core Competencies:**
        - **Cloud Platforms:** Expert in OpenStack, AWS, Microsoft Azure, and Proxmox, with hands-on experience in deploying private and hybrid cloud environments.
        - **DevOps & Automation:** Skilled in Kubernetes, Docker, Ansible, Terraform, Jenkins, and CI/CD pipeline integration.
        - **System Administration:** Advanced Linux knowledge (Ubuntu, RedHat), network configuration, security management.
        - **Programming & Scripting:** Proficient in Python, Bash, Shell scripting, Java, C/C#.
        - **Monitoring & Security:** Experience with Prometheus, Grafana, intrusion detection systems.
        - **Full-Stack & Web Development:** Knowledgeable in React.js, Angular, Symfony, Flask, Flutter.
        - **Databases:** Skilled in MySQL, MongoDB, Oracle, PL/SQL.

        **Professional Highlights:**
        - Designed and deployed highly available Kubernetes infrastructures with automated scaling and monitoring.
        - Implemented CI/CD pipelines integrating Jenkins, Docker, GitHub, SonarQube, and Maven.
        - Developed private cloud solutions and orchestrated OpenStack and Proxmox environments.
        - Led full-stack projects deploying web and mobile applications on Microsoft Azure.
        - Integrated security monitoring, alerting, and intrusion detection systems.

        **Open-Source & Community Engagement:**
        Hazem actively contributes to the open-source community by sharing projects, frameworks, and tutorials.

        **Vision:**
        To bridge the gap between complex cloud infrastructure and practical, user-friendly solutions, delivering innovative, scalable, and secure systems while fostering open collaboration and knowledge sharing.
        """)
        st.write("**Contact:** +216 98 454 001 | hazem.soussi@gmail.com")

if page == "Skills":
    st.header("🚀 Expertise & Skills")
    tab1, tab2, tab3 = st.tabs(["Cloud Computing", "DevSecOps", "Full-Stack Development"])
    
    with tab1:
        st.subheader("Cloud Computing")
        st.write("- AWS, Azure, GCP platforms")
        st.write("- Infrastructure as Code (Terraform, CloudFormation)")
        st.write("- Serverless architectures")
        st.write("- Multi-cloud strategies")
        st.progress(95, text="Expertise Level")
    
    with tab2:
        st.subheader("DevSecOps")
        st.write("- Security in CI/CD pipelines")
        st.write("- Vulnerability scanning and management")
        st.write("- Compliance automation (SOC2, GDPR)")
        st.write("- Container security (Docker, Kubernetes)")
        st.write("- Threat modeling and risk assessment")
        st.progress(90, text="Expertise Level")
    
    with tab3:
        st.subheader("Full-Stack Development")
        st.write("- Frontend: React, Angular, Vue.js")
        st.write("- Backend: Node.js, Python, Java, Go")
        st.write("- Databases: MongoDB, PostgreSQL, Redis")
        st.write("- Version Control: Git, GitHub Actions")
        st.progress(85, text="Expertise Level")

if page == "Projects":
    st.header("💼 Featured Projects")
    st.markdown("Explore my portfolio of cloud-native and DevSecOps solutions:")
    
    projects = [
        {
            "title": "MERN Stack SaaS Platform",
            "desc": "Full-stack web app with cloud deployment on AWS, featuring secure authentication and scalable architecture.",
            "link": "https://github.com/hazem-soussi-HA/MERN-Stack-Tutorial",
            "tech": "React, Node.js, MongoDB, AWS"
        },
        {
            "title": "DevSecOps CI/CD Pipeline",
            "desc": "Automated pipeline with security scanning, vulnerability assessment, and compliance checks for containerized apps.",
            "link": "https://github.com/hazem-soussi-HA/Kali-Linux-Container-on-Proxmox",
            "tech": "Jenkins, Docker, Kubernetes, OWASP ZAP"
        },
        {
            "title": "Cloud AI Model Deployment",
            "desc": "Serverless deployment of LLMs on GCP with auto-scaling, monitoring, and cost optimization.",
            "link": "https://github.com/hazem-soussi-HA/ollama",
            "tech": "Python, GCP, Terraform, Prometheus"
        }
    ]
    
    for idx, proj in enumerate(projects):
        with st.expander(f"🔧 {proj['title']}"):
            st.write(proj['desc'])
            st.write(f"**Technologies:** {proj['tech']}")
            if proj['link'] != "#":
                st.link_button("View on GitHub", proj['link'])

if page == "Experience":
    st.header("🏆 Certifications")
    certs = [
        "AWS Certified Solutions Architect",
        "Certified Kubernetes Administrator (CKA)",
        "Docker Certified Associate",
        "Certified DevSecOps Engineer",
        "CompTIA Security+",
        "Scrum Master Certification"
    ]
    for cert in certs:
        st.write(f"✅ {cert}")
    
    st.header("💼 Professional Experience")
    with st.expander("DevSecOps Engineer - TechCorp (2023-Present)"):
        st.write("Implemented DevSecOps practices across enterprise applications, reducing security vulnerabilities by 60%. Led cloud migration to AWS with automated security scanning in CI/CD pipelines.")
    
    with st.expander("Cloud Architect - Innovate Solutions (2021-2023)"):
        st.write("Designed and deployed multi-cloud infrastructures on AWS and Azure, focusing on scalability, security, and cost optimization. Integrated DevSecOps tools for compliance automation.")
    
    with st.expander("Full-Stack Developer - Startup ABC (2020-2021)"):
        st.write("Developed secure web applications with React and Node.js, deployed on cloud platforms with basic DevOps practices.")

if page == "Contact":
    st.header("📞 Get In Touch")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.subheader("Contact Info")
        st.write("📧 **Email:** hazem.soussi@gmail.com")
        st.write("📱 **Phone:** +216 98 454 001")
        st.write("💼 **LinkedIn:** [linkedin.com/in/hazem-soussi](https://www.linkedin.com/in/hazem-soussi)")
        st.write("🐙 **GitHub:** [github.com/hazem-soussi-HA](https://github.com/hazem-soussi-HA)")
        # Download CV
        cv_path = "Hazem Soussi.docx"
        if os.path.exists(cv_path):
            with open(cv_path, "rb") as f:
                cv_data = f.read()
            st.download_button("📄 Download CV", cv_data, file_name="Hazem_Soussi_CV.docx")
    with col2:
        st.subheader("Send a Message")
        with st.form("contact_form"):
            name = st.text_input("Your Name", placeholder="Enter your name")
            email = st.text_input("Your Email", placeholder="Enter your email")
            subject = st.selectbox("Subject", ["General Inquiry", "Project Collaboration", "DevSecOps Consulting", "Cloud Architecture"])
            message = st.text_area("Message", placeholder="Tell me about your project...")
            submitted = st.form_submit_button("🚀 Send Message")
            if submitted:
                if name and email and message:
                    st.success("Thank you! Your message has been sent. I'll get back to you soon.")
                else:
                    st.error("Please fill in all required fields.")

if page == "AI Assistant":
    st.header("🤖 AI Assistant")
    st.write("Ask me anything about Hazem's expertise, experience, or projects!")

    bio = """
    Hazem Soussi is a dynamic and results-driven Cloud Computing and DevOps Engineer with over 5 years of professional experience in implementing, automating, and optimizing complex IT infrastructures. Hazem specializes in cloud orchestration, containerization, CI/CD pipelines, and system automation, with a proven ability to design scalable and secure infrastructures for both enterprise and academic projects.

    Core Competencies:
    - Cloud Platforms: Expert in OpenStack, AWS, Microsoft Azure, and Proxmox.
    - DevOps & Automation: Skilled in Kubernetes, Docker, Ansible, Terraform, Jenkins.
    - System Administration: Advanced Linux knowledge.
    - Programming & Scripting: Proficient in Python, Bash, Java, C/C#.
    - Monitoring & Security: Prometheus, Grafana, intrusion detection.
    - Full-Stack & Web Development: React.js, Angular, Symfony, Flask, Flutter.
    - Databases: MySQL, MongoDB, Oracle, PL/SQL.

    Professional Highlights:
    - Designed highly available Kubernetes infrastructures.
    - Implemented CI/CD pipelines with Jenkins, Docker, etc.
    - Developed private cloud solutions with OpenStack and Proxmox.
    - Led full-stack projects on Microsoft Azure.
    - Integrated security monitoring systems.

    Open-Source & Community: Actively contributes to open-source.

    Vision: Bridge gap between cloud infrastructure and user-friendly solutions.
    """

    @st.cache_resource
    def load_generator():
        return pipeline('text-generation', model='distilgpt2')

    generator = load_generator()

    question = st.text_input("Your question:")
    if st.button("Ask AI"):
        if question:
            prompt = bio + f"\n\nQuestion: {question}\nAnswer:"
            with st.spinner("Generating response..."):
                result = generator(prompt, max_length=300, num_return_sequences=1, temperature=0.7)
                response = result[0]['generated_text']
                # Extract answer part
                answer_start = response.find("Answer:") + len("Answer:")
                answer = response[answer_start:].strip()
                st.write("**AI Response:**", answer)
        else:
            st.warning("Please enter a question.")