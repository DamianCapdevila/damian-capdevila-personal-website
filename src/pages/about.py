import streamlit as st
from forms.contact import contact_form

col1, col2 = st.columns(2, gap='small', vertical_alignment="top")

with col1:
    st.image("../src/assets/Damian-sin fondo-gris.png", width=300)
with col2:
    
    
    st.title("Damian Capdevila", anchor=False)
    st.write("**Software Engineer** - helping people worldwide transition into software engineering!")
    st.write("*Want to know more about me?*")
        
    if st.button("🤖 Ask my assistant!", use_container_width=False):
        st.switch_page("pages/chat.py")

st.subheader("Providing services", divider=True)
col5, col6, col7 = st.columns(3, gap='small', vertical_alignment="center")
with col5:
    if st.button("📈 Career Mentoring", type="primary"):
        contact_form()
with col6:
    if st.button("📄 Resume Reviewing", type="primary"):
        contact_form()

st.subheader("About Me", divider=True)
with st.expander(label="**Skills**", icon="🛠"):
    st.write("")
    st.write("""
    - **Presales:** *Technical Consultancy | Conference Speaking | Professional English | Native Spanish*  
    - **Programming:** *C#, .NET, REST API, WPF, Blazor, MVVM, Unity Container, Nunit, Python, Streamlit*  
    - **Industrial Automation:** *PLC, HMI, Drives, Commissioning*  
    - **Tools:** *Docker, Git, Azure, Visual Studio, VSCode, Azure DevOps Platform*   
    - **Methodologies:** *Agile Software Development, Refactoring Legacy Systems, Code Reviewing* 
    """)

with st.expander(label="**Experience**", icon="👨‍🏭"):
    st.write("")
    st.write("""
    **Presales Software Engineer - Siemens**  
    *Madrid, Spain (11/2023 - Current)*  
    - *Drove success of a multi-billion dollar project by achieving 100% faster machine-machine communication, providing engineering consultancy for the world's largest battery production project in South Korea.* 
    
    - *Collected over thirty business leads while overseeing the exhibition of a standardization use case at Hannover Messe*.
    
    - *Led the design and development of an enterprise-grade application used worldwide across 150 factories by an automotive brand, saving ~80k Euros quarterly by speeding up the SDLC by 400%*.
    
    - *Presented at the Siemens Technical Consultants Global Conference, sharing expertise in TIA Portal Openness API with 80 attendees.*
    
    - *Delivered 10+ features in 2 months for an RAG AI assistant, saving ~60k Euros in operation costs monthly. Currently migrating to Streamlit with Python.*
    """)

    st.write("""
    **Application Engineer - Siemens**  
    *Plzen, Czech Republic (07/2020 - 11/2023)*  
    - *Generated ~100k Euros by solving support requests and providing presales consultancy to Siemens’ branches worldwide.*
    
    - *Created a motion control application example with a technical manual that received over 11k views.*
    
    - *Coordinated the creation of a Motion Control Web-Based training, acting as a SME and curating the material.*
    """)

    st.write("""
    **Service Engineer - Siemens**  
    *La Plata, Argentina (05/2019 - 07/2020)*  
    - *Managed tens of contractors, ensuring quality and timeliness of their work, contributing to TecPlata’s success.*
             
    - *Saved TecPlata ~150k USD by reducing downtimes during ship load/unload operations.*
    """)

    st.write("---")
    st.write("""
    **Doctoral Researcher - UNLP**  
    *La Plata, Argentina (05/2018 - 05/2019)*  
    - *Published "Wearable platform for Human-Machine interfaces," focusing on hardware and software design (C#, Altium Designer).*
    """)

    st.write("---")
    st.write("""
    **Software Engineer - A.R.G SRL**  
    *La Plata, Argentina (10/2017 - 05/2018)*  
    - *Designed and programmed a desktop app for real-time waste treatment management for 1000+ hospitals, generating over 100k USD in revenue for VEOLIA.*
    """)

with st.expander("**Education**", icon="👨‍🎓"):
    st.subheader("Formal Education", divider=True)
    st.write("""
    **Master of Engineering (Electronics) - UNLP**  
    *La Plata, Argentina (03/2012 - 10/2017)*  
    - *Thesis in Brain-Computer Interfaces, based on Stationary-state visually-evoked potentials.*
    """)

    st.subheader("Relevant Courses", divider=True)
    st.write("""
    - *Microsoft Applied Skills: Develop an ASP.NET Core web app that consumes an API* – [Credential here](https://www.linkedin.com/in/damiancapdevila/)
    - *University of Michigan: Web Application Technologies and Django* – [Credential here](https://www.linkedin.com/in/damiancapdevila/)
    - *University of Michigan: Python for Everybody Specialization* – [Credential here](https://www.linkedin.com/in/damiancapdevila/)
    """)

# Call to Action - Contact Me
st.write("---")
st.subheader("📩 Let's Talk!")
st.write("*If you have any questions or want to work together, feel free to reach out!*")
with st.container():
    if st.button("**Contact Me**", type="primary", use_container_width=True):
        contact_form()