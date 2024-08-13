import streamlit as st
from forms.contact import contact_form

col1, col2 = st.columns(2, gap='small', vertical_alignment="top")

with col1:
    st.image("../src/assets/Damian-sin fondo-gris.png", width=300)
with col2:
    
    
    st.title("Damian Capdevila", anchor=False)
    st.write("**Software Engineer** - Empowering Engineers to Transition into Software Development with Confidence and Precision!")
        
    if st.button("🤖 Ask my assistant about me!", use_container_width=False):
        st.switch_page("pages/chat.py")

st.subheader("Providing services", divider=True)
col5, col6, col7 = st.columns(3, gap='small', vertical_alignment="center")
with col5:
    if st.button("📈 Career Mentoring", type="primary", help="Book a free initial consultation!"):
        contact_form()
with col6:
    if st.button("📄 Resume Reviewing", type="primary", help="Get my free resume-building cheatsheet!"):
        contact_form()

st.subheader("About Me", divider=True)
st.write("""*Over the last years, I [successfully transitioned from Automation Engineering into Software Development.](https://damiancapdevila.substack.com/p/from-automation-engineer-to-software) 
            Now, I want to share my experience with you!* 
         """)
with st.expander(label="**Skills**", icon="🛠"):
    st.write("")
    st.write("""
    - **Presales:** *Technical Consultancy, Conference Speaking, Professional English, Native Spanish*  
    - **Programming:** *C#, .NET, REST API, WPF, Blazor, MVVM, Unity Container, Nunit, Python, Streamlit*  
    - **Industrial Automation:** *PLC, HMI, Drives, Commissioning*  
    - **Tools:** *Docker, Git, Azure, Visual Studio, VSCode, Azure DevOps Platform*   
    - **Methodologies:** *Agile Software Development, Refactoring Legacy Systems, Code Reviewing* 
    """)

with st.expander(label="**Experience**", icon="👨‍🏭"):
    st.write("")
    with st.container(border=True):
        st.write("**📋 Summary**")
        st.write("""
                    Greetings! I'm Damián Capdevila, an accomplished electronic engineer with **seven years of experience spanning software development, 
                    solutions engineering, presales, and academic research**. My current focus is on **engineering enterprise-grade software using C# .NET, 
                    serving a global user base.**

                    As an Italian and Argentinian dual citizen, **I offer versatility and can work in the EU, LATAM, or GLOBALLY REMOTE.** 
                    **Fluent in Spanish and English**, I've worked in English-centric environments for over four years, 
                    including hybrid/remote roles at Siemens' International Hubs.
                """)
    
    with st.container(border=True):
        st.write("**🔎 Details**",)
        st.write("""
        **Presales Software Engineer - Siemens**  
        *Madrid, Spain (11/2023 - Current)*  
        - *[Drove success of a multi-billion dollar project](https://www.linkedin.com/posts/damiancapdevila_after-3-weeks-on-site-in-korea-giving-activity-7119254288891047936-Kd5a?utm_source=share&utm_medium=member_desktop) by achieving 100% faster machine-machine communication, providing engineering consultancy for the world's largest battery production project in South Korea (PLC programming, TIA Portal, Profinet).* 
        
        - *Led the design and development of an enterprise-grade application used worldwide across 150 factories by an automotive brand, saving ~80k Euros quarterly by speeding up the SDLC by 400%(C#, .NET Framework 4.8, MVVM, WPF, Unity Container for DI)*.
                
        - *Delivered 10+ features in 2 months for an RAG AI assistant, saving ~60k Euros in operation costs monthly (C#, .NET 8, MVVM, RAG, WPF, NUnit, Azure OpenAi Studio, Streamlit, Python).*
                
        - *Collected over thirty business leads while overseeing the exhibition of a standardization use case at [Hannover Messe](https://www.hannovermesse.de/en/)*.
        
        - *Presented at the Siemens Technical Consultants Global Conference, sharing expertise in TIA Portal Openness API with 80 attendees.*
        
        """)

        st.write("""
        **Application Engineer - Siemens**  
        *Plzen, Czech Republic (07/2020 - 11/2023)*  
        - *Generated ~100k Euros by solving support requests and providing presales consultancy to Siemens’ branches worldwide.*
        
        - *Created a [motion control application example](https://www.youtube.com/watch?v=K2I3nb9-okg) with a technical manual that received over 11k views.*
        
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
        **Doctoral Researcher - National University of La Plata**  
        *La Plata, Argentina (05/2018 - 05/2019)*  
        - *Published ["Wearable platform for Human-Machine interfaces"](https://sedici.unlp.edu.ar/bitstream/handle/10915/75309/Documento_completo.pdf-PDFA.pdf?sequence=1) focusing on hardware and software design (C#, Altium Designer).*
        """)

        st.write("---")
        st.write("""
        **Software Engineer - A.R.G SRL**  
        *La Plata, Argentina (10/2017 - 05/2018)*  
        - *Designed and programmed a desktop app for real-time waste treatment management for 1000+ hospitals. Generating over 100k USD in revenue (VB.NET + WinForms + Microsoft SQL)*
        """)

        st.write("")
    st.caption("**Disclaimer**: *All monetary estimates are based on a personal calculation. Please note that companies estimates might differ.*")

with st.expander("**Education**", icon="👨‍🎓"):
    st.subheader("Formal Education", divider=True)
    st.write("""
    **Master of Engineering (Electronics) - National University of La Plata**  
    *La Plata, Argentina (03/2012 - 10/2017)*  
    - *[Thesis in Brain-Computer Interfaces](https://drive.google.com/file/d/1y4BDSVnrj8vulKdOlVp3ZUHFDBYpUJ_v/view?usp=drive_link) based on Stationary-state visually-evoked potentials.*
    """)

    st.subheader("Relevant Courses", divider=True)
    st.write("""
    - **Microsoft Applied Skills:** *Develop an ASP.NET Core web app that consumes an API* – [Credential](https://learn.microsoft.com/api/credentials/share/en-us/DamianCapdevila/D6A902CF0642B0D0?sharingId=975F76F04E9A23A5)
    - **University of Michigan:** *Web Application Technologies and Django* – [Credential](https://coursera.org/share/ba8303b333e48ccf6ee9b5a8a687329e)
    - **University of Michigan:** *Python for Everybody Specialization* – [Credential](https://coursera.org/share/42c74c2cf60501210dd5f0d1c214a541)
    """)

# Call to Action - Contact Me
st.write("---")
st.subheader("📩 Let's Talk!")
st.write("*If you have any questions or want to work together, feel free to reach out!*")
with st.container():
    if st.button("**Contact Me**", type="primary", use_container_width=True):
        contact_form()

#Disclaimer
st.write("---")
st.write("")
st.write("**Disclaimer:** *All monetary estimates are based on a personal calculation. Please note that companies estimates might differ.*")
st.write("")
st.write("")
st.write("")

st.markdown("""
    <div style="text-align: center;">
        <p>Made with 💓 by <a href="https://linkedin.com/in/damiancapdevila" target="_blank">Damian Capdevila</a></p>
        <p><b>Damian Capdevila LLC</b> - All rights reserved</p>
    </div>
    """, unsafe_allow_html=True)